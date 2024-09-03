<img src="dep_sign.png" width=120, height=120 align="left" />

# Associated files

This script prapres input files for BEvis from metabolic models as described in Yusim, J et al. 2024.
This script utilizes results from Python-based metabolic models processing tools, Cobrapy (Ebrahim et al. 2013) with COMETS (Dukovski et al. 2021), or similar data format from another source, to generate these files.
Modification of user-provided parameters is performed within a single configuration file, associated_files_config.yml.

This script accepts input files generated from both KBASE, CARVME (BIGG format), and other tools.
The tool-specific format must be kept throughout all the files used in the script.
For example Compounds format, e.g., "cpd00030_e0" for KBASE or glc__D_c for CAREVME (BIGG format). It is like in the metabolic models used to generate input files for BEvis. 

The provided example uses input files from the KBASE tool.

Bacteria names must be consistent within input files (including file names) and BEvis_config.yml.

## Input files

- metabolic models - smbl format

- medium - csv

## Dependencies

* [matplotlib==3.2.2]
* [numpy==1.23.5]
* [pip==22.3.1]
* [python==3.8.0]

### pip:

* [cobra==0.26.3]

* [cometspy==0.4.16]

* [pandas==1.5.1]

* [pyyaml==6.0]


## Installation

### Download and install associated_files on Linux (Ubuntu 20.04)

Clone repository using git clone

or download the zip and extract the repository 

### Create a virtual environment and install dependencies

```shell
# Create env and install dependencies #

cd associated_files

conda env create -f associated_files_env.yml

```

### Activate the virtual environment and move to work directory  

```shell

conda activate associated_files_env 

cd associated_files

```

#### run script

```shell

cd associated_files

python associated_files.py

```

## Contributors

[Shlomit Medina](https://www.freilich-lab.com/shlomit-medina )  \
[Gon Carmi](https://www.freilich-lab.com/members) \
[Shiri Freilich](https://www.freilich-lab.com/shiri-detailes ) \
[Raphy Zarecki](https://www.linkedin.com/in/raphy-zarecki-3412663/?originalSubdomain=il)  \
[Jenny Yusim](https://www.freilich-lab.com/jenny-details) \

## References

Dukovski, I., Bajić, D., Chacón, J.M.  et al. "A metabolic modeling platform for the computation of microbial ecosystems in time and space (COMETS)." Nature protocols 16.11 (2021): 5030-5082.

Ebrahim, A., Lerman, J.A., Palsson, B.O. et al. COBRApy: COnstraints-Based Reconstruction and Analysis for Python. BMC Syst Biol 7, 74 (2013). https://doi.org/10.1186/1752-0509-7-74.

Yusim, J et al. 2024 “Integrated use of electrochemical anaerobic reactors and genomic based modeling for characterizing methanogenic activity in microbial communities exposed to BTEX contamination".

## Funding

This work was funded by the Joint NSFC-ISF Research Grant [grant number 3164/19]

