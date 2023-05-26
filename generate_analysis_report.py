# -*- coding:utf-8 -*-
# Copyright (C) BGI-Reasearch - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by STOmics development team P_stomics_dev@genomics.cn, May 2017

import os, sys
from optparse import OptionParser
from collections import defaultdict
import plotly
import numpy as np
import pandas as pd
import plotly.express as px
import h5py
import plotly.graph_objects as go
import json
import anndata
from PIL import Image
from pandas.core.frame import DataFrame
import matplotlib as mpl
from decimal import Decimal
from static_info import FILTER_COLLAPSE, hovertext_dict, parents_dict, parents_dict_sort, SUNBURST_COLLAPSE, SUNBURST_DEV_COLLAPSE, QUALITY_COLLAPSE, RNA_MAPPING_COLLAPSE, ANNOTATION_COLLAPSE, SPOT_SUMMARY_COLLAPSE, TissueCut_Bin_SUMMARY_COLLAPSE, Cell_Bin_SUMMARY_COLLAPSE, IMAGE_QC_COLLAPSE, IMAGE_STITCH_COLLAPSE, IMAGE_REGISTRATION_COLLAPSE, SUNBURST_COLLAPSE_TOB,SPOT_SUMMARY_COLLAPSE_DEV
from component import bin_canvas
import base64
import math
import locale
import time
from toBhtmlTemplate import html_template
from researchhtmlTemplate import html_research_template
from researchhtmlNoRpiTemplate import html_research_no_rpi_template
from researchhtmlNoCellTemplate import html_research_no_cell_template
from toBhtmlNoRpiTemplate import html_no_rpi_template
from toBhtmlNoCellTemplate import html_no_cell_template

color_map = {
    "DAPI":"#0000FF",
    "IF1":"#00FFFF",
    "IF2":"#FF00FF",
    "IF3":"#00FF00",
    "IF4":"#FFFF00",
    "IF5":"#FF0000",
    "IF6":"#FF9600",
}

# def generate_html_function(sn, resultPath, h5_file, h5ad_file, json_file, bin200Saturation, bin200violin, saturation, research_version='N', \
#     pipeline_Version='N', rpi_file='N', rpi_resolution=100, bin200MIDGeneDNB='N', bin1Saturation='N', bin50Saturation='N', bin50violin='N', bin50MIDGeneDNB='N', \
#     bin100Saturation='N', bin100violin='N', bin100MIDGeneDNB='N', binCellSaturation='N', binCellviolin='N', binCellMIDGeneDNB='N',midCellSaturation='N',areaCellSaturation='N', \
#     bin150Saturation='N', bin150violin='N', bin150MIDGeneDNB='N', cellCluster='N', iprFile='N', species='N', tissue='N', reference='N', logo='N'):
def generate_html_function(sn, resultPath, h5_file, h5ad_file, json_file, saturation, research_version='N', \
    pipeline_Version='N', rpi_file='N', rpi_resolution=100, bin1Saturation='N', \
    binCellSaturation='N', binCellviolin='N', binCellMIDGeneDNB='N',midCellSaturation='N',areaCellSaturation='N', \
    cellCluster='N', iprFile='N', species='N', tissue='N', reference='N', logo='N', bin_fig={}, bin_list=[]):

    """
    Generate raw html report file

    :param sn: Serial Number
    :param resultPath: Output path
    :param h5_file: The stereomics h5 file or gef file (stereomics.h5 or SN.gef)
    :param h5ad_file: The cluster h5ad file (cell_cluster.h5ad)
    :param json_file: The statistic json file (SN.statistics.json)
    :param bin200Saturation: The bin200 saturation img (scatter_200x200_MID_gene_counts.png)
    :param bin200violin: The bin200 violin img (violin_200x200_MID_gene.png)
    :param saturation: The sequence saturation img (plot_200x200_saturation.png)
    :param research_version: research_version/standard_version
    :param pipeline_Version: The analysis pipeline version
    :param rpi_file: The rpi file (.ssDNA.rpi)
    :param rpi_resolution: The resolution of rpi file
    :param bin200MIDGeneDNB: The png of statistic 200x200 MID gene DNB (statistic_200x200_MID_gene_DNB.png)
    :param bin1Saturation: The bin1 saturation img (plot_1x1_saturation.png)
    :param bin50Saturation: The bin50 saturation img (scatter_50x50_MID_gene_counts.png)
    :param bin50violin: The bin50 violin img (violin_50x50_MID_gene.png)
    :param bin50MIDGeneDNB: The png of statistic 50x50 MID gene DNB (statistic_50x50_MID_gene_DNB.png)
    :param bin100Saturation: The bin100 saturation img (scatter_100x100_MID_gene_counts.png)
    :param bin100violin: The bin100 violin img (violin_100x100_MID_gene.png)
    :param bin100MIDGeneDNB: The png of statistic 100x100 MID gene DNB (statistic_100x100_MID_gene_DNB.png)
    :param binCellSaturation: The binCell saturation img (scatter_CellxCell_MID_gene_counts.png)
    :param binCellviolin: The binCell violin img (violin_CellxCell_MID_gene.png)
    :param midCellSaturation:  Scatter plot of MID count and mRNA-captured DNBs in each bin(scatter_1x1_midcount_dnbs.png)
    :param areaCellSaturation: Scatter plot of cell area (pixel) and mRNA-captured DNBs in each bin (scatter_1x1_cellarea_dnbs.png)
    :param binCellMIDGeneDNB: The png of statistic CellxCell MID gene DNB (statistic_CellxCell_MID_gene_DNB.png)
    :param bin150Saturation: The bin150 saturation img (scatter_150x150_MID_gene_counts.png)
    :param bin150violin: The bin150 violin img (violin_150x150_MID_gene.png)
    :param bin150MIDGeneDNB: The png of statistic 150x150 MID gene DNB (statistic_150x150_MID_gene_DNB.png)
    :param cellCluster: The cell cluster h5ad file (SN.cell.cluster.h5ad)
    :param iprFile: The ipr file (SN.ipr)
    :param species: The species
    :param tissue: The tissue
    :param reference: The reference which used to mapping
    """

    # bin200_saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin200Saturation, 'rb').read()).decode('ascii'))
    # bin200_saturation_img = '<img style="height:400px;width:400px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(bin200_saturation_fig)

    # bin200_violin_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin200violin, 'rb').read()).decode('ascii'))
    # bin200_violin_img = '<img style="height:400px;width:700px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(bin200_violin_fig)

    saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(saturation, 'rb').read()).decode('ascii'))
    saturation_img = '<img id="saturation_plot" src={0} onclick="openImgBig(this.src)" style="cursor: pointer;">'.format(saturation_fig)
    if rpi_file != 'N':
        rpi_file = rpi_file
    else:
        rpi_file = ''

    if logo != 'N':
        logo_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(logo, 'rb').read()).decode('ascii'))
        logo_img = '<img src={0}>'.format(logo_fig)
    else:
        logo_img = '<img>'

    ###判断是否有分析流程版本信息###
    if pipeline_Version == 'N':
        pipeline_version = ''
    else:
        pipeline_version = pipeline_Version

    ###判断是研发版本或者商业版本###
    if research_version.upper() != "N":
        bin1_saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin1Saturation, 'rb').read()).decode('ascii'))
        bin1_saturation_img = '<img style="height:400px;width:1000px;cursor: pointer;" id="bin1_plot" src={0} onclick="openImg(this.src)">'.format(bin1_saturation_fig)

    binsize_canvas = ""
    # bin_list.sort()
    for i in bin_list:
        if i == '1':
            continue
        binsize_canvas += get_canvas(i, bin_fig)

    # bin200MIDGeneDNB_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin200MIDGeneDNB, 'rb').read()).decode('ascii'))
    # bin200MIDGeneDNB_img = '<img id="bin200MIDGeneDNB_plot" src={0} onclick="openImgBig(this.src)" style="cursor: pointer;">'.format(bin200MIDGeneDNB_fig)

    # bin50_saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin50Saturation, 'rb').read()).decode('ascii'))
    # bin50_saturation_img = '<img style="height:400px;width:400px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(bin50_saturation_fig)

    # bin50_violin_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin50violin, 'rb').read()).decode('ascii'))
    # bin50_violin_img = '<img style="height:400px;width:700px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(bin50_violin_fig)

    # bin50MIDGeneDNB_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin50MIDGeneDNB, 'rb').read()).decode('ascii'))
    # bin50MIDGeneDNB_img = '<img id="bin50MIDGeneDNB_plot" src={0} onclick="openImgBig(this.src)" style="cursor: pointer;">'.format(bin50MIDGeneDNB_fig)

    # bin100_saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin100Saturation, 'rb').read()).decode('ascii'))
    # bin100_saturation_img = '<img style="height:400px;width:400px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(bin100_saturation_fig)

    # bin100_violin_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin100violin, 'rb').read()).decode('ascii'))
    # bin100_violin_img = '<img style="height:400px;width:700px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(bin100_violin_fig)

    # bin100MIDGeneDNB_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin100MIDGeneDNB, 'rb').read()).decode('ascii'))
    # bin100MIDGeneDNB_img = '<img id="bin100MIDGeneDNB_plot" src={0} onclick="openImgBig(this.src)" style="cursor: pointer;">'.format(bin100MIDGeneDNB_fig)

    # bin150_saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin150Saturation, 'rb').read()).decode('ascii'))
    # bin150_saturation_img = '<img style="height:400px;width:400px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(bin150_saturation_fig)

    # bin150_violin_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin150violin, 'rb').read()).decode('ascii'))
    # bin150_violin_img = '<img style="height:400px;width:700px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(bin150_violin_fig)

    # bin150MIDGeneDNB_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(bin150MIDGeneDNB, 'rb').read()).decode('ascii'))
    # bin150MIDGeneDNB_img = '<img id="bin100MIDGeneDNB_plot" src={0} onclick="openImgBig(this.src)" style="cursor: pointer;">'.format(bin150MIDGeneDNB_fig)

    if binCellSaturation != 'N' and research_version.upper() == 'N':
        binCell_saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(binCellSaturation, 'rb').read()).decode('ascii'))
        binCell_saturation_img = '<img style="height:400px;width:400px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(binCell_saturation_fig)
    elif binCellSaturation != 'N':
        binCell_saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(binCellSaturation, 'rb').read()).decode('ascii'))
        binCell_saturation_img = '<img style="height:200px;width:200px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(binCell_saturation_fig)
    else:
        binCell_saturation_img = ''
    if binCellviolin != 'N' and research_version.upper() == 'N':
        binCell_violin_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(binCellviolin, 'rb').read()).decode('ascii'))
        binCell_violin_img = '<img style="height:400px;width:700px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(binCell_violin_fig)
    elif binCellviolin != 'N':
        binCell_violin_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(binCellviolin, 'rb').read()).decode('ascii'))
        binCell_violin_img = '<img style="height:200px;width:350px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(binCell_violin_fig)
    else:
        binCell_violin_img = ''
    if binCellMIDGeneDNB != 'N' and research_version.upper() == 'N':
        binCellMIDGeneDNB_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(binCellMIDGeneDNB, 'rb').read()).decode('ascii'))
        binCellMIDGeneDNB_img = '<img id="binCellMIDGeneDNB_plot" src={0} onclick="openImgBig(this.src)" style="cursor: pointer;">'.format(binCellMIDGeneDNB_fig)
    elif binCellMIDGeneDNB != 'N':
        binCellMIDGeneDNB_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(binCellMIDGeneDNB, 'rb').read()).decode('ascii'))
        binCellMIDGeneDNB_img = '<img id="binCellMIDGeneDNB_plot" src={0} onclick="openImgBig(this.src)" style="cursor: pointer;">'.format(binCellMIDGeneDNB_fig)
    else:
        binCellMIDGeneDNB_img = ''
    if midCellSaturation != 'N' and research_version.upper() == 'Y':
        midCell_saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(midCellSaturation, 'rb').read()).decode('ascii'))
        midCell_saturation_img = '<img style="height:200px;width:200px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(midCell_saturation_fig)
    else:
        midCell_saturation_img = ''
    if areaCellSaturation != 'N' and research_version.upper() == 'Y':
        areaCell_saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(areaCellSaturation, 'rb').read()).decode('ascii'))
        areaCell_saturation_img = '<img style="height:200px;width:200px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(areaCell_saturation_fig)
    else:
        areaCell_saturation_img = ''

    if h5_file != '':
        if h5_file.endswith('h5'):
            df_h5 = read_h5_file(h5_file)
            dnb_df_range = read_dnb_range_from_h5(h5_file)
        elif h5_file.endswith('gef'):
            df_h5, dnb_df_range = read_gef_file(h5_file)
        plot_y_range = dnb_df_range['max_y'] - dnb_df_range['min_y']
        plot_x_range = dnb_df_range['max_x'] - dnb_df_range['min_x']
        marker_x = [dnb_df_range['max_x'] + 500]
        marker_y = [dnb_df_range['min_y'] + 500]
        ratio_dnb = plot_y_range/plot_x_range
        ratio_plot = 600/720
        if ratio_dnb >= ratio_plot:
            ploy_height = 600
            bin_size = 200
            dot_size_h5 = round(ploy_height/(plot_y_range/bin_size),2)
        else:
            ploy_width = 720
            bin_size = 200
            dot_size_h5 = round(ploy_width/(plot_x_range/bin_size),2)
    else:
        dnb_df_range = {}
    ###如果bin 200聚类结果存在
    if h5ad_file !='':
        bin_size = 200
        adata = read_h5ad_file(h5ad_file)
        total_data_str, total_cluster = generate_cluster_data(h5ad_file,adata, bin_size)
        total_data_class_str, total_class = generate_class_data(h5ad_file,adata, bin_size)
    ###如果cell Bin结果存在
    if cellCluster !='N':
        bin_size = 40
        cellClusterAdata = read_h5ad_file(cellCluster)
        total_cell_data_str, total_cell_cluster = generate_cluster_data(cellCluster,cellClusterAdata, bin_size)
        total_cell_data_class_str, total_cell_class = generate_class_data(cellCluster,cellClusterAdata, bin_size)
    else:
        total_cell_data_str = ''
        total_cell_cluster = []
        total_cell_data_class_str = ''
        total_cell_class = []

    image_heatmap_div = '<div></div>'
    manual_scale_x, manual_scale_y, manual_rotation = "-", "-", "-"
    if iprFile != 'N':
        with h5py.File(iprFile, 'r') as f:
            if "ImageInfo" in f.keys():
                image_manufacture, image_model, scan_time, overlap, exposure_time, scan_rows, scan_columns, fov_height, fov_width, experimenter, stain_type, stitched_image, image_name, \
                    imageqc_version, qc_pass, track_line_score, clarity_score, good_fov_count, total_fov_count, stitching_score, tissue_seg_score, registration_score, \
                    template_source_x, template_source_y, global_height, global_width, \
                    scaleX, scaleY, rotation, flip, image_offset_x, image_offset_y, counter_rotation, matrix_x_start, matrix_y_start, matrix_width, matrix_height, image_heatmap_div = get_image_info_ipr(iprFile)
            else:
                image_manufacture, image_model, scan_time, overlap, exposure_time, scan_rows, scan_columns, fov_height, fov_width, experimenter, stain_type, stitched_image, image_name, \
                    imageqc_version, qc_pass, track_line_score, clarity_score, good_fov_count, total_fov_count, stitching_score, tissue_seg_score, registration_score, \
                    template_source_x, template_source_y, global_height, global_width, \
                    scaleX, scaleY, rotation, flip, image_offset_x, image_offset_y, counter_rotation, manual_scale_x, manual_scale_y, manual_rotation, matrix_x_start, matrix_y_start, matrix_width, matrix_height, image_heatmap_div = get_info_ipr_layer(iprFile)
    else:
        image_manufacture, image_model, scan_time, overlap, exposure_time, scan_rows, scan_columns, fov_height, fov_width, experimenter, stain_type, stitched_image, image_name = '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'
        imageqc_version, qc_pass, track_line_score, clarity_score, good_fov_count, total_fov_count, stitching_score, tissue_seg_score, registration_score =  '-','-','-','-','-','-','-','-','-'
        template_source_x, template_source_y, global_height, global_width = '-','-','-','-'
        scaleX, scaleY, rotation, flip, image_offset_x, image_offset_y, counter_rotation, matrix_x_start, matrix_y_start, matrix_width, matrix_height, = '-','-','-','-','-','-','-','-','-','-','-'
        image_heatmap_div = '<div></div>'

    if rpi_file !='':
        HE_path, HE_name, image_type, init_image_info = find_bg_images_info(rpi_file, 'ssDNA')
        plot_range = {'x0': init_image_info['x_start'], 'x1': init_image_info['x_start'] + init_image_info['sizex'],'y0': init_image_info['y_start'] - init_image_info['sizey'], 'y1': init_image_info['y_start']}
        plot_bin_size = {'dnb_res': rpi_resolution, 'dot_x': 200}
        images_small_dict = {}
        images_small = []
        images_small_cluster = []
        image_list=[]
        if len(init_image_info['layer']) > 0:
            for layer in init_image_info['layer']:
                image_list=showspan(init_image_info['layer'])
                images=get_small_images(HE_path, HE_name, plot_range, plot_bin_size,layer=layer)
                images_small_dict[layer] = images
                # images_small_cluster = images
                images_small = images
            for layer in images_small_dict.keys():
                if layer.upper()== "DAPI" or layer.upper()=="SSDNA" or layer.upper()=="HE":
                    # images_small_cluster = images
                    images_small = images_small_dict[layer]
            if "DAPI" in images_small_dict.keys():
                images_small_cluster = get_color_img(HE_path, HE_name, plot_range, plot_bin_size)
            else:
                images_small_cluster = images_small
        else:
            images_small = get_small_images(HE_path, HE_name, plot_range, plot_bin_size)
            images_small_dict['ssDNA'] = images_small
            images_small_cluster = images_small
        # images_small_cluster = get_small_images(HE_path, HE_name, plot_range, plot_bin_size)
    else:
        images_small_dict = {}
        image_list=[]
        images_small = []
        images_small_cluster = []
    if json_file != '':
        df_sun, sun_name_pro, fastq_name_str, Total_reads, Valid_CID_Reads, Clean_Reads, Reads_Mapped_to_Genome_reads, Unique_Reads, Duplicated_Reads, \
        Q30_Barcode_Rate, Q30_MID_Rate, Q30_seq_Rate, Input_read, Uniquely_Mapped_Read, Multi_Mapping_Read,\
        RNA_Unmapping_Read, Exonic, Intronic,Intergenic, Transcriotome, Antisense, \
        Contour_area, Number_of_DNB_under_tissue,ratio_of_dnb_under_tissue, Ratio,Total_Gene_type, MID_counts, Fraction_MID_in_Spots_Under_Tissue, Reads_under_tissue, Fraction_Reads_in_Spots_Under_Tissue, bin_div_title, Mean_Gene_per_bin200, Mean_UMI_per_bin200, \
        Too_Many_N_Reads, Low_Quality_Reads, Raw_Reads, Q30_Before_Filtering, Q30_After_Filtering, Too_Short_Reads, Reads_With_Adapter, Reads_With_DNB, mean_cell_area,cell_count, median_cell_area, mean_mid_count, median_mid_count, mean_dnb_count, median_dnb_count, mean_gene_type_count, median_gene_type_count, \
        Invalid_CID_Reads, Discarded_MID_Reads, \
        persent_total_reads,persent_cid_reads,persent_clean_reads,persent_unique_mapping_reads, \
        persent_transcriptome,persent_unique_reads,persent_duplicated_reads, \
        persent_intergenic,persent_multi_mapping_reads,persent_unmapping_reads,persent_too_short_reads, \
        persent_invalid_cid_reads,persent_discarded_mid_reads= get_sun_fig(json_file, research_version)
    sn_name = sn + '.report.tmp.html'
    html_report = os.path.join(resultPath, sn_name)
    sunburst_collapse = showCollapse(SUNBURST_COLLAPSE)
    sunburst_collapse_toB = showCollapse(SUNBURST_COLLAPSE_TOB)
    sunburst_dev_collapse = showCollapse(SUNBURST_DEV_COLLAPSE)
    quality_collapse = showCollapse(QUALITY_COLLAPSE)
    filter_collapse = showCollapse(FILTER_COLLAPSE)
    rna_collapse = showCollapse(RNA_MAPPING_COLLAPSE)
    rna_annotation_collapse = showCollapse(ANNOTATION_COLLAPSE)
    tissueCut_total_collapse = showCollapse(SPOT_SUMMARY_COLLAPSE)
    tissueCut_total_collapse_dev = showCollapse(SPOT_SUMMARY_COLLAPSE_DEV)
    tissueCut_bin_collapse = showCollapse(TissueCut_Bin_SUMMARY_COLLAPSE)
    cell_bin_collapse =  showCollapse(Cell_Bin_SUMMARY_COLLAPSE)
    image_qc_collapse = showCollapse(IMAGE_QC_COLLAPSE)
    image_stitch_collapse = showCollapse(IMAGE_STITCH_COLLAPSE)
    image_registration_collapse = showCollapse(IMAGE_REGISTRATION_COLLAPSE)


    ###商业版本###
    try:
        if research_version.upper() == 'N': 
            if rpi_file !='':
                if cellCluster != 'N':
                    html_toB_final_template = html_template
                else:
                    html_toB_final_template = html_no_cell_template
            else:
                html_toB_final_template = html_no_rpi_template
            with open(html_report,'w',encoding='utf-8') as f:
                f.write(html_toB_final_template.format(logo_img=logo_img, sn_name=sn, species=species, tissue=tissue, reference=reference,fastq_name=fastq_name_str,Total_read=Total_reads,Mean_UMI_per_bin200=Mean_UMI_per_bin200,Mean_Gene_per_bin200=Mean_Gene_per_bin200,\
                    sunburst_total_reads=Total_reads,valid_cid_reads=Valid_CID_Reads,invalid_cid_reads=Invalid_CID_Reads,discarded_mid_reads=Discarded_MID_Reads,clean_reads=Clean_Reads,reads_mapped_to_genome=Reads_Mapped_to_Genome_reads, unique_reads=Unique_Reads, duplicated_reads=Duplicated_Reads,\
                    sequencing_total_reads=Total_reads,rate_of_q30_bases_in_cid=Q30_Barcode_Rate,rate_of_q30_bases_in_mid=Q30_MID_Rate,rate_of_q30_bases_in_seq=Q30_seq_Rate,\
                    filter_collapse=filter_collapse,valid_cid_filter_reads=Valid_CID_Reads,q30_base_before_filtering=Q30_Before_Filtering,clean_filter_reads=Clean_Reads,q30_base_after_filtering=Q30_After_Filtering,low_quality_reads=Low_Quality_Reads,too_many_n_reads=Too_Many_N_Reads,too_short_reads=Too_Short_Reads,reads_with_adapter=Reads_With_Adapter,reads_with_dnb=Reads_With_DNB,\
                    rna_clean_reads=Input_read,unique_mapping_reads=Uniquely_Mapped_Read,multiple_mapping_reads=Multi_Mapping_Read,rna_unmapping_reads=RNA_Unmapping_Read,\
                    exonic=Exonic,intronic=Intronic,intergenic=Intergenic,transcriptome=Transcriotome,antisense=Antisense,\
                    contour_area=Contour_area,number_of_dnb_under_tissue=Number_of_DNB_under_tissue,ratio=Ratio,total_gene_type=Total_Gene_type,mid_under_tissue=MID_counts,fraction_mid_in_spots_under_tissue=Fraction_MID_in_Spots_Under_Tissue,reads_under_tissue=Reads_under_tissue,fraction_reads_in_spots_under_tissue=Fraction_Reads_in_Spots_Under_Tissue,\
                    x=df_h5['x'].tolist(), y=df_h5['y'].tolist(), text=df_h5['values'].tolist(), dot_size_h5=dot_size_h5, colorscale=DEFAULT_COLORSCALE, image=images_small, image_cluster=images_small_cluster, data_cluster=total_cluster, total_data_str=total_data_str, data_class=total_class, total_data_class_str=total_data_class_str, bin_div=bin_div_title,\
                    saturation_plot=saturation_img,  \
                    sun_label = df_sun.labels.tolist(), sun_value=df_sun.value.tolist(), sun_parent=df_sun.parents.tolist(), sun_hovertext=df_sun.text.tolist(), name_pro=sun_name_pro,\
                    sunburst_collapse = sunburst_collapse_toB, quality_collapse = quality_collapse, rna_collapse = rna_collapse, rna_annotation_collapse = rna_annotation_collapse, tissueCut_total_collapse = tissueCut_total_collapse, tissueCut_bin_collapse = tissueCut_bin_collapse,\
                    binCell_saturation_plot=binCell_saturation_img,binCell_violin_plot=binCell_violin_img,binCellMIDGeneDNB_plot=binCellMIDGeneDNB_img,\
                    pipeline_version=pipeline_version, marker_x=marker_x, marker_y=marker_y, cell_bin_collapse=cell_bin_collapse, \
                    mean_cell_area=mean_cell_area,cell_count=cell_count, median_cell_area=median_cell_area, mean_mid_count=mean_mid_count, median_mid_count=median_mid_count, \
                    mean_cell_boundary_dnb_count=mean_dnb_count, median_cell_boundary_dnb_count=median_dnb_count, mean_gene_type=mean_gene_type_count, median_gene_type=median_gene_type_count, \
                    cell_data_cluster = total_cell_cluster, total_cell_data_str=total_cell_data_str, cell_data_class=total_cell_class, total_cell_data_class_str=total_cell_data_class_str, \
                    image_manufacture = image_manufacture, image_model=image_model, scan_time = scan_time, overlap=overlap, exposure_time = exposure_time, scan_rows = scan_rows, scan_columns = scan_columns, fov_height = fov_height, \
                    fov_width = fov_width, experimenter = experimenter, stain_type = stain_type, stitched_image = stitched_image, image_name = image_name, \
                    imageqc_version =  imageqc_version, qc_pass = qc_pass, track_line_score = track_line_score, clarity_score = clarity_score, \
                    good_fov_count = good_fov_count, total_fov_count = total_fov_count, stitching_score = stitching_score, tissue_seg_score = tissue_seg_score, registration_score = registration_score, \
                    template_source_x = template_source_x, template_source_y=template_source_y, global_height = global_height, global_width = global_width, \
                    scaleX = scaleX, scaleY = scaleY, rotation = rotation, flip = flip, image_offset_x = image_offset_x, image_offset_y = image_offset_y, counter_rotation = counter_rotation, manual_scale_x=manual_scale_x, manual_scale_y=manual_scale_y, manual_rotation=manual_rotation, matrix_x_start = matrix_x_start, matrix_y_start =  matrix_y_start, matrix_height = matrix_height, matrix_width = matrix_width, \
                    image_qc_collapse = image_qc_collapse, image_stitching_collapse = image_stitch_collapse, image_registration_collapse = image_registration_collapse, \
                    image_heatmap_div = image_heatmap_div, persent_total_reads=persent_total_reads, persent_cid_reads=persent_cid_reads, persent_clean_reads=persent_clean_reads,persent_unique_mapping_reads=persent_unique_mapping_reads,\
                    persent_transcriptome=persent_transcriptome,persent_unique_reads=persent_unique_reads,persent_duplicated_reads=persent_duplicated_reads,persent_intergenic=persent_intergenic,persent_multi_mapping_reads=persent_multi_mapping_reads,\
                    persent_unmapping_reads=persent_unmapping_reads,persent_too_short_reads=persent_too_short_reads,persent_invalid_cid_reads=persent_invalid_cid_reads,persent_discarded_mid_reads=persent_discarded_mid_reads, \
                    image_dict=str(images_small_dict),image_list=image_list, binsize_canvas=binsize_canvas))
            # with open(html_report,'w',encoding='utf-8') as f:
            #     f.write(html_toB_final_template.format(logo_img=logo_img, sn_name=sn, species=species, tissue=tissue, reference=reference,fastq_name=fastq_name_str,Total_read=Total_reads,Mean_UMI_per_bin200=Mean_UMI_per_bin200,Mean_Gene_per_bin200=Mean_Gene_per_bin200,\
            #         sunburst_total_reads=Total_reads,valid_cid_reads=Valid_CID_Reads,invalid_cid_reads=Invalid_CID_Reads,discarded_mid_reads=Discarded_MID_Reads,clean_reads=Clean_Reads,reads_mapped_to_genome=Reads_Mapped_to_Genome_reads, unique_reads=Unique_Reads, duplicated_reads=Duplicated_Reads,\
            #         sequencing_total_reads=Total_reads,rate_of_q30_bases_in_cid=Q30_Barcode_Rate,rate_of_q30_bases_in_mid=Q30_MID_Rate,rate_of_q30_bases_in_seq=Q30_seq_Rate,\
            #         filter_collapse=filter_collapse,valid_cid_filter_reads=Valid_CID_Reads,q30_base_before_filtering=Q30_Before_Filtering,clean_filter_reads=Clean_Reads,q30_base_after_filtering=Q30_After_Filtering,low_quality_reads=Low_Quality_Reads,too_many_n_reads=Too_Many_N_Reads,too_short_reads=Too_Short_Reads,reads_with_adapter=Reads_With_Adapter,reads_with_dnb=Reads_With_DNB,\
            #         rna_clean_reads=Input_read,unique_mapping_reads=Uniquely_Mapped_Read,multiple_mapping_reads=Multi_Mapping_Read,rna_unmapping_reads=RNA_Unmapping_Read,\
            #         exonic=Exonic,intronic=Intronic,intergenic=Intergenic,transcriptome=Transcriotome,antisense=Antisense,\
            #         contour_area=Contour_area,number_of_dnb_under_tissue=Number_of_DNB_under_tissue,ratio=Ratio,total_gene_type=Total_Gene_type,mid_under_tissue=MID_counts,fraction_mid_in_spots_under_tissue=Fraction_MID_in_Spots_Under_Tissue,reads_under_tissue=Reads_under_tissue,fraction_reads_in_spots_under_tissue=Fraction_Reads_in_Spots_Under_Tissue,\
            #         x=df_h5['x'].tolist(), y=df_h5['y'].tolist(), text=df_h5['values'].tolist(), dot_size_h5=dot_size_h5, colorscale=DEFAULT_COLORSCALE, image=images_small, image_cluster=images_small_cluster, data_cluster=total_cluster, total_data_str=total_data_str, data_class=total_class, total_data_class_str=total_data_class_str, bin_div=bin_div_title,\
            #         bin200_saturation_plot=bin200_saturation_img,bin200_violin_plot=bin200_violin_img,saturation_plot=saturation_img, bin200MIDGeneDNB_plot=bin200MIDGeneDNB_img, \
            #         sun_label = df_sun.labels.tolist(), sun_value=df_sun.value.tolist(), sun_parent=df_sun.parents.tolist(), sun_hovertext=df_sun.text.tolist(), name_pro=sun_name_pro,\
            #         sunburst_collapse = sunburst_collapse_toB, quality_collapse = quality_collapse, rna_collapse = rna_collapse, rna_annotation_collapse = rna_annotation_collapse, tissueCut_total_collapse = tissueCut_total_collapse, tissueCut_bin_collapse = tissueCut_bin_collapse,\
            #         bin50_saturation_plot=bin50_saturation_img,bin50_violin_plot=bin50_violin_img,bin50MIDGeneDNB_plot=bin50MIDGeneDNB_img, \
            #         bin100_saturation_plot=bin100_saturation_img,bin100_violin_plot=bin100_violin_img,bin100MIDGeneDNB_plot=bin100MIDGeneDNB_img, \
            #         bin150_saturation_plot=bin150_saturation_img,bin150_violin_plot=bin150_violin_img,bin150MIDGeneDNB_plot=bin150MIDGeneDNB_img, \
            #         binCell_saturation_plot=binCell_saturation_img,binCell_violin_plot=binCell_violin_img,binCellMIDGeneDNB_plot=binCellMIDGeneDNB_img,\
            #         pipeline_version=pipeline_version, marker_x=marker_x, marker_y=marker_y, cell_bin_collapse=cell_bin_collapse, \
            #         mean_cell_area=mean_cell_area,cell_count=cell_count, median_cell_area=median_cell_area, mean_mid_count=mean_mid_count, median_mid_count=median_mid_count, \
            #         mean_cell_boundary_dnb_count=mean_dnb_count, median_cell_boundary_dnb_count=median_dnb_count, mean_gene_type=mean_gene_type_count, median_gene_type=median_gene_type_count, \
            #         cell_data_cluster = total_cell_cluster, total_cell_data_str=total_cell_data_str, cell_data_class=total_cell_class, total_cell_data_class_str=total_cell_data_class_str, \
            #         image_manufacture = image_manufacture, image_model=image_model, scan_time = scan_time, overlap=overlap, exposure_time = exposure_time, scan_rows = scan_rows, scan_columns = scan_columns, fov_height = fov_height, \
            #         fov_width = fov_width, experimenter = experimenter, stain_type = stain_type, stitched_image = stitched_image, image_name = image_name, \
            #         imageqc_version =  imageqc_version, qc_pass = qc_pass, track_line_score = track_line_score, clarity_score = clarity_score, \
            #         good_fov_count = good_fov_count, total_fov_count = total_fov_count, stitching_score = stitching_score, tissue_seg_score = tissue_seg_score, registration_score = registration_score, \
            #         template_source_x = template_source_x, template_source_y=template_source_y, global_height = global_height, global_width = global_width, \
            #         scaleX = scaleX, scaleY = scaleY, rotation = rotation, flip = flip, image_offset_x = image_offset_x, image_offset_y = image_offset_y, counter_rotation = counter_rotation, matrix_x_start = matrix_x_start, matrix_y_start =  matrix_y_start, matrix_height = matrix_height, matrix_width = matrix_width, \
            #         image_qc_collapse = image_qc_collapse, image_stitching_collapse = image_stitch_collapse, image_registration_collapse = image_registration_collapse, \
            #         image_heatmap_div = image_heatmap_div, persent_total_reads=persent_total_reads, persent_cid_reads=persent_cid_reads, persent_clean_reads=persent_clean_reads,persent_unique_mapping_reads=persent_unique_mapping_reads,\
            #         persent_transcriptome=persent_transcriptome,persent_unique_reads=persent_unique_reads,persent_duplicated_reads=persent_duplicated_reads,persent_intergenic=persent_intergenic,persent_multi_mapping_reads=persent_multi_mapping_reads,\
            #         persent_unmapping_reads=persent_unmapping_reads,persent_too_short_reads=persent_too_short_reads,persent_invalid_cid_reads=persent_invalid_cid_reads,persent_discarded_mid_reads=persent_discarded_mid_reads, \
            #         image_dict=str(images_small_dict),image_list=image_list))
        ###研发版本###
        elif research_version.upper() == 'Y':
            if rpi_file !='':
                if cellCluster != 'N':
                    html_research_final_template = html_research_template
                else:
                    html_research_final_template = html_research_no_cell_template
            else:
                html_research_final_template = html_research_no_rpi_template
            with open(html_report,'w',encoding='utf-8') as f:
                f.write(html_research_final_template.format(logo_img=logo_img, sn_name=sn, species=species, tissue=tissue, reference=reference,fastq_name=fastq_name_str,Total_read=number2humanDev(Total_reads),Mean_UMI_per_bin200=number2humanDev(Mean_UMI_per_bin200),Mean_Gene_per_bin200=number2humanDev(Mean_Gene_per_bin200),\
                    sunburst_total_reads=number2humanDev(Total_reads),valid_cid_reads=number2humanDev(Valid_CID_Reads),invalid_cid_reads=number2humanDev(Invalid_CID_Reads),discarded_mid_reads=number2humanDev(Discarded_MID_Reads),clean_reads=number2humanDev(Clean_Reads),reads_mapped_to_genome=number2humanDev(Reads_Mapped_to_Genome_reads), unique_reads=number2humanDev(Unique_Reads), duplicated_reads=number2humanDev(Duplicated_Reads),\
                    sequencing_total_reads=Total_reads,rate_of_q30_bases_in_cid=number2humanDev(Q30_Barcode_Rate),rate_of_q30_bases_in_mid=number2humanDev(Q30_MID_Rate),rate_of_q30_bases_in_seq=number2humanDev(Q30_seq_Rate),\
                    filter_collapse=filter_collapse,valid_cid_filter_reads=number2humanDev(Valid_CID_Reads),q30_base_before_filtering=Q30_Before_Filtering,clean_filter_reads=Clean_Reads,q30_base_after_filtering=Q30_After_Filtering,low_quality_reads=Low_Quality_Reads,too_many_n_reads=Too_Many_N_Reads,too_short_reads=number2humanDev(Too_Short_Reads),reads_with_adapter=number2humanDev(Reads_With_Adapter),reads_with_dnb=number2humanDev(Reads_With_DNB),\
                    rna_clean_reads=number2humanDev(Input_read),unique_mapping_reads=number2humanDev(Uniquely_Mapped_Read),multiple_mapping_reads=number2humanDev(Multi_Mapping_Read),rna_unmapping_reads=number2humanDev(RNA_Unmapping_Read),\
                    exonic=number2humanDev(Exonic),intronic=number2humanDev(Intronic),intergenic=number2humanDev(Intergenic),transcriptome=number2humanDev(Transcriotome),antisense=number2humanDev(Antisense),\
                    contour_area=number2humanDev(Contour_area),number_of_dnb_under_tissue=number2humanDev(Number_of_DNB_under_tissue),ratio_of_dnb_under_tissue=ratio_of_dnb_under_tissue,ratio=Ratio,total_gene_type=number2humanDev(Total_Gene_type),mid_under_tissue=number2humanDev(MID_counts),fraction_mid_in_spots_under_tissue=number2humanDev(Fraction_MID_in_Spots_Under_Tissue),reads_under_tissue=number2humanDev(Reads_under_tissue),fraction_reads_in_spots_under_tissue=number2humanDev(Fraction_Reads_in_Spots_Under_Tissue),\
                    x=df_h5['x'].tolist(), y=df_h5['y'].tolist(), text=df_h5['values'].tolist(), dot_size_h5=dot_size_h5, colorscale=DEFAULT_COLORSCALE, image=images_small, image_cluster=images_small_cluster, data_cluster=total_cluster, total_data_str=total_data_str, data_class=total_class, total_data_class_str=total_data_class_str, bin_div=bin_div_title,\
                    saturation_plot=saturation_img, \
                    sun_label = df_sun.labels.tolist(), sun_value=df_sun.value.tolist(), sun_parent=df_sun.parents.tolist(), sun_hovertext=df_sun.text.tolist(), name_pro=sun_name_pro,\
                    sunburst_collapse = sunburst_dev_collapse, quality_collapse = quality_collapse, rna_collapse = rna_collapse, rna_annotation_collapse = rna_annotation_collapse, tissueCut_total_collapse = tissueCut_total_collapse_dev, tissueCut_bin_collapse = tissueCut_bin_collapse,\
                    bin1_saturation_plot = bin1_saturation_img, binsize_canvas=binsize_canvas, \
                    binCell_saturation_plot=binCell_saturation_img,binCell_violin_plot=binCell_violin_img,binCellMIDGeneDNB_plot=binCellMIDGeneDNB_img,midCell_saturation_plot=midCell_saturation_img,areaCell_saturation_plot=areaCell_saturation_img,\
                    pipeline_version=pipeline_version, marker_x=marker_x, marker_y=marker_y, cell_bin_collapse=cell_bin_collapse, \
                    mean_cell_area=mean_cell_area, cell_count=cell_count,median_cell_area=median_cell_area, mean_mid_count=mean_mid_count, median_mid_count=median_mid_count, \
                    mean_cell_boundary_dnb_count=mean_dnb_count, median_cell_boundary_dnb_count=median_dnb_count, mean_gene_type=mean_gene_type_count, median_gene_type=median_gene_type_count, \
                    cell_data_cluster = total_cell_cluster, total_cell_data_str=total_cell_data_str, cell_data_class=total_cell_class, total_cell_data_class_str=total_cell_data_class_str, \
                    image_manufacture = image_manufacture, image_model=image_model, scan_time = scan_time, overlap=overlap, exposure_time = exposure_time, scan_rows = scan_rows, scan_columns = scan_columns, fov_height = fov_height, \
                    fov_width = fov_width, experimenter = experimenter, stain_type = stain_type, stitched_image = stitched_image, image_name = image_name, \
                    imageqc_version =  imageqc_version, qc_pass = qc_pass, track_line_score = track_line_score, clarity_score = clarity_score, \
                    good_fov_count = good_fov_count, total_fov_count = total_fov_count, stitching_score = stitching_score, tissue_seg_score = tissue_seg_score, registration_score = registration_score, \
                    template_source_x = template_source_x, template_source_y=template_source_y, global_height = global_height, global_width = global_width, \
                    scaleX = scaleX, scaleY = scaleY, rotation = rotation, flip = flip, image_offset_x = image_offset_x, image_offset_y = image_offset_y, counter_rotation = counter_rotation, manual_scale_x=manual_scale_x, manual_scale_y=manual_scale_y, manual_rotation=manual_rotation, matrix_x_start = matrix_x_start, matrix_y_start =  matrix_y_start, matrix_height = matrix_height, matrix_width = matrix_width, \
                    image_qc_collapse = image_qc_collapse, image_stitching_collapse = image_stitch_collapse, image_registration_collapse = image_registration_collapse, \
                    image_heatmap_div = image_heatmap_div, persent_total_reads=persent_total_reads, persent_cid_reads=persent_cid_reads, persent_clean_reads=persent_clean_reads,persent_unique_mapping_reads=persent_unique_mapping_reads,\
                    persent_transcriptome=persent_transcriptome,persent_unique_reads=persent_unique_reads,persent_duplicated_reads=persent_duplicated_reads,persent_intergenic=persent_intergenic,persent_multi_mapping_reads=persent_multi_mapping_reads,\
                    persent_unmapping_reads=persent_unmapping_reads,persent_too_short_reads=persent_too_short_reads,persent_invalid_cid_reads=persent_invalid_cid_reads,persent_discarded_mid_reads=persent_discarded_mid_reads, \
                    image_dict=str(images_small_dict),image_list=image_list
                    ))
            # with open(html_report,'w',encoding='utf-8') as f:
            #     f.write(html_research_final_template.format(logo_img=logo_img, sn_name=sn, species=species, tissue=tissue, reference=reference,fastq_name=fastq_name_str,Total_read=number2humanDev(Total_reads),Mean_UMI_per_bin200=number2humanDev(Mean_UMI_per_bin200),Mean_Gene_per_bin200=number2humanDev(Mean_Gene_per_bin200),\
            #         sunburst_total_reads=number2humanDev(Total_reads),valid_cid_reads=number2humanDev(Valid_CID_Reads),invalid_cid_reads=number2humanDev(Invalid_CID_Reads),discarded_mid_reads=number2humanDev(Discarded_MID_Reads),clean_reads=number2humanDev(Clean_Reads),reads_mapped_to_genome=number2humanDev(Reads_Mapped_to_Genome_reads), unique_reads=number2humanDev(Unique_Reads), duplicated_reads=number2humanDev(Duplicated_Reads),\
            #         sequencing_total_reads=Total_reads,rate_of_q30_bases_in_cid=number2humanDev(Q30_Barcode_Rate),rate_of_q30_bases_in_mid=number2humanDev(Q30_MID_Rate),rate_of_q30_bases_in_seq=number2humanDev(Q30_seq_Rate),\
            #         filter_collapse=filter_collapse,valid_cid_filter_reads=number2humanDev(Valid_CID_Reads),q30_base_before_filtering=Q30_Before_Filtering,clean_filter_reads=Clean_Reads,q30_base_after_filtering=Q30_After_Filtering,low_quality_reads=Low_Quality_Reads,too_many_n_reads=Too_Many_N_Reads,too_short_reads=number2humanDev(Too_Short_Reads),reads_with_adapter=number2humanDev(Reads_With_Adapter),reads_with_dnb=number2humanDev(Reads_With_DNB),\
            #         rna_clean_reads=number2humanDev(Input_read),unique_mapping_reads=number2humanDev(Uniquely_Mapped_Read),multiple_mapping_reads=number2humanDev(Multi_Mapping_Read),rna_unmapping_reads=number2humanDev(RNA_Unmapping_Read),\
            #         exonic=number2humanDev(Exonic),intronic=number2humanDev(Intronic),intergenic=number2humanDev(Intergenic),transcriptome=number2humanDev(Transcriotome),antisense=number2humanDev(Antisense),\
            #         contour_area=number2humanDev(Contour_area),number_of_dnb_under_tissue=number2humanDev(Number_of_DNB_under_tissue),ratio_of_dnb_under_tissue=ratio_of_dnb_under_tissue,ratio=Ratio,total_gene_type=number2humanDev(Total_Gene_type),mid_under_tissue=number2humanDev(MID_counts),fraction_mid_in_spots_under_tissue=number2humanDev(Fraction_MID_in_Spots_Under_Tissue),reads_under_tissue=number2humanDev(Reads_under_tissue),fraction_reads_in_spots_under_tissue=number2humanDev(Fraction_Reads_in_Spots_Under_Tissue),\
            #         x=df_h5['x'].tolist(), y=df_h5['y'].tolist(), text=df_h5['values'].tolist(), dot_size_h5=dot_size_h5, colorscale=DEFAULT_COLORSCALE, image=images_small, image_cluster=images_small_cluster, data_cluster=total_cluster, total_data_str=total_data_str, data_class=total_class, total_data_class_str=total_data_class_str, bin_div=bin_div_title,\
            #         bin200_saturation_plot=bin200_saturation_img,bin200_violin_plot=bin200_violin_img,saturation_plot=saturation_img, bin200MIDGeneDNB_plot=bin200MIDGeneDNB_img, \
            #         sun_label = df_sun.labels.tolist(), sun_value=df_sun.value.tolist(), sun_parent=df_sun.parents.tolist(), sun_hovertext=df_sun.text.tolist(), name_pro=sun_name_pro,\
            #         sunburst_collapse = sunburst_dev_collapse, quality_collapse = quality_collapse, rna_collapse = rna_collapse, rna_annotation_collapse = rna_annotation_collapse, tissueCut_total_collapse = tissueCut_total_collapse_dev, tissueCut_bin_collapse = tissueCut_bin_collapse,\
            #         bin1_saturation_plot = bin1_saturation_img, bin50_saturation_plot=bin50_saturation_img,bin50_violin_plot=bin50_violin_img,bin50MIDGeneDNB_plot=bin50MIDGeneDNB_img, \
            #         bin100_saturation_plot=bin100_saturation_img,bin100_violin_plot=bin100_violin_img,bin100MIDGeneDNB_plot=bin100MIDGeneDNB_img, \
            #         bin150_saturation_plot=bin150_saturation_img,bin150_violin_plot=bin150_violin_img,bin150MIDGeneDNB_plot=bin150MIDGeneDNB_img, \
            #         binCell_saturation_plot=binCell_saturation_img,binCell_violin_plot=binCell_violin_img,binCellMIDGeneDNB_plot=binCellMIDGeneDNB_img,midCell_saturation_plot=midCell_saturation_img,areaCell_saturation_plot=areaCell_saturation_img,\
            #         pipeline_version=pipeline_version, marker_x=marker_x, marker_y=marker_y, cell_bin_collapse=cell_bin_collapse, \
            #         mean_cell_area=mean_cell_area, cell_count=cell_count,median_cell_area=median_cell_area, mean_mid_count=mean_mid_count, median_mid_count=median_mid_count, \
            #         mean_cell_boundary_dnb_count=mean_dnb_count, median_cell_boundary_dnb_count=median_dnb_count, mean_gene_type=mean_gene_type_count, median_gene_type=median_gene_type_count, \
            #         cell_data_cluster = total_cell_cluster, total_cell_data_str=total_cell_data_str, cell_data_class=total_cell_class, total_cell_data_class_str=total_cell_data_class_str, \
            #         image_manufacture = image_manufacture, image_model=image_model, scan_time = scan_time, overlap=overlap, exposure_time = exposure_time, scan_rows = scan_rows, scan_columns = scan_columns, fov_height = fov_height, \
            #         fov_width = fov_width, experimenter = experimenter, stain_type = stain_type, stitched_image = stitched_image, image_name = image_name, \
            #         imageqc_version =  imageqc_version, qc_pass = qc_pass, track_line_score = track_line_score, clarity_score = clarity_score, \
            #         good_fov_count = good_fov_count, total_fov_count = total_fov_count, stitching_score = stitching_score, tissue_seg_score = tissue_seg_score, registration_score = registration_score, \
            #         template_source_x = template_source_x, template_source_y=template_source_y, global_height = global_height, global_width = global_width, \
            #         scaleX = scaleX, scaleY = scaleY, rotation = rotation, flip = flip, image_offset_x = image_offset_x, image_offset_y = image_offset_y, counter_rotation = counter_rotation, matrix_x_start = matrix_x_start, matrix_y_start =  matrix_y_start, matrix_height = matrix_height, matrix_width = matrix_width, \
            #         image_qc_collapse = image_qc_collapse, image_stitching_collapse = image_stitch_collapse, image_registration_collapse = image_registration_collapse, \
            #         image_heatmap_div = image_heatmap_div, persent_total_reads=persent_total_reads, persent_cid_reads=persent_cid_reads, persent_clean_reads=persent_clean_reads,persent_unique_mapping_reads=persent_unique_mapping_reads,\
            #         persent_transcriptome=persent_transcriptome,persent_unique_reads=persent_unique_reads,persent_duplicated_reads=persent_duplicated_reads,persent_intergenic=persent_intergenic,persent_multi_mapping_reads=persent_multi_mapping_reads,\
            #         persent_unmapping_reads=persent_unmapping_reads,persent_too_short_reads=persent_too_short_reads,persent_invalid_cid_reads=persent_invalid_cid_reads,persent_discarded_mid_reads=persent_discarded_mid_reads, \
            #         image_dict=str(images_small_dict),image_list=image_list
            #         ))
    except IOError:
        print_err("write_err:failed to write in html",'SAW-A90005')

# def print_err(*args):
#     sys.stderr.write(' '.join(map(str,args)) + '\n')

def get_canvas(bin_size, bin_fig):
    Saturation = bin_fig[f"bin{bin_size}Saturation"]
    violin = bin_fig[f"bin{bin_size}violin"]
    MIDGeneDNB = bin_fig[f"bin{bin_size}MIDGeneDNB"]
    MIDGeneDNB_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(MIDGeneDNB, 'rb').read()).decode('ascii'))
    MIDGeneDNB_img = '<img id="bin200MIDGeneDNB_plot" src={0} onclick="openImgBig(this.src)" style="cursor: pointer;">'.format(MIDGeneDNB_fig)

    saturation_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(Saturation, 'rb').read()).decode('ascii'))
    saturation_img = '<img style="height:400px;width:400px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(saturation_fig)

    violin_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(violin, 'rb').read()).decode('ascii'))
    violin_img = '<img style="height:400px;width:700px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(violin_fig)

    return bin_canvas.format(bin_size=bin_size, saturation_plot=saturation_img, violin_plot=violin_img, MIDGeneDNB_plot=MIDGeneDNB_img)

def print_err(case ,code):
    """
    print error code
    """
    err_code={
        "SAW-A90001":"{} is missing.",
        "SAW-A90002":"cannot access {}: No such file or directory.",
        "SAW-A90003":"{} file format error.",
        "SAW-A90004":"information loss: {}.",
        "SAW-A90005":"{}."
    }
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("errcode.log","a") as err_info:
        err_info.write("[{}] {}: {}\n".format(nowtime, code,err_code[code].format(case)))
    # sys.stderr.write(' '.join(map(str,args)) + '\n')
    sys.stderr.write("[{}] {}: {}\n".format(nowtime, code,err_code[code].format(case)))
    sys.exit(1)

def get_image_info(imageinfojson):
    clarity_score, good_fov_count, total_fov_count, stitching_score, template_source, global_height, global_width, flip = '-', '-', '-', '-', '-', '-', '-', '-'
    with open(imageinfojson, 'r') as load_f:
        image_info_dict = json.loads(load_f.read().replace('_','').lower())
    
    image_manufacture = image_info_dict["imageinfo"]["manufacturer"]
    scan_time = image_info_dict["imageinfo"]["scantime"]
    overlap =  image_info_dict["imageinfo"]["overlap"]
    exposure_time = round(image_info_dict["imageinfo"]["exposuretime"],3)
    scan_rows = image_info_dict["imageinfo"]["scanrows"]
    scan_columns = image_info_dict["imageinfo"]["scancols"]
    fov_height = image_info_dict["imageinfo"]["fovheight"]
    fov_width = image_info_dict["imageinfo"]["fovwidth"]
    experimenter = image_info_dict["imageinfo"]["experimenter"]
    stain_type = 'ssDNA'
    stitched_image = image_info_dict["imageinfo"]["stitchedimage"]
    image_name = os.path.basename(imageinfojson).split('.json')[0]
    image_path = os.path.dirname(os.path.dirname(imageinfojson))

    imageqc_version = image_info_dict["qcinfo"]["qcversion"]
    if image_info_dict["qcinfo"]["qcresultflag"] == 1:
        qc_pass = 'Pass'
    else:
        qc_pass = 'Fail'
    track_line_score = round(image_info_dict["qcinfo"]["qcscore"],3)
    if 'qcblurscore' in image_info_dict["qcinfo"].keys():
        clarity_score = round(image_info_dict["qcinfo"]["qcblurscore"],3)
    if 'yolo' in image_info_dict["qcinfo"].keys():
        good_fov_count = image_info_dict["qcinfo"]["yolo"]
    if 'fovcount' in image_info_dict["qcinfo"].keys():
        total_fov_count = image_info_dict["qcinfo"]["fovcount"]
    tissue_edge_score = round(image_info_dict["tissuecutinfo"]["outscore"],3)
    tissue_average_score = round(image_info_dict["tissuecutinfo"]["avgscore"],3)
    registration_score = round(image_info_dict["registerinfo"]["registerscore"],3)

    scale = round(image_info_dict["registerinfo"]["scale"],3)
    rotation = round(image_info_dict["registerinfo"]["rotation"],3)

    if "flip" in image_info_dict["analysisinfo"]["inputdct"].keys():
        flip = str(image_info_dict["analysisinfo"]["inputdct"]["flip"])

    offset = [round(i,3) for i in image_info_dict["analysisinfo"]["inputdct"]["offset"]]
    counter_rotation = image_info_dict["analysisinfo"]["inputdct"]["rottype"] * 90
    matrix_x_start = number2human(image_info_dict["analysisinfo"]["inputdct"]["xstart"])
    matrix_y_start = number2human(image_info_dict["analysisinfo"]["inputdct"]["ystart"])
    matrix_width = image_info_dict["analysisinfo"]["inputdct"]["visshape"][0]
    matrix_height = image_info_dict["analysisinfo"]["inputdct"]["visshape"][1]

    if not stitched_image:
        stitching_score = round(image_info_dict["stitchinfo"]["stitcheval"]["evaler"],3)
        template_source = image_info_dict["stitchinfo"]["stitcheval"]["templatesrc"]
        global_height = image_info_dict["stitchinfo"]["stitcheval"]["globalheight"]
        global_width = image_info_dict["stitchinfo"]["stitcheval"]["globalwidth"]
        heatmap_img_path = os.path.join(image_path, '2_stitch', 'heatmap_tissue.jpg')
    else:
        fig_name = image_name + '_stitchevalheatmap.png'
        heatmap_img_path = os.path.join(image_path, '1_origin', fig_name)

    image_heatmap_fig = 'data:image/png;base64,{}'.format(base64.b64encode(open(heatmap_img_path, 'rb').read()).decode('ascii'))
    image_heatmap_img = '<img style="height:400px;width:600px;cursor: pointer;" id="bin200_plot" src={0} onclick="openImg(this.src)">'.format(image_heatmap_fig)

    return image_manufacture, scan_time, overlap, exposure_time, scan_rows, scan_columns, fov_height, fov_width, experimenter, stain_type, stitched_image, image_name, \
        imageqc_version, qc_pass, track_line_score, clarity_score, good_fov_count, total_fov_count, stitching_score, tissue_edge_score, tissue_average_score, registration_score, \
        stitching_score, template_source, global_height, global_width, \
        scale, rotation, flip, offset, counter_rotation, matrix_x_start, matrix_y_start, matrix_width, matrix_height, image_heatmap_img

def read_gef_file(h5_file):
    dnb_df_range = {}
    h5_hf = h5py.File(h5_file,'r')
    h5_key = ["geneExp","stat","wholeExp","wholeExpExon"]
    for i in h5_key:
        if i not in h5_hf.keys():
            print_err("fail to find '{}' item in {}".format(i,os.path.abspath(h5_file)),"SAW-A90004")
    range_data  = h5_hf['wholeExp']['bin200'][:]
    minX = h5_hf['wholeExp']['bin200'].attrs['minX'][0]
    minY = h5_hf['wholeExp']['bin200'].attrs['minY'][0]
    dtype = np.dtype([('x', '<f4'), ('y', '<f4'),  ('values', '<u4'), ('gene_counts', '<u4')])
    (rows, cols) = np.where(range_data)
    total_count = len(rows)
    array = np.empty(total_count, dtype=dtype)
    rows = (rows)*200
    cols = (cols)*200
    array['x'] = np.array(rows)
    array['y'] = np.array(cols)
    nozero_data = range_data[np.where(range_data)]
    array['values'] = nozero_data['MIDcount']
    array['gene_counts']= nozero_data['genecount']
    df = pd.DataFrame(array)
    df['x'] = df['x'] + 100
    df['y'] = df['y'] + 100

    lenX = h5_hf['wholeExp']['bin200'].attrs['lenX'][0]
    lenY = h5_hf['wholeExp']['bin200'].attrs['lenY'][0]

    dnb_df_range['min_x'] = 0
    dnb_df_range['min_y'] = 0
    dnb_df_range['max_x'] = 0 + lenX
    dnb_df_range['max_y'] = 0 + lenY

    return df, dnb_df_range

def read_h5_file(h5_file):
    h5_hf = h5py.File(h5_file,'r')
    df_h5 = pd.DataFrame(h5_hf['dnb_merge']['bin200'][()],columns=['x','y','values','gene_counts'])
    df_h5['x'] = df_h5['x'] + 100
    df_h5['y'] = df_h5['y'] + 100

    return df_h5

def get_image_info_ipr(iprFile):
    image_manufacture, image_model, scan_time, overlap, exposure_time, scan_rows, scan_columns, fov_height, fov_width, experimenter, stain_type, stitched_image, image_name = '-','-','-','-','-','-','-','-','-','-','-','-','-'
    imageqc_version, track_line_score, clarity_score, good_fov_count, total_fov_count, tissue_seg_score, stitching_score, template_source  = '-', '-', '-', '-', '-', '-', '-', '-'
    scaleX, scaleY, rotation, flip, image_offset_x, image_offset_y, counter_rotation, matrix_x_start, matrix_y_start, matrix_width, matrix_height = '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'
    global_height, global_width = '-', '-'
    template_source_x, template_source_y = '-', '-'
    ipr_h5py = h5py.File(iprFile, 'r')  
    
    if 'Manufacturer' in ipr_h5py["ImageInfo"].attrs.keys():
        image_manufacture = ipr_h5py["ImageInfo"].attrs["Manufacturer"]
    if 'Model' in ipr_h5py["ImageInfo"].attrs.keys():
        image_model = ipr_h5py["ImageInfo"].attrs["Model"]
    if 'ScanTime' in ipr_h5py["ImageInfo"].attrs.keys():  
        scan_time = ipr_h5py["ImageInfo"].attrs["ScanTime"]
    if 'Overlap' in ipr_h5py["ImageInfo"].attrs.keys():
        overlap =  ipr_h5py["ImageInfo"].attrs["Overlap"]
    if 'ExposureTime' in ipr_h5py["ImageInfo"].attrs.keys():
        exposure_time = round(ipr_h5py["ImageInfo"].attrs["ExposureTime"],3)
    if 'ScanRows' in ipr_h5py["ImageInfo"].attrs.keys():
        scan_rows = ipr_h5py["ImageInfo"].attrs["ScanRows"]
    if 'ScanCols' in ipr_h5py["ImageInfo"].attrs.keys():
        scan_columns = ipr_h5py["ImageInfo"].attrs["ScanCols"]
    if 'FOVHeight' in ipr_h5py["ImageInfo"].attrs.keys():
        fov_height_tmp = ipr_h5py["ImageInfo"].attrs["FOVHeight"]
        fov_height = number2human(fov_height_tmp)
    if 'FOVWidth' in ipr_h5py["ImageInfo"].attrs.keys():
        fov_width_tmp = ipr_h5py["ImageInfo"].attrs["FOVWidth"]
        fov_width = number2human(fov_width_tmp)
    if 'Experimenter' in ipr_h5py["QCInfo"].attrs.keys():
        experimenter = ipr_h5py["QCInfo"].attrs["Experimenter"]
    if 'StainType' in ipr_h5py["QCInfo"].attrs.keys():
        stain_type = ipr_h5py["QCInfo"].attrs["StainType"]
    if 'StitchedImage' in ipr_h5py["ImageInfo"].attrs.keys():
        if ipr_h5py["ImageInfo"].attrs["StitchedImage"]:
            stitched_image = 'Yes'
        else:
            stitched_image = 'No'
    if 'QCResultFile' in ipr_h5py["ImageInfo"].attrs.keys():
        image_name = ipr_h5py["ImageInfo"].attrs["QCResultFile"]

    if 'ImageQCVersion' in ipr_h5py["QCInfo"].attrs.keys():
        imageqc_version = ipr_h5py["QCInfo"].attrs["ImageQCVersion"]
    if ipr_h5py["QCInfo"].attrs["QCPassFlag"] == 1:
        qc_pass = 'Pass'
    else:
        qc_pass = 'Fail'
    if 'TrackLineScore' in ipr_h5py["QCInfo"].attrs.keys():
        track_line_score = round(ipr_h5py["QCInfo"].attrs["TrackLineScore"],3)
    if 'ClarityScore' in ipr_h5py["QCInfo"].attrs.keys():
        if ipr_h5py["QCInfo"].attrs["ClarityScore"] == '-':
            clarity_score = ipr_h5py["QCInfo"].attrs["ClarityScore"]
        else:
            clarity_score = round(ipr_h5py["QCInfo"].attrs["ClarityScore"],3)
    if 'GoodFOVCount' in ipr_h5py["QCInfo"].attrs.keys():
        good_fov_count = ipr_h5py["QCInfo"].attrs["GoodFOVCount"]
    if 'TotalFOVcount' in ipr_h5py["QCInfo"].attrs.keys():
        total_fov_count = ipr_h5py["QCInfo"].attrs["TotalFOVcount"]
    elif 'TotalFOVCount' in ipr_h5py["QCInfo"].attrs.keys():
        total_fov_count = ipr_h5py["QCInfo"].attrs["TotalFOVCount"]
    if 'TissueSegScore' in ipr_h5py['TissueSeg'].attrs.keys():
        if ipr_h5py["TissueSeg"].attrs["TissueSegScore"] == '-':
            tissue_seg_score = ipr_h5py["TissueSeg"].attrs["TissueSegScore"]
        else:
            tissue_seg_score = round(ipr_h5py["TissueSeg"].attrs["TissueSegScore"],3)
    if 'RegisterScore' in ipr_h5py['Register'].attrs.keys():
        registration_score = round(ipr_h5py["Register"].attrs["RegisterScore"],3)

    if 'ScaleX' in ipr_h5py['Register'].attrs.keys():
        scaleX = str(round(ipr_h5py["Register"].attrs["ScaleX"],3))
    if 'ScaleY' in ipr_h5py['Register'].attrs.keys():
        scaleY = str(round(ipr_h5py["Register"].attrs["ScaleY"],3))
    if 'Rotation' in ipr_h5py['Register'].attrs.keys():
        rotation = round(ipr_h5py["Register"].attrs["Rotation"],3)

    if 'Flip' in ipr_h5py['Register'].attrs.keys():
        flip = str(ipr_h5py["Register"].attrs["Flip"])

    if 'OffsetX' in ipr_h5py['Register'].attrs.keys():
        image_offset_x = number2human(str(round(ipr_h5py["Register"].attrs["OffsetX"],3)))
    if 'OffsetY' in ipr_h5py['Register'].attrs.keys():
        image_offset_y = number2human(str(round(ipr_h5py["Register"].attrs["OffsetY"],3)))
    if 'CounterRot90' in ipr_h5py['Register'].attrs.keys():
        counter_rotation = ipr_h5py["Register"].attrs["CounterRot90"] * 90
    if 'XStart' in ipr_h5py['Register'].attrs.keys():
        matrix_x_start = number2human(ipr_h5py["Register"].attrs["XStart"])
    if 'YStart' in ipr_h5py['Register'].attrs.keys():
        matrix_y_start = number2human(ipr_h5py["Register"].attrs["YStart"])
    if 'MatrixShape' in ipr_h5py['Register'].attrs.keys():
        matrix_width = number2human(ipr_h5py["Register"].attrs["MatrixShape"][0])
        matrix_height = number2human(ipr_h5py["Register"].attrs["MatrixShape"][1])

    if 'GlobalHeight' in ipr_h5py['Stitch']['ScopeStitch'].attrs.keys():
        global_height = number2human(ipr_h5py["Stitch"]['ScopeStitch'].attrs["GlobalHeight"])
    if 'GlobalWidth' in ipr_h5py['Stitch']['ScopeStitch'].attrs.keys():
        global_width = number2human(ipr_h5py["Stitch"]['ScopeStitch'].attrs["GlobalWidth"])

    if stitched_image == 'No':
        if 'StitchEval' not in ipr_h5py['Stitch'].keys():
            image_heatmap_div = '<div></div>'
        #如果StitchEvalH在attrs的key里，则为'-'，不画热图
        elif 'StitchEvalH' in ipr_h5py['Stitch']['StitchEval'].attrs.keys():
            image_heatmap_div = '<div></div>'
        else:
            stitching_score = round(ipr_h5py["Stitch"].attrs["StitchingScore"],3)
            image_heatmap_div = read_small_ipr_file(ipr_h5py, fov_height_tmp, fov_width_tmp)
    else:
        if 'StitchEval' not in ipr_h5py['Stitch'].keys():
            image_heatmap_div = '<div></div>'
        #如果GlobalDeviation在attrs的key里，则为'-'，不画热图
        elif 'GlobalDeviation' in ipr_h5py['Stitch']['StitchEval'].attrs.keys():
            image_heatmap_div = '<div></div>'
        else:
            image_heatmap_div = read_big_ipr_file(ipr_h5py, fov_height_tmp, fov_width_tmp)

    template_source = ipr_h5py["Stitch"].attrs["TemplateSource"]
    template_source_x = template_source.split('_')[0]
    template_source_y = template_source.split('_')[1]

    return image_manufacture, image_model, scan_time, overlap, exposure_time, scan_rows, scan_columns, fov_height, fov_width, experimenter, stain_type, stitched_image, image_name, \
        imageqc_version, qc_pass, track_line_score, clarity_score, good_fov_count, total_fov_count, stitching_score, tissue_seg_score, registration_score, \
        template_source_x, template_source_y, global_height, global_width, \
        scaleX, scaleY, rotation, flip, image_offset_x, image_offset_y, counter_rotation, matrix_x_start, matrix_y_start, matrix_width, matrix_height, image_heatmap_div

def get_info_ipr_layer(iprFile):
    image_manufacture, image_model, scan_time, overlap, exposure_time, scan_rows, scan_columns, fov_height, fov_width, experimenter, stain_type, stitched_image, image_name = '-','-','-','-','-','-','-','-','-','-','-','-','-'
    imageqc_version, track_line_score, clarity_score, good_fov_count, total_fov_count, tissue_seg_score, stitching_score, template_source  = '-', '-', '-', '-', '-', '-', '-', '-'
    scaleX, scaleY, rotation, flip, image_offset_x, image_offset_y, counter_rotation, matrix_x_start, matrix_y_start, matrix_width, matrix_height = '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'
    global_height, global_width = '-', '-'
    manual_scale_x, manual_scale_y, manual_rotation = "-", "-", "-"
    template_source_x, template_source_y = '-', '-'
    ipr_h5py = h5py.File(iprFile, 'r')  
    layer = ""
    if "ssDNA" in ipr_h5py.keys():
        layer = "ssDNA"
    elif "DAPI" in ipr_h5py.keys():
        layer = "DAPI"
    else:
        print_err("ipr file loss 'ssDNA' and 'DAPI' group","SAW-A90005")

    if 'Manufacturer' in ipr_h5py[layer]["ImageInfo"].attrs.keys():
        image_manufacture = ipr_h5py[layer]["ImageInfo"].attrs["Manufacturer"]
    if 'Model' in ipr_h5py[layer]["ImageInfo"].attrs.keys():
        image_model = ipr_h5py[layer]["ImageInfo"].attrs["Model"]
    if 'ScanTime' in ipr_h5py[layer]["ImageInfo"].attrs.keys():  
        scan_time = ipr_h5py[layer]["ImageInfo"].attrs["ScanTime"]
    if 'Overlap' in ipr_h5py[layer]["ImageInfo"].attrs.keys():
        overlap =  ipr_h5py[layer]["ImageInfo"].attrs["Overlap"]
    if 'ExposureTime' in ipr_h5py[layer]["ImageInfo"].attrs.keys():
        exposure_time = round(ipr_h5py[layer]["ImageInfo"].attrs["ExposureTime"],3)
    if 'ScanRows' in ipr_h5py[layer]["ImageInfo"].attrs.keys():
        scan_rows = ipr_h5py[layer]["ImageInfo"].attrs["ScanRows"]
    if 'ScanCols' in ipr_h5py[layer]["ImageInfo"].attrs.keys():
        scan_columns = ipr_h5py[layer]["ImageInfo"].attrs["ScanCols"]
    if 'FOVHeight' in ipr_h5py[layer]["ImageInfo"].attrs.keys():
        fov_height_tmp = ipr_h5py[layer]["ImageInfo"].attrs["FOVHeight"]
        fov_height = number2human(fov_height_tmp)
    if 'FOVWidth' in ipr_h5py[layer]["ImageInfo"].attrs.keys():
        fov_width_tmp = ipr_h5py[layer]["ImageInfo"].attrs["FOVWidth"]
        fov_width = number2human(fov_width_tmp)
    if 'Experimenter' in ipr_h5py[layer]["QCInfo"].attrs.keys():
        experimenter = ipr_h5py[layer]["QCInfo"].attrs["Experimenter"]
    if 'StainType' in ipr_h5py[layer]["QCInfo"].attrs.keys():
        stain_type = ipr_h5py[layer]["QCInfo"].attrs["StainType"]
    if 'StitchedImage' in ipr_h5py[layer]["ImageInfo"].attrs.keys():
        if ipr_h5py[layer]["ImageInfo"].attrs["StitchedImage"]:
            stitched_image = 'Yes'
        else:
            stitched_image = 'No'
    if 'QCResultFile' in ipr_h5py[layer]["ImageInfo"].attrs.keys():
        image_name = ipr_h5py[layer]["ImageInfo"].attrs["QCResultFile"]

    if 'ImageQCVersion' in ipr_h5py[layer]["QCInfo"].attrs.keys():
        imageqc_version = ipr_h5py[layer]["QCInfo"].attrs["ImageQCVersion"]
    if ipr_h5py[layer]["QCInfo"].attrs["QCPassFlag"] == 1:
        qc_pass = 'Pass'
    else:
        qc_pass = 'Fail'
    if 'TrackLineScore' in ipr_h5py[layer]["QCInfo"].attrs.keys():
        track_line_score = round(ipr_h5py[layer]["QCInfo"].attrs["TrackLineScore"],3)
    if 'ClarityScore' in ipr_h5py[layer]["QCInfo"].attrs.keys():
        if ipr_h5py[layer]["QCInfo"].attrs["ClarityScore"] == '-':
            clarity_score = ipr_h5py[layer]["QCInfo"].attrs["ClarityScore"]
        else:
            clarity_score = round(ipr_h5py[layer]["QCInfo"].attrs["ClarityScore"],3)
    if 'GoodFOVCount' in ipr_h5py[layer]["QCInfo"].attrs.keys():
        good_fov_count = ipr_h5py[layer]["QCInfo"].attrs["GoodFOVCount"]
    if 'TotalFOVcount' in ipr_h5py[layer]["QCInfo"].attrs.keys():
        total_fov_count = ipr_h5py[layer]["QCInfo"].attrs["TotalFOVcount"]
    elif 'TotalFOVCount' in ipr_h5py[layer]["QCInfo"].attrs.keys():
        total_fov_count = ipr_h5py[layer]["QCInfo"].attrs["TotalFOVCount"]
    if 'TissueSegScore' in ipr_h5py[layer]['TissueSeg'].attrs.keys():
        if ipr_h5py[layer]["TissueSeg"].attrs["TissueSegScore"] == '-':
            tissue_seg_score = ipr_h5py[layer]["TissueSeg"].attrs["TissueSegScore"]
        else:
            tissue_seg_score = round(ipr_h5py[layer]["TissueSeg"].attrs["TissueSegScore"],3)
    if 'RegisterScore' in ipr_h5py[layer]['Register'].attrs.keys():
        registration_score = round(ipr_h5py[layer]["Register"].attrs["RegisterScore"],3)

    if 'ScaleX' in ipr_h5py[layer]['Register'].attrs.keys():
        manual_scale_x = str(round(ipr_h5py[layer]["Register"].attrs["ScaleX"],3))
    if 'ScaleY' in ipr_h5py[layer]['Register'].attrs.keys():
        manual_scale_y = str(round(ipr_h5py[layer]["Register"].attrs["ScaleY"],3))
    if 'Rotation' in ipr_h5py[layer]['Register'].attrs.keys():
        manual_rotation = round(ipr_h5py[layer]["Register"].attrs["Rotation"],3)

    if 'ManualScaleX' in ipr_h5py[layer]['Register'].attrs.keys():
        scaleX = str(round(ipr_h5py[layer]["Register"].attrs["ManualScaleX"],3))
    if 'ManualScaleY' in ipr_h5py[layer]['Register'].attrs.keys():
        scaleY = str(round(ipr_h5py[layer]["Register"].attrs["ManualScaleY"],3))
    if 'ManualRotation' in ipr_h5py[layer]['Register'].attrs.keys():
        rotation = round(ipr_h5py[layer]["Register"].attrs["ManualRotation"],3)

    if 'Flip' in ipr_h5py[layer]['Register'].attrs.keys():
        flip = str(ipr_h5py[layer]["Register"].attrs["Flip"])

    if 'OffsetX' in ipr_h5py[layer]['Register'].attrs.keys():
        image_offset_x = number2human(str(round(ipr_h5py[layer]["Register"].attrs["OffsetX"],3)))
    if 'OffsetY' in ipr_h5py[layer]['Register'].attrs.keys():
        image_offset_y = number2human(str(round(ipr_h5py[layer]["Register"].attrs["OffsetY"],3)))
    if 'CounterRot90' in ipr_h5py[layer]['Register'].attrs.keys():
        counter_rotation = ipr_h5py[layer]["Register"].attrs["CounterRot90"] * 90
    if 'XStart' in ipr_h5py[layer]['Register'].attrs.keys():
        matrix_x_start = number2human(ipr_h5py[layer]["Register"].attrs["XStart"])
    if 'YStart' in ipr_h5py[layer]['Register'].attrs.keys():
        matrix_y_start = number2human(ipr_h5py[layer]["Register"].attrs["YStart"])
    if 'MatrixShape' in ipr_h5py[layer]['Register'].attrs.keys():
        matrix_width = number2human(ipr_h5py[layer]["Register"].attrs["MatrixShape"][0])
        matrix_height = number2human(ipr_h5py[layer]["Register"].attrs["MatrixShape"][1])

    if 'GlobalHeight' in ipr_h5py[layer]['Stitch']['ScopeStitch'].attrs.keys():
        global_height = number2human(ipr_h5py[layer]["Stitch"]['ScopeStitch'].attrs["GlobalHeight"])
    if 'GlobalWidth' in ipr_h5py[layer]['Stitch']['ScopeStitch'].attrs.keys():
        global_width = number2human(ipr_h5py[layer]["Stitch"]['ScopeStitch'].attrs["GlobalWidth"])

    if stitched_image == 'No':
        if 'StitchEval' not in ipr_h5py[layer]['Stitch'].keys():
            image_heatmap_div = '<div></div>'
        #如果StitchEvalH在attrs的key里，则为'-'，不画热图
        elif 'StitchEvalH' in ipr_h5py[layer]['Stitch']['StitchEval'].attrs.keys():
            image_heatmap_div = '<div></div>'
        else:
            stitching_score = round(ipr_h5py[layer]["Stitch"].attrs["StitchingScore"],3)
            image_heatmap_div = read_small_ipr_file(ipr_h5py[layer], fov_height_tmp, fov_width_tmp)
    else:
        if 'StitchEval' not in ipr_h5py[layer]['Stitch'].keys():
            image_heatmap_div = '<div></div>'
        #如果GlobalDeviation在attrs的key里，则为'-'，不画热图
        elif 'GlobalDeviation' in ipr_h5py[layer]['Stitch']['StitchEval'].attrs.keys():
            image_heatmap_div = '<div></div>'
        else:
            image_heatmap_div = read_big_ipr_file(ipr_h5py[layer], fov_height_tmp, fov_width_tmp)

    template_source = ipr_h5py[layer]["Stitch"].attrs["TemplateSource"]
    template_source_x = template_source.split('_')[0]
    template_source_y = template_source.split('_')[1]

    return image_manufacture, image_model, scan_time, overlap, exposure_time, scan_rows, scan_columns, fov_height, fov_width, experimenter, stain_type, stitched_image, image_name, \
        imageqc_version, qc_pass, track_line_score, clarity_score, good_fov_count, total_fov_count, stitching_score, tissue_seg_score, registration_score, \
        template_source_x, template_source_y, global_height, global_width, \
        scaleX, scaleY, rotation, flip, image_offset_x, image_offset_y, counter_rotation, manual_scale_x, manual_scale_y, manual_rotation,\
        matrix_x_start, matrix_y_start, matrix_width, matrix_height, image_heatmap_div

def read_small_ipr_file(iprFile, fov_height, fov_width):
    demo_cb_h5py = iprFile
    np_eval_h = demo_cb_h5py['Stitch']['StitchEval']['StitchEvalH'][()]
    flip = demo_cb_h5py['Register'].attrs["Flip"]
    rot90 = demo_cb_h5py['Register'].attrs["CounterRot90"]
    rowi = "i"
    colj = "j"
    if rot90%2 == 1:
        fov_ratio = fov_height/fov_width
        np_eval_h = np.rot90(np_eval_h,1)
        np_eval_h = np.flip(np_eval_h,axis=0)
        rowi = "j"
        colj = "i"
    else:
        fov_ratio = fov_width/fov_height
    Yautorange = "'autorange': 'reversed',"
    Xautorange = ""
    y_flip = 1
    x_flip = 0
    if rot90 == 1 :
        x_flip += 1
    elif rot90 == 2:
        x_flip += 1
        y_flip += 1
    elif rot90 == 3:
        y_flip += 1
    if flip == True:
        x_flip += 1
    if x_flip%2 == 1:
        Xautorange = "'autorange': 'reversed',"
    if y_flip%2 == 0:
        Yautorange = ""

    np_eval_h[np_eval_h < 0] = 0
    np_eval_h = np.round(np_eval_h, decimals=3)
    
    h_y_max = np_eval_h.shape[0]
    h_x_max = np_eval_h.shape[1]
    np_eval_h = np.array2string(np_eval_h, separator=',')
    
    h_y_range = [-1, h_y_max]   
    h_x_range = [-1, h_x_max]
    

    np_eval_v = demo_cb_h5py['Stitch']['StitchEval']['StitchEvalV'][()]
    np_eval_v[np_eval_v < 0] = 0
    np_eval_v = np.round(np_eval_v, decimals=3)
    if rot90%2 == 1:
        np_eval_v = np.rot90(np_eval_v,1)
        np_eval_v = np.flip(np_eval_v,axis=0)
    v_y_max = np_eval_v.shape[0]
    v_x_max = np_eval_v.shape[1]
    np_eval_v = np.array2string(np_eval_v, separator=',')
    v_y_range = [-1, v_y_max]
    v_x_range = [-1, v_x_max]

    horizontal_image_heatmap = """
        <div id='heatmap_left'>
            <div>Horizontal Image Stitching Deviation Heatmap
                <button class="button_explain" onclick="show_image_left()">
                    <i class="fa">?</i>
                </button>
                <div id='div_explain_image_left'>
                    Image stitching deviation in the horizontal axis, a lighter color indicates better stitching (the heatmap and frame of axes have been adjusted with the registration parameters)
                </div>
            </div>
            <div id='divHeatmap', style="width:500px;height:400px;margin-left:auto;margin-right:auto;">
            <script>
                var z = {NP_EVAL_H}
                var text = z.map((row, i) => row.map((item, j) => {{
                    return `Row: ${{{i}}}<br>Col: ${{{j}}}<br>Deviation: ${{item.toFixed(3)}}` 
                    }}))
                var data_heatmap = {{
                    z: z,
                    type: 'heatmap',
                    text: text,
                    hoverinfo: 'text',
                    colorbar: {{thickness:20}},
                    colorscale: [[0, 'rgb(245,245,245)'], [0.25, 'rgb(181, 137, 214)'], [0.5, 'rgb(153, 105, 199)'], [0.75, 'rgb(106, 53, 156)'], [1, 'rgb(61, 27, 97)']]
                }};

                var data = [data_heatmap];
                var layout = {{
                    yaxis: {{{Yautorange}'scaleanchor': "x", 'scaleratio': {SCALERATIO}, 'showgrid': false, 'rangemode':'tozero', 'zeroline': false, 'range':{HRANGEY}}},
                    xaxis: {{{Xautorange}'showgrid': false, 'rangemode': 'tozero', 'zeroline': false, 'range':{HRANGEX}}},
                    dragmode:"zoom",
                    margin: {{'l' : 30, 't' : 30, 'r' : 30, 'b' : 30}},
                    showlegend: true,
                }}
                Plotly.newPlot('divHeatmap', data, layout, {{scrollZoom:true, displaylogo:false, modeBarButtonsToRemove:["hoverClosestCartesian","hoverCompareCartesian","toggleSpikelines","autoScale2d","lasso2d","select2d","zoom2d","zoomIn2d","zoomOut2d"]}});
            </script>
        </div>
        </div>
    """.format(NP_EVAL_H = np_eval_h, HRANGEY = h_y_range, HRANGEX = h_x_range, SCALERATIO=fov_ratio,i=rowi, j=colj,Xautorange = Xautorange, Yautorange = Yautorange)
    
    vertical_image_heatmap = """
        <div id='heatmap_right'>
            <div>Vertical Image Stitching Deviation Heatmap
                <button class="button_explain" onclick="show_image_right()">
                    <i class="fa">?</i>
                </button>
                <div id='div_explain_image_right'>
                    Image stitching deviation in the vertical axis, a lighter color indicates better stitching (the heatmap and frame of axes have been adjusted with the registration parameters)
                </div>
            </div>
            <div id='divHeatmapVertical', style="width:500px;height:400px;margin-left:auto;margin-right:auto;">
            <script>
                var z = {NP_EVAL_V}
                var text = z.map((row, i) => row.map((item, j) => {{
                    return `Row: ${{{i}}}<br>Col: ${{{j}}}<br>Deviation: ${{item.toFixed(3)}}` 
                    }}))
                var data_heatmap = {{
                    z: z,
                    type: 'heatmap',
                    text: text,
                    hoverinfo: 'text',
                    colorbar: {{thickness:20}},
                    colorscale: [[0, 'rgb(245,245,245)'], [0.25, 'rgb(181, 137, 214)'], [0.5, 'rgb(153, 105, 199)'], [0.75, 'rgb(106, 53, 156)'], [1, 'rgb(61, 27, 97)']]
                }};

                var data = [data_heatmap];
                var layout = {{
                    yaxis: {{{Yautorange}'scaleanchor': "x", 'scaleratio': {SCALERATIO}, 'showgrid': false, 'rangemode':'tozero', 'zeroline': false, 'range':{VRANGEY}}},
                    xaxis: {{{Xautorange}'showgrid': false, 'rangemode': 'tozero', 'zeroline': false, 'range':{VRANGEX}}},
                    dragmode:"zoom",
                    margin: {{'l' : 30, 't' : 30, 'r' : 30, 'b' : 30}},
                    showlegend: true,
                }}
                Plotly.newPlot('divHeatmapVertical', data, layout, {{scrollZoom:true, displaylogo:false, modeBarButtonsToRemove:["hoverClosestCartesian","hoverCompareCartesian","toggleSpikelines","autoScale2d","lasso2d","select2d","zoom2d","zoomIn2d","zoomOut2d"]}});
            </script>
        </div>
        </div>
    """.format(NP_EVAL_V = np_eval_v, VRANGEY = v_y_range, VRANGEX = v_x_range, SCALERATIO=fov_ratio,i=rowi, j=colj,Xautorange = Xautorange, Yautorange = Yautorange)

    image_heatmap_div = horizontal_image_heatmap + '\n' + vertical_image_heatmap

    return image_heatmap_div

def read_big_ipr_file(iprFile, fov_height, fov_width):
    demo_cb_h5py = iprFile
    flip = demo_cb_h5py['Register'].attrs["Flip"]
    rot90 = demo_cb_h5py['Register'].attrs["CounterRot90"]
    np_eval_g = demo_cb_h5py['Stitch']['StitchEval']['GlobalDeviation'][()]
    rowi = "i"
    colj = "j"
    if rot90%2 == 1:
        fov_ratio = fov_height/fov_width
        np_eval_g = np.rot90(np_eval_g,1)
        np_eval_g = np.flip(np_eval_g,axis=0)
        rowi = "j"
        colj = "i"
    else:
        fov_ratio = fov_width/fov_height
    np_eval_g[np_eval_g < 0] = 0
    np_eval_g = np.round(np_eval_g, decimals=3)
    g_y_max = np_eval_g.shape[0]
    g_x_max = np_eval_g.shape[1]
    np_eval_g = np.array2string(np_eval_g, separator=',')
    
    Yautorange = "'autorange': 'reversed',"
    Xautorange = ""
    y_flip = 1
    x_flip = 0
    if rot90 == 1 :
        x_flip += 1
    elif rot90 == 2:
        x_flip += 1
        y_flip += 1
    elif rot90 == 3:
        y_flip += 1
    if flip == True:
        x_flip += 1
    if x_flip%2 == 1:
        Xautorange = "'autorange': 'reversed',"
    if y_flip%2 == 0:
        Yautorange = ""

    g_y_range = [-1, g_y_max]   
    g_x_range = [-1, g_x_max]

    image_heatmap_div = """
        <div id='heatmap_center'>
            <div>Global Image Stitching Deviation Heatmap
                <button class="button_explain" onclick="show_image_middle()">
                    <i class="fa">?</i>
                </button>
                <div id='div_explain_image_middle'>
                    Image stitching deviation, a lighter color indicates better stitching(the heatmap and frame of axes have been adjusted with the registration parameters)
                </div>
            </div>
            <div id='divHeatmap', style="width:500px;height:400px;margin-left:auto;margin-right:auto;">
            <script>
                var z = {NP_EVAL_G}
                var text = z.map((row, i) => row.map((item, j) => {{
                    return `Row: ${{{i}}}<br>Col: ${{{j}}}<br>Deviation: ${{item.toFixed(3)}}` 
                    }}))
                var data_heatmap = {{
                    z: z,
                    type: 'heatmap',
                    text: text,
                    hoverinfo: 'text',
                    colorbar: {{thickness:20}},
                    colorscale: [[0, 'rgb(245,245,245)'], [0.25, 'rgb(181, 137, 214)'], [0.5, 'rgb(153, 105, 199)'], [0.75, 'rgb(106, 53, 156)'], [1, 'rgb(61, 27, 97)']]
                }};

                var data = [data_heatmap];
                var layout = {{
                    yaxis: {{{Yautorange} 'scaleanchor': "x", 'scaleratio': {SCALERATIO}, 'showgrid': false, 'rangemode':'tozero', 'zeroline': false, 'range':{GRANGEY}}},
                    xaxis: {{{Xautorange}'showgrid': false, 'rangemode': 'tozero', 'zeroline': false, 'range':{GRANGEX}}},
                    dragmode:"zoom",
                    margin: {{'l' : 30, 't' : 30, 'r' : 30, 'b' : 30}},
                    showlegend: true,
                }}
                Plotly.newPlot('divHeatmap', data, layout, {{scrollZoom:true, displaylogo:false, modeBarButtonsToRemove:["hoverClosestCartesian","hoverCompareCartesian","toggleSpikelines","autoScale2d","lasso2d","select2d","zoom2d","zoomIn2d","zoomOut2d"]}});
            </script>
        </div>
        </div>
    """.format(NP_EVAL_G = np_eval_g, GRANGEY = g_y_range, GRANGEX = g_x_range, SCALERATIO=fov_ratio,i=rowi, j=colj,Xautorange = Xautorange, Yautorange = Yautorange)

    return image_heatmap_div

def read_dnb_range_from_h5(h5_file):
    h5_f = h5_file
    if os.path.exists(h5_f):
        h5_data = h5py.File(h5_f, 'r')
        dnb_range = json.loads(h5_data['dnb_merge']['dnb_range'][0])
        h5_data.close()
        return dnb_range
    return {}

def read_h5ad_file(h5ad_file):
    adata = anndata.read_h5ad(h5ad_file)
    return adata

def generate_cluster_data(h5adfile ,adata, bin_size=200):
    if '-' in adata.obs.index[0]:
        dots = np.array([i.split('-') for i in adata.obs.index])
    else:
        dots = adata.obsm['spatial']
    max_x = max(list(map(int,dots[:,0])))
    min_x = min(list(map(int,dots[:,0])))
    max_y = max(list(map(int,dots[:,1])))
    min_y = min(list(map(int,dots[:,1])))
    raw_rangex = max_x-min_x
    raw_rangey = max_y-min_y
    ratio_dnb = raw_rangey/raw_rangex
    ratio_plot = 400/300
    if ratio_dnb > ratio_plot:
        ploy_height = 400
        cluster_size = round(ploy_height/(raw_rangey/bin_size),2)
    else:
        ploy_width = 300
        cluster_size = round(ploy_width/(raw_rangex/bin_size),2)
    if 'leiden' in adata.obs.keys():

        if adata.obs['leiden'].dtype == 'int32':
            vart = int
        else:
            vart = str
        data_cluster_list = []
        total_data_str = '['
        for t in sorted(adata.obs['leiden'].unique().astype('int')):
        #for t in range(2):
            total_data_str = total_data_str + 'cluster' + str(t) + ','
            x = dots[:,0][adata.obs['leiden'] == vart(t)]
            y = dots[:,1][adata.obs['leiden'] == vart(t)]
            text = 'Cluster{0}'.format(t)
            customdata = adata.obs.index[adata.obs['leiden'] == vart(t)]
            js_data = """
                var cluster{t} = {{
                    x: {x},
                    y: {y},
                    mode: 'markers',
                    name: 'Cluster {t}',
                    type: 'scattergl',
                    customdata: {customdata},
                    marker: {{
                        'size': {cluster_size},
                        'opacity': 1.0,
                        'symbol': 'square'
                    }}
                }};
            """.format(t=str(t), x=x.tolist(), y=y.tolist(), text=str(text), customdata=customdata.tolist(), cluster_size=cluster_size)
            data_cluster_list.append(js_data)
        total_data_str = total_data_str + ']'
        total_cluster = "\n".join(data_cluster_list)
    else:
        total_cluster = ''
        total_data_str = []
        
        print_err("fail to find 'lenden' result in '{}'".format(h5adfile),'SAW-A90004')

    return total_data_str, total_cluster

def generate_class_data(h5adfile,adata, bin_size=200):
    if '-' in adata.obs.index[0]:
        dots = np.array([i.split('-') for i in adata.obs.index])
    else:
        dots = adata.obsm['spatial']
    max_x = max(list(map(int,dots[:,0])))
    min_x = min(list(map(int,dots[:,0])))
    max_y = max(list(map(int,dots[:,1])))
    min_y = min(list(map(int,dots[:,1])))
    raw_rangex = max_x-min_x
    raw_rangey = max_y-min_y
    ratio_dnb = raw_rangey/raw_rangex
    ratio_plot = 400/300
    if ratio_dnb > ratio_plot:
        ploy_height = 400
        cluster_size = round(ploy_height/(raw_rangey/bin_size),2)
    else:
        ploy_width = 300
        cluster_size = round(ploy_width/(raw_rangex/bin_size),2)
    if 'leiden' in adata.obs.keys():
        if adata.obs['leiden'].dtype == 'int32':
            vart = int
        else:
            vart = str
        data_class_list = []
        total_data_class_str = '['
        for t in sorted(adata.obs['leiden'].unique().astype('int')):
            total_data_class_str = total_data_class_str + 'class' + str(t) + ','
            x = adata.obsm['X_umap'][:,0][adata.obs['leiden'] == vart(t)]
            y = adata.obsm['X_umap'][:,1][adata.obs['leiden'] == vart(t)]
            text = 'Class{0}'.format(t)
            customdata = adata.obs.index[adata.obs['leiden'] == vart(t)]
            js_data = """
                var class{t} = {{
                    x: {x},
                    y: {y},
                    mode: 'markers',
                    name: 'Cluster {t}',
                    type: 'scattergl',
                    customdata: {customdata},
                    marker: {{
                        'size': {cluster_size},
                        'opacity': 1.0
                    }}
                }};
            """.format(t=str(t), x=x.tolist(), y=y.tolist(), text=str(text), customdata=customdata.tolist(), cluster_size=cluster_size)
            data_class_list.append(js_data)
        total_data_class_str = total_data_class_str + ']'
        total_class = "\n".join(data_class_list)
    else:
        total_data_class_str = []
        total_class = ''
        print_err("fail to find 'lenden' result in '{}'".format(h5adfile),'SAW-A90004')

    return total_data_class_str, total_class

def get_small_images(HE_path, HE_name, plot_range, plot_bin_size,layer="ssDNA", offset_x=0, offset_y=0):
    if not plot_range or not plot_bin_size:
        return [], {}
    dnb_res = int(plot_bin_size['dnb_res'])
    with h5py.File(os.path.join(HE_path, HE_name), 'r') as f:
        full_w , full_h = int(f['metaInfo'].attrs['sizex']), int(f['metaInfo'].attrs['sizey'])
        img_w = img_h = int(f['metaInfo'].attrs['imgSize'])
        x0, y0 = int(f['metaInfo'].attrs['x_start']), int(f['metaInfo'].attrs['y_start'])
        if layer not in f.keys():
            max_indexX, max_indexY = int(f[f'bin_{dnb_res}'].attrs["XimageNumber"]), int(f[f'bin_{dnb_res}'].attrs["YimageNumber"])
        elif "Image" in f[layer].keys():
            max_indexX, max_indexY = int(f[layer]['Image'][f'bin_{dnb_res}'].attrs["XimageNumber"]), int(f[layer]['Image'][f'bin_{dnb_res}'].attrs["YimageNumber"])
        else:
            max_indexX, max_indexY = int(f[layer][f'bin_{dnb_res}'].attrs["XimageNumber"]), int(f[layer][f'bin_{dnb_res}'].attrs["YimageNumber"])

    w, h = plot_range['x1']-plot_range['x0']+1, plot_range['y1']-plot_range['y0']+1

    px0, px1, py0, py1 = plot_range['x0']-w/2-offset_x, plot_range['x1']+w/2-offset_x, plot_range['y0']-h/2-offset_y, plot_range['y1']+h/2-offset_y

    min_idx = int(np.floor((px0 - x0)/(img_w * dnb_res)))
    max_idx = int(np.ceil((px1 - x0)/(img_w * dnb_res)))
    min_idy = int(np.floor((py0 - y0)/(img_h * dnb_res)))
    max_idy = int(np.ceil((py1 - y0)/(img_h * dnb_res)))
    #if min_idx > 0:
    #    min_idx = 0
    #if min_idy > 0:
    #    min_idy = 0
    #idxs = list(filter(lambda x : (x>=0 and x<max_indexX), range(min_idx, max_idx+1)))
    #idys = list(filter(lambda y : (y>=0 and y<max_indexY), range(min_idy, max_idy+1)))
    idxs = list(filter(lambda x : (x>=0 and x<max_indexX), range(min_idx, max_indexX+1)))
    idys = list(filter(lambda y : (y>=0 and y<max_indexY), range(min_idy, max_indexY+1)))
    images = []
    import itertools
    
    with h5py.File(os.path.join(HE_path, HE_name), 'r') as f:
        for (idx, idy) in itertools.product( idxs, idys):
            # full_img_file = os.path.join(HE_path, image_json[f'{dnb_res}'][f'{idx}'][f'{idy}'])
            # img_crop = image_to_base64(full_img_file)
            # if 'ssDNA' not in f.keys():
            #     if f'bin_{dnb_res}' not in f.keys():
            #         print_err("fail to find '{}' or 'ssDNA' item in '{}'".format(f'bin_{dnb_res}',os.path.join(HE_path, HE_name)), "SAW-A90004")
            #     img = f[f'bin_{dnb_res}'][f'{idx}'][f'{idy}'][()]
            # else:
            #     img = f['ssDNA'][f'bin_{dnb_res}'][f'{idx}'][f'{idy}'][()]
            if f'bin_{dnb_res}' in f.keys():
                img = f[f'bin_{dnb_res}'][f'{idx}'][f'{idy}'][()]
            elif "Image" in f[layer].keys():
                img = f[layer]['Image'][f'bin_{dnb_res}'][f'{idx}'][f'{idy}'][()]
            else:
                img = f[layer][f'bin_{dnb_res}'][f'{idx}'][f'{idy}'][()]
            img_crop = image_array_to_base64(img)

            x_start = idx * (img_w * dnb_res) + offset_x
            y_start = idy * (img_h * dnb_res) + offset_y

            if idx == max_indexX-1: ## last one image
                small_img_w = full_w - idx * img_w * dnb_res
            else:
                small_img_w = img_w * dnb_res

            if idy == max_indexY-1: ## last one image
                small_img_h = full_h - idy * img_h * dnb_res
            else:
                small_img_h = img_h * dnb_res
            # print(x_start, y_start, small_img_w, small_img_h)

            # 'source' : '{0}{1}?path={2}'.format('/Stereo-Draftsman/static_img/', os.path.basename(full_img_file), os.path.dirname(full_img_file)),
            image = {
                'source' : img_crop,
                'xref' : 'x',
                'yref' : 'y',
                'sizing' : 'stretch',
                'layer' : 'below',
                'x' : x_start,
                'y' : y_start,
                'sizex' : small_img_w,
                'sizey' : small_img_h
            }
            images.append(image)
    return images

def image_array_to_base64(img_array):
    image = Image.fromarray(img_array)
    return image2base64(image)

def get_color_img(HE_path, HE_name, plot_range, plot_bin_size, offset_x=0, offset_y=0):
    if not plot_range or not plot_bin_size:
        return [], {}
    dnb_res = int(plot_bin_size['dnb_res'])
    with h5py.File(os.path.join(HE_path, HE_name), 'r') as f:
        full_w , full_h = int(f['metaInfo'].attrs['sizex']), int(f['metaInfo'].attrs['sizey'])
        img_w = img_h = int(f['metaInfo'].attrs['imgSize'])
        x0, y0 = int(f['metaInfo'].attrs['x_start']), int(f['metaInfo'].attrs['y_start'])
        max_indexX, max_indexY = int(f["DAPI"]['Image'][f'bin_{dnb_res}'].attrs["XimageNumber"]), int(f["DAPI"]['Image'][f'bin_{dnb_res}'].attrs["YimageNumber"])

    w, h = plot_range['x1']-plot_range['x0']+1, plot_range['y1']-plot_range['y0']+1

    px0, px1, py0, py1 = plot_range['x0']-w/2-offset_x, plot_range['x1']+w/2-offset_x, plot_range['y0']-h/2-offset_y, plot_range['y1']+h/2-offset_y

    min_idx = int(np.floor((px0 - x0)/(img_w * dnb_res)))
    min_idy = int(np.floor((py0 - y0)/(img_h * dnb_res)))

    idxs = list(filter(lambda x : (x>=0 and x<max_indexX), range(min_idx, max_indexX+1)))
    idys = list(filter(lambda y : (y>=0 and y<max_indexY), range(min_idy, max_indexY+1)))
    images = []
    import itertools
    
    with h5py.File(os.path.join(HE_path, HE_name), 'r') as f:
        for (idx, idy) in itertools.product( idxs, idys):
            img_list = []
            if_num = 1
            for i in f.keys():
                if i == "DAPI":
                    img = f[i]['Image'][f'bin_{dnb_res}'][f'{idx}'][f'{idy}'][()]
                    if img.dtype == 'uint16':
                        img = transfer_16bit_to_8bit(img)
                    cmap = get_color(color_map["DAPI"])
                    img_color = gray2color(img,cmap)
                    img_list.append(img_color)
                elif i.endswith("_IF"):
                    img = f[i]['Image'][f'bin_{dnb_res}'][f'{idx}'][f'{idy}'][()]
                    if img.dtype == 'uint16':
                        img = transfer_16bit_to_8bit(img)
                    cmap = get_color(color_map["IF{}".format(if_num)])
                    if_num+=1
                    img_color = gray2color(img,cmap)
                    img_list.append(img_color)
            img_crop = image_array_to_base64(sum(img_list))

            x_start = idx * (img_w * dnb_res) + offset_x
            y_start = idy * (img_h * dnb_res) + offset_y

            if idx == max_indexX-1: ## last one image
                small_img_w = full_w - idx * img_w * dnb_res
            else:
                small_img_w = img_w * dnb_res

            if idy == max_indexY-1: ## last one image
                small_img_h = full_h - idy * img_h * dnb_res
            else:
                small_img_h = img_h * dnb_res
            # print(x_start, y_start, small_img_w, small_img_h)

            # 'source' : '{0}{1}?path={2}'.format('/Stereo-Draftsman/static_img/', os.path.basename(full_img_file), os.path.dirname(full_img_file)),
            image = {
                'source' : img_crop,
                'xref' : 'x',
                'yref' : 'y',
                'sizing' : 'stretch',
                'layer' : 'below',
                'x' : x_start,
                'y' : y_start,
                'sizex' : small_img_w,
                'sizey' : small_img_h
            }
            images.append(image)
    return images

def transfer_16bit_to_8bit(image_16bit):
    min_16bit = np.min(image_16bit)
    max_16bit = np.max(image_16bit)

    image_8bit = np.array(np.rint(255 * ((image_16bit - min_16bit) / (max_16bit - min_16bit))), dtype=np.uint8)
    return image_8bit

def gray2color(gray_array, color_map):
    rows, cols = gray_array.shape
    color_array = np.zeros((rows, cols, 3), np.uint8)
 
    for i in range(0, rows):
        for j in range(0, cols):
            color_array[i, j] = color_map[gray_array[i, j]]

    return color_array

def get_color(color):
    cmap = mpl.colors.LinearSegmentedColormap.from_list('cmap', ['#000000', color], 256)
    colormap_int = np.zeros((256, 3), np.uint8)
    colormap_float = np.zeros((256, 3), np.float)
 
    for i in range(0, 256, 1):
       colormap_float[i, 0] = cmap(i)[0]
       colormap_float[i, 1] = cmap(i)[1]
       colormap_float[i, 2] = cmap(i)[2]
 
       colormap_int[i, 0] = np.int_(np.round(cmap(i)[0] * 255.0))
       colormap_int[i, 1] = np.int_(np.round(cmap(i)[1] * 255.0))
       colormap_int[i, 2] = np.int_(np.round(cmap(i)[2] * 255.0))

    return colormap_int

def image2base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    base64_str = 'data:image/png;base64,{}'.format(base64.b64encode(buffered.getvalue()).decode())
    return base64_str

def find_bg_images_info(file_dir, tissue='ssDNA'):
    HE_path, HE_name, image_type, suffix = find_HE_image_path(file_dir, tissue)
    init_image_info = get_init_image_info(HE_path, HE_name, image_type, suffix)
    return HE_path, HE_name, image_type, init_image_info

def find_HE_image_path(file_dir, tissue='ssDNA'):
    f = file_dir
    froot = os.path.dirname(f)
    f = os.path.basename(file_dir)
    suffix = os.path.splitext(f)[-1]
    image_type = 'small'
    return froot, f, image_type, suffix
    # if tissue == 'ssDNA' :
    #     if f.endswith('ssDNA.h5') or f.endswith('ssDNA.rpi') or f.endswith('.rpi'):
    #         suffix = os.path.splitext(f)[-1]
    #         image_type = 'small'
    #         return froot, f, image_type, suffix
    #     elif f.startswith('HE_') or f.startswith('ssDNA_'):
    #         suffix = os.path.splitext(f)[-1]
    #         image_type = 'full'
    #         return froot, f, image_type, suffix        
                
    # elif tissue == 'conA':
    #     if f.endswith('conA.h5') or f.endswith('conA.rpi'):
    #         suffix = os.path.splitext(f)[-1]
    #         image_type = 'small'
    #         return froot, f, image_type, suffix
    #     elif f.startswith('conA_'):
    #         suffix = os.path.splitext(f)[-1]
    #         image_type = 'full'
    #         return froot, f, image_type, suffix
                
    # return '', '', '', ''

def get_init_image_info(HE_path, HE_name, image_type, suffix):
    image_info = {}
    if not HE_path:
        pass
    elif image_type == 'full':
        coor = HE_name.rstrip(suffix).split('_')[1:]
        if len(coor) == 4:
            image_info['x_start'] = eval(coor[0])
            image_info['y_start'] = eval(coor[1])
            image_info['sizex'] = eval(coor[2])
            image_info['sizey'] = eval(coor[3])
    else:  ## small
        with h5py.File(os.path.join(HE_path, HE_name), 'r') as f:
            image_info['x_start'], image_info['y_start'] = int(f['metaInfo'].attrs['x_start']), int(f['metaInfo'].attrs['y_start'])
            image_info['sizex'], image_info['sizey'] = int(f['metaInfo'].attrs['sizex']), int(f['metaInfo'].attrs['sizey'])
            image_info['layer']=[]
            for layer in f.keys():
                if layer == "metaInfo":
                    continue
                image_info['layer'].append(layer)
    return image_info

def get_sun_fig(file_dir, research_version):
    loadJson = LoadStatJson(file_dir)
    data_json = loadJson.data_json
    data_dict = loadJson.getDataDict(loadJson.data_json)
    values = [i for i in data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"].keys()]
    Total_reads, Valid_CID_Reads, Invalid_CID_Reads, Clean_Reads, Removed_Reads, Reads_Mapped_to_Genome_reads, \
        Uniquely_Mapped_Reads, Multiple_Mapping_Reads, Unmapped_Reads, Discarded_MID_Reads, \
        Too_Short_Reads, Reads_With_Adapter, Reads_With_DNB , Too_Long_Reads, Too_Many_N_Reads, Low_Quality_Reads, Duplicated_Reads, Annotated_Reads, Unannotated_Reads,\
        Unique_Reads, Fail_Filter, Raw_Reads, mapped_reads, Q30_Before_Filtering, Q30_After_Filtering, \
        Q10_Barcode,Q20_Barcode,Q30_Barcode,Q10_MID,Q20_MID,Q30_MID,Q30_seq,\
        Exonic, Intronic, Intergenic, Transcriotome, Antisense,\
        Input_read, Uniquely_Mapped_Read, Multi_Mapping_Read, RNA_Unmapping_Read = loadJson.getReadsStatData(values)
    Q30_Barcode,Q30_Barcode_Rate = Q30_Barcode.split('&')
    Q30_MID,Q30_MID_Rate = Q30_MID.split('&')
    Q30_seq,Q30_seq_Rate = Q30_seq.split('&')
    Duplicated_Reads, Unique_Reads = loadJson.getDupUniqReads(values)
    flag, spot_summary = loadJson.getSpotSummary(data_json)
    ratio_of_dnb_under_tissue = "{:.2f}%".format(float(spot_summary['Number_of_DNB_under_tissue'])*100/float(spot_summary['Contour_area'])) if float(spot_summary['Contour_area'])!=0 else "0%"
    fastq_name_list = [] 
    for i in data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"].keys():
        # fastq_name_list.append('<div class="fastq_margin_top">{fastq_name}</div>'.format(fastq_name=i))
        fastq_name_list.append(i)
    # fastq_name_str = "".join(fastq_name_list)
    fastq_name_str = ",".join(fastq_name_list)

    df_table = loadJson.getDfTable(data_json)
    ###如果是针对to B版本，去除bin1统计结果
    if research_version.upper() == 'N':        
        df_table = df_table.drop([0])

    mean_cell_area, median_cell_area, mean_mid_count, median_mid_count, mean_dnb_count, median_dnb_count, mean_gene_type_count, median_gene_type_count =  '-','-','-','-','-','-','-','-'
    cell_count = "-"
    if '5.CellBin' in data_json.keys():
        for k,v in data_json['5.CellBin']['5.1.CellBin_Stat'][0].items():
            if k == 'Mean Cell Area':
                mean_cell_area = v
            elif k == 'Median Cell Area':
                median_cell_area = v
            elif k == 'Mean MID Count':
                mean_mid_count = v
            elif k == 'Median MID Count':
                median_mid_count = v
            elif k == 'Mean DNB Count':
                mean_dnb_count = v
            elif k == 'Median DNB Count':
                median_dnb_count = v
            elif k == 'Mean Gene Type Count':
                mean_gene_type_count = v
            elif k == 'Median Gene Type Count':
                median_gene_type_count = v
            elif k == 'Cell Count':
                cell_count = v

    #1030 get sunburst persent
    persent_dict,persent_total_reads,persent_cid_reads,persent_clean_reads,persent_unique_mapping_reads, \
        persent_transcriptome,persent_unique_reads,persent_duplicated_reads, \
        persent_intergenic,persent_multi_mapping_reads,persent_unmapping_reads,persent_too_short_reads, \
        persent_invalid_cid_reads,persent_discarded_mid_reads=get_sun_persent(Total_reads,Valid_CID_Reads,Clean_Reads,Transcriotome, \
            Unique_Reads,Duplicated_Reads,RNA_Unmapping_Read,Intergenic,Uniquely_Mapped_Read,Multi_Mapping_Read,Too_Short_Reads,Invalid_CID_Reads,Discarded_MID_Reads)

    bin_div_temple = "<div class='summary_six_content_div'>\
                <div class='summary_bin_content_value'>{0}</div>\
                <div class='summary_bin_content_value'>{1}</div>\
                <div class='summary_bin_content_value'>{2}</div>\
                <div class='summary_bin_content_value'>{3}</div>\
                <div class='summary_bin_content_value'>{4}</div>\
                <div class='summary_bin_content_value'>{5}</div>\
                <div class='summary_bin_content_value'>{6}</div>\
            </div>"

    bin_div_title = "<div>"
    bin_size,mean_reads,median_reads,mean_gene_type,median_gene_type,mean_mid,median_mid='-','-','-','-','-','-','-'
    Mean_Gene_per_bin200, Mean_UMI_per_bin200 = '-','-'
    for i in df_table.iloc:
        for colname in df_table.columns.values.tolist():
            if colname == 'Bin Size':
                bin_size = i[colname]
                if bin_size == '200':
                    Mean_Gene_per_bin200 = i['Mean Gene Type']
                    Mean_UMI_per_bin200 = i['Mean MID']
            elif colname == 'Mean Reads':
                mean_reads = number2human(i[colname])
            elif colname == 'Median Reads':
                median_reads = number2humanInt(i[colname])
            elif colname == 'Mean Gene Type':
                mean_gene_type = number2human(i[colname])
            elif colname == 'Median Gene Type':
                median_gene_type = number2humanInt(i[colname])
            elif colname == 'Mean MID':
                mean_mid = number2human(i[colname])
            elif colname == 'Median MID':
                 median_mid = number2humanInt(i[colname])
        if research_version.upper() == 'N':
            bin_div = bin_div_temple.format(bin_size, mean_reads, median_reads, mean_gene_type, median_gene_type, mean_mid, median_mid)
        else:
            if bin_size == 'cell':
                continue
            else:
                bin_div = bin_div_temple.format(bin_size, number2humanDev(mean_reads), number2humanDev(median_reads), number2humanDev(mean_gene_type), number2humanDev(median_gene_type), number2humanDev(mean_mid), number2humanDev(median_mid))

        bin_div_title += bin_div
    bin_div_title += '</div>' 
    

    name_pro = []
    df = [['labels','parents','value','text']]

    if len(values) == len(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"].keys()):
        parents = parents_dict
    else:
        parents = parents_dict_sort
    
    for k,v in parents.items():
        df.append([k.replace('_',' '),v.replace('_',' '),str(eval(k)),persent_dict[k] + hovertext_dict[k]])
        if k == 'Total_reads':
            if research_version.upper() == 'N': 
                name_pro.append('{}'.format(number2human(eval(k))))
            else:
                name_pro.append('{}'.format(number2humanDev(eval(k))))
        else:
            if research_version.upper() == 'N': 
                name_pro.append('{} ({}%)'.format(number2human(eval(k)),round(eval(k)/eval(parents_dict[k])*100,2)))
            else:
                name_pro.append('{}({}%)'.format(str(number2humanDev(eval(k))),round(eval(k)/eval(parents_dict[k])*100,2)))

    # for k,v in parents.items():
    #     if research_version.upper() == 'N':
    #         if k == 'Unique_Reads' or k == 'Duplicated_Reads':
    #             continue
    #         else:
    #             df.append([k.replace('_',' '),v.replace('_',' '),str(eval(k)),persent_dict[k] + hovertext_dict[k]])
    #             if k == 'Total_reads':
    #                 name_pro.append('{}'.format(number2human(eval(k))))
    #             else:
    #                 name_pro.append('{} ({}%)'.format(number2human(eval(k)),round(eval(k)/eval(parents_dict[k])*100,2)))
    #     else:
    #         df.append([k.replace('_',' '),v.replace('_',' '),str(eval(k)),persent_dict[k] + hovertext_dict[k]])
    #         if k == 'Total_reads':
    #             if research_version.upper() == 'N': 
    #                 name_pro.append('{}'.format(number2human(eval(k))))
    #             else:
    #                 name_pro.append('{}'.format(number2humanDev(eval(k))))
    #         else:
    #             if research_version.upper() == 'N': 
    #                 name_pro.append('{} ({}%)'.format(number2human(eval(k)),round(eval(k)/eval(parents_dict[k])*100,2)))
    #             else:
    #                 name_pro.append('{}({}%)'.format(str(number2humanDev(eval(k))),round(eval(k)/eval(parents_dict[k])*100,2)))
    
    
    df = DataFrame(df)
    df.columns = df.loc[0,:]
    df = df.loc[1:,:]
    # print(df['labels'])
    df['labels'][6] = 'Non-Relevant Short Reads'
    df['labels'][10] = 'Multi-Mapped Reads'
    if research_version.upper() == 'N':
       df['labels'][14] = "Sequencing Saturation"
    # print(df['labels'])

    #return df,name_pro
    return df,name_pro, fastq_name_str, number2human(Total_reads), number2human(Valid_CID_Reads), number2human(Clean_Reads), number2human(Reads_Mapped_to_Genome_reads), number2human(Unique_Reads), number2human(Duplicated_Reads), \
        Q30_Barcode_Rate, Q30_MID_Rate, Q30_seq_Rate, number2human(Input_read), number2human(Uniquely_Mapped_Read), number2human(Multi_Mapping_Read),\
        number2human(RNA_Unmapping_Read), number2human(Exonic), number2human(Intronic),number2human(Intergenic), number2human(Transcriotome), number2human(Antisense), \
        number2human(spot_summary['Contour_area']), number2human(spot_summary['Number_of_DNB_under_tissue']),ratio_of_dnb_under_tissue, spot_summary['Ratio'], number2human(spot_summary['Total_gene_type']), number2human(spot_summary['MID_counts']), spot_summary['Fraction_MID_in_spots_under_tissue'], number2human(spot_summary['Reads_under_tissue']), spot_summary['Fraction_reads_in_spots_under_tissue'], bin_div_title, \
        number2human(Mean_Gene_per_bin200), number2human(Mean_UMI_per_bin200), Too_Many_N_Reads, Low_Quality_Reads, Raw_Reads, Q30_Before_Filtering, Q30_After_Filtering, number2human(Too_Short_Reads), number2human(Reads_With_Adapter), number2human(Reads_With_DNB), number2human(mean_cell_area),number2human(cell_count), number2human(median_cell_area), number2human(mean_mid_count), number2humanInt(median_mid_count), number2human(mean_dnb_count), number2humanInt(median_dnb_count), number2human(mean_gene_type_count), number2humanInt(median_gene_type_count),\
        number2human(Invalid_CID_Reads), number2human(Discarded_MID_Reads), \
        persent_total_reads,persent_cid_reads,persent_clean_reads,persent_unique_mapping_reads, \
        persent_transcriptome,persent_unique_reads,persent_duplicated_reads, \
        persent_intergenic,persent_multi_mapping_reads,persent_unmapping_reads,persent_too_short_reads, \
        persent_invalid_cid_reads,persent_discarded_mid_reads

def get_sun_persent(Total_reads,Valid_CID_Reads,Clean_Reads,Transcriotome, \
            Unique_Reads,Duplicated_Reads,RNA_Unmapping_Read,Intergenic,Uniquely_Mapped_Read,Multi_Mapping_Read,Too_Short_Reads,Invalid_CID_Reads,Discarded_MID_Reads):
    persent_total_reads,persent_cid_reads,persent_clean_reads,persent_unique_mapping_reads, \
        persent_transcriptome,persent_unique_reads,persent_duplicated_reads, \
        persent_intergenic,persent_multi_mapping_reads,persent_unmapping_reads,persent_too_short_reads, \
        persent_invalid_cid_reads,persent_discarded_mid_reads="0%","0%","0%","0%","0%","0%","0%","0%","0%","0%","0%","0%","0%"
    persent_dict=defaultdict(str)
    if Total_reads>0:
        persent_total_reads="100%"
        persent_dict["Total_reads"]=persent_total_reads
        persent_cid_reads = "{:.1f}%".format(Valid_CID_Reads*100/Total_reads)
        persent_dict["Valid_CID_Reads"]=persent_cid_reads
        persent_clean_reads = "{:.1f}%".format(Clean_Reads*100/Valid_CID_Reads) if Valid_CID_Reads!=0 else "0%" 
        persent_dict["Clean_Reads"]=persent_clean_reads
        persent_unique_mapping_reads = "{:.1f}%".format(Uniquely_Mapped_Read*100/Clean_Reads) if Clean_Reads !=0 else "0%" 
        persent_dict["Uniquely_Mapped_Reads"]=persent_unique_mapping_reads
        persent_transcriptome = "{:.1f}%".format(Transcriotome*100/Uniquely_Mapped_Read) if Uniquely_Mapped_Read !=0 else "0%" 
        persent_dict["Annotated_Reads"]=persent_transcriptome
        persent_unique_reads = "{:.1f}%".format(Unique_Reads*100/Transcriotome) if Transcriotome !=0 else "0%" 
        persent_dict["Unique_Reads"]=persent_unique_reads
        persent_duplicated_reads = "{:.1f}%".format(Duplicated_Reads*100/Transcriotome) if Transcriotome !=0 else "0%" 
        persent_dict["Duplicated_Reads"]=persent_duplicated_reads
        persent_intergenic = "{:.1f}%".format(Intergenic*100/Uniquely_Mapped_Read) if Uniquely_Mapped_Read !=0 else "0%" 
        persent_dict["Unannotated_Reads"]=persent_intergenic
        persent_multi_mapping_reads = "{:.1f}%".format(Multi_Mapping_Read*100/Clean_Reads) if Clean_Reads !=0 else "0%" 
        persent_dict["Multiple_Mapping_Reads"]=persent_multi_mapping_reads
        persent_unmapping_reads = "{:.1f}%".format(RNA_Unmapping_Read*100/Clean_Reads) if Clean_Reads !=0 else "0%" 
        persent_dict["Unmapped_Reads"]=persent_unmapping_reads
        persent_too_short_reads = "{:.1f}%".format(Too_Short_Reads*100/Valid_CID_Reads) if Valid_CID_Reads !=0 else "0%"
        persent_dict["Too_Short_Reads"]=persent_too_short_reads
        persent_invalid_cid_reads = "{:.1f}%".format(Invalid_CID_Reads*100/Total_reads)
        persent_dict["Invalid_CID_Reads"]=persent_invalid_cid_reads
        persent_discarded_mid_reads = "{:.1f}%".format(Discarded_MID_Reads*100/Total_reads)
        persent_dict["Discarded_MID_Reads"]=persent_discarded_mid_reads

    return persent_dict,persent_total_reads,persent_cid_reads,persent_clean_reads,persent_unique_mapping_reads, \
        persent_transcriptome,persent_unique_reads,persent_duplicated_reads, \
        persent_intergenic,persent_multi_mapping_reads,persent_unmapping_reads,persent_too_short_reads, \
        persent_invalid_cid_reads,persent_discarded_mid_reads

class LoadStatJson(object):
    def __init__(self, file_dir):
        self.data_json = self.readStatJson(file_dir)

    def readStatJson(self, file_dir):
        f = file_dir
        if not  os.path.getsize(f):
            print_err(f, "SAW-A90003")
        with open(f,'r') as read_json:
            data_json = json.loads(read_json.read().replace('Umi','MID').replace('umi','MID').replace('barcode','CID').replace('Barcode','CID'))
        return data_json

    def getDfTable(self, data_json):
        if '4.TissueCut' in data_json:
            df_table = pd.DataFrame(
                    [list(i.values()) for i in data_json["4.TissueCut"]["4.2.TissueCut_Bin_stat"]]  
                )
            df_table.columns = ['Bin Size', 'Mean Reads', 'Median Reads', 'Mean Gene Type', 'Median Gene Type', 'Mean MID', 'Median MID']
        elif '3.Basic' in data_json:
            df_table = pd.DataFrame(
                    [list(i.values()) for i in data_json["3.Basic"]["3.2.Bin"]]  
                )
            df_table.columns = ['Bin Size', 'Filter Mini Umi', 'Bin Numbers', 'Gene Numbers', 'Umi Counts/Bin', 'Gene Counts/Bin']
        else:
            df_table = pd.DataFrame()
        
        return df_table
    
    def getSpotSummary(self, data_json):
        flag = 'None'
        spot_summary = []
        if '4.TissueCut' in data_json:
            spot_summary = data_json["4.TissueCut"]["4.1.TissueCut_Total_Stat"][0]
            flag = '4'
        elif '3.Basic' in data_json:
            spot_summary = data_json["3.Basic"]["3.1.Get_Exp"][0]
            flag = '3'
        return flag, spot_summary
    
    def IsCell(self, data_json):
        is_cell = None
        total_stat_summary = []
        bin_stat_summary = []
        if '4.TissueCut' in data_json:
            is_cell = False
        elif '4.CellCut' in data_json:
            is_cell = True
            total_stat_summary = data_json["4.CellCut"]["4.1.CellCut_Total_Stat"][0]
            bin_stat_summary = data_json["4.CellCut"]["4.3.CellCut_Bin_stat"][0]
        return is_cell,total_stat_summary, bin_stat_summary

    def getDataDict(self, data_json):
        data_dict = Vividict()
        sample_count = Vividict()
        for k1,v1 in data_json.items():
            if k1 == 'version':
                data_dict['version'] = data_json[k1]
                continue
            for k2,v2 in v1.items():
                count = 0
                for i in v2:
                    sample_id = count
                    if "Sample_id" in i.keys():
                        sample_id = i["Sample_id"]
                    elif "Sample_Name" in i.keys():
                        sample_id = i["Sample_Name"]
                    elif "Sample_Id" in i.keys():
                        sample_id = i["Sample_Id"]
                    if sample_id not in data_dict[k1][k2]:
                        sample_count[k1][k2][sample_id] = 0
                    else:
                        sample_count[k1][k2][sample_id] += 1
                        sample_id = '{0}_{1}'.format(sample_id, sample_count[k1][k2][sample_id])
                        
                    data_dict[k1][k2][sample_id] = i
                    count += 1
        if 'version' not in data_dict.keys():
            data_dict['version'] = 'version_v1'
        return data_dict
    
    def getReadsStatData(self, samples):
        data_dict = self.getDataDict(self.data_json)
        Q10_Barcode,Q20_Barcode,Q30_Barcode,Q10_MID,Q20_MID,Q30_MID, Q30_seq = 0, 0, 0, 0, 0, 0, 0

        Total_reads, Valid_CID_Reads, Invalid_CID_Reads, Clean_Reads, Removed_Reads, Reads_Mapped_to_Genome_reads, \
        Uniquely_Mapped_Reads, Multiple_Mapping_Reads, Unmapped_Reads, Discarded_MID_Reads, \
        Too_Short_Reads, Reads_With_Adapter, Reads_With_DNB, Too_Long_Reads, Too_Many_N_Reads, Low_Quality_Reads, Duplicated_Reads, \
        Unique_Reads, Fail_Filter, Raw_Reads, mapped_reads, \
        Q30_Before_Filtering, Q30_After_Filtering, Total_Base_Before_Filtering, Total_Base_After_Filtering = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0         

        Input_read, Uniquely_Mapped_Read, Multi_Mapping_Read, RNA_Unmapping_Read= 0,0,0,0

        for value in samples:
            
            # Clean Reads Data
            # mapping reads
            Uniquely_Mapped_Reads += tran_data(data_dict["2.Alignment"]["2.2.Uniquely_Mapped_Read"][value]['Mapped_Reads_Number']) 
            Multiple_Mapping_Reads += tran_data(data_dict["2.Alignment"]["2.3.Multi_Mapping_Read"][value]['Multiple_Loci'].split('(')[0]) + tran_data(data_dict["2.Alignment"]["2.3.Multi_Mapping_Read"][value]["Many_Loci"].split('(')[0])
            Reads_Mapped_to_Genome_reads = round(Uniquely_Mapped_Reads + Multiple_Mapping_Reads,2)
            # Unmaping reads
            #Unmapping_RATE = round(Decimal(data_dict["2.Alignment"]["2.4.Unmapping_Read"][value]["Too_Many_Mismatches"].split('(')[-1].strip('%)'))/100 + Decimal(data_dict["2.Alignment"]["2.4.Unmapping_Read"][value]["Too_Short"].split('(')[-1].strip('%)'))/100 + Decimal(data_dict["2.Alignment"]["2.4.Unmapping_Read"][value]["Other"].split('(')[-1].strip('%)'))/100,2)
            Clean_Reads += tran_data(data_dict["2.Alignment"]["2.1.Input_Read"][value]["Number_Of_Input_Reads"])
            Unmapped_Reads = round(Clean_Reads-Reads_Mapped_to_Genome_reads, 2)
            if 'Total_Base_Before_Filtering' in data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]:
                Q30_Before_Filtering += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]['Q30_Before_Filtering'].split('(')[-2])
                Q30_After_Filtering += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]['Q30_After_Filtering'].split('(')[-2])
                Total_Base_Before_Filtering += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]['Total_Base_Before_Filtering'])
                Total_Base_After_Filtering += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]['Total_Base_After_Filtering'])            

            # Filiter reads Data
            Raw_Reads += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]["Raw_Reads"])
            Low_Quality_Reads += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]["Low_Quality_Reads"])
            Too_Many_N_Reads += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]["Too_Many_N_Reads"])
            if data_dict['version'] == 'version_v2':
                Reads_With_Adapter += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]["reads_with_adapter"])
                Reads_With_DNB += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]["reads_with_dnb"])
                Too_Short_Reads = Reads_With_Adapter + Reads_With_DNB
            else:
                Reads_With_Adapter = '-'
                Reads_With_DNB = '-'
                Too_Short_Reads += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]["Too_Short_Reads"])
            Too_Long_Reads += tran_data(data_dict["1.Filter_and_Map"]["1.2.Filter_Stat"][value]["Too_Long_Reads"])
            mapped_reads += tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["mapped_reads"].split('(')[-2])
            Discarded_MID_Reads = mapped_reads - Raw_Reads
            
            # Invalid_CID_Reads Data
            Invalid_CID_Reads += tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["total_reads"]) - tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["mapped_reads"].split('(')[-2]) 
            #Removed_Reads = Discarded_MID_Reads + Too_Long_Reads + Too_Short_Reads + Low_Quality_Reads + Too_Many_N_Reads
            if data_dict['version'] == 'version_v2':
                Removed_Reads = Reads_With_Adapter + Reads_With_DNB + Low_Quality_Reads + Too_Many_N_Reads
            else:
                Removed_Reads = Too_Short_Reads + Low_Quality_Reads + Too_Many_N_Reads
            # print(Removed_Reads , Discarded_MID_Reads , Too_Long_Reads , Too_Short_Reads , Low_Quality_Reads , Too_Many_N_Reads)
            Valid_CID_Reads = Removed_Reads + Clean_Reads
            
            #Total reads Data
            #Total_reads = Valid_CID_Reads + Invalid_CID_Reads
            if value == 'Spark_total':
                Discarded_MID_Reads = 0
            
            Total_reads = Valid_CID_Reads + Invalid_CID_Reads + Discarded_MID_Reads

            # Seq QC Data
            if data_dict['version'] == 'version_v2':
                Q30_seq_rate = tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["Q30_bases_in_seq"].replace('%',''))/100
                Q30_seq += round(Q30_seq_rate*tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["total_reads"]),2)
            else:
                Q30_seq_rate = '-'
                Q30_seq = '-'

            # Barcode and MID QC Data
            Q10_Barcode_rate = tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["Q10_bases_in_CID"].replace('%',''))/100
            Q20_Barcode_rate = tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["Q20_bases_in_CID"].replace('%',''))/100
            Q30_Barcode_rate = tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["Q30_bases_in_CID"].replace('%',''))/100
            Q10_MID_rate = tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["Q10_bases_in_MID"].replace('%',''))/100
            Q20_MID_rate = tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]['Q20_bases_in_MID'].replace('%',''))/100
            Q30_MID_rate = tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["Q30_bases_in_MID"].replace('%',''))/100
            
            Q10_Barcode += round(Q10_Barcode_rate*tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["total_reads"]),2)
            Q20_Barcode += round(Q20_Barcode_rate*tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["total_reads"]),2)
            Q30_Barcode += round(Q30_Barcode_rate*tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["total_reads"]),2)
            Q10_MID += round(Q10_MID_rate*tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["total_reads"]),2)
            Q20_MID += round(Q20_MID_rate*tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["total_reads"]),2)
            Q30_MID += round(Q30_MID_rate*tran_data(data_dict["1.Filter_and_Map"]["1.1.Adapter_Filter"][value]["total_reads"]),2)

            # RNA mapping Data
            Input_read += tran_data(data_dict["2.Alignment"]["2.1.Input_Read"][value]["Number_Of_Input_Reads"])
            Uniquely_Mapped_Read += tran_data(data_dict["2.Alignment"]["2.2.Uniquely_Mapped_Read"][value]["Mapped_Reads_Number"])
            Multi_Mapping_Read += tran_data(data_dict["2.Alignment"]["2.3.Multi_Mapping_Read"][value]["Multiple_Loci"].split('(')[0]) + tran_data(data_dict["2.Alignment"]["2.3.Multi_Mapping_Read"][value]["Many_Loci"].split('(')[0])
            RNA_Unmapping_Read += tran_data(data_dict["2.Alignment"]["2.4.Unmapping_Read"][value]["Too_Many_Mismatches"].split('(')[0]) + tran_data(data_dict["2.Alignment"]["2.4.Unmapping_Read"][value]["Too_Short"].split('(')[0]) + tran_data(data_dict["2.Alignment"]["2.4.Unmapping_Read"][value]["Other"].split('(')[0])

        # Annotation Data
        Exonic = tran_data(data_dict["2.Alignment"]["2.7.Annotation"][0]["EXONIC"].split('(')[0])
        Intronic = tran_data(data_dict["2.Alignment"]["2.7.Annotation"][0]["INTRONIC"].split('(')[0])
        Intergenic = tran_data(data_dict["2.Alignment"]["2.7.Annotation"][0]["INTERGENIC"].split('(')[0])
        Transcriotome = tran_data(data_dict["2.Alignment"]["2.7.Annotation"][0]["TRANSCRIPTOME"].split('(')[0])
        Antisense = tran_data(data_dict["2.Alignment"]["2.7.Annotation"][0]["ANTISENSE"].split('(')[0])
        
        # Filter and deduplication
        # Pass Filter Data
        Annotated_Reads = Exonic+Intronic
        Unannotated_Reads = Uniquely_Mapped_Reads - Annotated_Reads
        Unique_Reads = tran_data(data_dict["2.Alignment"]["2.6.Filter_And_Deduplication"][0]['UNIQUE_READS'])

        Duplicated_Reads = round(Annotated_Reads-Unique_Reads,2)
    
        # Fail Filter Data
        Fail_Filter = round(Reads_Mapped_to_Genome_reads - Unique_Reads - Duplicated_Reads, 2)

        #print(Input_read, Uniquely_Mapped_Read, Multi_Mapping_Read, RNA_Unmapping_Read, Chimeric_Read)
        Q10_Barcode = '{}&{}%'.format(number2human(Q10_Barcode),round(Q10_Barcode/Total_reads*100,2))
        Q20_Barcode = '{}&{}%'.format(number2human(Q20_Barcode),round(Q20_Barcode/Total_reads*100,2))
        Q30_Barcode = '{}&{}%'.format(number2human(Q30_Barcode),round(Q30_Barcode/Total_reads*100,2))
        Q10_MID = '{}&{}%'.format(number2human(Q10_MID),round(Q10_MID/Total_reads*100,2))
        Q20_MID = '{}&{}%'.format(number2human(Q20_MID),round(Q20_MID/Total_reads*100,2))
        Q30_MID = '{}&{}%'.format(number2human(Q30_MID),round(Q30_MID/Total_reads*100,2))
        if data_dict['version'] != 'version_v2':
            Q30_seq = '{}&{}'.format('-','-')
        else:
            Q30_seq = '{}&{}%'.format(number2human(Q30_seq),round(Q30_seq/Total_reads*100,2))

        if Total_Base_Before_Filtering:
            Q30_Before_Filtering = '{}%'.format(round(Q30_Before_Filtering/Total_Base_Before_Filtering*100,2))
        if Total_Base_After_Filtering:
            Q30_After_Filtering = '{}%'.format(round(Q30_After_Filtering/Total_Base_After_Filtering*100,2))

        return Total_reads, Valid_CID_Reads, Invalid_CID_Reads, Clean_Reads, Removed_Reads, Reads_Mapped_to_Genome_reads, \
        Uniquely_Mapped_Reads, Multiple_Mapping_Reads, Unmapped_Reads, Discarded_MID_Reads, \
        Too_Short_Reads, Reads_With_Adapter, Reads_With_DNB, Too_Long_Reads, Too_Many_N_Reads, Low_Quality_Reads, Duplicated_Reads, Annotated_Reads, Unannotated_Reads,\
        Unique_Reads, Fail_Filter, Raw_Reads, mapped_reads, Q30_Before_Filtering, Q30_After_Filtering, \
        Q10_Barcode,Q20_Barcode,Q30_Barcode,Q10_MID,Q20_MID,Q30_MID,Q30_seq,\
        Exonic, Intronic, Intergenic, Transcriotome, Antisense,\
        Input_read, Uniquely_Mapped_Read, Multi_Mapping_Read, RNA_Unmapping_Read
    
    def getDupUniqReads(self, samples):
        data_dict = self.getDataDict(self.data_json)
        Unique_Reads = tran_data(data_dict["2.Alignment"]["2.6.Filter_And_Deduplication"][0]['UNIQUE_READS'])
        Exonic = tran_data(data_dict["2.Alignment"]["2.7.Annotation"][0]["EXONIC"].split('(')[0])
        Intronic = tran_data(data_dict["2.Alignment"]["2.7.Annotation"][0]["INTRONIC"].split('(')[0])
        Annotated_Reads = Exonic+Intronic

        Duplicated_Reads = round(Annotated_Reads-Unique_Reads,2)
        return Duplicated_Reads, Unique_Reads

class LoadImageJson(object):
    def __init__(self, file_dir):
        self.data_json = self.readImageJson(file_dir)

    def readImageJson(self, file_dir):
        f = file_dir
        with open(f,'r') as read_json:
            data_json = json.loads(read_json.read().replace('_',''))
        return data_json

def tran_data(data):
    if isinstance(data, str):
        if data.isdigit():
            number = int(data)
        else:
            number = float(data)
    elif isinstance(data, int):
        number = int(data)
    else:
        number = float(data)

    return number

def number2human(number_raw):
    if number_raw == '-':
        number = number_raw
    elif isinstance(number_raw, str):
        if  number_raw.isdigit():
            number = (format(int(number_raw), ',d'))
        else:
            if float(number_raw) > 100:
                number = (format(int(float(number_raw)), ',d'))
            else:
                number = (format(float(number_raw), ',.2f'))
    elif isinstance(number_raw, int):
        number = (format(int(number_raw), ',d'))
    else:
        if float(number_raw) > 100:
            number = (format(int(number_raw), ',d'))
        else:
            number = (format(float(number_raw), ',.2f'))

    return str(number)

def number2humanInt(number_raw):
    if number_raw == '-':
        number = number_raw
    elif isinstance(number_raw, str):
        if  number_raw.isdigit():
            number = (format(int(number_raw), ',d'))
        else:
            number = (format(int(float(number_raw)), ',d'))
    elif isinstance(number_raw, int):
        number = (format(int(number_raw), ',d'))
    else:
        number = (format(int(number_raw), ',d'))

    return str(number)

def number2humanDev(n):
    m = 0
    n = str(n).replace(',',"")
    try:
        m = float(n)
    except:
        return n
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {'K': 1000, 'M': 1000000, 'G': 1000000000, 'T': 1000000000000, 'P': 1000000000000000, 'E': 1000000000000000000, 'Z': 1000000000000000000000, 'Y': 1000000000000000000000000}
    for s in reversed(symbols):
        if m >= prefix[s]:
            value = m / prefix[s]
            return '%.2f%s' % (value,s)
    return '%s' % n

class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()    # retain local pointer to value
        return value                        # faster to return than dict lookup

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def showCollapse(info_list):
    collapse = '<div>'
    for info in info_list:
        collapse += '<h6 class="collapse-title text-blue">{0}</h6>'.format(info['title'])
        collapse += '<span class="collapse-text">{0}</span>'.format(info['content'])
        collapse += '<br>'
    collapse += '</div>'
    return collapse

def showspan(spanlist):
    spaninfo = ""
    for i in spanlist:
        if i.upper()== "DAPI" or i.upper()== "SSDNA" or i.upper()== "HE":
            spaninfo+="<option selected=selected value="
            spaninfo+=i
            spaninfo+=">"+i+"</option>"
        else:
            spaninfo+="<option value="
            spaninfo+=i
            spaninfo+=">"+i+"</option>"
    return spaninfo

axisx = {
    'showgrid' : True, 
    'showticklabels' : True,
    'zeroline' : True,
}
axisy = {
    'showgrid' : True, 
    'showticklabels' : True,
    'zeroline' : True,
    'autorange': 'reversed',
}
DEFAULT_COLORSCALE = [[0, 'rgb(12,51,131)'], [0.25, 'rgb(10,136,186)'],\
        [0.5, 'rgb(242,211,56)'], [0.75, 'rgb(242,143,56)'], \
        [1, 'rgb(217,30,30)']]
