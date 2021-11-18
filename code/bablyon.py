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
#data="../data/Hugo_data.csv"
@st.cache
def load_data():
    df = pd.read_csv("../data/Hugo_data.csv")
    return df
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
#load_data()
#df = pd.read_csv("../data/Hugo_data.csv")
df = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df[1:100])
user_input = st.text_area("Gene Set", "ABCC6 ABCC8 APPL1 ASXL1 B9D1 B9D2 BICC1 BLK CASR CC2D2A CCND1 CDKN1C CEL CEP290 CEP55 CFTR CNOT1 CP CPA1 CSPP1 CTRC DIS3L2 DNAJC21 DYNC2I1 DZIP1L EFL1 EIF2AK3 ENPP1 FANCD2 FLI1 FLNB FOXF1 GABRD GANAB GATA6 GCK GLIS3 HNF1A HNF1B HNF4A IGF2 INS KCNAB2 KCNJ11 KCNQ1 KCNQ1OT1 KLF11 LHX1MKS1 MYCN NEK1 NEUROD1 NPHP3 OFD1 PAX4 PDX1 PKD1 PKD2 PKHD1 PRDM16 PRSS1 PRSS2 PTF1A PTRH2 RARB RBM8A RECQL4 RERE RFX6 RPGRIP1 RPGRIP1L SBDS SETBP1 SIK3 SKI SLC29A3 SPINK1 SRP54 STAT3 STRA6 TCTN2 TELO2 TMEM107 TMEM216 TMEM231 TMEM67 VHL WDPCP WDR19 XPNPEP3")
#user_input = st.text_input("Gene List", 0)
gene_list = user_input.split()
#Uploading geneset
STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""

FILE_TYPES = ["csv", "txt", "tsv"]


class FileType(Enum):
    """Used to distinguish between file types"""

    IMAGE = "Image"
    CSV = "csv"
    PYTHON = "Python"


def get_file_type(file: Union[BytesIO, StringIO]) -> FileType:
    """The file uploader widget does not provide information on the type of file uploaded so we have
    to guess using rules or ML. See
    [Issue 896](https://github.com/streamlit/streamlit/issues/896)

    I've implemented rules for now :-)

    Arguments:
        file {Union[BytesIO, StringIO]} -- The file uploaded

    Returns:
        FileType -- A best guess of the file type
    """

    if isinstance(file, BytesIO):
        return FileType.IMAGE
    content = file.getvalue()
    if (
        content.startswith('"""')
        or "import" in content
        or "from " in content
        or "def " in content
        or "class " in content
        or "print(" in content
    ):
        return FileType.PYTHON

    return FileType.CSV


def main():
    """Run this function to display the Streamlit app"""
    st.info(__doc__)
    st.markdown(STYLE, unsafe_allow_html=True)

    file = st.file_uploader("Upload Gene set", type=FILE_TYPES)
    show_file = st.empty()
    if not file:
        show_file.info("Please upload a file of type: " + ", ".join(FILE_TYPES))
        return

    file_type = get_file_type(file)
    if file_type == FileType.IMAGE:
        show_file.image(file)
    elif file_type == FileType.PYTHON:
        st.code(file.getvalue())
    else:
        gene_list = open(file).read().splitlines()
        st.dataframe(gene_list.head(10))

    file.close()


main()


#st.write(gene_list)
df_selected=df[df['gene_id'].isin(gene_list)]
#st.write(df_selected)
df_selected = df_selected.set_index('gene_id')
df_selected=df_selected.astype('float16')
if st.checkbox('Log scale'):
    #Log Scale the selected data
    df_selected = (1+df_selected)/2 # (-1,1] -> (0,1]
    df_selected=np.log(df_selected)
color_option = st.selectbox('Color', ("mako", "RdBu","vlag"))
fig=sns.clustermap(df_selected, metric="euclidean", standard_scale=1, method="ward",cmap=color_option)
st.pyplot(fig)

# Download clustermap
    # look into kwargs arg on pyplot for plt.savefig option
# Download selected data_table Option
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
csv = convert_df(df_selected)
st.download_button(
    label="Download selected data as CSV",
    data=csv,
    file_name='selected_data.csv',
    mime='text/csv',)


#csv = df_selected.to_csv(index=True)
#b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
#href = f'<a href="data:file/csv;base64,{b64}">Download Selected Data</a> (right-click and save as &lt;some_name&gt;.csv)'
#st.markdown(href, unsafe_allow_html=True)
