import scipy as scp
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
import csv
from scipy.cluster.hierarchy import dendrogram, linkage
import base64
from enum import Enum
from io import BytesIO, StringIO
from typing import Union
import streamlit as st
st.title('Babylon: A Stream-Lit On-The-Fly Hierarchal Clustering Application for User Gene Lists')

@st.cache
def load_data():
    df = pd.read_csv("data/Hugo_data.csv")
    return df
@st.cache
def load_covariates():
    covariates=pd.read_csv("data/covariates.csv")
    return covariates
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
#load_data()
#df = pd.read_csv("../data/Hugo_data.csv")
df = load_data()
covariates=load_covariates()
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done!")

# USER INPUT GENES
user_input = st.text_area("Gene Set", "ABCC6 ABCC8 APPL1 ASXL1 B9D1 B9D2 BICC1 BLK CASR CC2D2A CCND1 CDKN1C CEL CEP290 CEP55 CFTR CNOT1 CP CPA1 CSPP1 CTRC DIS3L2 DNAJC21 DYNC2I1 DZIP1L EFL1 EIF2AK3 ENPP1 FANCD2 FLI1 FLNB FOXF1 GABRD GANAB GATA6 GCK GLIS3 HNF1A HNF1B HNF4A IGF2 INS KCNAB2 KCNJ11 KCNQ1 KCNQ1OT1 KLF11 LHX1MKS1 MYCN NEK1 NEUROD1 NPHP3 OFD1 PAX4 PDX1 PKD1 PKD2 PKHD1 PRDM16 PRSS1 PRSS2 PTF1A PTRH2 RARB RBM8A RECQL4 RERE RFX6 RPGRIP1 RPGRIP1L SBDS SETBP1 SIK3 SKI SLC29A3 SPINK1 SRP54 STAT3 STRA6 TCTN2 TELO2 TMEM107 TMEM216 TMEM231 TMEM67 VHL WDPCP WDR19 XPNPEP3")
#user_input = st.text_input("Gene List", 0)
gene_list = user_input.split()

df[1:100]

# #Grab selected genes
# #st.write(gene_list)
# df_selected = df.query('gene_id in @gene_list')
# #df_selected=df[df['gene_id'].isin(gene_list)]
# #st.write(df_selected)
# df_selected = df_selected.set_index('gene_id')
# df_selected=df_selected.astype('float16')
#
# # Log Scale selected data Option
# st.write("Normalizing Options")
# if st.checkbox('Log scale'):
#     #Log Scale the selected data
#     df_selected = (1+df_selected)/2 # (-1,1] -> (0,1]
#     df_selected=np.log(df_selected)
#
# #Covariate Selection
# st.write("Covariate Selection")
# gender=st.checkbox('Gender')
# race=st.checkbox('Race')
# ethnicity=st.checkbox('Ethnicity')
# ajcc_pathologic_stage=st.checkbox('ajcc_pathologic_stage')
# primary_diagnosis=st.checkbox('primary_diagnosis')
# tissue_or_organ_of_origin=st.checkbox('tissue_or_organ_of_origin')
# vital_status=st.checkbox('vital_status')
# #Color Options
# color_option = st.selectbox('Color', ("mako", "RdBu","vlag"),key = "color_choice")
#
# # PLOT FIGURE
#
# if gender:
#     #Select Gender data
#     gender_dict=pd.Series(covariates.gender.values,index=covariates["Sample Name"]).to_dict()
#     df_selected.rename(columns=gender_dict, inplace=True)
#     df_selected = df_selected.loc[:, df_selected.columns.notnull()]
#     lut = dict(zip(df_selected.columns[0:len(df_selected.columns)].unique(), "rb"))
#     col_colors = df_selected.columns[0:len(df_selected.columns)].map(lut)
#     def plot():
#         fig=sns.clustermap(df_selected, metric="euclidean", standard_scale=1, method="ward",cmap=color_option,col_colors=col_colors)
#         st.pyplot(fig)
#     plot()
# if race:
#     #Select Race data
#     race_dict=pd.Series(covariates.race.values,index=covariates["Sample Name"]).to_dict()
#     df_selected.rename(columns=race_dict, inplace=True)
#     df_selected = df_selected.loc[:, df_selected.columns.notnull()]
#     lut = dict(zip(df_selected.columns[0:len(df_selected.columns)].unique(), "rbg"))
#     col_colors = df_selected.columns[0:len(df_selected.columns)].map(lut)
#     def plot():
#         fig=sns.clustermap(df_selected, metric="euclidean", standard_scale=1, method="ward",cmap=color_option,col_colors=col_colors)
#         st.pyplot(fig)
#     plot()
# if ethnicity:
#     #Select Ethnicity data
#     ethnicity_dict=pd.Series(covariates.ethnicity.values,index=covariates["Sample Name"]).to_dict()
#     df_selected.rename(columns=ethnicity_dict, inplace=True)
#     df_selected = df_selected.loc[:, df_selected.columns.notnull()]
#     lut = dict(zip(df_selected.columns[0:len(df_selected.columns)].unique(), "rb"))
#     col_colors = df_selected.columns[0:len(df_selected.columns)].map(lut)
#     def plot():
#         fig=sns.clustermap(df_selected, metric="euclidean", standard_scale=1, method="ward",cmap=color_option,col_colors=col_colors)
#         st.pyplot(fig)
#     plot()
# if ajcc_pathologic_stage:
#     ajcc_pathologic_stage_dict=pd.Series(covariates.ajcc_pathologic_stage.values,index=covariates["Sample Name"]).to_dict()
#     df_selected.rename(columns=ajcc_pathologic_stage_dict, inplace=True)
#     df_selected = df_selected.loc[:, df_selected.columns.notnull()]
#     lut = dict(zip(df_selected.columns[0:len(df_selected.columns)].unique(), "rbgcmykw"))
#     col_colors = df_selected.columns[0:len(df_selected.columns)].map(lut)
#     def plot():
#         fig=sns.clustermap(df_selected, metric="euclidean", standard_scale=1, method="ward",cmap=color_option,col_colors=col_colors)
#         st.pyplot(fig)
#     plot()
# if primary_diagnosis:
#     primary_diagnosis_dict=pd.Series(covariates.primary_diagnosis.values,index=covariates["Sample Name"]).to_dict()
#     df_selected.rename(columns=primary_diagnosis_dict, inplace=True)
#     df_selected = df_selected.loc[:, df_selected.columns.notnull()]
#     lut = dict(zip(df_selected.columns[0:len(df_selected.columns)].unique(), "rbgcmy"))
#     col_colors = df_selected.columns[0:len(df_selected.columns)].map(lut)
#     def plot():
#         fig=sns.clustermap(df_selected, metric="euclidean", standard_scale=1, method="ward",cmap=color_option,col_colors=col_colors)
#         st.pyplot(fig)
#     plot()
# if tissue_or_organ_of_origin:
#     tissue_or_organ_of_origin_dict=pd.Series(covariates.tissue_or_organ_of_origin.values,index=covariates["Sample Name"]).to_dict()
#     df_selected.rename(columns=tissue_or_organ_of_origin_dict, inplace=True)
#     df_selected = df_selected.loc[:, df_selected.columns.notnull()]
#     lut = dict(zip(df_selected.columns[0:len(df_selected.columns)].unique(), "rbgcm"))
#     col_colors = df_selected.columns[0:len(df_selected.columns)].map(lut)
#     def plot():
#         fig=sns.clustermap(df_selected, metric="euclidean", standard_scale=1, method="ward",cmap=color_option,col_colors=col_colors)
#         st.pyplot(fig)
#     plot()
# if vital_status:
#     vital_status_dict=pd.Series(covariates.vital_status.values,index=covariates["Sample Name"]).to_dict()
#     df_selected.rename(columns=vital_status_dict, inplace=True)
#     df_selected = df_selected.loc[:, df_selected.columns.notnull()]
#     lut = dict(zip(df_selected.columns[0:len(df_selected.columns)].unique(), "rb"))
#     col_colors = df_selected.columns[0:len(df_selected.columns)].map(lut)
#     def plot():
#         fig=sns.clustermap(df_selected, metric="euclidean", standard_scale=1, method="ward",cmap=color_option,col_colors=col_colors)
#         st.pyplot(fig)
#     plot()
# else:
#     def plot():
#         fig=sns.clustermap(df_selected, metric="euclidean", standard_scale=1, method="ward",cmap=color_option)
#         st.pyplot(fig)
#     plot()
#
# #fig=sns.clustermap(df_selected, metric="euclidean", standard_scale=1, method="ward",cmap=color_option)
# #st.pyplot(plot())
#
# # Download clustermap
#     # look into kwargs arg on pyplot for plt.savefig option
# # Download selected data_table Option
# @st.cache
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8')
# csv = convert_df(df_selected)
# st.download_button(
#     label="Download selected data as CSV",
#     data=csv,
#     file_name='selected_data.csv',
#     mime='text/csv',)
#
#
# #csv = df_selected.to_csv(index=True)
# #b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
# #href = f'<a href="data:file/csv;base64,{b64}">Download Selected Data</a> (right-click and save as &lt;some_name&gt;.csv)'
# #st.markdown(href, unsafe_allow_html=True)
