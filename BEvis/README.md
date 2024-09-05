<img src="dep_sign.png" width=120, height=120 align="left" />

# BEvis - Bacterial Exchange Visualization

BEvis is a pipeline for visualization of exchange fluxes in microbial communities. 
Here we provide a script to visualize metabolites exchange in a bacterial community as described in Yusim, J et al. " Integrated use of electrochemical anaerobic reactors and genomic based modeling for characterizing methanogenic activity in microbial communities exposed to BTEX contamination".
The script uses networkX package of Python 3.8.0 for network visualization. The script takes input files produced by metabolic models processing tools, e.g., Cobrapy (Ebrahim et al. 2013) and COMETS (Dukovski et al. 2021), to generate visualization of the exchange networks.
This script makes use of files describing exchange interactions in microbial communities (in the format of “get_species_exchange_fluxes” function in COMETS). In addition, visualization requires associating graphical features, e.g., edge thickness, vertex size, with numerical features, such as flux and biomass from the input files. Modification of user provided parameters is performed within a single configuration file, BEvis_config.yml.
Example input and output files are in the "data" and "results" directories respectively. 

## Input files

- Bacteria biomass in time (df_BM.csv).
This is a CSV file with "cycle", "species", and "biomass" as header.

- In separate folder, data/model_exchanges, exchange files of each model (e.g., Mesotoga_infera.csv) 
Exchanges of each compound in a specific cycle.

- A dictionary of compound id, compound name, and formula (dicComp_df.csv)

- Metabolites amounts in time (df_metabolites.csv)

## Determine cycle (day) for visualization

The user provides a specific day, e.g., 159 or 0 for automaticaly determie the
day as described below:

Cycle (day) for visualization, c\_i is calculated as a fixed number of cycles, nc, before c_max. c_i = c_max - nc.

Where c_max is the cycle in which maximal growth (biomass = 0.1) is achieved and nc is user-provided.

Lower c_i, or higher nc, corresponds to lower biomass point, during the bacterial exponential growth phase.

## Dependencies

* [matplotlib==3.2.2]
* [networkx==3.1]
* [numpy==1.23.5]
* [pip==22.3.1]
* [python==3.8.0]

### pip:

* [pandas==1.5.1]
* [pyyaml==6.0]

## Installation

### Download and install BEvis on Linux (Ubuntu 20.04)

Clone repository using git clone

or download the zip and extract the repository 

### Create a virtual environment and install dependencies

```shell
# Create env and install dependencies #

conda env create -f BEvis_env.yml

```

### Activate the virtual environment and move to work directory  

```shell

conda activate BEvis_env

cd BEvis

```

#### run script

```shell

cd ./data/model_exchanges/

ls *.csv > ../model_id_list.txt 

cd  ../../

python BEvis.py

#Or a single bash script:

bash BEvis_all.sh


```

## Contributors

[Shlomit Medina](https://www.freilich-lab.com/shlomit-medina )  \
[Gon Carmi](https://www.freilich-lab.com/members) \
[Shiri Freilich](https://www.freilich-lab.com/shiri-detailes ) \
[Raphy Zarecki](https://www.linkedin.com/in/raphy-zarecki-3412663/?originalSubdomain=il)  \
[Jenny Yusim](https://www.freilich-lab.com/jenny-details)

## References

Dukovski, I., Bajić, D., Chacón, J.M.  et al. "A metabolic modeling platform for the computation of microbial ecosystems in time and space (COMETS)." Nature protocols 16.11 (2021): 5030-5082.

Ebrahim, A., Lerman, J.A., Palsson, B.O. et al. COBRApy: COnstraints-Based Reconstruction and Analysis for Python. BMC Syst Biol 7, 74 (2013). https://doi.org/10.1186/1752-0509-7-74.

Yusim, J et al. 2024 “Integrated use of electrochemical anaerobic reactors and genomic based modeling for characterizing methanogenic activity in microbial communities exposed to BTEX contamination".

## Funding

This work was funded by the Joint NSFC-ISF Research Grant [grant number 3164/19]

