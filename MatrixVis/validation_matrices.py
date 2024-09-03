import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

 
Add_file = open(r"input1_organisms_media_secretion.txt","r")
Add_lines = Add_file.readlines()

new_strings = []
for line in Add_lines:
    new_string = line.replace("cpd00027:glucose", "Glucose") 
    new_string = new_string.replace("cpd00013:nh4", "NH4")
    new_string = new_string.replace("cpd01007:Benzene", "B")
    new_string = new_string.replace("cpd01034:Toluene", "T")
    new_string = new_string.replace("cpd04383:Ethylbenzene", "E")
    new_string = new_string.replace("cpd01034:Toluene", "T")
    new_string = new_string.replace("cpd04450:xylene", "X")
    new_string = new_string.replace("cpd00067:h2", "H2")
    new_string = new_string.replace("cpd00011:co2", "CO2")
    new_string = new_string.replace("cpd10516:Fe3", "Fe3")
    new_string = new_string.replace("cpd00209:NO3", "NO3")
    new_string = new_string.replace("cpd00048:SO4", "SO4")
    new_string = new_string.replace("cpd00007:O2", "O2")
    new_string = new_string.replace("cpd00047:Formic", "Formic")
    new_string = new_string.replace("cpd00029:Acetate", "Acetate")
    new_string = new_string.replace("cpd00141:Propionate", "Propionate")
    new_string = new_string.replace("cpd01711:Isobutyrate", "Isobutyrate")
    new_string = new_string.replace("Parabacteroides_goldsteinii", "Macellibacteroides_fermentans")
    new_string = new_string.replace("cpd00023:glutomate", "Glutomate")
    new_string = new_string.replace("cpd00041:aspartate", "Aspartate")	
    new_string = new_string.replace("cpd00221:lactate", "Lactate")
    new_string = new_string.replace("cpd00020:pyruvate", "Pyruvate")
    new_string = new_string.replace("cpd00130:malate", "Malate")
    new_string = new_string.replace("cpd00106:fumarate", "Fumarate")
    new_string = new_string.replace("cpd00011:CO2", "CO2")
    new_string = new_string.replace("cpd00094:oxobutyrate", "Oxobutyrate")
    new_string = new_string.replace("cpd00211:butyrate", "Butyrate")
    new_string = new_string.replace("cpd00039:Lysine", "Lysine")
    new_string = new_string.replace("cpd01024:Methane", "CH4")
    new_string = new_string.replace("cpd00048:Sulfate", "SO4")
    new_string = new_string.replace("cpd00054:Serine", "Serine")
    new_string = new_string.replace("cpd00129:Proline", "Proline")
    new_string = new_string.replace("cpd00035:alenine", "Alanine")
    new_string = new_string.replace("cpd00035:Alanine", "Alanine")
    new_string = new_string.replace("cpd00082:fructose", "Fructose")
    new_string = new_string.replace("cpd00023:Glutamate", "Glutamate")
    new_string = new_string.replace("cpd00156:Vanine", "Valine")
    new_string = new_string.replace("cpd00041:Aspartate", "Aspartate")
    new_string = new_string.replace(";", "+") # לשים לב אם זה לא פסיק
    new_strings.append(new_string)

sep_list = []
for line in new_strings:
    l = line.split()
    sep_list.append(l)

# small numbers to 0
ov0list = [sep_list[0]]
for line in sep_list[1:]:
    
    if float(line[2]) < 0.01:
        line[2] = 0
    ov0list.append(line)    

# remove "
ov0list2 = []
for x in ov0list:
    x[1] = x[1].strip('"')
    ov0list2.append(x)

#creating new table - all bacs and media names have to be as it in Raphi's file

table_file = open(r"input2_empty_table.txt","r")
table_lines = table_file.readlines()

#making list from table for further work

sep_table = []
for line in table_lines:
    l = line.split()
    sep_table.append(l)

table_file.close()
Add_file.close()  

#estimating color for each func group. Names of bacs have to be same as in Raphi's file

coding_names_df= pd.read_csv('input3_Functional_group_list.csv', index_col=0)

bb = coding_names_df["Group"]# group for every line

lut = dict(zip(bb.unique(), ['royalblue', '#669999','orange', '#ff7326', 'red', '#a6a6a6', 'olive','seagreen']))# dict: a color for every group

colcolors = [] # list of all the colors by line
for group in bb:
    colcolors.append(lut[group])
    

#filling the empty table (a table as a list now)

table_val = [sep_table[0]]
for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:
            (line[sep_table[0].index(Lline[0])]) = str(Lline[2])
    table_val.append(line)

#making table file from the list

filled_table_file = open("filled_table.txt", "w")

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

#open filled table 
filled = open(r"filled_table.txt","r")
filledr = filled.read()

#removing "_"
filled_tab = filledr.replace(',_',',')

#making file for heatmap
file_for_heatmap = open(r"for_heatmap.txt","w")
file_for_heatmap.write(filled_tab)
file_for_heatmap.close()

df= pd.read_csv('for_heatmap.txt' ,index_col=0)

#creating heatmap - Biomass
gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, row_cluster=False, col_cluster=False, cbar_pos=(0, .3, .03, .4))
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('all_BM.png', bbox_inches='tight', dpi=600)

################

table_val = [sep_table[0]]
for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:

            (line[sep_table[0].index(Lline[0])]) = str(Lline[2]) # BM 
          
    table_val.append(line)

table_file.close()
Add_file.close()

# list to file
filled_table_file = open("filled_table_BM.txt", "w")

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

df= pd.read_csv('filled_table_BM.txt' ,index_col=0)

gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, row_cluster=False, col_cluster=False, cbar_pos=(0, .3, .03, .4)) # numbers are cbar location. 
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('BTEX_BM.png', bbox_inches='tight', dpi=600) 

#################

table_val = [sep_table[0]]
for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:
            (line[sep_table[0].index(Lline[0])]) = str(Lline[3]) # Formic לשנות
    table_val.append(line)

# list to file
filled_table_file = open("filled_table_Formic.txt", "w")     #לשנות

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

df= pd.read_csv('filled_table_Formic.txt' ,index_col=0)    

gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, row_cluster=False, col_cluster=False, cbar_pos=(0, .3, .03, .4)) # numbers are cbar location. 
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('BTEX_Formic_Fcolor.png', bbox_inches='tight', dpi=600) 

######################


table_val = [sep_table[0]]
for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:
            (line[sep_table[0].index(Lline[0])]) = str(Lline[4]) # Acetate לשנות
    table_val.append(line)

# list to file
filled_table_file = open("filled_table_Acetate.txt", "w") #לשנות

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

df= pd.read_csv('filled_table_Acetate.txt' ,index_col=0) 

gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, row_cluster=False,vmax = 5, vmin = -20, col_cluster=False, cbar_pos=(0, .3, .03, .4)) # numbers are cbar location. 
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('BTEX_Acetate.png', bbox_inches='tight', dpi=600) # לשנות

####################

table_val = [sep_table[0]]
for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:
            (line[sep_table[0].index(Lline[0])]) = str(Lline[5]) # Propionate לשנות
    table_val.append(line)

# list to file
filled_table_file = open("filled_table_Propionate.txt", "w") #לשנות

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

df= pd.read_csv('filled_table_Propionate.txt' ,index_col=0)   

gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, row_cluster=False, col_cluster=False, cbar_pos=(0, .3, .03, .4)) # numbers are cbar location. 
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('BTEX_Propionate.png', bbox_inches='tight', dpi=600)

######################

table_val = [sep_table[0]]
for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:
            (line[sep_table[0].index(Lline[0])]) = str(Lline[7]) # H2 לשנות
    table_val.append(line)

# list to file
filled_table_file = open("filled_table_H2.txt", "w") #לשנות

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

#-------------------------------------------------
df= pd.read_csv('filled_table_H2.txt' ,index_col=0)                #לשנות
#--------------------------------------------------
# no tree no legend for strip.
# the mid value is 0.
gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, row_cluster=False, col_cluster=False,
                     cbar_pos=(0, .3, .03, .4), vmax = 500, vmin = -700, robust= False) # numbers are cbar location. 
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('BTEX_H2.png', bbox_inches='tight', dpi=600)

################

table_val = [sep_table[0]]
for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:
            (line[sep_table[0].index(Lline[0])]) = str(Lline[8]) # CO2 לשנות
    table_val.append(line)

# list to file
filled_table_file = open("filled_table_CO2.txt", "w") #לשנות

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

#-------------------------------------------------
df= pd.read_csv('filled_table_CO2.txt' ,index_col=0)                #לשנות
#--------------------------------------------------
# no tree no legend for strip.
# the mid value is 0.
gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, vmax = 100, vmin = -150, row_cluster=False, col_cluster=False, cbar_pos=(0, .3, .03, .4)) # numbers are cbar location. 
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('BTEX_CO2.png', bbox_inches='tight', dpi=600) 

###################

table_val = [sep_table[0]]

for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:
            (line[sep_table[0].index(Lline[0])]) = str(Lline[10]) # Methane לשנות
    table_val.append(line)

# מרשימה לקובץ
filled_table_file = open("filled_table_Methane.txt", "w") #לשנות

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

df= pd.read_csv('filled_table_Methane.txt' ,index_col=0)                #לשנות
#--------------------------------------------------
# no tree no legend for strip.
# the mid value is 0.
gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, row_cluster=False, col_cluster=False, cbar_pos=(0, .3, .03, .4)) # numbers are cbar location. 
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('BTEX_Methane.png', bbox_inches='tight', dpi=600) 

###################

table_val = [sep_table[0]]
for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:
            (line[sep_table[0].index(Lline[0])]) = str(Lline[11]) # Potential_Formic לשנות
    table_val.append(line)

# list to file
filled_table_file = open("filled_table_Potential_Formic.txt", "w") #לשנות

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

df= pd.read_csv('filled_table_Potential_Formic.txt' ,index_col=0)                #לשנות
#--------------------------------------------------
# no tree no legend for strip.
# the mid value is 0.
gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, row_cluster=False, col_cluster=False, cbar_pos=(0, .3, .03, .4)) # numbers are cbar location. 
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('BTEX_Potential_Formic.png', bbox_inches='tight', dpi=600) 

#######################

table_val = [sep_table[0]]
for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:
            (line[sep_table[0].index(Lline[0])]) = str(Lline[12]) # Potential_Acetic לשנות
    table_val.append(line)

# list to file
filled_table_file = open("filled_table_Potential_Acetic.txt", "w") #לשנות

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

df= pd.read_csv('filled_table_Potential_Acetic.txt' ,index_col=0)                #לשנות
#--------------------------------------------------
# no tree no legend for strip.
# the mid value is 0.
gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, row_cluster=False, col_cluster=False, cbar_pos=(0, .3, .03, .4)) # numbers are cbar location. 
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('BTEX_Potential_Acetic.png', bbox_inches='tight', dpi=600) 

#################

table_val = [sep_table[0]]
for line in sep_table[1:]:
    for Lline in ov0list2[1:]:
        if line[0] == Lline[1]:
            (line[sep_table[0].index(Lline[0])]) = str(Lline[13]) # Potential_Propionate לשנות
    table_val.append(line)

# list to file
filled_table_file = open("filled_table_Potential_Propionate.txt", "w") #לשנות

for x in table_val:
    a = ','.join(x)
    filled_table_file.write(a + "\n")
filled_table_file.close()

df= pd.read_csv('filled_table_Potential_Propionate.txt' ,index_col=0)                #לשנות
#--------------------------------------------------
# no tree no legend for strip.
# the mid value is 0.
gr = sns.clustermap(df, cmap='coolwarm',center=0, col_colors= colcolors, row_cluster=False, col_cluster=False, cbar_pos=(0, .3, .03, .4)) # numbers are cbar location. 
gr.ax_heatmap.set_xticklabels([r'$\it{' + ticklabel.get_text().replace('_', '\\ ') + '}$'
                              for ticklabel in gr.ax_heatmap.get_xticklabels()]) # for italic font
gr.savefig('BTEX_Potential_Propionate.png', bbox_inches='tight', dpi=600) 

###############
