# Long-term consequences of early life exposure to scarlet fever

## Purpose
This is the repository for the work undertaken on investigating the impact of early life regional exposures to scarlet fever on later life cardiovascular disease, fluid intelligence, and educational attainment. **This repository has the following structure:**

### Code
* Analysis.do
    * This contains the code used to format the data to run the analysis in stata, as well as the analysis itself
* create_figures.py
    * This script takes the log files created from stata and creates figures for the paper via pyBlendFigures.
* Formatting.ipynb 
    * Used to construct the data for analysis in stata via python in a Jupyter Notebook.

### External Files
* Definitions.csv
    * This contains the ICD 9 and 10 codes that where used to construct the definitions of the multiple forms of cardiovascular disease

### Figures and Tables
* BlendFigures
    * This folder contains the figures that where made in pyBlendFigures for the paper. Each figure is represented as a csv, an image of type .png, and a .blend that can be used to make micro adjustments. 
* LogFiles
    * This contains the raw logs from the analysis. The only thing that has been changed is to censure the file path usually found at the top of the bottom after ***Log: F:/File/Path/Here***
    
### Paper
* This contains all the raw markdown files that where used to construct the paper via pandoc. 

## Abstract

### Background
Exposure to Streptococcus pyogenes (S. pyogenes) in childhood, which causes, amongst others, strep throat and scarlet fever, has previously been shown to increase the risk of heart disease and acute rheumatic fever. Rates of scarlet fever have recently risen to the highest levels in the UK since the 1960s, yet few studies have been dedicated to investigating the potential long-term effects using scarlet fever rates. 
 
### Methods
We linked birth locations from UK Biobank participants to regional data on weekly disease notifications of 
scarlet fever from the Registrar-General’s Weekly Returns. We calculated the average incidence of scarlet fever at the ages of one, five, and ten years old. We estimated the associations of early life exposure to scarlet fever and later life cardiovascular health, fluid intelligence and educational attainment.

### Results
We analysed 241 685 individuals born between 1946 and 1971 who were sampled by the UK Biobank.
An additional case of scarlet fever per 100 population in the district of birth by the age of 10 was associated with 7.25 additional cases of ischemic heart disease per 100 individuals.

### Conclusions
Participants who experienced higher incidence of scarlet fever in early childhood had higher risk of ischemic heart 
disease later in life. 

### Keywords
Cardiovascular Disease; Scarlet Fever; UK Biobank;
 
### Key Messages

* Incidence of scarlet fever in childhood associates with later life ischemic heart disease
* Recent rises in scarlet fever seen in the UK may have long term repercussions 

