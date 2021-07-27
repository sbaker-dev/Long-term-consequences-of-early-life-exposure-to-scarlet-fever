---
title: Long term consequences of early life exposure to scarlet fever
author: Samuel Baker*, Neil Davies, Frank Windmeijer, and Stephanie von Hinke
csl: C:/Users/Samuel/PycharmProjects/ProjectPlanner/CLS/elsevier-vancouver.csl.txt
---


## Supplementary Information

### Supplement 1: Cardiovascular definitions

Definitions of heart disease are taken from the ICD 9 and 10 codes from the diagnosis and death registrar. AMI is constructed from I21-22, IHD including I21-25, stroke from I6 and G45, with cardiovascular disease being all codes within I as well as G45 as previously^[@Carter2019]^ Given the valvular nature of many of the complications that can follow a preceding infection, Non-Rheumatic damage to any of the valves is created based on I34-38 with Rheumatic damage being from I0. The full list of codes for ICD 9 and 10 are within the github link of [this papers repository][PaperRepo] and can be reconstructed via [ICDBioAssign][ICDB] to replicate our construction with your own Biobank Application.


### Supplement 2: Weighting Data to a base Year

Districts from 1931 to 1971 change multiple times, and our empirical specification is utilising within variation. To maximise our within variation, we want to standardise the districts boundaries to a single definition so that individuals born in the same settlement are comparable across the whole study period. To do this we use [weightGIS][WGIS], and standardise our districts to the 1951 census definition of districts. As we have parishes available, we use parish level population data for our weights. Once our weighting parameter is set, we then use these weights on data from 1941-1973 from the Registrar-General’s Weekly Return^[@Office]^ and Great British Historical Database on Health and Health Care^[@Ell2020]^. This weighted data is linked to the districts, which individuals have been assigned based on their birth coordinates. We can then use individuals year and month of birth to iterate forward 52 weeks to construct the first year's exposure and so on. 

 
[WGIS]: https://github.com/sbaker-dev/weightGIS
[ICDB]: https://github.com/sbaker-dev/ICDBioAssign
[PaperRepo]: https://github.com/sbaker-dev/PAPERHERE

### References