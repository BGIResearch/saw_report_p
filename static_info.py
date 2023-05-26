SPOT_SUMMARY_COLLAPSE_DEV=[
    {'title':"DNB Under Tissue", 'content':"Number of DNBs under tissue coverage region"},
    {'title':"mRNA-Captured DNBs Under Tissue", 'content':"Number of DNBs under tissue that have captured mRNA"},
    {'title':"Fraction mRNA-Captured DNBs Under Tissue", 'content':"Fraction mRNA-captured DNBs under tissue over DNB under tissue coverage region (mRNA-Captured DNBs Under Tissue / DNB Under Tissue)"},
    {'title':"Genes Under Tissue", 'content':"Number of detected gene under tissue coverage"},
    {'title':"Number of MID Under Tissue Coverage", 'content': 'Number of MID under tissue coverage'},
    {'title':"Fraction MID in Spots Under Tissue", 'content':"Fraction of MID under tissue over total unique reads (MID Under Tissue / Unique Reads)"},
    {'title':"Reads Under Tissue", 'content': "Number of reads with position prior to filtration under tissue coverage"},
    {'title':"Fraction Reads in Spots Under Tissue", 'content':"Fraction of mapped reads under tissue over total mapped reads (Mapped Reads in Spots Under Tissue / (Valid CID Reads + Discarded MID Reads))"},
]

SPOT_SUMMARY_COLLAPSE=[
    {'title':"DNB Under Tissue", 'content':"Number of DNBs under tissue coverage region"},
    {'title':"mRNA-Captured DNBs Under Tissue", 'content':"Number of DNBs under tissue that have captured mRNA"},
    # {'title':"Fraction mRNA-Captured DNBs Under Tissue", 'content':"Fraction mRNA-captured DNBs under tissue over DNB under tissue coverage region (mRNA-Captured DNBs Under Tissue / DNB Under Tissue)"},
    {'title':"Genes Under Tissue", 'content':"Number of detected gene under tissue coverage"},
    {'title':"Number of MID Under Tissue Coverage", 'content': 'Number of MID under tissue coverage'},
    {'title':"Fraction MID in Spots Under Tissue", 'content':"Fraction of MID under tissue over total unique reads (MID Under Tissue / Unique Reads)"},
    {'title':"Reads Under Tissue", 'content': "Number of reads with position prior to filtration under tissue coverage"},
    {'title':"Fraction Reads in Spots Under Tissue", 'content':"Fraction of mapped reads under tissue over total mapped reads (Mapped Reads in Spots Under Tissue / (Valid CID Reads + Discarded MID Reads))"},
]

SPOT_SUMMARY_FIELD = [
    {'label': "Contour area", 'id':'Contour_area'},
    {'label': "Number of DNB under tissue", 'id':'Number_of_DNB_under_tissue'},
    {'label': "Ratio", 'id':'Ratio'},
    {'label': "Total Gene type", 'id': 'Total_Gene_type'},
    {'label': "MID under tissue", 'id':'MID_counts'},
    {'label': "Reads under tissue", 'id':'Reads_under_tissue'},
    {'label': "Fraction Reads in Spots Under Tissue", 'id':'Fraction_Reads_in_Spots_Under_Tissue'},
]

BIN_SUMMARY_COLLAPSE=[
    {'title': "Total MID Mapping To Gene And slide", 'content': "Total number of MIDs mapped to gene region"},
    {'title': "Gene Number", 'content': "Number of types of genes that captured"},
    {'title': "Number Of DNB With Reads", 'content': "Number of DNB that captured mRNA"},
    {'title': "Slide Area", 'content': "Area of debris"},
    {'title': "Density Of DNB", 'content': "Ratio of mRNA and DNB that are captured(Number_Of_DNB_With_Reads/Slide_Area*100)"},
]

BIN_SUMMARY_FIELD = [
    {'label': "Total MID Mapping To Gene And slide", 'id': 'Total_MID_Mapping_To_Gene_And_slide'},
    {'label': "Gene Number", 'id': 'Gene_Number'},
    {'label': "Number Of DNB With Reads", 'id': 'Number_Of_DNB_With_Reads'},
    {'label': "Slide Area", 'id': 'Slide_Area'},
    {'label': "Density Of DNB", 'id': 'Density_Of_DNB'}
]

TissueCut_Bin_SUMMARY_COLLAPSE = [
    {'title':"Bin Size", 'content': "The size of Bin which is the unit of aggregated DNBs in a squared region (i.e. Bin 50 = 50 * 50 DNBs)"},
    {'title':"Mean Reads (per bin)", 'content': "Mean number of sequenced reads divided by the number of bins under tissue coverage"},
    {'title':"Median Reads (per bin)", 'content': "Median number of sequenced reads divided by the number of bins under tissue coverage (pick the middle value after sorting)"},
    {'title':"Mean Gene Type (per bin)", 'content': 'Mean number of unique gene types divided by the number of bins under tissue coverage'},
    {'title':"Median Gene Type (per bin)", 'content': "Median number of unique gene types divided by the number of bins under tissue coverage"},
    {'title':"Mean MID (per bin)", 'content': "Mean number of MIDs divided by the number of bins under tissue coverage"},
    {'title':"Median MID (per bin)", 'content': "Median number of MIDs divided by the number of bins under tissue coverage"},
]

CELLCUT_TOTAL_STAT_COLLAPSE =[
    {'content': "Size of the area closed by tissue outline", 'title':'Total Contour Area'},
    {'content': "Number of DNBs that have captured mRNA and under the cell covered region", 'title':'Number of DNB Under Cell'},
    {'content': "Number of DNB under cell/Contour area, fraction of DNBs under the cell covered region that have captured mRNA", 'title':'Ratio'},
    {'content': "Total types of the gene that have been captured by probes under cell covered region", 'title':'Total Gene type'},
    {'content': "Number of unique mRNA molecular that have been captured by the probes under cell covered region", 'title':'Total MID Under Cell'},
    {'content': "Fraction of raw reads with position under cell covered region", 'title':'Reads Under Cell'},
    {'content': "Reads under cell/total raw reads, fraction of raw reads with position under cell covered region", 'title':'Fraction Reads in Spots Under Tissue'}
]

CELLCUT_TOTAL_STAT_FIELD =[
    {'label': "Total Contour Area", 'id':'Total_contour_area'},
    {'label': "Number of DNB Under Cell", 'id':'Number_of_DNB_under_cell'},
    {'label': "Ratio", 'id':'Ratio'},
    {'label': "Total Gene type", 'id':'Total_Gene_type'},
    {'label': "Total MID Under Cell", 'id':'Total_MID_under_cell'},
    {'label': "Reads Under Cell", 'id':'Reads_under_cell'},
    {'label': "Fraction Reads in Spots Under Tissue", 'id':'Fraction_Reads_in_Spots_Under_cell'}
]

CELLCUT_BIN_STAT_COLLAPSE =[
    {'content': "Number of all detected cells", 'title':'Total Cell Count'},
    {'content': "Average number of reads per cell", 'title':'Mean Reads'},
    {'content': "Median of reads count per cell", 'title':'Median Reads'},
    {'content': "Average number of gene type per cell", 'title':'Mean Gene Type Per Cell'},
    {'content': "Median of gene type per cell", 'title':'Median Gene Type Per Cell'},
    {'content': "Average number of unique mRNA molecular per cell", 'title':'Mean MID Per Cell'},
    {'content': "Median of unique mRNA molecular per cell", 'title':'Median MID Per Cell'},
    {'content': "The average area of all the detected cells", 'title':'Mean Cell Area'},
    {'content': "Average number of DNB that have captured mRNA and under the tissue covered region per cell", 'title':'Mean DNB Per Cell'},
    {'content': "Median of DNB that have captured mRNA and under the tissue covered region per cell", 'title':'Median DNB Per Cell'}
]

CELLCUT_BIN_STAT_FIELD =[
    {'label': "Total Cell Count", 'id':'Total_cell_count'},
    {'label': "Mean Reads", 'id':'Mean_reads'},
    {'label': "Median Reads", 'id':'Median_reads'},
    {'label': "Mean Gene Type Per Cell", 'id':'Mean_Gene_type_per_cell'},
    {'label': "Median Gene Type Per Cell", 'id':'Median_Gene_type_per_cell'},
    {'label': "Mean MID Per Cell", 'id':'Mean_MID_per_cell'},
    {'label': "Median MID Per Cell", 'id':'Median_MID_per_cell'},
    {'label': "Mean Cell Area", 'id':'Mean_cell_area'},
    {'label': "Mean DNB Per Cell", 'id':'Mean_DNB_per_cell'},
    {'label': "Median DNB Per Cell", 'id':'Median_DNB_per_cell'}
]

QUALITY_COLLAPSE = [
    {'title':"Total Reads",  'content': "Total number of sequenced reads"},
    {'title':"Total Q30",  'content': "Ratio of bases with quality value exceeded 30 in the sequenced reads"},
    {'title':"CID Q30",  'content': "Ratio of CID (Coordinate ID) bases with quality value exceeded 30"},
    {'title':"MID Q30",  'content': "Ratio of MID (Molecule ID) bases with quality value exceeded 30"},
]
QUALITY_FIELD = [
    {'label': "Total Reads", 'id':'Total_Reads'},
    {'label': "CID Q30", 'id':'Q30_Barcode_Rate'},
    {'label': "MID Q30", 'id':'Q30_MID_Rate'},
    {'label': "Total Q30", 'id':'Q30_seq_Rate'},
]

FILTER_COLLAPSE = [
    {'title':"Valid CID Reads",  'content': "Number of reads with CIDs matching the mask file and with MIDs passing QC"},
    {'title':"Clean Reads",  'content': "Number of Valid CID Reads that have passed QC"},
    {'title':"Non-Relevent Short Reads",  'content': "Number of non-relevant short reads"},
    {'title':"Reads With Adapter", 'content':'Number of reads contains adapter sequence'},
    {'title':"Reads With DNB", 'content':'Number of reads contains DNB sequence'},
]

FILTER_FIELD = [
    {'label': 'Valid CID Reads', 'id': 'Raw_Reads'},
    {'label': 'Q30 Base Before Filtering', 'id':'Q30_Before_Filtering'},
    {'label': 'Clean Reads', 'id':'Clean_Reads'},
    {'label': 'Q30 Base After Filtering', 'id':'Q30_After_Filtering'},
    {'label': "Low Quality Reads", 'id':'Low_Quality_Reads'},
    {'label': "Too Many N Reads", 'id':'Too_Many_N_Reads'},
    {'label': "Too Short Reads", 'id':'Too_Short_Reads'},
    {'label':"Reads With Adapter", 'id':'Reads_With_Adapter'},
    {'label':"Reads With DNB", 'id':'Reads_With_DNB'},
]
IMPORTANT_FIELD = [
    {'id' : 'raw_reads', 'label' : "Total Reads"},
    {'id' : 'mapped_reads', 'label' : "Valid CID Reads"},
    {'id' : 'clean_reads', 'label' : "Clean Reads"},
    {'id' : 'reference_mapping_reads', 'label' :"Reads Mapped to Genome"},
    {'id' : 'uniquely_reads', 'label' :"Unique Reads"},
]
RNA_MAPPING_FIELD = [
    {'id' : 'Input_read', 'label' : "Clean Reads"},
    {'id' : 'Uniquely_Mapped_Read', 'label' : "Uniquely Mapped Reads"},
    {'id' : 'Multi_Mapping_Read', 'label' : "Multiple Mapping Reads"},
    {'id' : 'RNA_Unmapping_Read', 'label' :"RNA Unmapping Reads"},
]
RNA_MAPPING_COLLAPSE = [
    {'content' : 'Number of Valid CID Reads that have passed QC', 'title' : "Clean Reads"},
    {'content' : 'Number of reads that mapped uniquely to the reference genome', 'title' : "Uniquely Mapped Reads"},
    {'content' : 'Number of reads that mapped more than one time on the genome', 'title' : "Multi-Mapped Reads"},
    {'content' : 'Number of reads that cannot be mapped to the reference genome', 'title' :"Unmapped Reads"},
]
ANNOTATION_COLLAPSE = [
    {'content' : 'Number of reads that mapped uniquely to an exonic region and on the same strand of the genome', 'title' : "Exonic"},
    {'content' : 'Number of reads that mapped uniquely to an intronic region and on the same strand of the genome', 'title' : "Intronic"},
    {'content' : 'Number of reads that mapped uniquely to an intergenic region and on the same strand of the genome', 'title' : "Intergenic"},
    {'content' : 'Number of reads that mapped to a unique gene in the transcriptome. These reads are considered for MID counting. (Transcriptome = Exonic + Intronic)', 'title' :"Transcriptome"},
    {'content' : 'Number of reads mapped to the transcriptome but on the opposite strand of their annotated gene', 'title' :"Antisense"},
]
ANNOTATION_FIELD = [
    {'id' : 'Exonic', 'label' : "Exonic"},
    {'id' : 'Intronic', 'label' : "Intronic"},
    {'id' : 'Intergenic', 'label' : "Intergenic"},
    {'id' : 'Transcriotome', 'label' :"Transcriptome"},
    {'id' : 'Antisense', 'label' :"Antisense"},
]

labels_color = {'Total_reads':'#F0FFFF','Valid_CID_Reads':'Total_reads','Invalid_CID_Reads':'Total_reads','Removed_Reads':'Valid_CID_Reads',
    'Clean_Reads':'Valid_CID_Reads', 'Discarded_MID_Reads':'Removed_Reads',
    'Too_Short_Reads':'Removed_Reads','Too_Many_N_Reads':'Removed_Reads','Low_Quality_Reads':'Removed_Reads',
    'Reads_Mapped_to_Genome_reads':'Clean_Reads','Unmapped_Reads':'Clean_Reads','Duplicated_Reads':'Reads_Mapped_to_Genome_reads',
    'Fail_Filter':'Reads_Mapped_to_Genome_reads','Unique_Reads':'Reads_Mapped_to_Genome_reads'
}

hovertext_dict = {'Total_reads':' of Total reads<br>Total number of sequenced reads',
    'Valid_CID_Reads':' of Total reads<br>Number of reads with CIDs matching the mask file and with MIDs passing QC',
    'Invalid_CID_Reads':' of Total reads<br>Number of reads with CIDs that cannot be matched with the mask file',
    'Removed_Reads':'<br>Number of filter reads after quality control. <br>(% = Removed Reads / Valid CID Reads)',
    'Clean_Reads':' of Valid CID Reads<br>Number of Valid CID Reads that have passed QC', 
    'Discarded_MID_Reads':' of <br>Number of reads with MID that have been discarded <br>since MID sequence quality does not satisfy with further analysis',
    'Too_Short_Reads':'Valid CID Reads of <br>Number of non-relevant short reads',
    'Reads_With_Adapter':'<br>Number of reads with adapter.<br>(% = Reads_With_Adapter / Removed Reads)',
    'Reads_With_DNB':'<br>Number of reads with DNB.<br>(% = Reads_With_DNB / Removed Reads)',
    'Too_Many_N_Reads':'Valid CID Reads of <br>Number of reads filtered that contain too many N.<br>(% = Too Many N Reads / Removed Reads)',
    'Low_Quality_Reads':'Valid CID Reads of <br>Number of reads filtered due to low quality.<br>(% = Low Quality Reads / Removed Reads)',
    'Uniquely_Mapped_Reads':' of Clean Reads<br>Number of reads that mapped uniquely to the reference genome',
    'Multiple_Mapping_Reads':' of Clean Reads<br>Number of reads that mapped more than one time on the genome',
    'Unmapped_Reads':' of Clean Reads<br>Number of reads that cannot be mapped to the reference genome',
    'Duplicated_Reads':' of Annotated Reads<br>Number of annotated reads that have been corrected by MAPQ with duplicated MID',
    'Unique_Reads':' of Annotated Reads<br>Number of annotated reads that have been corrected by MAPQ and deduplicated',
    'Annotated_Reads':' of Uniquely Mapped Reads<br>Number of reads that are aligned to transcripts of at least one gene',
    'Unannotated_Reads':' of Uniquely Mapped Reads<br>Number of reads that cannot be aligned to transcript of one gene'
}

parents_dict = {'Total_reads':'','Valid_CID_Reads':'Total_reads','Invalid_CID_Reads':'Total_reads',
    'Discarded_MID_Reads':'Total_reads','Clean_Reads':'Valid_CID_Reads', 
    'Too_Short_Reads':'Valid_CID_Reads','Too_Many_N_Reads':'Valid_CID_Reads',
    'Low_Quality_Reads':'Valid_CID_Reads','Uniquely_Mapped_Reads':'Clean_Reads',
    'Multiple_Mapping_Reads':'Clean_Reads','Unmapped_Reads':'Clean_Reads', 
    'Annotated_Reads':'Uniquely_Mapped_Reads', 'Unannotated_Reads':'Uniquely_Mapped_Reads',
    'Duplicated_Reads':'Annotated_Reads','Unique_Reads':'Annotated_Reads'
}

parents_dict_sort = {'Total_reads':'','Valid_CID_Reads':'Total_reads','Invalid_CID_Reads':'Total_reads',
    'Discarded_MID_Reads':'Total_reads','Clean_Reads':'Valid_CID_Reads', 
    'Too_Short_Reads':'Valid_CID_Reads','Too_Many_N_Reads':'Valid_CID_Reads',
    'Low_Quality_Reads':'Valid_CID_Reads','Uniquely_Mapped_Reads':'Clean_Reads',
    'Multiple_Mapping_Reads':'Clean_Reads','Unmapped_Reads':'Clean_Reads'
}

SUNBURST_COLLAPSE = [
    {'title':"Total Reads",  'content': "Total number of sequenced reads"},
    {'title':"Valid CID Reads",  'content': "Number of reads with CIDs matching the mask file and with MIDs passing QC"},
    {'title':"Clean Reads",  'content': "Number of Valid CID Reads that have passed QC"},
    {'title':"Reads Mapped to Genome", 'content' :"Number of reads that mapped to the reference genome (Uniquely Mapped Reads + Multi-mapped Reads)"},
]

SUNBURST_DEV_COLLAPSE = [
    {'title':"Total Reads",  'content': "Total number of sequenced reads"},
    {'title':"Valid CID Reads",  'content': "Number of reads with CIDs matching the mask file and with MIDs passing QC"},
    {'title':"Invalid CID Reads",  'content': "Number of reads with CIDs that cannot be matched with the mask file"},
    {'title':"Discarded MID Reads",  'content': "Number of reads with MID that have been discarded since MID sequence quality does not satisfy with further analysis"},
    {'title':"Clean Reads",  'content': "Number of Valid CID Reads that have passed QC"},
    {'title':"Non-Relevant Short Reads",  'content': "Number of non-relevant short reads"},
    {'title':"Uniquely Mapped Reads",  'content': "Number of reads that mapped uniquely to the reference genome"},
    {'title':"Multi-Mapped Reads",  'content': "Number of reads that mapped more than one time on the genome"},
    {'title':"Unmapped Reads",  'content': "Number of reads that cannot be mapped to the reference genome"},
    {'title':"Annotated Reads",  'content': "Number of reads that are aligned to transcripts of at least one gene"},
    {'title':"Unannotated Reads",  'content': "Number of reads that cannot be aligned to transcript of one gene"},
    {'title':"Unique Reads",  'content': "Number of annotated reads that have been corrected by MAPQ and deduplicated"},
    {'title':"Duplicated Reads",  'content': "Number of annotated reads that have been corrected by MAPQ with duplicated MID"},
]

SUNBURST_COLLAPSE_TOB = [
    {'title':"Total Reads",  'content': "Total number of sequenced reads"},
    {'title':"Valid CID Reads",  'content': "Number of reads with CIDs matching the mask file and with MIDs passing QC"},
    {'title':"Invalid CID Reads",  'content': "Number of reads with CIDs that cannot be matched with the mask file"},
    {'title':"Discarded MID Reads",  'content': "Number of reads with MID that have been discarded since MID sequence quality does not satisfy with further analysis"},
    {'title':"Clean Reads",  'content': "Number of Valid CID Reads that have passed QC"},
    {'title':"Non-Relevant Short Reads",  'content': "Number of non-relevant short reads"},
    {'title':"Uniquely Mapped Reads",  'content': "Number of reads that mapped uniquely to the reference genome"},
    {'title':"Multi-Mapped Reads",  'content': "Number of reads that mapped more than one time on the genome"},
    {'title':"Unmapped Reads",  'content': "Number of reads that cannot be mapped to the reference genome"},
    {'title':"Annotated Reads",  'content': "Number of reads that are aligned to transcripts of at least one gene"},
    {'title':"Unannotated Reads",  'content': "Number of reads that cannot be aligned to transcript of one gene"},
]

SUNBURST_FIELD = [
    {'label': "Total Reads", 'id':'Total_Reads_sun'},
    {'label': "Valid CID Reads", 'id':'Valid_CID_Reads_sun'},
    {'label': "Clean Reads", 'id':'Clean_Reads_sun'},
    {'label': "Reads Mapped to Genome", 'id':'Mapped_Reads_sun'},
    {'label': "Unique Reads", 'id':'Unique_Reads_sun'},
    {'label': "Duplicated Reads", 'id':'Duplicated_Reads_sun'},
]

Cell_Bin_SUMMARY_COLLAPSE = [
    {'title':"Cell Count", 'content':"Number of cells"},
    {'title':"Mean/Median Cell Area", 'content':"Mean/Median cell area (pixel)"},
    {'title':"Mean/Median DNB Count", 'content':"Mean/Median number of DNBs that have captured-mRNAs per cell"},
    {'title':"Mean/Median Gene Type", 'content': "Mean/Median genes per cell"},
    {'title':"Mean/Median MID", 'content':"Mean/Median MID count per cell"},
]

IMAGE_QC_COLLAPSE = [
    {'title':"ImageQC version", 'content':"ImageQC version"},
    {'title':"QC Pass", 'content':"Whether the image(s) passed imageQC quality check"},
    {'title':"Track Line Score", 'content':"Reference score for track line detection"},
    {'title':"Clarity Score", 'content':"Reference score for image clarity"},
    {'title':"Good FOV Count", 'content':"Number of FOVs that have at least one track dot detected"},
    {'title':"Total FOV Count", 'content':"Total number of FOVs"},
    {'title':"Stitching Score", 'content':"Reference score for stitching"},
    {'title':"Tissue Segmentation Score", 'content':"Reference score for tissue segmentation"},
    {'title':"Registration Score", 'content':"Reference score for aligning image with gene expression matrix"}
]

IMAGE_STITCH_COLLAPSE = [
    {'title':"Template Source Row No.", 'content':"The row number of the template FOV used for predicting the entire template"},
    {'title':"Template Source Column No.", 'content':"The column number of the template FOV used for predicting the entire template"},
    {'title':"Global Height", 'content':"Height of the stitched image"},
    {'title':"Global Width", 'content':"Width of the stitched image"}
]

IMAGE_REGISTRATION_COLLAPSE = [
    {'title':"ScaleX", 'content':"The lateral scaling between image and template"},
    {'title':"ScaleY", 'content':"The longitudinal scaling between image and template"},
    {'title':"Rotation", 'content':"The rotation angle of the image relative to the template"},
    {'title':"Flip", 'content':"Whether the image is flipped horizontally"},
    {'title':"Image X Offset", 'content':"Offset between image and matrix in x direction"},
    {'title':"Image Y Offset", 'content':"Offset between image and matrix in y direction"},
    {'title':"Counter Clockwise Rotation", 'content':"Counter clockwise rotation angle"},
    {'title':"Manual ScaleX", 'content':"The lateral scaling based on image center (manual-registration)"},
    {'title':"Manual ScaleY", 'content':"The longitudinal scaling based on image center (manual-registration)"},
    {'title':"Manual Rotation", 'content':"The rotation angle based on image center (manual-registration)"},
    {'title':"Matrix X Start", 'content':"Gene expression matrix offset in x direction by DNB numbers "},
    {'title':"Matrix Y Start", 'content':"Gene expression matrix offset in y direction by DNB numbers"},
    {'title':"Matrix Height", 'content':"Gene expression matrix height"},
    {'title':"Matrix Width", 'content':"Gene expression matrix width"}
]