""" CirGO 
    Version 1.0 01/03/2018
    
    CirGO (Circular Gene Ontologies) is an alternative way of visualizing GO terms in 2D space 
    that is suitable for publishing and presenting gene expression ontologies data.

    Copyright (C) 2018 Irina Kuznetsova
    This software is licensed under the terms of the GNU general public license (version 3).
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
    If you are using the softwareas a part of your research work, please cite the following publication
    
    Conract info:   irina.kuznetsova@uwa.edu.au 
    GitHub:         https://github.com/KIVMito/CirGO.git 
"""


##----------------------------------------------------------------------------------------------------
## 1. Import required modules
## ----------------------------------------------------------------------------------------------------
import os
import argparse
import numpy as np                     
import matplotlib as mpl
#mpl.use("TkAgg")       #  MacOS so it sees Py as a framework
from matplotlib import pyplot as plt
from collections import OrderedDict   
from argparse import RawTextHelpFormatter


## ----------------------------------------------------------------------------------------------------
## 2. Functions, a)- Calculates color gradient; b)- Prepares parameters required for Visualization
## ----------------------------------------------------------------------------------------------------
def ColorGradient(gradient_range, hex_rgb):
    convert_hexrgb_to_rgba = mpl.colors.to_rgba(hex_rgb)
    color_val_list = []
    input_color = convert_hexrgb_to_rgba[3]
    find_delta_color = input_color / gradient_range
    for gradient_ind in range(gradient_range):
        update_value = (gradient_ind + 1) * find_delta_color
        gradient_color = (convert_hexrgb_to_rgba[0], convert_hexrgb_to_rgba[1], convert_hexrgb_to_rgba[2], update_value)
        color_val_list.append(gradient_color)
    return color_val_list


def SubsetSortedSelectedCateg(indexes, column, num_of_categories):
    """ Subset input data to a number of selected categories. """
    selected_categ = np.asarray([column[b1] for b1 in indexes][::-1][0:num_of_categories])
    return selected_categ
   
 
def SubsetSortedResidualCateg(column, num_of_categories, sorted_indices): 
    """Subset input data to a number of residual categories.  """
    residual_categ = [column[a1] for a1 in sorted_indices][::-1][num_of_categories:]
    return residual_categ


def ResidualCategAnnotatedAsAdditional(unique_parent_records_residual_datste, residual_categories_dataset):
    """ Use ResidualCategories dataset and sum-up all SliceSize values that belong to the same
    ParentRecord, and assign AdditionalCategories annotation to the ChildRecord """
    
    # 1.1.1 Obtain abs(log10pval) values for Residual Categories. 
    # Save values as nested list where each list contains "slice size" values for related parent records
    num_val_not_incl_categ = []  
    for val0 in range(0, len(unique_parent_records_residual_datste)):
        unq_process = unique_parent_records_residual_datste[val0]
        tem = []
        num_val_not_incl_categ.append(tem)
        for val1 in range(0, len(residual_categories_dataset)): 
            tuple_one = residual_categories_dataset[val1]
            if unq_process == tuple_one[2]:  
                process_value = tuple_one[1]
                tem.append(float(process_value))
                
    # 1.1.2 Sum-up numeric values obtained at 1.7.1, and assign 'additional categories' annotation.           
    sum_num_val_not_incl_categ = []   
    for numeric_values in num_val_not_incl_categ:
        sum_num_val_not_incl_categ.append(["additional categories", str(sum(numeric_values))])
        
    # 1.1.3 Create a list which holds (category name, sumup values, inner ring info) for not included in selected number of categories.
    not_includ_categor_temp = zip(sum_num_val_not_incl_categ, unique_parent_records_residual_datste)     
    not_incl_categ_final_summed_process = []        
    for lis in not_includ_categor_temp:
        not_incl_categ_final_summed_process.append((lis[0][0], str(lis[0][1]), lis[1]))   
    return not_incl_categ_final_summed_process


def SelectedCategoriesIncludeAdditionalCategValues(unique_process_list, not_incl_categ_final_summed_process, data_lim_to_num_categ):

    """ Use "Selected Categories" dataset to extract matching "parent records" between list of unique parent records (or inner ring) and 
     data where "child records" as annotated  as "additional categories".  """
    
    # 1.1.1 Find which ParentRecords in the dataset annotated as the AdditionalCategories match 
    # to the unique ParentRecords in the SelectedCategories subset.
    not_includ_categ_narrowed_to_inner_info = []
    for inner_porcess in unique_process_list:
        for row1 in range(0, len(not_incl_categ_final_summed_process)):
            if inner_porcess == not_incl_categ_final_summed_process[row1][2]:
                not_includ_categ_narrowed_to_inner_info.append(not_incl_categ_final_summed_process[row1])
                
    # 1.1.2 Obtain ChildRecords categories and related ParentRecords for SelectedCategories 
    # dataset that will represent outer ring.
    child_categ_outer_ring = []      
    for numeric_inf in range(0, len(unique_process_list)):
        temp = []
        for indices in range(0, len(data_lim_to_num_categ)):    
            hold_info = data_lim_to_num_categ[indices]
            if hold_info[2] == unique_process_list[numeric_inf]:
                temp.append(data_lim_to_num_categ[indices].tolist())
        child_categ_outer_ring.append(sorted(temp, key=lambda x: float(x[1])))
        
    # 1.1.3. Add AdditionalCategories info such as child record, value, parent record to 
    # outer ring info based on related ParentRecord 
    add_addit_categ_to_outer_ring = []
    for ind_item_first in range(0, len(not_includ_categ_narrowed_to_inner_info)):    
        full_outer_ring_info_temp = list([not_includ_categ_narrowed_to_inner_info[ind_item_first]])
        for ind_item_second in range(0, len(child_categ_outer_ring)):
            if child_categ_outer_ring[ind_item_second][0][2] == not_includ_categ_narrowed_to_inner_info[ind_item_first][2]:
                full_outer_ring_info_temp.append(child_categ_outer_ring[ind_item_second])
            else:
                pass
        add_addit_categ_to_outer_ring.append(full_outer_ring_info_temp)
    return not_includ_categ_narrowed_to_inner_info,  child_categ_outer_ring, add_addit_categ_to_outer_ring



# 1.4 Generate dataset  that contains all categories that will be plotted for the outer ring
def OuterRingCompleteInfo(not_includ_categ_narrowed_to_inner_info, child_categ_outer_ring, add_addit_categ_to_outer_ring):
    """ Generate dataset  that contains all categories that will be plotted for the outer ring. """
    # 1.1.1 Find indexes
    indices_to_remove = []        
    for ind, val in enumerate(child_categ_outer_ring):
        for others in range(0, len(not_includ_categ_narrowed_to_inner_info)):
            if not_includ_categ_narrowed_to_inner_info[others][2] in val[0][2]:
                indices_to_remove.append(ind)
    
    # 1.1.2 Exclude AdditionalCategories that ParentRecord matches to the ParentRecord of the inner ring             
    addit_categ_excluded = [i for j, i in enumerate(child_categ_outer_ring) if j not in indices_to_remove]
        
    # 1.1.3 Add AdditionalCategories information to the outer ring dataset based on related ParentRecord.
    whole_info = add_addit_categ_to_outer_ring + addit_categ_excluded   
    return whole_info


def DataInfoForVisualization(outer_ring_complete_data):
    """ Obtain information such as Child Records, Slice Size, Parent Records for plotting. """
    # 1.1.1. Obtain labels, p-values information. 
    outer_ring_categor_flatten = []   
    outer_ring_categor_nested = []
    pval_slice_size_flatten = []      
    pval_slice_size_nested = []
    inner_ring_categor = []           
    for iter_val in outer_ring_complete_data:
        temp_lab_a = []
        temp_val_a = []
        temp_inner_a = []
        if len(iter_val) == 2 and iter_val[0][0] == "additional categories":               
            temp_lab_a.append(iter_val[0][0])   
            temp_val_a.append(float(iter_val[0][1]))
            temp_inner_a.append(iter_val[0][2])
            for iter_val2 in range(0, len(iter_val[1])):    
                temp_lab_a.append(iter_val[1][iter_val2][0])
                temp_val_a.append(float(iter_val[1][iter_val2][1]))
                temp_inner_a.append(iter_val[1][iter_val2][2])
        else:      
            for iter_val3 in iter_val:
                temp_lab_a.append(iter_val3[0])
                temp_val_a.append(float(iter_val3[1]))
                temp_inner_a.append(iter_val3[2])
        [outer_ring_categor_flatten.append(item1) for item1 in temp_lab_a]      
        outer_ring_categor_nested.append(temp_lab_a)
        [pval_slice_size_flatten.append(item2) for item2 in temp_val_a]         
        pval_slice_size_nested.append(temp_val_a)
        [inner_ring_categor.append(item3) for item3 in temp_inner_a if item3 not in inner_ring_categor]    

    # 1.1.2 Expand with zeros misiing info to build up arrays to the same length
    categories_freq = []                        
    for coord in range(0, len(outer_ring_categor_nested)):
        categories_freq.append(len(outer_ring_categor_nested[coord]))
    largest_row_len = max(categories_freq)     
    
    expanded_outer_labels = []
    for inner_list in outer_ring_categor_nested:
        if len(inner_list) < largest_row_len:
            expanded_to_largest_row_len = inner_list + [""] * (largest_row_len-len(inner_list))   
            expanded_outer_labels.append(expanded_to_largest_row_len)
        else:
            expanded_outer_labels.append(inner_list)
    
    expand_outer_pvalue = []
    for inner_list2 in pval_slice_size_nested:
        if len(inner_list2) < largest_row_len:
            expanded_to_largest_row_len2 = inner_list2 + [0] * (largest_row_len-len(inner_list2))   
            expand_outer_pvalue.append(expanded_to_largest_row_len2)
        else:
            expand_outer_pvalue.append(inner_list2)
    return pval_slice_size_nested, inner_ring_categor, expanded_outer_labels, expand_outer_pvalue, largest_row_len
    

## ----------------------------------------------------------------------------------------------------
## 3. Visualize
## ----------------------------------------------------------------------------------------------------

def CircularVisualGO(infile, num_of_categories, font_size, legend_name, outfile):
## ----------------------------------------------------------------------------------------------------
## 1. Parameters calculation part
## ----------------------------------------------------------------------------------------------------
    # 1.0 Parse file
    dataa =  np.genfromtxt(fname = infile, 
                               dtype = None, 
                               skip_header =1,
                               delimiter = "\t")
        
    # 1.1. Sort data from Largest to Smallest.  Initialize a number of categorise.   
    second_col = []
    first_col = []
    third_col = []
    for d in dataa:
        second_col.append(d[1])
        first_col.append(d[0])
        third_col.append(d[2])

    sorted_indices = sorted(range(len(second_col)), key=lambda k: second_col[k])        
      
    # 1.2 Combine into one | Selected categories     
    sorted_second_col = SubsetSortedSelectedCateg(sorted_indices, second_col, num_of_categories)
    sorted_first_col = SubsetSortedSelectedCateg(sorted_indices, first_col, num_of_categories)
    sorted_third_col = SubsetSortedSelectedCateg(sorted_indices, third_col, num_of_categories)
    data_lim_to_num_categ = np.dstack((sorted_first_col, sorted_second_col, sorted_third_col))[0] 
           
    # 1.3 Combine into one | Residual categories 
    first_col_not_included_categ = SubsetSortedResidualCateg(first_col, num_of_categories, sorted_indices)
    second_col_not_included_categ = SubsetSortedResidualCateg(second_col, num_of_categories, sorted_indices)
    third_col_not_included_categ = SubsetSortedResidualCateg(third_col, num_of_categories, sorted_indices)
    data_categ_not_included = np.dstack((first_col_not_included_categ, second_col_not_included_categ, third_col_not_included_categ))[0]   
  
    # 1.4 Obtain unique categories of the 3rd column that represents parent records or inner ring.  
    uniq_val, unique_ind = np.unique(sorted_third_col, return_index = True)      
    unique_process_list = sorted_third_col[np.sort(unique_ind)].tolist()       
   
    # 1.5 Obtain unique categories of the 3rd column for Residual Categories subset.
    uniq_proc_not_in_selected_categ = list(OrderedDict.fromkeys(third_col_not_included_categ))     
   
    # 1.6 Use Residual Categories dataset and sum-up all Slice Size values that belong to the same
    #    Parent Record, and assign Additional Categories annotation to the Child Record
    not_incl_categ_final_summed_process = ResidualCategAnnotatedAsAdditional(uniq_proc_not_in_selected_categ, data_categ_not_included)
        
    # 1.7 Use Selected Categories dataset to extract matching Parent Records between list of unique parent records (or inner ring) 
    # and data where  Child Records are annotated as Additional Categories. 
    not_includ_categ_narrowed_to_inner_info = SelectedCategoriesIncludeAdditionalCategValues(unique_process_list, not_incl_categ_final_summed_process, data_lim_to_num_categ)[0]
    child_categ_outer_ring = SelectedCategoriesIncludeAdditionalCategValues(unique_process_list, not_incl_categ_final_summed_process, data_lim_to_num_categ)[1]
    add_addit_categ_to_outer_ring = SelectedCategoriesIncludeAdditionalCategValues(unique_process_list, not_incl_categ_final_summed_process, data_lim_to_num_categ)[2]
    
    # 1.8 Generate dataset  that contains all categories that will be plotted for the outer ring
    outer_ring_complete_data = OuterRingCompleteInfo(not_includ_categ_narrowed_to_inner_info, child_categ_outer_ring, add_addit_categ_to_outer_ring)
             
    # 1.9 Obtain information such as Child Records, Slice size, Parent Records for plotting.
    visual_info = DataInfoForVisualization(outer_ring_complete_data)
    
    
    ind = sorted(range(len(visual_info[0])), key = lambda k: [sum(one_category) for one_category in visual_info[0]][k])
    inner = [visual_info[1][x] for x in ind]
    outer_lab = [visual_info[2][x] for x in ind]
    outer_val =  [visual_info[3][x] for x in ind]
    
    
    ## ----------------------------------------------------------------------------------------------------
    ## 2.Visualization part 
    ## ----------------------------------------------------------------------------------------------------
    # 2.0 Initialize a list of hex colors
    required_color_list = ["#7FFFD4", "#FF1493", "#00BFFF", "#FF7F50", "#FFFF00", "#9ACD32",
                           "#CD3333", "#00FFFF", "#B8860B", "#F5DEB3", "#FF00FF", "#00FF00",
                           "#FFB6C1", "#2E8B57", "#9FB6CD", "#DA70D6", "#FF4500", "#4169E1",
                           "#7FFFD4", "#FF1493", "#00BFFF", "#FF7F50", "#FFFF00", "#9ACD32",
                           "#CD3333", "#00FFFF", "#B8860B", "#F5DEB3", "#FF00FF", "#00FF00", 
                           "#FFB6C1", "#2E8B57", "#9FB6CD", "#DA70D6", "#FF4500", "#4169E1",
                           "#7FFFD4", "#FF1493", "#00BFFF", "#FF7F50", "#FFFF00", "#9ACD32",
                           "#CD3333", "#00FFFF", "#B8860B", "#F5DEB3", "#FF00FF", "#00FF00", 
                           "#FFB6C1", "#2E8B57", "#9FB6CD", "#DA70D6", "#FF4500", "#4169E1",
                           "#7FFFD4", "#FF1493", "#00BFFF", "#FF7F50", "#FFFF00", "#9ACD32",
                           "#CD3333", "#00FFFF", "#B8860B", "#F5DEB3", "#FF00FF", "#00FF00", 
                           "#FFB6C1", "#2E8B57", "#9FB6CD", "#DA70D6", "#FF4500", "#4169E1"]  
    largest_row_len = visual_info[4]                       
    gradient_num = 2 * largest_row_len 
    
    
    # 2.1 Calculate and assign colors for inner and outer ring.
    outer_ring_colors = []
    for color_string in required_color_list[0 : len(outer_val)]:
        outer_ring_colors.append(ColorGradient(gradient_num, color_string)[largest_row_len: gradient_num])   
    
    freq_not_zero_values = []  
    for nested_list in np.array(outer_val):
        freq_not_zero_values.append(sum(not_zero_value > 0 for not_zero_value in nested_list))
    
    out_ring_color_distrub = []
    for color_ind in range(0, len(np.array(outer_ring_colors))):    
        freq_val = freq_not_zero_values[color_ind]                         
        if freq_val == 1:
            out_ring_color_distrub.append(outer_ring_colors[color_ind][ ::-1])       
        else:
            out_ring_color_distrub.append(outer_ring_colors[color_ind][-freq_val : ] + outer_ring_colors[color_ind][0 : (len(outer_ring_colors[color_ind]) -freq_val)])
    
    outer_concat_color = np.concatenate(np.array(out_ring_color_distrub))
    inner_concat_inner = np.array(required_color_list)
    
    
    # 2.2 Calculate wedges information in percent
    # Note: this information can be extracted only if we create dummy plot.
    fig, ax = plt.subplots()  
    v = ax.pie(np.array(outer_val).sum(axis = 1), 
               radius = 0.8,
               autopct = "%1.2f%%") 
    percent_dummy = v[2]
    plt.close()  # get rid of dummy image
    
    
    # 2.3. Initialize plotting parameters.
    mpl.rcParams["font.size"] = font_size
    mpl.rcParams["font.sans-serif"] = "Arial"    
    fig, ax = plt.subplots()     
    
    ax.axis("equal")          
    pie_chart_percent = []  
    for perc_info in percent_dummy:
        pie_chart_percent.append(float(str(perc_info.get_text())[:-1])) 
    
    # 2.3.0 Outer ring plotting
    patches, texts = ax.pie(np.array(outer_val).flatten(), 
                            radius = 0.8,     
                            labels = np.array(outer_lab).flatten(), 
                            colors = outer_concat_color, 
                            labeldistance = 1.1,
                            startangle = 90,   
                            frame = True, 
                            rotatelabels = True,
                            wedgeprops = {"linewidth": 0.1, 
                                          "edgecolor": "black"})        
    
    # 2.3.1 Obtain supporting infomation such as prefix "GO" for inner ring
    inner_ring_percent_labels = []
    legend_labeling = []
    set_percent_threshold = 3 # This wedge size value plays a threshold role that 
                              # limits prifix plotting on small size wedges  
    n = len([1 for i in pie_chart_percent if i >= set_percent_threshold])      
    m = n
    for num in range(0, len(pie_chart_percent)):
        if pie_chart_percent[num] >= set_percent_threshold:
            inner_ring_percent_labels.append("GO" + str(m))
            addGO = "GO" + str(m) + " " + inner[num]
            legend_labeling.append(addGO)
            m = m - 1
        else:
            inner_ring_percent_labels.append("")
            legend_labeling.append(inner[num])
            n = n + 1 
    
    # 2.3.2 Inner ring plotting
    p_inner, p_text = ax.pie(np.array(outer_val).sum(axis = 1), 
                             radius = 0.8 -.1, 
                             labels = inner_ring_percent_labels, 
                             labeldistance = 0.70, 
                             rotatelabels = True,
                             colors = inner_concat_inner, 
                             startangle = 90,
                             wedgeprops = {"linewidth": 0.1, 
                                           "edgecolor": "black"})
        
    # 2.3.3 Initialize parameters for legend
    plt.rcParams["svg.fonttype"] = "none"    
    plt.rcParams["xtick.top"] = True 
    font = {"family" : "Arial", 
            "size": font_size}
    
    mpl.rc("font", **font)   
    plt.legend(p_inner[ ::-1], 
               ["%s, %1.1f%%" % (l, s) for l, s in zip(np.array(legend_labeling), pie_chart_percent )[ ::-1]],      
               ncol = 1,
               loc = "upper left", 
               bbox_to_anchor = (1.25, 1.25),   
               frameon = False, 
               prop = {"size": font_size },   
               title = legend_name,
               bbox_transform = plt.gcf().transFigure)
    
    # 2.4 Save created image 
    plt.savefig(outfile, 
                format = "svg", 
                bbox_inches = "tight", 
                dpi = 1200)
    plt.show()



## ----------------------------------------------------------------------------------------------------
## 4. Version control
## ----------------------------------------------------------------------------------------------------
## 4.0. Python version
## import sys
##  print (sys.version)     # 2.7.13 |Continuum Analytics, Inc.| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)]

## 4.1. Python modules version
## np.__version__       # 1.13.1
## mpl.__version__      # 2.1.0

