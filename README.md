# LncTarget
A computational platform to predict the binding sites and the directly regulated genes of a given lncRNA 

### Installation
**install with conda**
```
git clone https://github.com/summus-kong/LncTarget.git
cd LncTarget
conda env create -f=lnctarget_conda.yml -p /path/conda/env/lnctarget
conda activate lnctarget
```
To deactivate the environment use:
```
conda deactivate
```
To learn more about conda and environments, please consider the following [conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#)
\# 
### Usage
```
python LncTarget -h
```
or
```
chmod u+x LncTarget
# write LncTarget dir path to bashrc
echo "export PATH=\$PATH:/project/houwb/pro/LncTarget/" >> ~/.bashrc
source ~/.bashrc
```
```
LncTarget -h
```
