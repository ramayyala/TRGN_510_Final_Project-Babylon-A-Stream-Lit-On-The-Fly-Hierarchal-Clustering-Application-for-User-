# Final Project Outline
## Title
Babylon: A Stream-Lit On-The-Fly Hierarchal Clustering Application for User Gene Lists
## Author
Ram Ayyala 
## Overview of Project
I will create a stream-lit application that allows the user to input a set of genes from a specific pathway.
  Ex.)https://www.gsea-msigdb.org/gsea/msigdb/genesets.jsp
The application will then carry out hierarchal clustering on the gene set with the sample set using [scipy's cluster.hierarchy module](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html) and create a heatmap/dendrogram of the inputted gene set with a set of pancreatic cancer FPKMs on the fly and output a heatmap/dendrogram for the client. I also add a covariate option that will allow for users to add in covariates such as gender, ethnicity, race, AJCC pathologic stage of sample, and cigarettes per day.  
This application will be written in python using the [streamlit API](https://streamlit.io/) 
## Data
I will be using the data from the [National Cancer Institute GDC Data Portal](https://portal.gdc.cancer.gov/). I will using a total of 446 FPKM files, which were gathered from 385 cases of pancreatic cancer, of which 325 are from Primary Tumors sample types, 68 samples are from Next Generation Cancer Model sample types, 50 are Solid Tissue Normal sample types, 2 from metastatic sample types and 1 from Expanded Next Generation Cancer Model. These specific files are available [here](https://portal.gdc.cancer.gov/)
## Milestone 1
**Due Date:** Thursday November 11th
Hierarchal Clustering base code will be completed in base python on a notebook
## Milestone 2
**Due Date:** Tuesday November 23rd
Initial analysis pipeline for hierarchal clustering will be completed on streamlit 
## Deliverable
**Due Date** December 3rd: 11:50pm
Completed streamlit app with user input function built in and working on the fly hierarchal clustering analysis completed 
 