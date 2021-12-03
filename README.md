# Babylon: A Stream-Lit On-The-Fly Hierarchal Clustering Application for User Gene Lists
# Author
Ram Ayyala 
# About
Babylon uses  [seaborn's clustermap function](https://seaborn.pydata.org/generated/seaborn.clustermap.html) which makes use of [scipy's cluster.hierarchy module](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html) to create a hierarchal clustering heatmap of the inputed genes in real time. The app is hosted using Streamlit's sharing function and can be accessed [here](https://share.streamlit.io/ramayyala/final_project/main/code/babylon.py). 

# Database
Babylon uses the user's inputted genes to select the genes from a predownloaded pancreatic cancer database created from the  [National Cancer Institute GDC Data Portal](https://portal.gdc.cancer.gov/). Babylon's database currently holds 446 samples, but will be expanded to other FPKM samples. The database is being hosted on Github LFS which can be found in the data/Hugo_data.csv. All gene names in the database are taken from the GTF file provided by National Cancer Institute. 
# Functionality
## Gene List Input
Please input your gene list into the **Gene Set** text area. Make sure to input the gene list such that each gene is **separated by a space** as shown below and that your gene set is in the Gene Name or Hugo Format. Currently, Babylon does not support use of ENSEMBL names. 
### Example
![](/misc/gene_input_screenshot.png)
## Normalization
After the genes have been selected, the user has the option to normalize the data using the log scale button. Currently, Babylon only supports log10 scaling but other normalization options will be added in the future. 
![](/misc/normalization_options.png)
## Covariates
The user also has the option to add covariates to their clustermap, which were taken from the metadata provided by the National Cancer Institute. The current options for covariates are the following:
**Gender:** Provides the gender of the samples.
**Race:** Provides the race of the samples.
**Ethnicity:** Provides the ethnicity of the samples
**AJCC Pathologic Stage:** The AJCC Pathologic Stage is the stage of pancreatic cancer the sample is at. 
**Primary Diagnosis:** Provides the type of pancreatic cancer the sample suffers from
**Origin of Cancer (Tissue or Organ):** Provides the origin of the cancer which can either be a tissue or an organ.
**Vital Status:** Provides the vital status of the sample which is either **alive** or **dead**. 
![](/misc/covariate_options.png)

When selecting the covariate, please **only choose one at a time**! Babylon doesn't currently support adding multiple covariates to the clustermap. **So when the user chooses one covariate and wishes to switch to another covariate, it is reccomended that the user unchecks the previously selected covariate and then selects the new covariate.** 
Coovariates will appear on the column dednrogram of the clustermap as shown below:
![](/misc/covariate_on_clustermap.png)
## Color
Babylon also provides the user the option of selecting their color scheme for the clustermap. Currently Babylon supports these three color palettes:
**mako**
**RdBu**
**vlag**
![](/misc/color_options.png)
More color palettes will be added in the future. 
## Download CSV
Babylon allows the user to download the FPKM csv of their selected genes from the database by clicking the **Download selected data as CSV** button, which is located underneath the clustermap. 
![](/misc/download_csv_option.png)
# Installation
If you wish to install this app and run it locally instead of using the streamlit server version of it which is availbale online [here]((https://share.streamlit.io/ramayyala/final_project/main/code/babylon.py), then follow the instructrions below to install. 
## Clone the Repository 
```
git clone https://github.com/ramayyala/final_project
```
## Install streamlit and other dependencies onto your computer using pip or whatever package manager you prefer
Example:
```
pip install streamlit
```
**Dependecies:**
1. scipy
2. pandas
3. numpy
4. seaborn
5. matplotlib
6. streamlit
7. python= 3.8.8 (should be fine with higher versions)

# License
MIT License
Copyright (c) 2021 Ram Ayyala
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



