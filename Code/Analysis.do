/*
Author : Samuel Baker
Version: 1.3.0
Date   : 26/07/2021
Paper  : Long term consequences of exposure to Scarlet Fever
Purpose: This script sets up the environment for our analysis and then runs our
	     regressions to produce the output for our tables.
Notes  : For this script to work you need to set the global environment 
		 variables. You can do this within this file, or you can create another
		 do file with the following content:
		 
		 DoEnv.do
		 global project_dir "PATH_HERE"
		 global log_dir "PATH_HERE"
		 
		 This script also gas the following Dependencies, that can install by 
		 coping these lines and placing them in the command bar.
		 
		 ssc install reghdfe
*/

* Load the Analysis sample
set more off
import delimited "$project_dir/ScarletLong.csv"

* District Fixed effects and standardise fluid_intelligence / Educational attainment
egen dfe = group(did)
egen fi = std(fluid_intelligence)
egen eu = std(eduyears)
rename id ID

* Set our phenotype and exposure globals
global y_list rd v ami ihd stroke cvd eu fi
global scarlet_average sfa_1 sfa_5 sfa_10

* Write out the summary statistics for the exposures
log using "$log_dir/Summary.log", replace
sum $scarlet_average $y_list
log close

* Note tabulations for paper write up
log using "$log_dir/Tab.log", replace
foreach var of varlist $y_list{
	tab `var'
}
log close

* Write the Average Exposures
log using "$log_dir/Averages.log", replace
foreach y of varlist $y_list{
	foreach exp of varlist $scarlet_average{
		reghdfe `y' `exp' gender, absorb(i.mob i.sepyob i.dfe) cluster(dfe)
	}
}

log close

