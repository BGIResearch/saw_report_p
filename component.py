bin_canvas="""
                        <div class="bin{bin_size}_canvas">
                            <div class="sub_title">
                                <div class="title_label"></div>
                                <div class="span_title">Bin {bin_size}</div>
                                <button class="button_explain" onclick="show_bin{bin_size}()">
                                    <i class="fa">?</i>
                                </button>
                                <div id='div_explain_bin50'>
                                    <div>(left) Scatter plot of MID count and gene number in each bin</div>
                                    <div>(right) Violin plots show the distribution of deduplicated MID count and gene number in each bin</div>
                                    <div>(bottom) Univariate distribution of MID count, gene numbers, and DNB numbers with rug along the x axis</div>
                                </div>
                                <div class="content_canvas_div">
                                    {saturation_plot}
                                    {violin_plot}
                                    {MIDGeneDNB_plot}
                                </div>
                            </div>
                        </div>
                        
"""