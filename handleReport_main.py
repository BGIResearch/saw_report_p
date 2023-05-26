# Copyright (C) BGI-Reasearch - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by STOmics development team P_stomics_dev@genomics.cn, May 2017
# -*- coding:utf-8 -*-
#!/usr/bin/env python3

from email.policy import default
import os, sys
from optparse import OptionParser
import sys
import time
from handleReport_develop import statistic
from handleReport_develop import cgef_stat_addition
from generate_analysis_report import generate_html_function
import gefpy
from gefpy import plot

def main():
    """
    %prog [options]
    generate SN.statistics.json and analysis report
    """

    parser = OptionParser(main.__doc__)
    parser.add_option("-p", "--plotlyjsPackage",help = "The plotly js package")
    parser.add_option("-m", "--barcodeMapStat", help = "The barcodeMap stat file (*read_barcodeMap.stat)")
    parser.add_option("-a", "--alignmentLog", help = "The alignment log file (*.Log.final.out)")
    parser.add_option("-g", "--alignmentStat", help = "The alignment stat file (*dedup.target.bam.summary.stat)")
    parser.add_option("-l", "--tissueCutLog", help = "The tissue cut log file (TissueCut.log)")
    parser.add_option("-o", "--outfile" , default = None, help = "The output file (result path)")

    parser.add_option("-n", "--h5File", help = "The stereomics h5 file or gef file (stereomics.h5 or SN.gef)")
    parser.add_option("-d", "--h5adFile", help = "The cluster h5ad file (cell_cluster.h5ad)")
    parser.add_option("-i", "--rpi", help = "The rpi file (.ssDNA.rpi)")
    parser.add_option("-b", "--bin200Saturation", default="N", help = "The bin200 saturation img (scatter_200x200_MID_gene_counts.png)")
    parser.add_option("-v", "--bin200violin", default="N", help = "The bin200 violin img (violin_200x200_MID_gene.png)")
    parser.add_option("-t", "--saturation", help = "The sequence saturation img (plot_200x200_saturation.png)")
    parser.add_option("-s", "--sn", help = "The sample id")
    parser.add_option("-r", "--research", default="standard_version", help = "research_version/standard_version")
    parser.add_option("-c", "--bin200MIDGeneDNB", default="N", help = "The png of statistic 200x200 MID gene DNB (statistic_200x200_MID_gene_DNB.png)")
    
    parser.add_option("--bin1Saturation", default="N", help = "The bin1 saturation img (plot_1x1_saturation.png)")
    # parser.add_option("--bin1Saturation", default="N", help = "The bin1 saturation img (scatter_1x1_MID_gene_counts.png)")
    # parser.add_option("--bin1violin", default="N", help = "The bin1 violin img (violin_1x1_MID_gene.png)")
    # parser.add_option("--bin1MIDGeneDNB", default="N", help = "The png of statistic 1x1 MID gene DNB (statistic_1x1_MID_gene_DNB.png)")
    parser.add_option("--bin20Saturation", default="N", help = "The bin20 saturation img (scatter_20x20_MID_gene_counts.png)")
    parser.add_option("--bin20violin", default="N", help = "The bin20 violin img (violin_20x20_MID_gene.png)")
    parser.add_option("--bin20MIDGeneDNB", default="N", help = "The png of statistic 20x20 MID gene DNB (statistic_20x20_MID_gene_DNB.png)")
    parser.add_option("--bin50Saturation", default="N", help = "The bin50 saturation img (scatter_50x50_MID_gene_counts.png)")
    parser.add_option("--bin50violin", default="N", help = "The bin50 violin img (violin_50x50_MID_gene.png)")
    parser.add_option("--bin50MIDGeneDNB", default="N", help = "The png of statistic 50x50 MID gene DNB (statistic_50x50_MID_gene_DNB.png)")
    parser.add_option("--bin100Saturation", default="N", help = "The bin100 saturation img (scatter_100x100_MID_gene_counts.png)")
    parser.add_option("--bin100violin", default="N", help = "The bin100 violin img (violin_100x100_MID_gene.png)")
    parser.add_option("--bin100MIDGeneDNB", default="N", help = "The png of statistic 100x100 MID gene DNB (statistic_100x100_MID_gene_DNB.png)")
    parser.add_option("--bin150Saturation", default="N", help = "The bin150 saturation img (scatter_150x150_MID_gene_counts.png)")
    parser.add_option("--bin150violin", default="N", help = "The bin150 violin img (violin_150x150_MID_gene.png)")
    parser.add_option("--bin150MIDGeneDNB", default="N", help = "The png of statistic 150x150 MID gene DNB (statistic_150x150_MID_gene_DNB.png)")
    # parser.add_option("--bin200Saturation", default="N", help = "The bin200 saturation img (scatter_200x200_MID_gene_counts.png)")
    # parser.add_option("--bin200violin", default="N", help = "The bin200 violin img (violin_200x200_MID_gene.png)")
    # parser.add_option("--bin200MIDGeneDNB", default="N", help = "The png of statistic 200x200 MID gene DNB (statistic_200x200_MID_gene_DNB.png)")
    
    parser.add_option("--cellBinGef", default="N", help = "The cell bin gef file (SN.cellbin.gef)")
    parser.add_option("--cellCluster", default="N", help = "The cell cluster h5ad file (SN.cell.cluster.h5ad)")
    parser.add_option("--iprFile", default="N", help = "The ipr file (SN.ipr)")
    parser.add_option("--rpi_resolution", default=100, help = "The resolution or rpi")
    parser.add_option("--species", default="N", help = "Species")
    parser.add_option("--tissue", default="N", help = "Tissue")
    parser.add_option("--logo", default="N", help = "Logo.png")
    parser.add_option("--tissue_fig", default="N", help = "tissue_fig")
    parser.add_option("--reference", default="N", help = "The reference which used to mapping")

    parser.add_option("--pipelineVersion", default="N", help = "The analysis pipeline version")


    opts, args = parser.parse_args()
    
    root_path = os.path.dirname(__file__)

    if(opts.barcodeMapStat == None):
        print_err("-m or --barcodeMapStat","SAW-A90001")
    elif (opts.alignmentLog == None):
        print_err("-a or --alignmentLog","SAW-A90001")
    elif (opts.alignmentStat == None):
        print_err("-g or --alignmentStat","SAW-A90001")
    elif( not os.path.exists(opts.alignmentStat)):
        print_err(os.path.abspath(opts.alignmentStat),"SAW-A90002")
    elif (opts.tissueCutLog == None):
        print_err("-l or --tissueCutLog","SAW-A90001")
    elif( not os.path.exists(opts.tissueCutLog)):
        print_err(os.path.abspath(opts.tissueCutLog),"SAW-A90002")
    elif (opts.outfile == None):
        print_err("-o or --outfile","SAW-A90001")
    # elif( not os.path.exists(opts.plotlyjsPackage)):
    #     print_err(os.path.abspath(opts.plotlyjsPackage),"SAW-A90002")
    elif (opts.species == None):
        print_err("--species","SAW-A90001")
    elif (opts.tissue == None):
        print_err("--tissue","SAW-A90001")
    elif (opts.reference == None):
        print_err("--reference","SAW-A90001")
    elif (opts.sn == None):
        print_err("-s or --sn","SAW-A90001")
    else:
        barcodeMapStat = opts.barcodeMapStat
        alignmentLog = opts.alignmentLog
        alignmentStat = opts.alignmentStat
        tissueCutLog = opts.tissueCutLog
        outfile_path = opts.outfile
        os.makedirs(outfile_path, exist_ok=True)
        plotlyJsFile=""
        if (opts.plotlyjsPackage == None):
            plotlyJsFile=os.path.join(root_path,"plotly_package.txt")
        else:
            plotlyJsFile = opts.plotlyjsPackage
        pipeline_Version = opts.pipelineVersion
        rpi_resolution = opts.rpi_resolution
        sn = opts.sn
        species = opts.species
        tissue = opts.tissue
        reference = opts.reference

        if opts.logo != 'N':
            if os.path.exists(opts.logo):
                logo = opts.logo
            else:
                print_err(os.path.abspath(opts.logo),"SAW-A90002")
        else:
            logo = os.path.join(root_path,"logo.png")

        if opts.cellBinGef != 'N':
            if os.path.exists(opts.cellBinGef):
                cellBinGef = opts.cellBinGef
                plot.cgef_stat(cellBinGef, outfile_path)
                if opts.research == "research_version":
                    cgef_stat_addition(cellBinGef, outfile_path)
            else:
                cellBinGef = 'N'
                if opts.iprFile != 'N' and not os.path.exists(opts.iprFile):
                    print_err(os.path.abspath(opts.iprFile),"SAW-A90002")
        else:
            cellBinGef = 'N'

        #generate SN.statistics.json file
        Statistic = statistic(barcodeMapStat, alignmentLog, alignmentStat, tissueCutLog, outfile_path, cellBinGef, sn)
        Statistic.run()
        bin_list = Statistic.bin_list

        if(opts.h5File == None):
            print_err("-n or --h5File","SAW-A90001")
        elif not os.path.exists(opts.h5File):
            print_err(os.path.abspath(opts.h5File),"SAW-A90002")
        elif (opts.h5adFile == None):
            print_err("-d or --h5adFile","SAW-A90001")
        elif not os.path.exists(opts.h5adFile):
            print_err(os.path.abspath(opts.h5adFile),"SAW-A90002")
        # elif (opts.bin200Saturation == None):
        #     print_err("--bin200Saturation","SAW-A90001")
        # elif not os.path.exists(opts.bin200Saturation):
        #     print_err(os.path.abspath(opts.bin200Saturation),"SAW-A90002")
        # elif (opts.bin200violin == None):
        #     print_err("--bin200violin","SAW-A90001")
        # elif not os.path.exists(opts.bin200violin):
        #     print_err(os.path.abspath(opts.bin200violin),"SAW-A90002")
        elif (opts.saturation == None):
            print_err("-t or --saturation","SAW-A90001")
        elif not os.path.exists(opts.saturation):
            print_err(os.path.abspath(opts.saturation),"SAW-A90002")
        # elif (opts.sn == None):
        #     print_err("-s or --sn","SAW-A90001")
        else:
            h5_file = opts.h5File
            h5ad_file = opts.h5adFile
            json_file_name = sn + '.statistics.json'
            json_file = os.path.join(outfile_path, json_file_name)
            bin200Saturation = opts.bin200Saturation
            bin200violin = opts.bin200violin
            saturation = opts.saturation

            binCellSaturation = 'N'
            binCellviolin = 'N'
            binCellMIDGeneDNB = 'N'
            cellCluster = 'N'
            midCellSaturation = 'N'
            areaCellSaturation = 'N'

            if opts.cellBinGef != 'N':
                binCellSaturation_pic = os.path.join(outfile_path, 'scatter_1x1_MID_gene_counts.png')
                if os.path.exists(binCellSaturation_pic):
                    binCellSaturation = binCellSaturation_pic
                else:
                    print_err(os.path.abspath(binCellSaturation_pic),"SAW-A90002")
            
                binCellviolin_pic = os.path.join(outfile_path, 'violin_1x1_MID_gene.png')
                if os.path.exists(binCellviolin_pic):
                    binCellviolin = binCellviolin_pic
                else:
                    print_err(os.path.abspath(binCellviolin_pic),"SAW-A90002")
            
                binCellMIDGeneDNB_pic = os.path.join(outfile_path, 'statistic_1x1_MID_gene_DNB.png')
                if os.path.exists(binCellMIDGeneDNB_pic):
                    binCellMIDGeneDNB = binCellMIDGeneDNB_pic
                else:
                    print_err(os.path.abspath(binCellMIDGeneDNB_pic),"SAW-A90002")
                if opts.research == "research_version":
                    midCellSaturation_pc=os.path.join(outfile_path, 'scatter_1x1_midcount_dnbs.png')
                    if os.path.exists(midCellSaturation_pc):
                        midCellSaturation = midCellSaturation_pc
                    else:
                        print_err(os.path.abspath(midCellSaturation_pc),"SAW-A90002")
                    areaCellSaturation_pc=os.path.join(outfile_path, 'scatter_1x1_cellarea_dnbs.png')
                    if os.path.exists(areaCellSaturation_pc):
                        areaCellSaturation = areaCellSaturation_pc
                    else:
                        print_err(os.path.abspath(areaCellSaturation_pc),"SAW-A90002")

            if opts.cellCluster != 'N':
                if os.path.exists(opts.cellCluster):
                    cellCluster = opts.cellCluster
                else:
                    print_err(os.path.abspath(opts.cellCluster),"SAW-A90002")

            if opts.rpi != None:
                rpi_file = opts.rpi
            else:
                rpi_file = 'N'

            if opts.iprFile == 'N':
                iprFile = 'N'
            elif opts.iprFile == None :
                iprFile = 'N'
            elif opts.iprFile != 'N' and opts.iprFile != None and (not os.path.exists(opts.iprFile)):
                print_err(os.path.abspath(opts.iprFile),"SAW-A90002")
                iprFile = 'N'
            else:
                iprFile = opts.iprFile

            if opts.research == "research_version":
                research_version = 'Y'
                if opts.bin1Saturation == 'N':
                    print_err("--bin1Saturation","SAW-A90001")
                elif not os.path.exists(opts.bin1Saturation):
                    print_err(os.path.abspath(opts.bin1Saturation),"SAW-A90002")
                else:
                    bin1Saturation = opts.bin1Saturation
            else:
                research_version = 'N'
                bin1Saturation = 'N'
            
            # if opts.bin50Saturation != 'N'and not os.path.exists(opts.bin50Saturation):
            #     print_err(os.path.abspath(opts.bin50Saturation),"SAW-A90002")
            # else:
            #     bin50Saturation = opts.bin50Saturation
            
            # if opts.bin50violin != 'N' and not os.path.exists(opts.bin50violin):
            #     print_err(os.path.abspath(opts.bin50violin),"SAW-A90002")
            # else:
            #     bin50violin = opts.bin50violin

            # if opts.bin50MIDGeneDNB != 'N' and not os.path.exists(opts.bin50MIDGeneDNB):
            #     print_err(os.path.abspath(opts.bin50MIDGeneDNB),"SAW-A90002")
            # else:
            #     bin50MIDGeneDNB = opts.bin50MIDGeneDNB

            # if opts.bin100Saturation == 'N' and not os.path.exists(opts.bin100Saturation):
            #     print_err(os.path.abspath(opts.bin100Saturation),"SAW-A90002")
            # else:
            #     bin100Saturation = opts.bin100Saturation

            # if opts.bin100violin != 'N' and not os.path.exists(opts.bin100violin):
            #     print_err(os.path.abspath(opts.bin100violin),"SAW-A90002")
            # else:
            #     bin100violin = opts.bin100violin

            # if opts.bin100MIDGeneDNB != 'N' and not os.path.exists(opts.bin100MIDGeneDNB):
            #     print_err(os.path.abspath(opts.bin100MIDGeneDNB),"SAW-A90002")
            # else:
            #     bin100MIDGeneDNB = opts.bin100MIDGeneDNB

            # if opts.bin200MIDGeneDNB != 'N' and not os.path.exists(opts.bin200MIDGeneDNB):
            #     print_err(os.path.abspath(opts.bin200MIDGeneDNB),"SAW-A90002")
            # else:
            #     bin200MIDGeneDNB = opts.bin200MIDGeneDNB

            # if opts.bin150Saturation != 'N' and not os.path.exists(opts.bin150Saturation):
            #     print_err(os.path.abspath(opts.bin150Saturation),"SAW-A90002")
            # else:
            #     bin150Saturation = opts.bin150Saturation

            # if opts.bin150violin != 'N' and not os.path.exists(opts.bin150violin):
            #     print_err(os.path.abspath(opts.bin150violin),"SAW-A90002")
            # else:
            #     bin150violin = opts.bin150violin

            # if opts.bin150MIDGeneDNB != 'N' and not os.path.exists(opts.bin150MIDGeneDNB):
            #     print_err(os.path.abspath(opts.bin150MIDGeneDNB),"SAW-A90002")
            # else:
            #     bin150MIDGeneDNB = opts.bin150MIDGeneDNB

            if opts.tissue_fig != 'N' and not os.path.exists(opts.tissue_fig):
                print_err(os.path.abspath(opts.tissue_fig),"SAW-A90002")
            else:
                tissue_fig = opts.tissue_fig

            # if opts.bin200Saturation != 'N' and not os.path.exists(opts.bin200Saturation):
            #     print_err(os.path.abspath(opts.bin200Saturation),"SAW-A90002")
            # else:
            #     bin200Saturation = opts.bin200Saturation

            # if opts.bin200violin != 'N' and not os.path.exists(opts.bin200violin):
            #     print_err(os.path.abspath(opts.bin200violin),"SAW-A90002")
            # else:
            #     bin200violin = opts.bin200violin

            bin_fig = {}
                
            for i in bin_list:
                if i not in ["1",'20','50','100', '150', '200']:
                    print_err("tissueCut.stat binsize name error","SAW-A90003")
                if i == '1':
                    continue
                binsaturation=""
                binviolin=""
                binMIDGeneDNB=""
                binsaturation = eval(f"opts.bin{i}Saturation")
                binviolin = eval(f"opts.bin{i}violin")
                binMIDGeneDNB = eval(f"opts.bin{i}MIDGeneDNB")
                if binsaturation != "N" and not os.path.exists(binsaturation):
                    print_err(os.path.abspath(binsaturation),"SAW-A90002")
                elif binsaturation == "N":
                    if tissue_fig == "N" and binsaturation == "N":
                        print_err(f"--tissue_fig and --bin{i}Saturation","SAW-A90001")
                    binsaturation = os.path.join(tissue_fig,f"scatter_{i}x{i}_MID_gene_counts.png")
                    if not os.path.exists(binsaturation):
                        print_err(({} in {}).format(binsaturation, tissue_fig),"SAW-A90002")
                
                if binviolin != "N" and not os.path.exists(binviolin):
                    print_err(os.path.abspath(binviolin),"SAW-A90002")
                elif  binviolin == "N":
                    if tissue_fig == "N":
                        print_err(f"--tissue_fig and --bin{i}violin","SAW-A90001")
                    binviolin = os.path.join(tissue_fig,f"violin_{i}x{i}_MID_gene.png")
                    if not os.path.exists(binviolin):
                        print_err(({} in {}).format(binviolin, tissue_fig),"SAW-A90002")
                
                if binMIDGeneDNB != "N" and not os.path.exists(binMIDGeneDNB):
                    print_err(os.path.abspath(binMIDGeneDNB),"SAW-A90002")
                elif binMIDGeneDNB == "N":
                    if tissue_fig == "N":
                        print_err(f"--tissue_fig and --bin{i}MIDGeneDNB","SAW-A90001")
                    binMIDGeneDNB = os.path.join(tissue_fig,f"statistic_{i}x{i}_MID_gene_DNB.png")
                    if not os.path.exists(binMIDGeneDNB):
                        print_err(({} in {}).format(binMIDGeneDNB, tissue_fig),"SAW-A90002")
                
                bin_fig[f"bin{i}Saturation"] = binsaturation
                bin_fig[f"bin{i}violin"] = binviolin
                bin_fig[f"bin{i}MIDGeneDNB"] = binMIDGeneDNB
                


            #generate html report file
            # generate_html_function(sn, outfile_path, h5_file, h5ad_file, json_file, bin200Saturation, bin200violin, saturation, research_version, pipeline_Version, rpi_file, rpi_resolution, bin200MIDGeneDNB, bin1Saturation, bin50Saturation, bin50violin, bin50MIDGeneDNB, bin100Saturation, bin100violin, bin100MIDGeneDNB, binCellSaturation, binCellviolin, binCellMIDGeneDNB,midCellSaturation,areaCellSaturation,bin150Saturation, bin150violin, bin150MIDGeneDNB, cellCluster, iprFile, species, tissue, reference, logo, tissue_fig, bin_list)
            generate_html_function(sn, outfile_path, h5_file, h5ad_file, json_file, saturation, research_version, pipeline_Version, rpi_file, rpi_resolution, bin1Saturation,binCellSaturation, binCellviolin, binCellMIDGeneDNB,midCellSaturation,areaCellSaturation, cellCluster, iprFile, species, tissue, reference, logo, bin_fig, bin_list)
            finalHtmlFileName = sn + '.report.html'
            finalHtmlFile = os.path.join(outfile_path, finalHtmlFileName)
            rawHtmlFileName = sn + '.report.tmp.html'
            rawHtmlFile = os.path.join(outfile_path, rawHtmlFileName)
            combine(rawHtmlFile, plotlyJsFile, finalHtmlFile)

def combine(rawHtmlFile, plotlyJsFile, finalHtmlFile):
    """
    combine plotly.js package into html report file for offline view

    :param rawHtmlFile: Html report file without plotly.js package
    :param plotlyJsFile: Plotly.js package
    :param finalHtmlFile: Final output html report file

    """
    
    finalHtmlFile_writer = open(finalHtmlFile, 'w', encoding='utf-8')
    with open(rawHtmlFile, 'r', encoding='utf-8') as fr:
        line_fr = 0
        for line in fr:
            if line_fr == 2:
                with open(plotlyJsFile, 'r', encoding='utf-8') as fp:
                    for linefp in fp:
                        finalHtmlFile_writer.write(linefp)
            finalHtmlFile_writer.write(line)
            line_fr += 1
    finalHtmlFile_writer.close()

    cmd = 'rm ' + rawHtmlFile

    os.system(cmd)


# 
def print_err(case ,code):
    """
    print error code
    """
    err_code={
        "SAW-A90001":"{} is missing.",
        "SAW-A90002":"cannot access {}: No such file or directory.",
        "SAW-A90003":"{} file format error.",
        "SAW-A90004":"infomation loss:{}.",
    }
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("errcode.log","a") as err_info:
        err_info.write("[{}] {}: {}\n".format(nowtime,  code,err_code[code].format(case) ))
    # sys.stderr.write(' '.join(map(str,args)) + '\n')
    sys.stderr.write("[{}] {}: {}\n".format(nowtime,  code,err_code[code].format(case) ))
    sys.exit(1)

if __name__=="__main__":
    main()
