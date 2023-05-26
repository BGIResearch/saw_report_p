# Copyright (C) BGI-Reasearch - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by STOmics development team P_stomics_dev@genomics.cn, May 2017

# !/usr/bin/env python3
import os
from optparse import OptionParser
import sys
from collections import defaultdict
from Bio import SeqIO
import re
import json
import types
import h5py
import time
import threading
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from numpy import *



def main():
    """
    %prog [options]
    stat spatial filter result to visualization report
    """

    parser = OptionParser(main.__doc__)
    parser.add_option("-s", "--barcodeMapStat", help="The barcodeMap stat file")
    parser.add_option("-a", "--alignmentLog", help="The alignment log file")
    parser.add_option("-t", "--alignmentStat", help="The alignment stat file")
    parser.add_option("-l", "--tissueCutLog", help="The tissue cut log file")
    parser.add_option("-o", "--outfile", default=None, help="The output file")
    opts, args = parser.parse_args()

    if (
            opts.barcodeMapStat == None or opts.alignmentLog == None or opts.alignmentStat == None or opts.tissueCutLog == None or opts.outfile == None):
        sys.exit(not parser.print_help())

    barcodeMapStat = opts.barcodeMapStat
    alignmentLog = opts.alignmentLog
    alignmentStat = opts.alignmentStat
    tissueCutLog = opts.tissueCutLog
    outfile_path = opts.outfile

    Statistic = statistic(barcodeMapStat, alignmentLog, alignmentStat, tissueCutLog, outfile_path)
    Statistic.run()


class statistic():
    def __init__(self, barcodeMapStat, alignmentLog, alignmentStat, tissueCutLog, outfile_path, cellBinGef='N', sn='N'):
        """
        A statistic tool set for saw pipeline. include barcode mapping stat, alingment log, tissuce cut log and etc.

        :param barcodeMapStat: The barcodeMap stat file (*read_barcodeMap.stat)
        :param alignmentLog: The alignment log file (*.Log.final.out)
        :param alignmentStat: The alignment stat file (*dedup.target.bam.summary.stat)
        :param tissueCutLog: The tissue cut log file (TissueCut.log)
        :param outfile_path: The output file path
        :param cellBinGef: The cell bin gef file (SN.cellbin.gef)
        """
        self.outfile_path = outfile_path
        self.barcodeMapStat = barcodeMapStat
        self.alignmentLog = alignmentLog
        self.alignmentStat = alignmentStat
        self.tissueCutLog = tissueCutLog
        self.cellBinGef = cellBinGef
        json_file_name = sn + '.statistics.json'
        self.final_result_json = os.path.join(outfile_path, json_file_name)
        self.result_dict = defaultdict(dict)
        self.result_dict['version'] = "version_v2"
        self.bin_list = []
        os.makedirs(self.outfile_path, exist_ok=True)

    def run(self):
        """
        Run all statistic pipeline
        """
        self.filter_result()
        self.alignment_result()
        self.tissueCutStat()
        if self.cellBinGef != 'N':
            self.cellCutBinStat()
        try:
            with open(self.final_result_json, 'w') as f:
                t_result_dict = json.loads(
                    json.dumps(self.result_dict).replace('Umi', 'MID').replace('umi', 'MID').replace('barcode',
                                                                                                     'CID').replace(
                        'Barcode', 'CID'))
                j = json.dump(t_result_dict, f, indent=4)
        except IOError:
            self.print_err("failed to write final_result_json", "SAW-A90005")

    # def print_err(*args):
    #     """
    #     print error code
    #     """
    #     sys.stderr.write(' '.join(map(str,args)) + '\n')
    def print_err(self, case, code):
        """
        print error code
        """
        err_code = {
            "SAW-A90001": "{} is missing.",
            "SAW-A90002": "cannot access {}: No such file or directory.",
            "SAW-A90003": "{} file format error.",
            "SAW-A90004": "infomation loss:{}.",
            "SAW-A90005": "{}."
        }
        nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open("errcode.log", "a") as err_info:
            err_info.write("[{}] {}: {}\n".format(nowtime, code, err_code[code].format(case)))
        # sys.stderr.write(' '.join(map(str,args)) + '\n')
        sys.stderr.write("[{}] {}: {}\n".format(nowtime, code, err_code[code].format(case)))
        sys.exit(1)

    def number_transfer(self, num):
        """
        Data cleaning

        :param num: Data whitout clean
        """
        if isinstance(num, int) or isinstance(num, float):
            return (self.change(num))
        elif isinstance(num, str):
            if num.endswith('%'):
                return (num.replace(" ", ""))
            else:
                return (self.change(num))
        elif isinstance(num, list):
            number_list = num
            if len(number_list) == 1:
                if number_list[0].endswith('%'):
                    return (number_list[0])
                else:
                    return (self.change(number_list[0]))
            elif len(number_list) == 2:
                number = number_list[0]
                percentage = number_list[1]
                if percentage.endswith('%'):
                    final_percentage = percentage
                else:
                    final_percentage = str(round(float(percentage) * 100, 2)) + '%'
                number_changed = self.change(number)
                return (str(number_changed) + '(' + str(final_percentage) + ')')

    def change(self, number_raw):
        """
        Change number to human readable format

        :param number_raw:
        """
        # if isinstance(number_raw, str):
        #     if  number_raw.isdigit():
        #         number = (format(int(number_raw), ',d'))
        #     else:
        #         number = (format(float(number_raw), ',.2f'))
        # elif isinstance(number_raw, int):
        #     number = (format(int(number_raw), ',d'))
        # elif isinstance(number_raw, float):
        #     number = (format(float(number_raw), ',.2f'))

        return str(number_raw)

    def cellCutBinStat(self):
        """
        Dealing the cell bin gef file (SN.cellbin.gef)
        """
        attrs_lst = {'Mean Cell Area': 'averageArea', 'Median Cell Area': 'medianArea',
                     'Mean MID Count': 'averageExpCount', 'Median MID Count': 'medianExpCount',
                     'Mean DNB Count': 'averageDnbCount', 'Median DNB Count': 'medianDnbCount',
                     'Mean Gene Type Count': 'averageGeneCount', 'Median Gene Type Count': 'medianGeneCount'}

        cellgef = h5py.File(self.cellBinGef, 'r')

        cellCutBin_dict = defaultdict(list)
        total_dict = defaultdict()

        for k, v in attrs_lst.items():
            dk = k
            dv = self.number_transfer(str(cellgef['cellBin/cell'].attrs.get(v)[0]))
            total_dict[dk] = dv
        total_dict["Cell Count"] = cellgef['cellBin/cell'].shape[0]
        cellCutBin_dict['5.1.CellBin_Stat'].append(total_dict)

        self.result_dict['5.CellBin'] = cellCutBin_dict

    def tissueCutStat(self):
        """
        Dealing the tissue cut log file (TissueCut.log)
        """
        tissueCut_dict = defaultdict(list)
        line_num = 0
        with open(self.tissueCutLog, 'r') as file_tissue_cut:
            total_dict = defaultdict()
            name_bin_cut_list = []
            value_bin_cut_list = []
            flag_cell = 0
            for line in file_tissue_cut:
                line_num += 1
                if line_num == 1:
                    if re.search('Cell', line.strip()):
                        sub_title = '4.3.CellCut_Bin_stat'
                        total_title = '4.1.CellCut_Total_Stat'
                        final_title = '4.CellCut'
                        flag_cell = 1
                    else:
                        sub_title = '4.2.TissueCut_Bin_stat'
                        total_title = '4.1.TissueCut_Total_Stat'
                        final_title = '4.TissueCut'
                if flag_cell == 0:
                    if line_num < 10 and line_num > 1:
                        name = line.strip().split(':')[0]
                        value = self.number_transfer(line.strip().split(':')[1].replace(" ", ""))
                        total_dict[name] = value
                    else:
                        if re.search('=', line):
                            name = line.strip().split('=')[0]
                            value = line.strip().split('=')[1].replace(" ", "")
                            name_bin_cut_list.append(name)
                            value_bin_cut_list.append(value)
                            self.bin_list.append(value)
                        elif re.search(':', line):
                            name = line.strip().split(':')[0]
                            value = self.number_transfer(line.strip().split(':')[1].replace(" ", ""))
                            name_bin_cut_list.append(name)
                            value_bin_cut_list.append(value)
                elif flag_cell == 1:
                    if line_num < 9 and line_num > 1:
                        name = line.strip().split(':')[0]
                        value = self.number_transfer(line.strip().split(':')[1].replace(" ", ""))
                        total_dict[name] = value
                    else:
                        if re.search('=', line):
                            name = line.strip().split('=')[0]
                            value = line.strip().split('=')[1].replace(" ", "")
                            name_bin_cut_list.append(name)
                            value_bin_cut_list.append(value)
                        elif re.search(':', line):
                            name = line.strip().split(':')[0]
                            value = self.number_transfer(line.strip().split(':')[1].replace(" ", ""))
                            name_bin_cut_list.append(name)
                            value_bin_cut_list.append(value)
        bin_line_num = 0
        if sub_title == '4.2.TissueCut_Bin_stat':
            for i in range(len(name_bin_cut_list)):
                bin_line_num += 1
                if bin_line_num % 7 == 1:
                    temp_bin_cut_dict = {}
                    temp_bin_cut_dict[name_bin_cut_list[i]] = value_bin_cut_list[i]
                elif bin_line_num % 7 == 0:
                    temp_bin_cut_dict[name_bin_cut_list[i]] = value_bin_cut_list[i]
                    tissueCut_dict[sub_title].append(temp_bin_cut_dict)
                else:
                    temp_bin_cut_dict[name_bin_cut_list[i]] = value_bin_cut_list[i]
        else:
            temp_bin_cut_dict = {}
            for i in range(len(name_bin_cut_list)):
                bin_line_num += 1
                if bin_line_num < 11:
                    temp_bin_cut_dict[name_bin_cut_list[i]] = value_bin_cut_list[i]
            tissueCut_dict[sub_title].append(temp_bin_cut_dict)

        tissueCut_dict[total_title].append(total_dict)
        self.result_dict[final_title] = tissueCut_dict

    def filter_result(self):
        """
        Dealing the barcodeMap stat file (*read_barcodeMap.stat)
        """
        adapter_filter_dict = defaultdict(list)
        list_sample_list = []
        for fnames in self.barcodeMapStat.split(','):
            list_sample_list.append(fnames)
        for list_index in range(len(list_sample_list)):
            stat_basename_id = os.path.basename(list_sample_list[list_index])
            real_sample_id = stat_basename_id.split('_barcodeMap.stat')[0]
            stat_id = list_sample_list[list_index]
            name_key_list = ['getBarcodePositionMap_uniqBarcodeTypes', 'total_reads', 'mapped_reads',
                             'reads_with_adapter', 'fixed_sequence_contianing_reads', 'barcode_misOverlap_reads',
                             'barcode_withN_reads', 'Q10_bases_in_barcode', 'Q20_bases_in_barcode',
                             'Q30_bases_in_barcode', 'Q10_bases_in_umi', 'Q20_bases_in_umi', 'Q30_bases_in_umi',
                             'Q10_bases_in_seq', 'Q20_bases_in_seq', 'Q30_bases_in_seq', 'umi_filter_reads',
                             'umi_with_N_reads', 'umi_with_polyA_reads', 'umi_with_low_quality_base_reads',
                             'reads_with_adapter', 'reads_with_dnb']
            q30_value_list = []
            total_base_list = []
            if os.path.exists(stat_id):
                temp_dict = {}
                filter_dict = {}
                map_dict = {}
                with open(stat_id, 'r') as file_stat_id:
                    for line_file_stat_id in file_stat_id:
                        for name_key in name_key_list:
                            if re.search(name_key, line_file_stat_id):
                                map_dict['Sample_id'] = real_sample_id
                                name = line_file_stat_id.strip().split(':')[0]
                                value = line_file_stat_id.strip().split(':')[1].strip().split('\t')
                                # value = self.number_transfer(number)
                                if (name == "reads_with_adapter"):
                                    filter_dict['reads_with_adapter'] = value[0]
                                elif (name == "reads_with_dnb"):
                                    filter_dict['reads_with_dnb'] = value[0]
                                else:
                                    temp_dict[name] = value[0]
                                    map_dict[name] = self.number_transfer(value)
                    if len(map_dict) == 0:
                        self.print_err("lack statistic info in {}".format(stat_id), "SAW-A90004")
                filter_dict['Sample_Name'] = real_sample_id
                filter_dict['Raw_Reads'] = self.number_transfer(
                    int(temp_dict['mapped_reads']) - int(temp_dict['umi_filter_reads']))
                filter_dict['Clean_Reads'] = self.number_transfer(
                    int(temp_dict['mapped_reads']) - int(temp_dict['umi_filter_reads']) - int(
                        filter_dict['reads_with_adapter']) - int(filter_dict['reads_with_dnb']))
                filter_dict['Low_Quality_Reads'] = '0'
                filter_dict['Too_Many_N_Reads'] = '0'
                filter_dict['Too_Long_Reads'] = '0'
                filter_dict['Remarks'] = '0'
                filter_dict['reads_with_adapter'] = self.number_transfer(filter_dict['reads_with_adapter'])
                filter_dict['reads_with_dnb'] = self.number_transfer(filter_dict['reads_with_dnb'])

                adapter_filter_dict['1.1.Adapter_Filter'].append(map_dict)
                adapter_filter_dict['1.2.Filter_Stat'].append(filter_dict)
            else:
                self.print_err(os.path.abspath(stat_id), 'SAW-A90002')

        self.result_dict['1.Filter_and_Map'] = adapter_filter_dict

    def filter_result_bcstar_v2(self):
        """
        Dealing the barcodeMap stat file (*read_barcodeMap.stat)
        """
        adapter_filter_dict = defaultdict(list)
        list_sample_list = []
        for fnames in self.barcodeMapStat.split(','):
            if (not os.path.exists(fnames)):
                self.print_err(os.path.abspath(fnames), "SAW-A90002")
            list_sample_list.append(fnames)
        for list_index in range(len(list_sample_list)):
            stat_basename_id = os.path.basename(list_sample_list[list_index])
            real_sample_id = stat_basename_id.split('_barcodeMap.stat')[0]
            stat_id = list_sample_list[list_index]
            name_key_list = ['unique_CID_in_mask', 'total_reads', 'CID_mapped_reads', 'reads_with_adapter',
                             'fixed_sequence_contianing_reads', 'CID_mapped_reads_with_mismatch', 'CID_with_N_reads',
                             'Q10_bases_in_CID', 'Q20_bases_in_CID', 'Q30_bases_in_CID', 'Q10_bases_in_MID',
                             'Q20_bases_in_MID', 'Q30_bases_in_MID', 'Q10_bases_in_seq', 'Q20_bases_in_seq',
                             'Q30_bases_in_seq', 'discarded_MID_reads', 'MID_with_N_reads', 'MID_with_polyA_reads',
                             'MID_with_low_quality_base_reads', 'reads_with_dnb']
            q30_value_list = []
            total_base_list = []
            if os.path.exists(stat_id):
                temp_dict = {}
                filter_dict = {}
                map_dict = {}
                with open(stat_id, 'r') as file_stat_id:
                    for line_file_stat_id in file_stat_id:
                        for name_key in name_key_list:
                            if re.search(name_key, line_file_stat_id):
                                map_dict['Sample_id'] = real_sample_id
                                name = line_file_stat_id.strip().split(':')[0]
                                value = line_file_stat_id.strip().split(':')[1].strip().split('\t')
                                # value = self.number_transfer(number)
                                if (name == "reads_with_adapter"):
                                    filter_dict['reads_with_adapter'] = value[0]
                                elif (name == "reads_with_dnb"):
                                    filter_dict['reads_with_dnb'] = value[0]
                                elif (name == "unique_CID_in_mask"):
                                    filter_dict['getBarcodePositionMap_uniqBarcodeTypes'] = value[0]
                                elif (name == "unique_CID_in_fq"):
                                    filter_dict['mapped_dnbs'] = value[0]
                                elif (name == "CID_mapped_reads"):
                                    filter_dict['mapped_reads'] = value[0]
                                elif (name == "CID_exactly_mapped_reads"):
                                    filter_dict['barcode_exactlyOverlap_reads'] = value[0]
                                elif (name == "CID_mapped_reads_with_mismatch"):
                                    filter_dict['barcode_misOverlap_read'] = value[0]
                                elif (name == "CID_with_N_reads"):
                                    filter_dict['barcode_withN_reads'] = value[0]
                                elif (name == "short_reads_filtered_with_polyA"):
                                    filter_dict['reads_filteredByPolyA'] = value[0]
                                elif (name == "discarded_MID_reads"):
                                    filter_dict['umi_filter_reads'] = value[0]
                                elif (name == "MID_with_N_reads"):
                                    filter_dict['umi_with_N_reads'] = value[0]
                                elif (name == "MID_with_polyA_reads"):
                                    filter_dict['umi_with_polyA_reads'] = value[0]
                                elif (name == "MID_with_low_quality_base_reads"):
                                    filter_dict['umi_with_low_quality_base_reads'] = value[0]
                                elif (name == "Q10_bases_in_MID"):
                                    filter_dict['Q10_bases_in_umi'] = value[0]
                                elif (name == "Q20_bases_in_MID"):
                                    filter_dict['Q20_bases_in_umi'] = value[0]
                                elif (name == "Q30_bases_in_MID"):
                                    filter_dict['Q30_bases_in_umi'] = value[0]
                                elif (name == "Q10_bases_in_CID"):
                                    filter_dict['Q10_bases_in_barcode'] = value[0]
                                elif (name == "Q20_bases_in_CID"):
                                    filter_dict['Q20_bases_in_barcode'] = value[0]
                                elif (name == "Q30_bases_in_CID"):
                                    filter_dict['Q30_bases_in_barcode'] = value[0]
                                else:
                                    temp_dict[name] = value[0]
                                    map_dict[name] = self.number_transfer(value)
                        if len(map_dict) == 0:
                            self.print_err("lack statistic info in {}".format(stat_id), "SAW-A90004")
                filter_dict['Sample_Name'] = real_sample_id
                filter_dict['Raw_Reads'] = self.number_transfer(
                    int(temp_dict['mapped_reads']) - int(temp_dict['discarded_MID_reads']))
                filter_dict['Clean_Reads'] = self.number_transfer(
                    int(temp_dict['mapped_reads']) - int(temp_dict['discarded_MID_reads']) - int(
                        filter_dict['reads_with_adapter']) - int(filter_dict['reads_with_dnb']))
                filter_dict['Low_Quality_Reads'] = '0'
                filter_dict['Too_Many_N_Reads'] = '0'
                filter_dict['Too_Long_Reads'] = '0'
                filter_dict['Remarks'] = '0'
                filter_dict['reads_with_adapter'] = self.number_transfer(filter_dict['reads_with_adapter'])
                filter_dict['reads_with_dnb'] = self.number_transfer(filter_dict['reads_with_dnb'])

                adapter_filter_dict['1.1.Adapter_Filter'].append(map_dict)
                adapter_filter_dict['1.2.Filter_Stat'].append(filter_dict)

            else:
                self.print_err(os.path.abspath(stat_id), 'SAW-A90002')

        self.result_dict['1.Filter_and_Map'] = adapter_filter_dict

    def alignment_result(self):
        """
        Dealing the alignment log file (*.Log.final.out)
        """
        alignment_dict = defaultdict(list)
        list_sample_id_list = []

        temp_dedup_dict = {}
        temp_annotation_dict = {}

        for fnames in self.alignmentLog.split(','):
            if fnames.endswith('.Log.final.out'):
                if (not os.path.exists(fnames)):
                    self.print_err(os.path.abspath(fnames), "SAW-A90002")
                sample_id = os.path.basename(fnames).split('.Log.final.out')[0]
                star_log = fnames
                line_num = 0
                temp_input_read_dict = {}
                temp_uniq_dict = {}
                temp_multi_dict = {}
                temp_unmapping_dict = {}
                temp_chimeric_dict = {}
                with open(star_log, 'r') as file_star_log:
                    for line_file_star_log in file_star_log:
                        temp_input_read_dict['Sample_Id'] = sample_id
                        temp_uniq_dict['Sample_Id'] = sample_id
                        temp_multi_dict['Sample_Id'] = sample_id
                        temp_unmapping_dict['Sample_Id'] = sample_id
                        temp_chimeric_dict['Sample_Id'] = sample_id
                        line_num = line_num + 1
                        if line_num < 5:
                            continue
                        elif line_num == 6:
                            temp_input_read_dict['Number_Of_Input_Reads'] = self.number_transfer(
                                line_file_star_log.strip().split('|')[1].replace("\t", ""))
                        elif line_num == 7:
                            temp_input_read_dict['Average_Input_Read_Length'] = self.number_transfer(
                                line_file_star_log.strip().split('|')[1].replace("\t", ""))
                        elif line_num == 9:
                            temp_uniq_dict['Mapped_Reads_Number'] = self.number_transfer(
                                line_file_star_log.strip().split('|')[1].replace("\t", ""))
                        elif line_num == 10:
                            temp_uniq_dict['Mapped_Reads(%)'] = line_file_star_log.strip().split('|')[1].replace("\t",
                                                                                                                 "")
                        elif line_num == 11:
                            temp_uniq_dict['Average_Mapped_Length'] = self.number_transfer(
                                line_file_star_log.strip().split('|')[1].replace("\t", ""))
                        elif line_num == 24:
                            multiRead = self.number_transfer(line_file_star_log.strip().split('|')[1].replace("\t", ""))
                        elif line_num == 25:
                            multiRead_percentage = line_file_star_log.strip().split('|')[1].replace("\t", "")
                            temp_multi_dict['Multiple_Loci'] = multiRead + '(' + multiRead_percentage + ')'
                        elif line_num == 26:
                            manyRead = self.number_transfer(line_file_star_log.strip().split('|')[1].replace("\t", ""))
                        elif line_num == 27:
                            manyRead_percentage = line_file_star_log.strip().split('|')[1].replace("\t", "")
                            temp_multi_dict['Many_Loci'] = manyRead + '(' + manyRead_percentage + ')'
                        elif line_num == 29:
                            mismatch_read = self.number_transfer(
                                line_file_star_log.strip().split('|')[1].replace("\t", ""))
                        elif line_num == 30:
                            mismatch_read_percentage = line_file_star_log.strip().split('|')[1].replace("\t", "")
                            temp_unmapping_dict[
                                'Too_Many_Mismatches'] = mismatch_read + '(' + mismatch_read_percentage + ')'
                        elif line_num == 31:
                            too_short_read = self.number_transfer(
                                line_file_star_log.strip().split('|')[1].replace("\t", ""))
                        elif line_num == 32:
                            too_short_read_percentage = line_file_star_log.strip().split('|')[1].replace("\t", "")
                            temp_unmapping_dict['Too_Short'] = too_short_read + '(' + too_short_read_percentage + ')'
                        elif line_num == 33:
                            other_read = self.number_transfer(
                                line_file_star_log.strip().split('|')[1].replace("\t", ""))
                        elif line_num == 34:
                            other_read_percentage = line_file_star_log.strip().split('|')[1].replace("\t", "")
                            temp_unmapping_dict['Other'] = other_read + '(' + other_read_percentage + ')'
                        elif line_num == 36:
                            chimeric_read = self.number_transfer(
                                line_file_star_log.strip().split('|')[1].replace("\t", ""))
                        elif line_num == 37:
                            chimeric_read_percentage = line_file_star_log.strip().split('|')[1].replace("\t", "")
                            temp_chimeric_dict[
                                'Number_Of_Chimeric_Reads'] = chimeric_read + '(' + chimeric_read_percentage + ')'
                alignment_dict['2.1.Input_Read'].append(temp_input_read_dict)
                alignment_dict['2.2.Uniquely_Mapped_Read'].append(temp_uniq_dict)
                alignment_dict['2.3.Multi_Mapping_Read'].append(temp_multi_dict)
                alignment_dict['2.4.Unmapping_Read'].append(temp_unmapping_dict)
                alignment_dict['2.5.Chimeric_Read'].append(temp_chimeric_dict)

            else:
                self.print_err(fnames, 'SAW-A90003')

        for fnames in self.alignmentStat.split(','):
            if fnames.endswith('summary.stat'):
                dedup_file = fnames
                line_num = 0
                with open(dedup_file, 'r') as file_dedup_file:
                    for line in file_dedup_file:
                        line_num = line_num + 1
                        if line_num == 2:
                            name_dup_list = line.strip().split('\t')
                        elif line_num == 3:
                            value_dup_list = line.strip().split('\t')
                            for i in range(len(name_dup_list)):
                                if name_dup_list[i] in temp_dedup_dict.keys():
                                    temp_dedup_dict[name_dup_list[i]].append(float(value_dup_list[i]))
                                else:
                                    temp_dedup_dict[name_dup_list[i]] = [float(value_dup_list[i])]
                        elif line_num == 5:
                            name_annotation_list = line.strip().split('\t')
                        elif line_num == 6:
                            value_annotation_list = line.strip().split('\t')
                            for i in range(len(name_annotation_list)):
                                if name_annotation_list[i] in temp_annotation_dict.keys():
                                    temp_annotation_dict[name_annotation_list[i]] = temp_annotation_dict[
                                                                                        name_annotation_list[
                                                                                            i]] + float(
                                        value_annotation_list[i])
                                else:
                                    temp_annotation_dict[name_annotation_list[i]] = float(value_annotation_list[i])
            else:
                self.print_err(".summary.stat", 'SAW-A90002')

        for k, v in temp_dedup_dict.items():
            if k != 'Sample_Id':
                if k == 'FAIL_FILTER_RATE' or k == 'FAIL_ANNOTATE_RATE' or k == 'DUPLICATION_RATE':
                    temp_dedup_dict[k] = self.number_transfer(mean(v))
                else:
                    temp_dedup_dict[k] = self.number_transfer(sum(v))

        for k, v in temp_annotation_dict.items():
            if k != 'Sample_Id':
                temp_annotation_dict[k] = self.number_transfer(v)

        alignment_dict['2.6.Filter_And_Deduplication'].append(temp_dedup_dict)
        alignment_dict['2.7.Annotation'].append(temp_annotation_dict)

        self.result_dict['2.Alignment'] = alignment_dict


class myThread(threading.Thread):
    def __init__(self, command):
        threading.Thread.__init__(self)
        self.cmd = command

    def run(self):
        os.system(self.cmd)


def cgef_stat_addition(input_cgef_path, output_figure_path):
    b = 1
    scapath = os.path.join(output_figure_path, "scatter_{0}x{0}_cellarea_dnbs.png".format(b if b != 0 else "cell"))
    scapath1 = os.path.join(output_figure_path, "scatter_{0}x{0}_midcount_dnbs.png".format(b if b != 0 else "cell"))
    plt.figure(figsize=(5, 5))

    cgef = h5py.File(input_cgef_path)
    df = pd.DataFrame(cgef['cellBin']['cell']['expCount', 'dnbCount', 'area'])
    df = df.rename(columns={'expCount': 'MID Count', 'dnbCount': 'DNB Number', 'area': 'Cell Area'})

    plt.scatter(df['Cell Area'], df['DNB Number'], color="gray", edgecolors="gray", s=0.8)
    plt.grid()
    plt.xlabel("cell area(pixel)")
    plt.ylabel("mRNA-captured DNBs")
    plt.savefig(scapath, format="png", bbox_inches="tight")

    plt.scatter(df['MID Count'], df['DNB Number'], color="gray", edgecolors="gray", s=0.8)
    plt.xlabel("MID Count")
    plt.ylabel("mRNA-captured DNBs")
    plt.savefig(scapath1, format="png", bbox_inches="tight")


if __name__ == "__main__":
    main()
