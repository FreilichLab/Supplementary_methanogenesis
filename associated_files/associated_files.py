#!/usr/bin/env python
# coding: utf-8
#exec(open("BEvis_test.py").read())
#--------------------------------------------

#impot configuration file

import yaml

config = yaml.safe_load(open("./BEvis_conf.yaml"))

# step_1: import packages and upload models.
#==============================================
# User input:

models_directory = config['step1']['models_directory']

#==============================================

import pandas as pd

import numpy as np

import cobra

import cometspy as c

import matplotlib.pyplot as plt

import matplotlib

import os

#from bs4 import BeautifulSoup

#--------------------------------------------
# Import required SBML models

cobra_models = []
# Iterate over files in the directory

with open(models_directory + "/model_list.txt") as file:

    lines = [line.rstrip() for line in file]

for file_name in lines:
    mod = cobra.io.read_sbml_model(models_directory + "/" + file_name)
    cobra_models.append(mod)
#---------------------------------------------
# Convert cobra models to comets models
comets_models = []
for mod in cobra_models:
    modelc = c.model(mod)
    comets_models.append(modelc)

#step1 works

# step_2: prepare data for COMETS
#==============================================
# User input:
medium_directory = config['step2']['medium_directory']
medium_file = config['step2']['medium_file']
metabolites_format = config['step2']['metabolites_format']
nc = config['step2']['nc']
output_dir = config['step2']['output_dir']
cmd = "mkdir -p " + output_dir
os.system(cmd)
#==============================================

# Initial population
for mod in comets_models:
    mod.initial_pop = [0, 0, 3.3e-8]

# iInsert models to "test_tube".
test_tube = c.layout()

for mod in comets_models:
    test_tube.add_model(mod)
#---------------------------------------------

# Import metabolites from metabolites file (medium_file in config file).

#=======================================
# preper 'medium.csv' with models compounds format. file like
#comp	quan
#ca2_e	0.02
#cl_e	0.02
#cu2_e	0.003
#fe2_e	0.5
#glc__D_e	10
#=======================================
# Insert medium metabolites to "test_tube".

medium = pd.read_csv(medium_directory + medium_file)

medium_dic = dict(medium.values) # making a dictionary

for k in medium_dic.keys():
    test_tube.set_specific_metabolite(k, medium_dic[k])

#--------------------------------------------
# Define parameters
my_params = c.params()

my_params.set_param('maxCycles', 1000)
my_params.set_param('writeTotalBiomassLog', True)
my_params.set_param('writeBiomassLog', True)
my_params.set_param('writeFluxLog', True)
my_params.set_param('writeMediaLog', True)
my_params.set_param('writeSpecificMediaLog', True)
my_params.set_param('specificMedia', metabolites_format)
#--------------------------------------------
# Run COMETS
comp_assay = c.comets(test_tube, my_params)
comp_assay.run()

def fix_cycle_near_10(n):
    #get day near 10, e.g., 79 to 80, 71 to 70
    #this is becuase days are in steps of 10 days
    t = n
    remider = n % 10
    if remider >= 5 :
        t = ((n // 10) +  1 )*10

    if remider >= 1  and remider < 5:
        t = ((n // 10))*10

    if n // 10 == 0 :
        t = 10
    return t

#find day(cycle)
##################################new part
#===========================
# Bacteria biomass in time file

biomass = comp_assay.total_biomass
#myplot = biomass.plot(x="cycle") 
df_BM = comp_assay.biomass.copy()
df_BM.to_csv(output_dir + "df_BM.csv")

#==========================================================
# Metabolites amount in time file

df_metabolites = comp_assay.get_metabolite_time_series().copy()
df_metabolites.to_csv(output_dir + 'df_metabolites.csv') 

#=======================================
# all exchange files of each model, in a special folder

f = open(output_dir + "model_id_list.txt",'w')
for model in cobra_models:
    df_EX = comp_assay.get_species_exchange_fluxes(model.id)
    df_EX.to_csv(output_dir + model.id + '.csv')
    f.write(model.id + '.csv')
    f.write("\n")
f.close()
   
#=========================================================
# making a dictionary of: compound_id:[compound_name, formula]

df_metabolites = pd.read_csv(output_dir + 'df_metabolites.csv')
df_metabolites1 = df_metabolites.iloc[:, 1:]
df_metabolites1.set_index('cycle', inplace=True)

ll = []
for model in cobra_models:
    for comp in df_metabolites1.columns:
        try:
            name = model.metabolites.get_by_id(comp).name
            formula = model.metabolites.get_by_id(comp).formula
            tup = (comp, name, formula)
            ll.append(tup)
        except Exception:
            pass
        
lll = tuple(ll)

#---------------------------
dicComp = {}
for tup in lll:
    k = list(tup)[0]
    v = list(tup)[1:3]
    dicComp[k] = v

dicComp_df = pd.DataFrame(dicComp)
dicComp_df.to_csv(output_dir + 'dicComp_df.csv')

#======================================================
