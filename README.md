# LncTargeter
A computational platform to predict the binding sites and the directly regulated genes of a given lncRNA 

### Installation
**install with conda**
```
git clone https://github.com/summus-kong/LncTargeter.git
cd LncTargeter
conda env create -f=lnctargeter_conda.yml -p /path/conda/env/lnctargeter
conda activate lnctargeter
```
To deactivate the environment use:
```
conda deactivate
```
To learn more about conda and environments, please consider the following [conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#)

**manually install dependent packages**

See the requirment.txt file

\# 
### Usage
```
python LncTargeter -h
```
or
```
chmod u+x LncTargeter
# write LncTargeter dir path to bashrc
echo "export PATH=$PATH:path/LncTargeter/" >> ~/.bashrc
source ~/.bashrc
```
```
LncTargeter -h
```
