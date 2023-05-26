# Copyright (C) BGI-Reasearch - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by STOmics development team P_stomics_dev@genomics.cn, May 2017

html_research_template = """
<html>
    <head>
        <style>
           :root {{
                font-family: system-ui, -apple-system, BlinkMacSystemFont, 
                segoe ui, Roboto, Helvetica, Arial, sans-serif;
            }}

            *,
            ::after,
            ::before {{
                font-family: inherit;
            }}

            .tab_content_all{{
                width: 1920px;
            }}

            .body_style{{
                background-color:#F0F2F5;
                margin-left: auto;
                margin-right: auto;
                min-width: 1200px;
                overflow: auto;
            }}

            .header{{
                height: 150px;
                background: #5F0185;
            }}

            .analyticalTitle{{
                width: 600px;
                height: 56px;
                font-size: 40px;
                font-weight: 500;
                color: #FFFFFF;
                line-height: 56px;
                padding-top: 43px;
            }}

            .header_logo{{
                float: left;
            }}
            
            .header_title{{
                margin-left: 50px;
            }}

            .fastq_div{{
                height: 110px;
                background: #FFFFFF;
            }}

            .fastq_title{{
                width: 299px;
                height: 46px;
                font-size: 32px;
                font-weight: 500;
                color: #333333;
                line-height: 45px;
                padding-top: 32px;
            }}

            .footer_div{{
                height: 100px;
                background: #FFFFFF;
            }}

            .footer{{
                width: 400px;
                height: 52px;
                font-size: 12px;
                font-weight: 400;
                color: #666666;
                line-height: 17px;
                text-align: center;
                padding-top: 24px;
                margin-left: auto;
                margin-right: auto;
            }}

            .div_tab{{
                background: #F9FBFC;
            }}

            #tab{{
                margin-top: -16px;
                margin-left: -35px;
            }}

            #tab li{{
                float: left;
                height: 28px;
                font-size: 20px;
                font-weight: 400;
                color: #999999;
                line-height: 28px;
                list-style: none;
                margin-top: 25px;
            }}

            #tab li.tabin {{
                float: left;
                height: 28px;
                font-size: 20px;
                font-weight: 500;
                color: #5F0185;
                line-height: 28px;
            }}

            .tab_content {{
                width: 1200px;
                position: relative;
                margin-left: auto;
                margin-right: auto;
                padding-left: 10px;
            }}

            .tab_margin{{
                margin-left: 56px;
            }}

            .tab_content .show{{
                display: block;
            }}

            .tab_content .unshow{{
                display: none;
            }}

            .canvas{{
                width: 1200px;
                margin-left: auto;
                margin-right: auto;
            }}

            .tab_height{{
                height: 78px;
            }}

            #scatter_canvas{{
                width: 780px;
                background: #FFFFFF;
                box-shadow: 0px 0px 4px 0px rgba(95,1,133,0.0500);
                border-radius: 8px;
                float: left;
            }}

            #clustering_square_bin_canvas, #cellBin_cluster_canvas{{
                background: #FFFFFF;
                box-shadow: 0px 0px 4px 0px rgba(95,1,133,0.0500);
                border-radius: 8px;
                float: left;
            }}

            .title_label{{
                width: 4px;
                height: 20px;
                background: #5F0185;
                float: left;
                margin-top: 34px;
                margin-left: 32px;
            }}

            .span_title{{
                float: left;
                height: 40px;
                font-size: 28px;
                font-weight: 500;
                color: #333333;
                line-height: 40px;
                padding-top: 24px;
                padding-left: 16px;
            }}

            .fa{{
                font-style: normal;
                line-height: 1;
                width: 9px;
                height: 15px;
                color: #CECECE;
            }}

            .button_explain{{
                margin-left: 16px;
                margin-top: 30px;
                border: 1px solid #CECECE;
                border-radius: 20px;
                background: #FFFFFF;
                width: 28px;
                height: 28px;
            }}

            #div_quation{{
                display: none;
                width: 550px;
                height: 20px;
                font-size: 14px;
                font-weight: 500;
                color: #999999;
                line-height: 20px;
                margin-left: 32px;
                margin-top: 16px;
            }}

            .divScatterBackground{{
                width: 716px;
                height: 640px;
                background: #F7F7F7;
                border-radius: 8px;
                margin-left: 32px;
                margin-top: 16px;
            }}

            .scatter_plot_title{{
                height: 28px;
                font-size: 20px;
                font-weight: 500;
                color: #333333;
                line-height: 28px;
                margin-top:20px;
                padding-bottom: 24px;
                text-align:center;
            }}

            .btn-link{{
                width: 128px;
                height: 50px;
                background: #FFFFFF;
                border-radius: 8px;
                border: 1px solid #5F0185;
                font-size: 12px;
                color: #5F0185;
                font-weight: 500;
            }}

            #slider_gene_exp, #slider_square_cluster{{
                text-align: center;
            }}

            #range, #range_cluster, #range_cell_cluster{{
                width:40%;
                height:3px;
                text-align: center;
                /*tira a barra do input range*/
                -webkit-appearance:none;  
                background:#A329D4;
                outline:none;
            }}

            #range::-webkit-slider-thumb{{
                -webkit-appearance:none;
                background:#5F0185;
                width:22px;
                height:22px;
                border-radius:50%;
                cursor:pointer;
            }}

            #range_cluster::-webkit-slider-thumb{{
                -webkit-appearance:none;
                background:#5F0185;
                width:22px;
                height:22px;
                border-radius:50%;
                cursor:pointer;
            }}

            #range_cell_cluster::-webkit-slider-thumb{{
                -webkit-appearance:none;
                background:#5F0185;
                width:22px;
                height:22px;
                border-radius:50%;
                cursor:pointer;
            }}

            #slider_content{{
                margin-top: 24px;
            }}

            .summary_info_div{{
                margin-left: 40px;
                float: left;
            }}

            .total_read_div{{
                width: 380px;
                height: 199px;
                background: #FFFFFF;
                box-shadow: 0px 0px 4px 0px rgba(95,1,133,0.0500);
                border-radius: 8px;
            }}

            .content_div{{
                display: grid;
                padding-bottom: 40px;
                background: #F9FBFC;
            }}
            
            .total_read_div_color{{
                width: 380px;
                height: 6px;
                background: #FF614F;
                border-radius: 8px 8px 0px 0px;
            }}

            .mean_mid_div_color{{
                width: 380px;
                height: 6px;
                background: #FFE6D1;
                border-radius: 8px 8px 0px 0px;
            }}

            .mean_gene_div_color{{
                width: 380px;
                height: 6px;
                background: #C6F3AE;
                border-radius: 8px 8px 0px 0px;
            }}

            .unique_read_div_color{{
                width: 380px;
                height: 6px;
                background: #949ECE;
                border-radius: 8px 8px 0px 0px;
            }}

            .summary_sub_number{{
                height: 56px;
                font-size: 40px;
                font-weight: 600;
                color: #333333;
                line-height: 56px;
                margin-top: 47px;
                text-align: center;
            }}

            .summary_sub_title{{
                height: 34px;
                font-size: 24px;
                font-weight: 500;
                color: #666666;
                line-height: 33px;
                margin-top: 16px;
                text-align: center;
            }}

            .margin_top_class{{
                margin-top: 21px;
            }}

            .sunburst_canvas, .information_canvas, .sequencing_saturation_canvas, .square_bin_statistics_canvas, .bin1_canvas, .bin50_canvas, .bin100_canvas, .bin150_canvas, .bin200_canvas, .clustering_square_bin_canvas, .CellBin_canvas, .cell_bin_stats_canvas, .cellBin_cluster_canvas{{
                margin-top: 40px;
                width: 1200px;
                background: #FFFFFF;
                border-radius: 8px;
                padding-bottom: 24px;
                display: grid;
            }}

            .summary_canvas{{
                display: flex;
                margin-top:24px;
            }}

            #div_explain_sunburst, #div_explain_sequencing_saturation, #div_explain_sequencing, #div_explain_rna_mapping, #div_explain_tissueCut, #div_explain_filtering, #div_explain_annotation, #div_explain_square_bin_statistics, #div_explain_bin1, #div_explain_bin50, #div_explain_bin100, #div_explain_bin150, #div_explain_bin200, #div_explain_clustering_square_bin, #div_explain_cellBin, #div_explain_cell_bin_stats, #div_explain_cellBin_clustering, #div_explain_stitching, #div_explain_registration, #div_explain_qc {{
                display: none;
                font-size: 14px;
                font-weight: 500;
                color: #999999;
                line-height: 20px;
                margin-left: 42px;
                margin-top: 16px;
                display: flex;
                align-items: center;
                justify-content: center;
                display: none;
                margin-bottom: 12px;
                margin-right: 32px;
            }}

            #div_explain_image_left{{
                display: none;
                font-size: 14px;
                font-weight: 500;
                color: #999999;
                line-height: 20px;
                margin-left: 86px;
                margin-top: 16px;
                display: flex;
                align-items: center;
                justify-content: center;
                display: none;
                margin-bottom: 12px;
                margin-right: 32px;
                text-align: left;
                width: 390px;
            }}

            #div_explain_image_middle{{
                display: none;
                font-size: 14px;
                font-weight: 500;
                color: #999999;
                line-height: 20px;
                margin-left: 415px;
                margin-top: 16px;
                display: flex;
                align-items: center;
                justify-content: center;
                display: none;
                margin-bottom: 12px;
                margin-right: 32px;
                text-align: left;
                width: 375px;
            }}

            #div_explain_image_right{{
                display: none;
                font-size: 14px;
                font-weight: 500;
                color: #999999;
                line-height: 20px;
                margin-left: 100px;
                margin-top: 16px;
                display: flex;
                align-items: center;
                justify-content: center;
                display: none;
                margin-bottom: 12px;
                margin-right: 32px;
                text-align: left;
                width: 390px;
            }}

            .sequencing_canvas, .rna_mapping_canvas, .tissueCut_canvas, .filtering_canvas, .annotation_canvas, .image_information_canvas, .stitching_canvas, .qc_canvas, .registration_canvas {{
                width: 580px;
                margin-top: 40px;
                background: #FFFFFF;
                border-radius: 8px;
                padding-bottom: 24px;
                display: grid;
            }}

            .sunburst_part_right{{
                float: right;
                margin-top: 25px;
                margin-right: 50px;
            }}

            .sunburst_part_left{{
                float: left;
                margin-top: 25px;
                margin-left: 30px;
                width: 500px;
            }}

            .circle_total_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #FF614F;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .sunburst_title{{
                height: 22px;
                font-size: 16px;
                font-weight: 400;
                color: #333333;
                line-height: 22px;
                float: left;
                margin-left: 8px;
            }}

            .sunburst_num{{
                float: right;
                height: 22px;
                font-size: 16px;
                font-weight: 400;
                color: #666666;
                line-height: 22px;
                margin-right: 28px;
            }}

            .sunburst_sub_div{{
                height: 30px;
                margin-top: 10px;
                /* z-index: 20; */
            }}

            .circle_cid_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #FFBD84;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_invalid_cid_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #FFCEA2;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_discarded_mid_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #FFE6D1;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_clean_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #A2D287;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_non_relevant_short_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #C6F3AE;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_uniquely_mapped_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #98C1DD;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_multi_mapped_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #C2E2F9;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_unmapped_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #D7EDFB;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_annotated_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #949ECE;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_unannotated_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #B1B8D7;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_unique_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #F7BCFF;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .circle_duplicated_read{{
                width: 10px;
                height: 10px;
                border-radius:8px;
                background: #EDD2F0;
                float:left;
                margin-top: 5px;
                margin-left: 8px;
            }}

            .sunburst_total_div{{
                display: inline-block;
                width: 1200px;
            }}

            .information_canvas{{
                width: 1200px;
                background: #FFFFFF;
                box-shadow: 0px 0px 4px 0px rgba(95,1,133,0.0500);
                border-radius: 8px;
            }}

            .summary_third_content_title{{
                margin-left: 5px;
                font-size: 16px;
                margin-top: 16px;
                margin-bottom: 16px;
                color: #666666 !important;
                float: left;
                width: 305px;
                font-weight: 400;
                color: #333333;
                line-height: 22px;
            }}

            .cell_content_title{{
                margin-left: 32px;
                font-size: 16px;
                margin-top: 16px;
                margin-bottom: 16px;
                color: #333333 !important;
                float: left;
                width: 290px;
                font-weight: 500;
                line-height: 22px;
            }}

            .summary_third_content_image_title{{
                margin-left: 5px;
                font-size: 16px;
                margin-top: 16px;
                margin-bottom: 16px;
                color: #333333;
                float: left;
                width: 100px;
                font-weight: 400;
                color: #333333;
                line-height: 22px;
            }}

            .summary_third_content_information_title{{
                margin-left: 32px;
                font-size: 16px;
                margin-top: 16px;
                margin-bottom: 16px;
                color: #333333;
                float: left;
                width: 90px;
                font-weight: 400;
                color: #333333;
                line-height: 22px;
            }}

            .summary_third_content_num{{
                margin-right: 5px;
                margin-top: 17px;
                color: #666666;
                float: right;
                font-size: 16px;
                font-weight: 400;
                line-height: 22px;
            }}

            .cell_content_num{{
                margin-right: 32px;
                margin-top: 17px;
                color: #666666;
                float: right;
                font-size: 16px;
                font-weight: 400;
                line-height: 22px;
            }}

            .summary_third_content_information_num{{
                margin-right: 32px;
                margin-top: 17px;
                color: #666666;
                float: right;
                font-size: 16px;
                font-weight: 400;
                line-height: 22px;
            }}


            .summary_third_content_div {{
                border: 1px solid #CCCCCC;
                position: relative;
                width: 568px;
                margin-left: -1px;
                height: 61px;
                border-bottom: 0px;
                float:left;
            }}

            .summary_third_content_left_top_div{{
                border: 1px solid #EEEEEE;
                position: relative;
                width: 568px;
                margin-left: -1px;
                height: 61px;
                float:left;
                border-left:0px;
                border-top:0px;
            }}

            .summary_third_content_right_top_div{{
                border: 1px solid #EEEEEE;
                position: relative;
                width: 568px;
                margin-left: -1px;
                height: 61px;
                float:left;
                border-right:0px;
                border-top:0px;
            }}

            .summary_third_content_left_bottom_div{{
                border: 1px solid #EEEEEE;
                position: relative;
                width: 568px;
                margin-left: -1px;
                height: 61px;
                float:left;
                border-left:0px;
                border-bottom:0px;
                border-top:0px;
            }}

            .summary_third_content_right_bottom_div{{
                border: 1px solid #EEEEEE;
                position: relative;
                width: 568px;
                margin-left: -1px;
                height: 61px;
                float:left;
                border-right:0px;
                border-bottom:0px;
                border-top:0px;
            }}

            .summary_third_content_sub_div {{
                border: 1px solid #CCCCCC;
                position: relative;
                width: 568px;
                margin-left: -1px;
                margin-top: -1px;
                height: 61px;
                /* border-bottom: 0px; */
                float:left;
            }}

            .summary_third_content_sub_total_div{{
                border: 1px solid #CCCCCC;
                position: relative;
                width: 1137px;
                margin-left: -1px;
                margin-top: -1px;
                /* border-bottom: 0px; */
                float:left;
                padding-bottom: 16px;
            }}

            .content_margin_top_left{{
                margin-top: 16px;
                margin-left: 36px;
            }}

            .content_margin_top{{
                margin-top: 16px;
                margin-left: 36px;
            }}

            .fastq_margin_top{{
                margin-bottom: 16px;
                margin-left: 36px;
            }}

            .content_margin_sub_top{{
                margin-left: 36px;
            }}

            .content_canvas_div{{
                display:inline-block;
                width: 1200px;
            }}
            
            .content_canvas_half_div{{
                display:inline-block;
            }}

            .summary_left_part{{
                float: left;
                width: 49%;
            }}

            .summary_right_part{{
                float: right;
                width: 49%;
                margin-left: 40px;
            }}

            .middle_canvas{{
                width: 1200px;
                margin-bottom: 16px;
                display: flex;
            }}

            .middle_content_div {{
                border: 1px solid #EEEEEE;
                position: relative;
                width: 516px;
                margin-left: -1px;
                border-top: 0px;
                border-left: 0px;
                border-right: 0px;
                float:left;
            }}

            .summary_six_title_div{{
                border: 1px solid #EEEEEE;
                position: relative;
                width: 1136px;
                height: 80px;
                margin-left: -1px;
                border-top: 0px;
                border-left: 0px;
                border-right: 0px;
                margin-left: auto;
                margin-right: auto;
            }}

            .summary_six_content_div{{
                border: 1px solid #EEEEEE;
                position: relative;
                width: 1136px;
                height: 54px;
                margin-left: -1px;
                border-top: 0px;
                border-left: 0px;
                border-right: 0px;
                margin-left: auto;
                margin-right: auto;
            }}

            .summary_bin_content_title{{
                margin-top: 21px;
                color: #666666;
                float: left;
                text-align: center;
                width: 154px;
                margin-left: 8px;
                height: 22px;
                font-size: 16px;
                font-weight: 500;
                color: #333333;
                line-height: 22px;
            }}

            .text-blue{{
                color: #5F0185;
                margin-bottom: 2px;
                font-size: 14px;
            }}

            #saturation_plot{{
                width: 1100px;
                margin-left: 50px;
                margin-top: 26px;
            }}

            #pop-img-big{{
                height: 90%;
            }}

            #pop-box{{
                position: fixed;
                top: 5%;
                left: 5%;
                width: 90%;
                height: 80vh;
                justify-content: center;
                align-items: center;
                display: none;
                z-index: 10;
                background-color: white;
                border: 1px solid black;
                border-radius: 10px;
                overflow: auto;
                cursor: pointer;
            }}

            #pop-box-big{{
                position: fixed;
                top: 5%;
                left: 5%;
                width: 90%;
                height: 80vh;
                justify-content: left;
                align-items: center;
                display: none;
                z-index: 10;
                background-color: white;
                border: 1px solid black;
                border-radius: 10px;
                overflow: auto;
                cursor: pointer;
            }}

            .summary_bin_content_value{{
                font-size: 18px;
                margin-top: 16px;
                color: #666666;
                float: left;
                text-align: center;
                width: 147px;
                margin-left: 14px;
                font-size: 16px;
                font-weight: 400;
                color: #666666;
                line-height: 22px;
            }}

            #bin1_plot{{
                margin-left: 65px;
                width: 550px;
                margin-top: 30px;
            }}

            #bin50_plot{{
                margin-left: 30px;
                width: 550px;
                margin-top: 30px;
            }}

            #bin100_plot{{
                margin-left: 30px;
                width: 550px;
                margin-top: 30px;
            }}

            #binCell_plot{{
                margin-left: 30px;
                width: 550px;
                margin-top: 30px;
            }}

            #bin200_plot{{
                margin-left: 30px;
                width: 550px;
                margin-top: 30px;
            }}

            .saturation_plot_div{{
                border:1px solid #CCCCCC;
                border-radius: 10px;
                margin-top: 30px;
                display: inline-block;
                width:1180px;
                text-align:center;
            }}

            #binCellMIDGeneDNB_plot, #bin50MIDGeneDNB_plot, #bin100MIDGeneDNB_plot, #bin200MIDGeneDNB_plot{{
                width: 1100px;
                margin-top:30px;
                margin-bottom: 10px;
                margin-left:50px;
            }}

            .title_margin{{
                margin-top: 24px;
            }}

            #heatmap_left{{
                width: 48%;
                float: left;
                border-radius: 8px;
                background: #FFFFFF;
            }}

            #heatmap_right{{
                width: 48%;
                float: left;
                margin-left: 20px;
                border-radius: 8px;
                background: #FFFFFF;
            }}

            #heatmap_center{{
                width: 1200px;
                margin-left: auto;
                margin-right: auto;
                text-align: center;
                border-radius: 8px;
                background: #FFFFFF;
            }}

            .heatmap_plot_div{{
                margin-top: 30px;
                text-align: center;
            }}

            /* 1030列表样式 */
            .box_total_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAXUlEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpIhWyALTln+dgeHIexgPQtsIMjBM1ISw8ZrICPQFDMBNhOmESaDTeE1EVky0QhZQYBofIxDgjAxbASFnMftNUPqUAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
            }}
            .box_cid_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAXUlEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpIhWyALTln+dgeHIexgPQtsIMjBM1ISw8ZrICPQFDMBNhOmESaDTeE1EVky0QhZQYBofIxDgjAxbASFnMftNUPqUAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 18px;
            }}
            .box_clean_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAXUlEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpIhWyALTln+dgeHIexgPQtsIMjBM1ISw8ZrICPQFDMBNhOmESaDTeE1EVky0QhZQYBofIxDgjAxbASFnMftNUPqUAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 36px;
            }}
            .box_uniquely_mapped_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAXUlEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpIhWyALTln+dgeHIexgPQtsIMjBM1ISw8ZrICPQFDMBNhOmESaDTeE1EVky0QhZQYBofIxDgjAxbASFnMftNUPqUAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 54px;
            }}
            .box_annotated_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAXUlEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpIhWyALTln+dgeHIexgPQtsIMjBM1ISw8ZrICPQFDMBNhOmESaDTeE1EVky0QhZQYBofIxDgjAxbASFnMftNUPqUAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 72px;
            }}
            .box_unique_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAM0lEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpEamQhZQYBofIxDgjAxbARhjLTv42vAuAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 90px;
            }}
            .box_duplicated_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAM0lEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpEamQhZQYBofIxDgjAxbARhjLTv42vAuAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 90px;
            }}
            .box_unannotated_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAM0lEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpEamQhZQYBofIxDgjAxbARhjLTv42vAuAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 72px;
            }}
            .box_multi_mapped_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAM0lEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpEamQhZQYBofIxDgjAxbARhjLTv42vAuAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 54px;
            }}
            .box_unmapped_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAM0lEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpEamQhZQYBofIxDgjAxbARhjLTv42vAuAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 54px;
            }}
            .box_non_relevant_short_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAM0lEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpEamQhZQYBofIxDgjAxbARhjLTv42vAuAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 36px;
            }}
            .box_invalid_cid_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAM0lEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpEamQhZQYBofIxDgjAxbARhjLTv42vAuAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 18px;
            }}
            .box_discarded_mid_read{{
                width: 10px;
                height: 10px;
                /* border-radius:8px; */
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAM0lEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpEamQhZQYBofIxDgjAxbARhjLTv42vAuAAAAAElFTkSuQmCC)
    100% no-repeat;
                background-size: 100% 100%;
                float:left;
                margin-top: 5px;
                margin-left: 18px;
            }}
            .sunburst_persent{{
                float: right;
                height: 22px;
                font-size: 16px;
                font-weight: 400;
                color: #666666;
                line-height: 22px;
                width: 60px;
                text-align: right;
            }}

            .sunburst_line1 {{
                height: 390px;
                /* background: darkgray; */
                background-size: 2px 413px;
                margin-left: 23px;
                margin-top: 65px;
                /* width: 1px; */
                z-index: 1000;
                position: absolute;
                border-left:1px dotted rgb(186, 185, 185); 
            }}
            .sunburst_line11 {{
                height: 30px;
                /* background: darkgray; */
                background-size: 2px 413px;
                margin-left: 23px;
                margin-top: 465px;
                /* width: 1px; */
                z-index: 1000;
                position: absolute;
                border-left:1px dotted rgb(186, 185, 185);
            }}
            .sunburst_line2 {{
                height: 310px;
                /* background: darkgray; */
                background-size: 2px 413px;
                margin-left: 40px;
                margin-top: 105px;
                /* width: 1px; */
                z-index: 1000;
                position: absolute;
                border-left:1px dotted rgb(186, 185, 185);
            }}
            .sunburst_line3 {{
                height: 190px;
                /* background: darkgray; */
                background-size: 2px 413px;
                margin-left: 58px;
                margin-top: 145px;
                /* width: 1px; */
                z-index: 1000;
                position: absolute;
                border-left:1px dotted rgb(186, 185, 185); 
            }}
            .sunburst_line31 {{
                height: 30px;
                /* background: darkgray; */
                background-size: 2px 413px;
                margin-left: 58px;
                margin-top: 345px;
                /* width: 1px; */
                z-index: 1000;
                position: absolute;
                border-left:1px dotted rgb(186, 185, 185); 
                display: none;
            }}
            .sunburst_line4 {{
                height: 110px;
                /* background: darkgray; */
                background-size: 2px 413px;
                margin-left: 76px;
                margin-top: 185px;
                /* width: 1px; */
                z-index: 1000;
                position: absolute;
                border-left:1px dotted rgb(186, 185, 185); 
            }}
            .sunburst_line5 {{
                height: 30px;
                /* background: darkgray; */
                background-size: 2px 413px;
                margin-left: 95px;
                margin-top: 225px;
                /* width: 1px; */
                z-index: 1000;
                position: absolute;
                border-left:1px dotted rgb(186, 185, 185); 
            }}
            .text_fastq_name {{
                width: 954px;
                /* height: 96px; */
                overflow-wrap: break-word;
                color: rgba(102, 102, 102, 1);
                font-size: 16px;
                font-family: PingFangSC-Regular;
                text-align: left;
                line-height: 24px;
                /* margin: 135px 0 0 57px; */
            }}
            /* 1130列表样式 */
            .span_form{{
                float: right;
                height: 50px;
                line-height: 40px;
                padding-top: 30px;
                padding-right: 32px;
            }}
            .span_select{{
                width: 150px;
                float: right;
                border-radius: 6px;
                height: 28px;
                font-size: 12px;
                font-weight: 500;
                color: #5F0185;
                line-height: 40px;
                padding-top: 0px;
                padding-right: 0px;
            }}

        </style>
    </head>

    <body class="body_style">
        <div class="header">
            <div class="canvas">
                <div class="analyticalTitle">
                    {logo_img}
                    <span class="header_title">Analytical Report</span>
                </div>
            </div>
        </div>
        <div class="fastq_div">
            <div class="canvas">
                <div class="fastq_title">{sn_name}</div>
            </div>
        </div>
        <div class="content_div">
            <div class="div_tab">
                <div class="canvas tab_height">
                    <ul id='tab', class='tab bin_div_class'>
                        <li class='tabin' style="cursor: pointer;">Summary</li>
                        <li><div class="tab_margin" style="cursor: pointer;">Square Bin</div></li>
                        <li><div class="tab_margin" style="cursor: pointer;">Cell Bin</div></li>
                        <li><div class="tab_margin" style="cursor: pointer;">Image</div></li>
                    </ul>
                </div>
                <div id="pop-box" onclick="openImg(this.src)">
                    <img id="pop-img" src="">
                </div>
                <div id="pop-box-big" onclick="openImgBig(this.src)">
                    <img id="pop-img-big" src="">
                </div>

                <div class='tab_content'>
                    <div class='summary_div show'>
                        <div class="summary_canvas">
                            <div id="scatter_canvas">
                                <div class="sub_title">
                                    <div class="title_label"></div>
                                    <div class="span_title">Spatial Gene Expression Distribution</div>
                                    <button class="button_explain" onclick="show()">
                                        <i class="fa">?</i>
                                    </button>
                                    <form action="" class="span_form">
                                        <select id="image_select"class="span_select" onchange="imageselection()" >
                                        {image_list}
                                        <option value="no-image">No image</option>
                                        </select>
                                    </form>
                                    <div id='div_quation'>Spatial gene expression distribution plot shows MID count at each spot (bin200)</div>
                                </div>
                                <div id='divScatter', class="divScatterBackground">
                                </div>
                                <div id='slider_gene_exp'>
                                    <div id='slider_content' class='show'>
                                        <button id='button_ssdna' class="btn btn-link" onclick="ssdna();">show image</button>
                                        <i class="far fa-sun"></i>
                                        <input type="range" id="range" min="0" max="1" value="1" step="0.1">
                                        <i class="fas fa-sun"></i>
                                        <button id='button_heatmap' class="btn btn-link" onclick="heatmap();">show expression</button>
                                    </div>
                                </div>
                                <div class="scatter_plot_title">Tissue Plot with Spot (bin200) Colored by MID Count</div>
                                <script>
                                    rangeInput = document.getElementById("range");
                                    container = document
                                        .getElementsByClassName("container")[0];
                                    
                                    var trace1 = {{
                                        x: {x},
                                        y: {y},
                                        text: {text},
                                        opacity: 1.0,
                                        mode: 'markers',
                                        type: 'scattergl',
                                        marker:{{
                                            color: {text},
                                            colorscale: {colorscale},
                                            line: {{"color": "white", "width": 0}},
                                            showscale: 'True',
                                            "size": {dot_size_h5},
                                            "colorbar": {{
                                                "len": 0.2,
                                                "thickness": 15,
                                                "x": 1.12,
                                                "xanchor": "right",
                                                "xpad": 8,
                                                "yanchor": "middle",
                                                "y": 0.1,
                                                "ticks":'inside',
                                                "ticklen":10,
                                                "tickwidth":2
                                            }},
                                        }}
                                    }};

                                    var data = [trace1];
                                    var layout = {{
                                        title: {{text:'ST','font':{{'color':'#CECECE', 'size':20}}, 'x':0.05, 'xanchor':'center', 'y':0.98, 'yanchor':'top'}},
                                        yaxis: {{'autorange': 'reversed', 'scaleanchor': "x", 'scaleratio': 1, 'showgrid': false, 'showticklabels': false, 'zeroline': false}},
                                        xaxis: {{'showgrid': false, 'showticklabels': false, 'zeroline': false}},
                                        margin: {{'l' : 30, 't' : 30, 'r' : 50, 'b' : 15}},
                                        showlegend: false,
                                        dragmode:"pan",
                                        plot_bgcolor:"black",
                                        paper_bgcolor:"#FFF3",
                                        images: {image}
                                    }}

                                    var config = {{
                                        toImageButtonOptions: {{
                                            format: 'png', // one of png, svg, jpeg, webp
                                            filename: 'custom_image',
                                            height: 640,
                                            width: 716,
                                            scale: 5 // Multiply title/legend/axis/canvas sizes by this factor
                                        }},
                                        scrollZoom:true,
                                        displaylogo:false,
                                        modeBarButtonsToRemove:["hoverClosestCartesian","hoverCompareCartesian","toggleSpikelines","autoScale2d","lasso2d","select2d"]
                                    }};

                                    Plotly.newPlot('divScatter', data, layout, config);
                                    rangeInput.addEventListener("change", function() {{
                                        var update = {{
                                            'marker.opacity': rangeInput.value,
                                        }};
                                        Plotly.restyle(divScatter, update);
                                    }});
                                </script>
                            </div>
                            <div class="summary_info_div">
                                <div class="total_read_div">
                                    <div class="total_read_div_color"></div>
                                    <div class='summary_sub_number'>{Total_read}</div>
                                    <div class='summary_sub_title'>Total Reads</div>
                                </div>
                                <div class="total_read_div margin_top_class">
                                    <div class="mean_mid_div_color"></div>
                                    <div class='summary_sub_number'>{Mean_UMI_per_bin200}</div>
                                    <div class='summary_sub_title'>Mean MID per Bin200</div>
                                </div>
                                <div class="total_read_div margin_top_class">
                                    <div class="mean_gene_div_color"></div>
                                    <div class='summary_sub_number'>{Mean_Gene_per_bin200}</div>
                                    <div class='summary_sub_title'>Mean Gene per Bin200</div>
                                </div>
                                <div class="total_read_div margin_top_class">
                                    <div class="unique_read_div_color"></div>
                                    <div class='summary_sub_number'>{unique_reads}</div>
                                    <div class='summary_sub_title'>Unique Reads</div>
                                </div>
                            </div>
                        </div>
                        <div class="sunburst_canvas">
                            <div class="sub_title">
                                <div class="title_label"></div>
                                <div class="span_title">Key Metrices</div>
                                <button class="button_explain" onclick="show_sunburst()">
                                    <i class="fa">?</i>
                                </button>
                                <div id='div_explain_sunburst'>{sunburst_collapse}</div>
                            </div>
                            <div class="sunburst_total_div">
                                <div class="sunburst_part_left">
                                    <div class="sunburst_line1" id="sunburst_line1"></div>
                                    <div class="sunburst_line11" id="sunburst_line11"></div>
                                    <div class="sunburst_line2" id="sunburst_line2"></div>
                                    <div class="sunburst_line3" id="sunburst_line3"></div>
                                    <div class="sunburst_line31" id="sunburst_line31"></div>
                                    <div class="sunburst_line4" id="sunburst_line4"></div>
                                    <div class="sunburst_line5" id="sunburst_line5"></div>
                                    <div class='sunburst_sub_div'>
                                        <div class="box_total_read" id="list_box1" onclick="show_list_element('1')"></div>
                                        <div class="circle_total_read"></div>
                                        <div class='sunburst_title'>Total Reads</div>
                                        <div class='sunburst_persent' style="color:#FF614F">{persent_total_reads}</div>
                                        <div class='sunburst_num'>{sunburst_total_reads}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key1" style="display:block">
                                        <div class="box_cid_read" id="list_box2" onclick="show_list_element('2')"></div>
                                        <div class="circle_cid_read"></div>
                                        <div class='sunburst_title'>Valid CID Reads</div>
                                        <div class='sunburst_persent' style="color:#FF614F">{persent_cid_reads}</div>
                                        <div class='sunburst_num'>{valid_cid_reads}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key2" style="display:block">
                                        <div class="box_clean_read" id="list_box3" onclick="show_list_element('3')"></div>
                                        <div class="circle_clean_read"></div>
                                        <div class='sunburst_title'>Clean Reads</div>
                                        <div class='sunburst_persent' style="color:#FFBD84">{persent_clean_reads}</div>
                                        <div class='sunburst_num'>{clean_reads}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key3" style="display:block">
                                        <div class="box_uniquely_mapped_read" id="list_box4" onclick="show_list_element('4')"></div>
                                        <div class="circle_uniquely_mapped_read"></div>
                                        <div class='sunburst_title'>Uniquely Mapped Reads</div>
                                        <div class='sunburst_persent' style="color:#A2D287">{persent_unique_mapping_reads}</div>
                                        <div class='sunburst_num'>{unique_mapping_reads}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key4" style="display:block">
                                        <div class="box_annotated_read" id="list_box5" onclick="show_list_element('5')"></div>
                                        <div class="circle_annotated_read"></div>
                                        <div class='sunburst_title'>Annotated Reads</div>
                                        <div class='sunburst_persent' style="color:#98C1DD">{persent_transcriptome}</div>
                                        <div class='sunburst_num'>{transcriptome}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key5" style="display:block">
                                        <div class="box_unique_read"></div>
                                        <div class="circle_unique_read"></div>
                                        <div class='sunburst_title'>Unique Reads</div>
                                        <div class='sunburst_persent' style="color:#949ECE">{persent_unique_reads}</div>
                                        <div class='sunburst_num'>{unique_reads}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key6" style="display:block">
                                        <div class="box_duplicated_read"></div>
                                        <div class="circle_duplicated_read"></div>
                                        <div class='sunburst_title'>Duplicated Reads</div>
                                        <div class='sunburst_persent' style="color:#949ECE">{persent_duplicated_reads}</div>
                                        <div class='sunburst_num'>{duplicated_reads}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key7" style="display:block">
                                        <div class="box_unannotated_read"></div>
                                        <div class="circle_unannotated_read"></div>
                                        <div class='sunburst_title'>Unannotated Reads</div>
                                        <div class='sunburst_persent' style="color:#98C1DD">{persent_intergenic}</div>
                                        <div class='sunburst_num'>{intergenic}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key8">
                                        <div class="box_multi_mapped_read"></div>
                                        <div class="circle_multi_mapped_read"></div>
                                        <div class='sunburst_title'>Multi-Mapped Reads</div>
                                        <div class='sunburst_persent' style="color:#A2D287">{persent_multi_mapping_reads}</div>
                                        <div class='sunburst_num'>{multiple_mapping_reads}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key9">
                                        <div class="box_unmapped_read"></div>
                                        <div class="circle_unmapped_read"></div>
                                        <div class='sunburst_title'>Unmapped Reads</div>
                                        <div class='sunburst_persent' style="color:#A2D287">{persent_unmapping_reads}</div>
                                        <div class='sunburst_num'>{rna_unmapping_reads}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key10">
                                        <div class="box_non_relevant_short_read"></div>
                                        <div class="circle_non_relevant_short_read"></div>
                                        <div class='sunburst_title'>Non-Relevant Short Reads</div>
                                        <div class='sunburst_persent' style="color:#FFBD84">{persent_too_short_reads}</div>
                                        <div class='sunburst_num'>{too_short_reads}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key11">
                                        <div class="box_invalid_cid_read"></div>
                                        <div class="circle_invalid_cid_read"></div>
                                        <div class='sunburst_title'>Invalid CID Reads</div>
                                        <div class='sunburst_persent' style="color:#FF614F">{persent_invalid_cid_reads}</div>
                                        <div class='sunburst_num'>{invalid_cid_reads}</div>
                                    </div>
                                    <div class='sunburst_sub_div' id="list_key12">
                                        <div class="box_discarded_mid_read"></div>
                                        <div class="circle_discarded_mid_read"></div>
                                        <div class='sunburst_title'>Discarded MID Reads</div>
                                        <div class='sunburst_persent' style="color:#FF614F">{persent_discarded_mid_reads}</div>
                                        <div class='sunburst_num'>{discarded_mid_reads}</div>
                                    </div>
                                </div>
                                <div class='sunburst_part_right'>
                                    <div class='sun_div'>
                                        <div id=divSunBurst></div>
                                        <script>
                                        var sun_data = [{{
                                            type: 'sunburst',
                                            labels: {sun_label},
                                            parents: {sun_parent},
                                            values: {sun_value},
                                            hovertext: {sun_hovertext},
                                            text: {name_pro},
                                            textinfo: 'label+text',
                                            hoverinfo: 'label+text',
                                            branchvalues: 'total',
                                            marker: {{'line':{{'width':1}},'colors':['#FF614F','#FFBD84','#FFCEA2','#FFE6D1','#A2D287','#C6F3AE','#FFFFFF','#FFFFFF','#98C1DD','#C2E2F9','#D7EDFB','#949ECE','#B1B8D7','#EDD2F0','#F7BCFF']}},
                                        }}];
                                        var sun_layout = {{
                                            margin: {{l:0, r:0, b:0, t:0}},
                                            width:500,
                                            height:500
                                        }};
                                        Plotly.newPlot('divSunBurst', sun_data, sun_layout, {{displaylogo:false}});
                                        </script>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="information_canvas">
                            <div class="sub_title">
                                <div class="title_label"></div>
                                <div class="span_title">Information</div>
                            </div>
                            <div>
                                <div class="content_margin_top_left">
                                    <div class="summary_third_content_div">
                                        <div class='summary_third_content_information_title'>Species</div>
                                        <div class='summary_third_content_information_num'>{species}</div>
                                    </div>
                                    <div class="summary_third_content_div">
                                        <div class='summary_third_content_information_title'>Tissue</div>
                                        <div class='summary_third_content_information_num'>{tissue}</div>
                                    </div>
                                </div>
                                <div class="content_margin_sub_top">
                                    <div class="summary_third_content_sub_div">
                                        <div class='summary_third_content_information_title'>Reference</div>
                                        <div class='summary_third_content_information_num'>{reference}</div>
                                    </div>
                                    <div class="summary_third_content_sub_div">
                                    </div>
                                </div>
                                <div class="content_margin_sub_top">
                                    <div class="summary_third_content_sub_total_div">
                                        <div class='summary_third_content_information_title' style="width:100">FASTQ</div>
                                        <div class='summary_third_content_information_num'>
                                            <div class="text_fastq_name">
                                                {fastq_name}
                                            </div>
                                        </div>
                                        
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="middle_canvas">
                            <div class="summary_left_part">
                                <div class="sequencing_canvas">
                                    <div class="sub_title">
                                        <div class="title_label"></div>
                                        <div class="span_title">Sequencing</div>
                                        <button class="button_explain" onclick="show_sequencing()">
                                            <i class="fa">?</i>
                                        </button>
                                        <div id='div_explain_sequencing'>
                                            {quality_collapse}
                                        </div>
                                        <div class="content_canvas_half_div">
                                            <div class="content_margin_sub_top">
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Total Reads</div>
                                                    <div class='summary_third_content_num'>{Total_read}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Total Q30</div>
                                                    <div class='summary_third_content_num'>{rate_of_q30_bases_in_seq}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>CID Q30</div>
                                                    <div class='summary_third_content_num'>{rate_of_q30_bases_in_cid}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>MID Q30</div>
                                                    <div class='summary_third_content_num'>{rate_of_q30_bases_in_mid}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="rna_mapping_canvas">
                                    <div class="sub_title">
                                        <div class="title_label"></div>
                                        <div class="span_title">RNA Mapping</div>
                                        <button class="button_explain" onclick="show_rna_mapping()">
                                            <i class="fa">?</i>
                                        </button>
                                        <div id='div_explain_rna_mapping'>
                                            {rna_collapse}
                                        </div>
                                        <div class="content_canvas_half_div">
                                            <div class="content_margin_sub_top">
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Clean Reads</div>
                                                    <div class='summary_third_content_num'>{rna_clean_reads}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Uniquely Mapped Reads</div>
                                                    <div class='summary_third_content_num'>{unique_mapping_reads}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Multi-Mapped Reads</div>
                                                    <div class='summary_third_content_num'>{multiple_mapping_reads}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Unmapped Reads</div>
                                                    <div class='summary_third_content_num'>{rna_unmapping_reads}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="tissueCut_canvas">
                                    <div class="sub_title">
                                        <div class="title_label"></div>
                                        <div class="span_title">Tissue</div>
                                        <button class="button_explain" onclick="show_tissueCut()">
                                            <i class="fa">?</i>
                                        </button>
                                        <div id='div_explain_tissueCut'>
                                            {tissueCut_total_collapse}
                                        </div>
                                        <div class="content_canvas_half_div">
                                            <div class="content_margin_sub_top">
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>DNB Under Tissue</div>
                                                    <div class='summary_third_content_num'>{contour_area}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>mRNA-Captured DNBs Under Tissue</div>
                                                    <div class='summary_third_content_num'>{number_of_dnb_under_tissue}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Fraction mRNA-Captured DNBs Under Tissue</div>
                                                    <div class='summary_third_content_num'>{ratio_of_dnb_under_tissue}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Genes Under Tissue</div>
                                                    <div class='summary_third_content_num'>{total_gene_type}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Number of MID Under Tissue Coverage</div>
                                                    <div class='summary_third_content_num'>{mid_under_tissue}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Fraction MID in Spots Under Tissue</div>
                                                    <div class='summary_third_content_num'>{fraction_mid_in_spots_under_tissue}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Reads Under Tissue</div>
                                                    <div class='summary_third_content_num'>{reads_under_tissue}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Fraction Reads in Spots Under Tissue</div>
                                                    <div class='summary_third_content_num'>{fraction_reads_in_spots_under_tissue}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="summary_right_part">
                                <div class="filtering_canvas">
                                    <div class="sub_title">
                                        <div class="title_label"></div>
                                        <div class="span_title">Filtering</div>
                                        <button class="button_explain" onclick="show_filtering()">
                                            <i class="fa">?</i>
                                        </button>
                                        <div id='div_explain_filtering'>
                                            {filter_collapse}
                                        </div>
                                        <div class="content_canvas_half_div">
                                            <div class="content_margin_sub_top">
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Valid CID Reads</div>
                                                    <div class='summary_third_content_num'>{valid_cid_reads}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Clean Reads</div>
                                                    <div class='summary_third_content_num'>{clean_reads}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Non-Relevent Short Reads</div>
                                                    <div class='summary_third_content_num'>{too_short_reads}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Reads With Adapter</div>
                                                    <div class='summary_third_content_num'>{reads_with_adapter}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Reads With DNB</div>
                                                    <div class='summary_third_content_num'>{reads_with_dnb}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="annotation_canvas">
                                    <div class="sub_title">
                                        <div class="title_label"></div>
                                        <div class="span_title">Annotation</div>
                                        <button class="button_explain" onclick="show_annotation()">
                                            <i class="fa">?</i>
                                        </button>
                                        <div id='div_explain_annotation'>
                                            {rna_annotation_collapse}
                                        </div>
                                        <div class="content_canvas_half_div">
                                            <div class="content_margin_sub_top">
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Exonic</div>
                                                    <div class='summary_third_content_num'>{exonic}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Intronic</div>
                                                    <div class='summary_third_content_num'>{intronic}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Intergenic</div>
                                                    <div class='summary_third_content_num'>{intergenic}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Transcriptome</div>
                                                    <div class='summary_third_content_num'>{transcriptome}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Antisense</div>
                                                    <div class='summary_third_content_num'>{antisense}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="sequencing_saturation_canvas">
                            <div class="sub_title">
                                <div class="title_label"></div>
                                <div class="span_title">Sequencing Saturation</div>
                                <button class="button_explain" onclick="show_sequencing_saturation()">
                                    <i class="fa">?</i>
                                </button>
                                <div id='div_explain_sequencing_saturation'>
                                    <div>(left) Plot of the sequencing saturation as a function of sequencing depth(bin200) </div>
                                    <div>(middle) Plot of the median number of genes detected per bin as a function of sequencing depth(bin200) </div>
                                    <div>(right) Plot of the unique reads detected per bin as a function of sequencing depth(bin200)</div>
                                </div>
                                <div class="content_canvas_div">{saturation_plot}</div>
                            </div>
                        </div>
                    </div>
                    <div class='square_bin_div unshow'>
                        <div class="square_bin_statistics_canvas title_margin">
                            <div class="sub_title">
                                <div class="title_label"></div>
                                <div class="span_title">Tissue Square Bin Statistics</div>
                                <button class="button_explain" onclick="show_square_bin_statistics()">
                                    <i class="fa">?</i>
                                </button>
                                <div id='div_explain_square_bin_statistics'>
                                    {tissueCut_bin_collapse}
                                </div>
                                <div class='summary_six_title_div content_margin_top'>
                                    <div class='summary_bin_content_title'>Bin Size</div>
                                    <div class='summary_bin_content_title'>Mean Reads<br>(per bin)</div>
                                    <div class='summary_bin_content_title'>Median Reads<br>(per bin)</div>
                                    <div class='summary_bin_content_title'>Mean Gene Type<br>(per bin)</div>
                                    <div class='summary_bin_content_title'>Median Gene Type<br>(per bin)</div>
                                    <div class='summary_bin_content_title'>Mean MID<br>(per bin)</div>
                                    <div class='summary_bin_content_title'>Median MID<br>(per bin)</div>
                                </div>
                                {bin_div}
                            </div>
                        </div>
                        <div class="bin1_canvas">
                            <div class="sub_title">
                                <div class="title_label"></div>
                                <div class="span_title">Bin 1</div>
                                <button class="button_explain" onclick="show_bin1()">
                                    <i class="fa">?</i>
                                </button>
                                <div id='div_explain_bin1'>
                                    <div>(left) Plot of the sequencing saturation as a function of sequencing depth</div>
                                    <div>(right) Plot of the median number of genes detected per CID as a function of sequencing depth</div>
                                </div>
                                <div class="content_canvas_div">{bin1_saturation_plot}</div>
                            </div>
                        </div>
                        {binsize_canvas}
                        <div id=clustering_square_bin_canvas, class="clustering_square_bin_canvas">
                            <div class="sub_title">
                                <div class="title_label"></div>
                                <div class="span_title">Clustering</div>
                                <button class="button_explain" onclick="show_clustering_square_bin()">
                                    <i class="fa">?</i>
                                </button>
                                <div id='div_explain_clustering_square_bin'>
                                    <div>(left) Clustering spots (bin200) under tissue covered with the Leiden algorithm</div>
                                    <div>(right) UMAP projections of spots (bin200) colored by automated clustering. Same color is assigned to  spots that are within shorter distance and with similar gene expression profile</div>
                                </div>
                                <div class="content_canvas_div">
                                    <div id='divCluster', style="width:500px;margin-left:50px;margin-right:auto;margin-top:10px;float:left;">
                                        <div id="slider_square_cluster">
                                            <div id='slider_cluster'>
                                                <button id='button_cluster_ssdna' class="btn btn-link" onclick="cluster_ssdna();">show ssDNA</button>
                                                <i class="far fa-sun"></i>
                                                <input type="range" id="range_cluster" min="0" max="1" value="1" step="0.1">
                                                <i class="fas fa-sun"></i>
                                                <button id='button_cluster' class="btn btn-link" onclick="cluster();">show cluster</button>
                                            </div>
                                        </div>
                                        <div style="margin-top:20px;text-align:center;font-weight: 500;font-style: normal;font-size:19px;">Tissue Plot with Spots (bin200)</div>
                                        <script>
                                            rangeInputCluster = document.getElementById("range_cluster");
                                            container = document
                                                .getElementsByClassName("container")[0];
                                                
                                            {data_cluster}
                                            var data_cluster = {total_data_str};
                                            var layout_cluster = {{
                                                yaxis: {{'autorange': 'reversed', 'scaleanchor': "x", 'scaleratio': 1, 'showgrid': false, 'showticklabels': false, 'zeroline': false}},
                                                xaxis: {{'showgrid': false, 'showticklabels': false, 'zeroline': false}},
                                                margin: {{'l' : 50, 't' : 30, 'r' : 10, 'b' : 15}},
                                                dragmode:"pan",
                                                images: {image_cluster}
                                            }}

                                            var config_cluster = {{
                                                toImageButtonOptions: {{
                                                    format: 'png', // one of png, svg, jpeg, webp
                                                    filename: 'custom_image',
                                                    height: 450,
                                                    width: 500,
                                                    scale: 5 // Multiply title/legend/axis/canvas sizes by this factor
                                                }},
                                                scrollZoom:true,
                                                displaylogo:false,
                                                modeBarButtonsToRemove:["hoverClosestCartesian","hoverCompareCartesian","toggleSpikelines","autoScale2d","lasso2d","select2d"]
                                            }};

                                            Plotly.newPlot('divCluster', data_cluster, layout_cluster, config_cluster);
                                            rangeInputCluster.addEventListener("change", function() {{
                                                var update = {{
                                                    'marker.opacity': rangeInputCluster.value,
                                                }};
                                                Plotly.restyle(divCluster, update);
                                            }});
                                        </script>
                                    </div>

                                    <div id='divClass', style="width:500px;height:500px;margin-left:100px;margin-right:auto;margin-top:10px;float:left;">
                                        <div style="margin-top:20px;text-align:center;font-weight: 500;font-style: normal;font-size:19px;">UMAP Projection of Spots (bin200)</div>
                                        <script>
                                            rangeInputClass = document.getElementById("range_class");
                                            container = document
                                                .getElementsByClassName("container")[0];
                                                
                                            {data_class}
                                            var data_class = {total_data_class_str};
                                            var layout_class = {{
                                                yaxis: {{'autorange': 'reversed', 'scaleanchor': "x", 'scaleratio': 1, 'showgrid': false, 'showticklabels': false, 'zeroline': false}},
                                                xaxis: {{'showgrid': false, 'showticklabels': false, 'zeroline': false}},
                                                margin: {{'l' : 50, 't' : 30, 'r' : 10, 'b' : 15}}
                                            }}

                                            var config_class = {{
                                                toImageButtonOptions: {{
                                                    format: 'png', // one of png, svg, jpeg, webp
                                                    filename: 'custom_image',
                                                    height: 500,
                                                    width: 500,
                                                    scale: 5 // Multiply title/legend/axis/canvas sizes by this factor
                                                }},
                                                scrollZoom:true,
                                                displaylogo:false,
                                                modeBarButtonsToRemove:["hoverClosestCartesian","hoverCompareCartesian","toggleSpikelines","autoScale2d","lasso2d","select2d"]
                                            }};

                                            Plotly.newPlot('divClass', data_class, layout_class, config_class);

                                        </script>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class='cell_bin_div unshow'>
                        <div class="cell_bin_stats_canvas title_margin">
                            <div class="sub_title">
                                <div class="title_label"></div>
                                <div class="span_title">Cell Bin Statistics</div>
                                <button class="button_explain" onclick="show_cell_bin_stats()">
                                    <i class="fa">?</i>
                                </button>
                                <div id='div_explain_cell_bin_stats'>{cell_bin_collapse}</div>
                            </div>
                            <div>
                                <div class="content_margin_top_left">
                                    <div class="summary_third_content_left_top_div">
                                        <div class='cell_content_title'>Cell Count</div>
                                        <div class='cell_content_num'>{cell_count}</div>
                                    </div>
                                    <div class="summary_third_content_right_top_div">
                                    </div>
                                </div>
                                <div class="content_margin_sub_top">
                                    <div class="summary_third_content_left_top_div">
                                        <div class='cell_content_title'>Mean Cell Area</div>
                                        <div class='cell_content_num'>{mean_cell_area}</div>
                                    </div>
                                    <div class="summary_third_content_right_top_div">
                                        <div class='cell_content_title'>Median Cell Area</div>
                                        <div class='cell_content_num'>{median_cell_area}</div>
                                    </div>
                                </div>
                                <div class="content_margin_sub_top">
                                    <div class="summary_third_content_left_top_div">
                                        <div class='cell_content_title'>Mean DNB Count</div>
                                        <div class='cell_content_num'>{mean_cell_boundary_dnb_count}</div>
                                    </div>
                                    <div class="summary_third_content_right_top_div">
                                        <div class='cell_content_title'>Median DNB Count</div>
                                        <div class='cell_content_num'>{median_cell_boundary_dnb_count}</div>
                                    </div>
                                </div>
                                <div class="content_margin_sub_top">
                                    <div class="summary_third_content_left_top_div">
                                        <div class='cell_content_title'>Mean Gene Type</div>
                                        <div class='cell_content_num'>{mean_gene_type}</div>
                                    </div>
                                    <div class="summary_third_content_right_top_div">
                                        <div class='cell_content_title'>Median Gene Type</div>
                                        <div class='cell_content_num'>{median_gene_type}</div>
                                    </div>
                                </div>
                                <div class="content_margin_sub_top">
                                    <div class="summary_third_content_left_bottom_div">
                                        <div class='cell_content_title'>Mean MID</div>
                                        <div class='cell_content_num'>{mean_mid_count}</div>
                                    </div>
                                    <div class="summary_third_content_right_bottom_div">
                                        <div class='cell_content_title'>Median MID</div>
                                        <div class='cell_content_num'>{median_mid_count}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="CellBin_canvas">
                            <div class="sub_title">
                                <div class="title_label"></div>
                                <div class="span_title">Cell Bin</div>
                                <button class="button_explain" onclick="show_cellBin()">
                                    <i class="fa">?</i>
                                </button>
                                <div id='div_explain_cellBin'>
                                    <div>(left) Scatter plot of MID count and gene number in each bin; Scatter plot of cell area (pixel) and mRNA-captured DNBs in each bin; Scatter plot of MID count and mRNA-captured DNBs in each bin</div>
                                    <div>(right) Violin plots show the distribution of deduplicated MID count and gene number in each bin</div>
                                    <div>(bottom) Univariate distribution of MID count, gene numbers, DNB numbers, and cell area (pixel) with rug along the x axis</div>
                                </div>
                                <div class="content_canvas_div">
                                    {binCell_saturation_plot}
                                    {areaCell_saturation_plot}
                                    {midCell_saturation_plot}
                                    {binCell_violin_plot}
                                    {binCellMIDGeneDNB_plot}
                                </div>
                            </div>
                        </div>
                        <div id="cellBin_cluster_canvas", class="cellBin_cluster_canvas">
                            <div class="sub_title">
                                <div class="title_label"></div>
                                <div class="span_title">Clustering</div>
                                <button class="button_explain" onclick="show_cellBin_clustering()">
                                    <i class="fa">?</i>
                                </button>
                                <div id='div_explain_cellBin_clustering'>
                                    <div>(left) Clustering spots (cell bin) under tissue covered region with the Leiden algorithm</div>
                                    <div>(right) UMAP projections of spots (cell bin) colored by automated clustering. Spots in the short distance are assigned with the same color have similar gene expression profile.</div>
                                </div>
                                <div class="content_canvas_div">
                                    <div id='divCellCluster', style="width:500px;margin-left:50px;margin-right:auto;margin-top:10px;float:left;">
                                        <div id='slider_cluster'>
                                            <button id='button_cell_cluster_ssdna' class="btn btn-link" onclick="cluster_cell_ssdna();">show ssDNA</button>
                                            <i class="far fa-sun"></i>
                                            <input type="range" id="range_cell_cluster" min="0" max="1" value="1" step="0.1">
                                            <i class="fas fa-sun"></i>
                                            <button id='button_cell_cluster' class="btn btn-link" onclick="cell_cluster();">show cluster</button>
                                        </div>
                                        <div style="margin-top:20px;text-align:center;font-weight: 500;font-style: normal;font-size:19px;">Tissue Plot with Spots (cell bin)</div>
                                        <script>
                                            rangeInputCellCluster = document.getElementById("range_cell_cluster");
                                            container = document
                                                .getElementsByClassName("container")[0];
                                                
                                            {cell_data_cluster}
                                            var data_cluster = {total_cell_data_str};
                                            var layout_cluster = {{
                                                yaxis: {{'autorange': 'reversed', 'scaleanchor': "x", 'scaleratio': 1, 'showgrid': false, 'showticklabels': false, 'zeroline': false}},
                                                xaxis: {{'showgrid': false, 'showticklabels': false, 'zeroline': false}},
                                                margin: {{'l' : 50, 't' : 30, 'r' : 10, 'b' : 15}},
                                                dragmode:"pan",
                                                images: {image_cluster}
                                            }}

                                            var config_cluster = {{
                                                toImageButtonOptions: {{
                                                    format: 'png', // one of png, svg, jpeg, webp
                                                    filename: 'custom_image',
                                                    height: 500,
                                                    width: 500,
                                                    scale: 5 // Multiply title/legend/axis/canvas sizes by this factor
                                                }},
                                                scrollZoom:true,
                                                displaylogo:false,
                                                modeBarButtonsToRemove:["hoverClosestCartesian","hoverCompareCartesian","toggleSpikelines","autoScale2d","lasso2d","select2d"]
                                            }};

                                            Plotly.newPlot('divCellCluster', data_cluster, layout_cluster, config_cluster);
                                            rangeInputCellCluster.addEventListener("change", function() {{
                                                var update = {{
                                                    'marker.opacity': rangeInputCellCluster.value,
                                                }};
                                                Plotly.restyle(divCellCluster, update);
                                            }});
                                        </script>
                                    </div>

                                    <div id='divCellClass', style="width:500px;height:500px;margin-left:100px;margin-right:auto;margin-top:10px;float:left;">
                                        <div style="margin-top:20px;text-align:center;font-weight: 500;font-style: normal;font-size:19px;">UMAP Projection of Spots (cellbin)</div>
                                        <script>
                                            rangeInputClass = document.getElementById("range_class");
                                            container = document
                                                .getElementsByClassName("container")[0];
                                                    
                                            {cell_data_class}
                                            var data_class = {total_cell_data_class_str};
                                            var layout_class = {{
                                                yaxis: {{'autorange': 'reversed', 'scaleanchor': "x", 'scaleratio': 1, 'showgrid': false, 'showticklabels': false, 'zeroline': false}},
                                                xaxis: {{'showgrid': false, 'showticklabels': false, 'zeroline': false}},
                                                margin: {{'l' : 50, 't' : 30, 'r' : 10, 'b' : 15}}
                                            }}

                                            var config_class = {{
                                                toImageButtonOptions: {{
                                                    format: 'png', // one of png, svg, jpeg, webp
                                                    filename: 'custom_image',
                                                    height: 500,
                                                    width: 500,
                                                    scale: 5 // Multiply title/legend/axis/canvas sizes by this factor
                                                }},
                                                scrollZoom:true,
                                                displaylogo:false,
                                                modeBarButtonsToRemove:["hoverClosestCartesian","hoverCompareCartesian","toggleSpikelines","autoScale2d","lasso2d","select2d"]
                                            }};

                                            Plotly.newPlot('divCellClass', data_class, layout_class, config_class);

                                        </script>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                    <div class='image_div unshow'>
                        <div class="middle_canvas">
                            <div class="summary_left_part">
                                <div class="image_information_canvas title_margin">
                                    <div class="sub_title">
                                        <div class="title_label"></div>
                                        <div class="span_title">Image Information</div>
                                        <div class="content_canvas_half_div">
                                            <div class="content_margin_sub_top">
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Manufacture</div>
                                                    <div class='summary_third_content_num'>{image_manufacture}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Model</div>
                                                    <div class='summary_third_content_num'>{image_model}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Scan Time</div>
                                                    <div class='summary_third_content_num'>{scan_time}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Overlap</div>
                                                    <div class='summary_third_content_num'>{overlap}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Exposure Time (ms)</div>
                                                    <div class='summary_third_content_num'>{exposure_time}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Scan Rows</div>
                                                    <div class='summary_third_content_num'>{scan_rows}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Scan Columns</div>
                                                    <div class='summary_third_content_num'>{scan_columns}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>FOV Height</div>
                                                    <div class='summary_third_content_num'>{fov_height}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>FOV Width</div>
                                                    <div class='summary_third_content_num'>{fov_width}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Stain Type</div>
                                                    <div class='summary_third_content_num'>{stain_type}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Stitched Image</div>
                                                    <div class='summary_third_content_num'>{stitched_image}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_image_title'>Image Name</div>
                                                    <div class='summary_third_content_num'>{image_name}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="stitching_canvas">
                                    <div class="sub_title">
                                        <div class="title_label"></div>
                                        <div class="span_title">Stitching</div>
                                        <button class="button_explain" onclick="show_stitching()">
                                            <i class="fa">?</i>
                                        </button>
                                        <div id='div_explain_stitching'>
                                            {image_stitching_collapse}
                                        </div>
                                        <div class="content_canvas_half_div">
                                            <div class="content_margin_sub_top">
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Template Source Row No.</div>
                                                    <div class='summary_third_content_num'>{template_source_x}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Template Source Column No.</div>
                                                    <div class='summary_third_content_num'>{template_source_y}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Global Height</div>
                                                    <div class='summary_third_content_num'>{global_height}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Global Width</div>
                                                    <div class='summary_third_content_num'>{global_width}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="summary_right_part">
                                <div class="qc_canvas title_margin">
                                    <div class="sub_title">
                                        <div class="title_label"></div>
                                        <div class="span_title">QC</div>
                                        <button class="button_explain" onclick="show_qc()">
                                            <i class="fa">?</i>
                                        </button>
                                        <div id='div_explain_qc'>
                                            {image_qc_collapse}
                                        </div>
                                        <div class="content_canvas_half_div">
                                            <div class="content_margin_sub_top">
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>ImageQC Version</div>
                                                    <div class='summary_third_content_num'>{imageqc_version}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>QC Pass</div>
                                                    <div class='summary_third_content_num'>{qc_pass}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Track Line Score</div>
                                                    <div class='summary_third_content_num'>{track_line_score}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Clarity Score</div>
                                                    <div class='summary_third_content_num'>{clarity_score}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Good FOV Count</div>
                                                    <div class='summary_third_content_num'>{good_fov_count}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Total FOV Count</div>
                                                    <div class='summary_third_content_num'>{total_fov_count}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Stitching Score</div>
                                                    <div class='summary_third_content_num'>{stitching_score}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Tissue Segmentation Score</div>
                                                    <div class='summary_third_content_num'>{tissue_seg_score}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Registration Score</div>
                                                    <div class='summary_third_content_num'>{registration_score}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="registration_canvas">
                                    <div class="sub_title">
                                        <div class="title_label"></div>
                                        <div class="span_title">Registration</div>
                                        <button class="button_explain" onclick="show_registration()">
                                            <i class="fa">?</i>
                                        </button>
                                        <div id='div_explain_registration'>
                                            {image_registration_collapse}
                                        </div>
                                        <div class="content_canvas_half_div">
                                            <div class="content_margin_sub_top">
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>ScaleX</div>
                                                    <div class='summary_third_content_num'>{scaleX}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>ScaleY</div>
                                                    <div class='summary_third_content_num'>{scaleY}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Rotation</div>
                                                    <div class='summary_third_content_num'>{rotation}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Flip</div>
                                                    <div class='summary_third_content_num'>{flip}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Image X Offset</div>
                                                    <div class='summary_third_content_num'>{image_offset_x}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Image Y Offset</div>
                                                    <div class='summary_third_content_num'>{image_offset_y}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Manual ScaleX</div>
                                                    <div class='summary_third_content_num'>{manual_scale_x}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Manual ScaleY</div>
                                                    <div class='summary_third_content_num'>{manual_scale_y}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Manual Rotation</div>
                                                    <div class='summary_third_content_num'>{manual_rotation}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Counter Clockwise Rotation</div>
                                                    <div class='summary_third_content_num'>{counter_rotation}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Matrix X Offset</div>
                                                    <div class='summary_third_content_num'>{matrix_x_start}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Matrix Y Offset</div>
                                                    <div class='summary_third_content_num'>{matrix_y_start}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Matrix Height</div>
                                                    <div class='summary_third_content_num'>{matrix_height}</div>
                                                </div>
                                                <div class="middle_content_div">
                                                    <div class='summary_third_content_title'>Matrix Width</div>
                                                    <div class='summary_third_content_num'>{matrix_width}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    <div class='heatmap_plot_div'>
                        {image_heatmap_div}
                    </div>
                    </div>
                </div>

            </div>
        </div>

        <div class="footer_div">
            <div class="footer">
                <div>
                    <span>
                        {pipeline_version}
                    </span>
                </div>
                <span>
                    v2.3.0_Research
                </span>
                <div>
                    <span>
                        Contact us: <B>stereo@genomics.cn</B>
                        <span>&#169;</span> 2022 BGI Research.
                    </span>
                </div>
            </div>
        </div>
    </body>
    <script>
        // Function to zoom img with click
        function openImg(e){{
                document.getElementById("pop-img").src = e;
                var targit = document.getElementById("pop-box");
                if (targit.style.display == "none" || targit.style.display == ""){{
                    targit.style.display = "flex";
                }} else{{
                    targit.style.display = "none";
                }}
            }}

        // Function to zoom img with click big
        function openImgBig(e){{
                document.getElementById("pop-img-big").src = e;
                var targit = document.getElementById("pop-box-big");
                if (targit.style.display == "none" || targit.style.display == ""){{
                    targit.style.display = "flex";
                }} else{{
                    targit.style.display = "none";
                }}
            }}

        //tab
        var tabs = document.getElementsByClassName('tab')[0].getElementsByTagName('li'),
        contents = document.getElementsByClassName('tab_content')[0].children;


        (function changeTab(tab) {{
            for(var i = 0, len = tabs.length; i < len; i++) {{
                tabs[i].onclick = showTab;
            }}
        }})();

        function showTab() {{
            for(var i = 0, len = tabs.length; i < len; i++) {{
                
                if(tabs[i] === this) {{
                    tabs[i].className = 'tabin';
                    contents[i].className = 'show';
                }} else {{
                    tabs[i].className = '';
                    contents[i].className = 'unshow';
                }}
            }}
        }}

        //Funtion to display explain div
        function show (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_quation').style.display === 'none' || document.getElementById('div_quation').style.display === '') {{
                document.getElementById('div_quation').style.display = 'block'
            }} else {{
                document.getElementById('div_quation').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_quation').style.display = 'none'
        }}
        document.getElementById('div_quation').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to plot heatmap ssDNA
        function heatmap() {{
            var update = {{
                'marker.opacity': 1,
            }};
            Plotly.restyle(divScatter, update);
            document.getElementById('range').value = 1;
        }}

        // Function to plot Heatmap
        function ssdna() {{
            var update = {{
                'marker.opacity': 0,
            }};
            Plotly.restyle(divScatter, update);    
            document.getElementById('range').value = 0;
        }}

        image_dict = {image_dict}

        // Function to select backgroup of image 
        function imageselection(){{
            var objselect =  document.getElementById("image_select");
            var layerName = objselect.value;
            if (layerName=="no-image"){{
                var update = {{
                    'images': [],
                            }};
                Plotly.relayout(divScatter, update)
            }} else{{
                var update = {{
                    'images' : image_dict[layerName]
                }}
                Plotly.relayout(divScatter, update)
            }}
            }}

        // Function to plot cluster square bin ssDNA
        function cluster() {{
            var update = {{
                'marker.opacity': 1,
            }};
            Plotly.restyle(divCluster, update);
            document.getElementById('range_cluster').value = 1;
        }}

        // Function to plot cluster square bin
        function cluster_ssdna() {{
            var update = {{
                'marker.opacity': 0,
            }};
            Plotly.restyle(divCluster, update);    
            document.getElementById('range_cluster').value = 0;
        }}

        // Function to plot cluster square bin ssDNA
        function cell_cluster() {{
            var update = {{
                'marker.opacity': 1,
            }};
            Plotly.restyle(divCellCluster, update);
            document.getElementById('range_cell_cluster').value = 1;
        }}

        // Function to plot cluster square bin
        function cluster_cell_ssdna() {{
            var update = {{
                'marker.opacity': 0,
            }};
            Plotly.restyle(divCellCluster, update);    
            document.getElementById('range_cell_cluster').value = 0;
        }}


        // Function to show sunburst explain
        function show_sunburst (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_sunburst').style.display === 'none' || document.getElementById('div_explain_sunburst').style.display === '') {{
                document.getElementById('div_explain_sunburst').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_sunburst').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_sunburst').style.display = 'none'
        }}
        document.getElementById('div_explain_sunburst').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}
        // Function to show sunburst explain
        function show_list_element (level,event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (level==='1'){{
                if (document.getElementById('list_key1').style.display === 'none' || document.getElementById('list_key1').style.display === '') {{
                    var l1 = ['1','2','3','4','5','6','7','8','9','10','11','12'];
                    var l2 = ['1','2','3','4','5'];
                    var l3 = ['1','11','2','3','31','4','5'];
                    for(var i in l1){{
                        document.getElementById('list_key'+l1[i]).style.display = 'block'
                    }}
                    for(var i in l2){{
                        document.getElementById('list_box'+l2[i]).style.background = 'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAXUlEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpIhWyALTln+dgeHIexgPQtsIMjBM1ISw8ZrICPQFDMBNhOmESaDTeE1EVky0QhZQYBofIxDgjAxbASFnMftNUPqUAAAAAElFTkSuQmCC)'
                    }}
                    for(var i in l3){{
                        document.getElementById('sunburst_line'+l3[i]).style.display = 'block'
                    }}
                    document.getElementById('sunburst_line1').style.height='390px';
                    document.getElementById('sunburst_line2').style.height='310px';
                    document.getElementById('sunburst_line3').style.height='190px';
                    document.getElementById('sunburst_line4').style.height='110px';
                    document.getElementById('sunburst_line11').style.marginTop='465px';
                    document.getElementById('sunburst_line31').style.marginTop='345px';
                }} else {{
                    var l1 = ['1','2','3','4','5','6','7','8','9','10','11','12'];
                    var l3 = ['1','11','2','3','31','4','5'];
                    for(var i in l1){{
                        document.getElementById('list_key'+l1[i]).style.display = 'none'
                    }}
                    for(var i in l3){{
                        document.getElementById('sunburst_line'+l3[i]).style.display = 'none'
                    }}
                    document.getElementById('list_box1').style.background = 'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAFVJREFUKFNjNDr6/zADA4MNA35whNHo6P//Z63wqzI+xsCAoTD5CkTTXB2EZqwKQYIggGwLikKQSRc+oTrBgA9iMnkKYWYRtBqmkGjPYAsomBuJCnAAiTo/JajQ0FgAAAAASUVORK5CYII=)'
            }}
            }}else if (level==='2'){{
                if (document.getElementById('list_key2').style.display === 'none' || document.getElementById('list_key1').style.display === '') {{
                    var l1 = ['2','3','4','5','6','7','8','9','10'];
                    var l2 = ['1','2','3','4','5'];
                    var l3 = ['1','11','2','3','31','4','5'];
                    for(var i in l1){{
                        document.getElementById('list_key'+l1[i]).style.display = 'block'
                    }}
                    for(var i in l2){{
                        document.getElementById('list_box'+l2[i]).style.background = 'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAXUlEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpIhWyALTln+dgeHIexgPQtsIMjBM1ISw8ZrICPQFDMBNhOmESaDTeE1EVky0QhZQYBofIxDgjAxbASFnMftNUPqUAAAAAElFTkSuQmCC)'
                    }}
                    for(var i in l3){{
                        document.getElementById('sunburst_line'+l3[i]).style.display = 'block'
                    }}
                    document.getElementById('sunburst_line1').style.height='390px';
                    document.getElementById('sunburst_line2').style.height='310px';
                    document.getElementById('sunburst_line3').style.height='190px';
                    document.getElementById('sunburst_line4').style.height='110px';
                    document.getElementById('sunburst_line11').style.marginTop='465px';
                    document.getElementById('sunburst_line31').style.marginTop='345px';
                }} else {{
                    var l1 = ['2','3','4','5','6','7','8','9','10'];
                    var l3 = ['2','3','31','4','5'];
                    for(var i in l1){{
                        document.getElementById('list_key'+l1[i]).style.display = 'none'
                    }}
                    for(var i in l3){{
                        document.getElementById('sunburst_line'+l3[i]).style.display = 'none'
                    }}
                    document.getElementById('sunburst_line1').style.height='30px';
                    document.getElementById('sunburst_line11').style.marginTop='105px';
                    document.getElementById('list_box2').style.background = 'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAFVJREFUKFNjNDr6/zADA4MNA35whNHo6P//Z63wqzI+xsCAoTD5CkTTXB2EZqwKQYIggGwLikKQSRc+oTrBgA9iMnkKYWYRtBqmkGjPYAsomBuJCnAAiTo/JajQ0FgAAAAASUVORK5CYII=)'
            }}
            }}else if (level==='3'){{
                if (document.getElementById('list_key3').style.display === 'none' || document.getElementById('list_key1').style.display === '') {{
                    var l1 = ['3','4','5','6','7','8','9'];
                    var l2 = ['3','4','5'];
                    var l3 = ['1','11','2','3','31','4','5'];
                    for(var i in l1){{
                        document.getElementById('list_key'+l1[i]).style.display = 'block'
                    }}
                    for(var i in l2){{
                        document.getElementById('list_box'+l2[i]).style.background = 'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAXUlEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpIhWyALTln+dgeHIexgPQtsIMjBM1ISw8ZrICPQFDMBNhOmESaDTeE1EVky0QhZQYBofIxDgjAxbASFnMftNUPqUAAAAAElFTkSuQmCC)'
                    }}
                    for(var i in l3){{
                        document.getElementById('sunburst_line'+l3[i]).style.display = 'block'
                    }}
                    document.getElementById('sunburst_line1').style.height='390px';
                    document.getElementById('sunburst_line2').style.height='310px';
                    document.getElementById('sunburst_line3').style.height='190px';
                    document.getElementById('sunburst_line4').style.height='110px';
                    document.getElementById('sunburst_line11').style.marginTop='465px';
                    document.getElementById('sunburst_line31').style.marginTop='345px';
                }} else {{
                    var l1 = ['3','4','5','6','7','8','9'];
                    var l3 = ['3','31','4','5'];
                    for(var i in l1){{
                        document.getElementById('list_key'+l1[i]).style.display = 'none'
                    }}
                    for(var i in l3){{
                        document.getElementById('sunburst_line'+l3[i]).style.display = 'none'
                    }}
                    document.getElementById('sunburst_line2').style.height='30px';
                    document.getElementById('sunburst_line1').style.height='110px';
                    document.getElementById('sunburst_line11').style.marginTop='185px';
                    document.getElementById('list_box3').style.background = 'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAFVJREFUKFNjNDr6/zADA4MNA35whNHo6P//Z63wqzI+xsCAoTD5CkTTXB2EZqwKQYIggGwLikKQSRc+oTrBgA9iMnkKYWYRtBqmkGjPYAsomBuJCnAAiTo/JajQ0FgAAAAASUVORK5CYII=)'
            }}
            }}else if (level==='4'){{
                if (document.getElementById('list_key4').style.display === 'none' || document.getElementById('list_key1').style.display === '') {{
                    var l1 = ['4','5','6','7'];
                    var l2 = ['4','5'];
                    var l3 = ['1','11','2','3','31','4','5'];
                    for(var i in l1){{
                        document.getElementById('list_key'+l1[i]).style.display = 'block'
                    }}
                    for(var i in l2){{
                        document.getElementById('list_box'+l2[i]).style.background = 'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAXUlEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpIhWyALTln+dgeHIexgPQtsIMjBM1ISw8ZrICPQFDMBNhOmESaDTeE1EVky0QhZQYBofIxDgjAxbASFnMftNUPqUAAAAAElFTkSuQmCC)'
                    }}
                    for(var i in l3){{
                        document.getElementById('sunburst_line'+l3[i]).style.display = 'block'
                    }}
                    document.getElementById('sunburst_line1').style.height='390px';
                    document.getElementById('sunburst_line2').style.height='310px';
                    document.getElementById('sunburst_line3').style.height='190px';
                    document.getElementById('sunburst_line4').style.height='110px';
                    document.getElementById('sunburst_line11').style.marginTop='465px';
                    document.getElementById('sunburst_line31').style.marginTop='345px';
                }} else {{
                    var l1 = ['4','5','6','7'];
                    var l3 = ['4','5'];
                    for(var i in l1){{
                        document.getElementById('list_key'+l1[i]).style.display = 'none'
                    }}
                    for(var i in l3){{
                        document.getElementById('sunburst_line'+l3[i]).style.display = 'none'
                    }}
                    document.getElementById('sunburst_line1').style.height='230px';
                    document.getElementById('sunburst_line2').style.height='150px';
                    document.getElementById('sunburst_line3').style.height='30px';
                    document.getElementById('sunburst_line11').style.marginTop='305px';
                    document.getElementById('sunburst_line31').style.marginTop='185px';
                    document.getElementById('list_box4').style.background = 'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAFVJREFUKFNjNDr6/zADA4MNA35whNHo6P//Z63wqzI+xsCAoTD5CkTTXB2EZqwKQYIggGwLikKQSRc+oTrBgA9iMnkKYWYRtBqmkGjPYAsomBuJCnAAiTo/JajQ0FgAAAAASUVORK5CYII=)'
            }}
            }}else if (level==='5'){{
                if (document.getElementById('list_key5').style.display === 'none' || document.getElementById('list_key1').style.display === '') {{
                    var l1 = ['5','6'];
                    var l3 = ['1','11','2','3','31','4','5'];
                    for(var i in l1){{
                        document.getElementById('list_key'+l1[i]).style.display = 'block'
                    }}
                    for(var i in l3){{
                        document.getElementById('sunburst_line'+l3[i]).style.display = 'block'
                    }}
                    document.getElementById('list_box5').style.background = 'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAACqADAAQAAAABAAAACgAAAAA7eLj1AAAAXUlEQVQYGWM0Pvp/638GBi8GPICRgWEbg9HR/wQBSA0THoNQpIhWyALTln+dgeHIexgPQtsIMjBM1ISw8ZrICPQFDMBNhOmESaDTeE1EVky0QhZQYBofIxDgjAxbASFnMftNUPqUAAAAAElFTkSuQmCC)'
                    document.getElementById('sunburst_line1').style.height='390px';
                    document.getElementById('sunburst_line2').style.height='310px';
                    document.getElementById('sunburst_line3').style.height='190px';
                    document.getElementById('sunburst_line4').style.height='110px';
                    document.getElementById('sunburst_line11').style.marginTop='465px';
                    document.getElementById('sunburst_line31').style.marginTop='345px';
                }} else {{
                    var l1 = ['5','6'];
                    for(var i in l1){{
                        document.getElementById('list_key'+l1[i]).style.display = 'none'
                    }}
                    document.getElementById('sunburst_line1').style.height='310px';
                    document.getElementById('sunburst_line2').style.height='230px';
                    document.getElementById('sunburst_line3').style.height='110px';
                    document.getElementById('sunburst_line11').style.marginTop='385px';
                    document.getElementById('sunburst_line31').style.marginTop='265px';
                    document.getElementById('sunburst_line4').style.height = '30px'
                    document.getElementById('sunburst_line5').style.display = 'none'
                    document.getElementById('list_box5').style.background = 'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAFVJREFUKFNjNDr6/zADA4MNA35whNHo6P//Z63wqzI+xsCAoTD5CkTTXB2EZqwKQYIggGwLikKQSRc+oTrBgA9iMnkKYWYRtBqmkGjPYAsomBuJCnAAiTo/JajQ0FgAAAAASUVORK5CYII=)'
            }}
            }}
        }}
        // document.onclick = function () {{
        //     document.getElementById('list_key1').style.display = 'none'
        // }}
        // document.getElementById('list_key1').onclick = function (event) {{
        //     let oevent = event || window.event
        //     oevent.stopPropagation()
        // }}
        

        // Function to show sequencing saturation explain
        function show_sequencing_saturation (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_sequencing_saturation').style.display === 'none' || document.getElementById('div_explain_sequencing_saturation').style.display === '') {{
                document.getElementById('div_explain_sequencing_saturation').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_sequencing_saturation').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_sequencing_saturation').style.display = 'none'
        }}
        document.getElementById('div_explain_sequencing_saturation').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show sequencing saturation explain
        function show_sequencing (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_sequencing').style.display === 'none' || document.getElementById('div_explain_sequencing').style.display === '') {{
                document.getElementById('div_explain_sequencing').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_sequencing').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_sequencing').style.display = 'none'
        }}
        document.getElementById('div_explain_sequencing').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show rna mapping explain
        function show_rna_mapping (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_rna_mapping').style.display === 'none' || document.getElementById('div_explain_rna_mapping').style.display === '') {{
                document.getElementById('div_explain_rna_mapping').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_rna_mapping').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_rna_mapping').style.display = 'none'
        }}
        document.getElementById('div_explain_rna_mapping').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show tissueCut explain
        function show_tissueCut (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_tissueCut').style.display === 'none' || document.getElementById('div_explain_tissueCut').style.display === '') {{
                document.getElementById('div_explain_tissueCut').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_tissueCut').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_tissueCut').style.display = 'none'
        }}
        document.getElementById('div_explain_tissueCut').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show filtering explain
        function show_filtering (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_filtering').style.display === 'none' || document.getElementById('div_explain_filtering').style.display === '') {{
                document.getElementById('div_explain_filtering').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_filtering').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_filtering').style.display = 'none'
        }}
        document.getElementById('div_explain_filtering').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show annotation explain
        function show_annotation (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_annotation').style.display === 'none' || document.getElementById('div_explain_annotation').style.display === '') {{
                document.getElementById('div_explain_annotation').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_annotation').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_annotation').style.display = 'none'
        }}
        document.getElementById('div_explain_annotation').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show square bin statistics
        function show_square_bin_statistics (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_square_bin_statistics').style.display === 'none' || document.getElementById('div_explain_square_bin_statistics').style.display === '') {{
                document.getElementById('div_explain_square_bin_statistics').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_square_bin_statistics').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_square_bin_statistics').style.display = 'none'
        }}
        document.getElementById('div_explain_square_bin_statistics').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show bin 1
        function show_bin1 (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_bin1').style.display === 'none' || document.getElementById('div_explain_bin1').style.display === '') {{
                document.getElementById('div_explain_bin1').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_bin1').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_bin1').style.display = 'none'
        }}
        document.getElementById('div_explain_bin1').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show bin 50
        function show_bin50 (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_bin50').style.display === 'none' || document.getElementById('div_explain_bin50').style.display === '') {{
                document.getElementById('div_explain_bin50').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_bin50').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_bin50').style.display = 'none'
        }}
        document.getElementById('div_explain_bin50').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show bin 100
        function show_bin100 (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_bin100').style.display === 'none' || document.getElementById('div_explain_bin100').style.display === '') {{
                document.getElementById('div_explain_bin100').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_bin100').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_bin100').style.display = 'none'
        }}
        document.getElementById('div_explain_bin100').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show bin 150
        function show_bin150 (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_bin150').style.display === 'none' || document.getElementById('div_explain_bin150').style.display === '') {{
                document.getElementById('div_explain_bin150').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_bin150').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_bin150').style.display = 'none'
        }}
        document.getElementById('div_explain_bin150').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show bin 200
        function show_bin200 (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_bin200').style.display === 'none' || document.getElementById('div_explain_bin200').style.display === '') {{
                document.getElementById('div_explain_bin200').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_bin200').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_bin200').style.display = 'none'
        }}
        document.getElementById('div_explain_bin200').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show clustering square bin
        function show_clustering_square_bin (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_clustering_square_bin').style.display === 'none' || document.getElementById('div_explain_clustering_square_bin').style.display === '') {{
                document.getElementById('div_explain_clustering_square_bin').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_clustering_square_bin').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_clustering_square_bin').style.display = 'none'
        }}
        document.getElementById('div_explain_clustering_square_bin').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show cell bin
        function show_cellBin (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_cellBin').style.display === 'none' || document.getElementById('div_explain_cellBin').style.display === '') {{
                document.getElementById('div_explain_cellBin').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_cellBin').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_cellBin').style.display = 'none'
        }}
        document.getElementById('div_explain_cellBin').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show cell bin stats
        function show_cell_bin_stats (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_cell_bin_stats').style.display === 'none' || document.getElementById('div_explain_cell_bin_stats').style.display === '') {{
                document.getElementById('div_explain_cell_bin_stats').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_cell_bin_stats').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_cell_bin_stats').style.display = 'none'
        }}
        document.getElementById('div_explain_cell_bin_stats').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show cell bin clustering
        function show_cellBin_clustering (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_cellBin_clustering').style.display === 'none' || document.getElementById('div_explain_cellBin_clustering').style.display === '') {{
                document.getElementById('div_explain_cellBin_clustering').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_cellBin_clustering').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_cellBin_clustering').style.display = 'none'
        }}
        document.getElementById('div_explain_cellBin_clustering').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show image stitching
        function show_stitching (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_stitching').style.display === 'none' || document.getElementById('div_explain_stitching').style.display === '') {{
                document.getElementById('div_explain_stitching').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_stitching').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_stitching').style.display = 'none'
        }}
        document.getElementById('div_explain_stitching').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show image qc
        function show_qc (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_qc').style.display === 'none' || document.getElementById('div_explain_qc').style.display === '') {{
                document.getElementById('div_explain_qc').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_qc').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_qc').style.display = 'none'
        }}
        document.getElementById('div_explain_qc').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show image registration
        function show_registration (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_registration').style.display === 'none' || document.getElementById('div_explain_registration').style.display === '') {{
                document.getElementById('div_explain_registration').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_registration').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_registration').style.display = 'none'
        }}
        document.getElementById('div_explain_registration').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show image middle
        function show_image_middle (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_image_middle').style.display === 'none' || document.getElementById('div_explain_image_middle').style.display === '') {{
                document.getElementById('div_explain_image_middle').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_image_middle').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_image_middle').style.display = 'none'
        }}
        document.getElementById('div_explain_image_middle').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show image heatmap left
        function show_image_left (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_image_left').style.display === 'none' || document.getElementById('div_explain_image_left').style.display === '') {{
                document.getElementById('div_explain_image_left').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_image_left').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_image_left').style.display = 'none'
        }}
        document.getElementById('div_explain_image_left').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}

        // Function to show image heatmap right
        function show_image_right (event) {{
            let oevent = event || window.event
            if (document.all) {{
                oevent.cancelBubble = true
            }} else {{
                oevent.stopPropagation()
            }}
            if (document.getElementById('div_explain_image_right').style.display === 'none' || document.getElementById('div_explain_image_right').style.display === '') {{
                document.getElementById('div_explain_image_right').style.display = 'block'
            }} else {{
                document.getElementById('div_explain_image_right').style.display = 'none'
            }}
        }}
        document.onclick = function () {{
            document.getElementById('div_explain_image_right').style.display = 'none'
        }}
        document.getElementById('div_explain_image_right').onclick = function (event) {{
            let oevent = event || window.event
            oevent.stopPropagation()
        }}
        
        
    </script>
</html>
"""