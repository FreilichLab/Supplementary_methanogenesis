<img src="dep_sign.png" width=120, height=120 align="left" />

# MatrixVis Bacteria Metabolite Production Simulation matrix

MatrixVis is a pipeline for comparative visualization of predict growth and metabolite production of multiple microorganisms in multiple environments. 
Here we provide the script together with input and output files described in Yusim, J et al. “Integrated use of electrochemical anaerobic reactors and genomic based modeling for characterizing methanogenic activity in microbial communities exposed to BTEX contamination".
The script uses seaborn package of Python 3.0 for network visualization. 

## Dependencies

* [matplotlib==3.2.2]
* [networkx==3.1]
* [numpy==1.23.5]
* [pip==22.3.1]
* [python==3.8.0]

### pip:

* [pandas==1.5.1]
* [pyyaml==6.0]

## Input files 

- input1_organisms_media_secretion.txt
- input2_empty_table.txt
- input3_Functional_group_list.csv

## Output files

- all_BM.png
- BTEX_Acetate.png
- BTEX_BM.png
- BTEX_CO2.png
- BTEX_Formic_Fcolor.png
- BTEX_H2.png
- BTEX_Methane.png
- BTEX_Potential_Acetic.png
- BTEX_Potential_Formic.png
- BTEX_Potential_Propionate.png
- BTEX_Propionate.png

Also sveral interdiate files are generated to facilated with the creationg of visualiztions (png)

## Installation

### Download and install BEvis on Linux (Ubuntu 20.04)

Clone repository using git clone

or download the zip and extract the repository 

### Create a virtual environment and install dependencies

```shell
# Create env and install dependencies #

cd MatrixVis

conda env create -f MatrixVis_env.yml

```

### Activate the virtual environment and move to work directory  

```shell

cd MatrixVis

conda activate MatrixVis_env

```

#### run script

```shell

cd MatrixVis

python validation_matrices.py

```

## Contributors

[Shlomit Medina](https://www.freilich-lab.com/shlomit-medina )  \
[Gon Carmi](https://www.freilich-lab.com/members) \
[Shiri Freilich](https://www.freilich-lab.com/shiri-detailes ) \
[Raphy Zarecki](https://www.linkedin.com/in/raphy-zarecki-3412663/?originalSubdomain=il)  \
[Jenny Yusim](https://www.freilich-lab.com/jenny-details) \

## References

Yusim, J et al. 2024 “Integrated use of electrochemical anaerobic reactors and genomic based modeling for characterizing methanogenic activity in microbial communities exposed to BTEX contamination".

## Funding

This work was funded by the Joint NSFC-ISF Research Grant [grant number 3164/19]

