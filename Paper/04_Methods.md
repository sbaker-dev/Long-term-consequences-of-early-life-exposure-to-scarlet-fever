
---

## Methods

### Study sample

Data on participants were obtained from the UK Biobank, application reference 41382, a prospective cohort study of UK adults aged 40-69 at the time of recruitment in 2006 to 2010 whom where within 25 miles of an assessment center^[@Littlejohns2019]^. The UK Biobank has detailed data from its baseline questionnaire, linked data such as the Hospital Episode Statistics (HES)^[@Davis2018a]^, and subsequent longitudinal follow-up, but has collected relatively little information exists on individuals’ early life circumstances. We addressed this limitation by linking regional disease incidence data from the Registrar-General’s Weekly Returns of notifiable diseases.

### Disease incidence rates

To construct incidence rates, we used participants birth coordinates to assign them to one of the 1472 Local Government Districts from the 1951 census using a shapefile of England and Wales from Vision of Britain^[@Project2011]^. We extracted each districts counts of cases of scarlet fever from the Registrar-General’s Weekly Return^[@Office]^, and calculated the incidence rates using population estimates from the Great British Historical Database on Health and Health  Care^[@Ell2020]^. To allow for changes to districts over time, we standardised all district data to the 1951 census; more information is provided in the supplementary material. 

We created regional incidences of scarlet fever up to the age of ten. Scarlet fever is mostly a childhood disease commonly found between the ages of 2-10^[@Mahara2016]^, peaking between the ages of 4-6^[@Lu2019]^. We constructed each participants exposure to scarlet fever at a given age by summing up the exposure in the 52 weeks from the first full week of the year and month of birth. We construct the average regional exposure to scarlet fever by the ages of one, five, and ten, constructed as the mean of the annual exposure rates. For example, the average exposure by age five is the average of the rate of annual exposure at ages one to five. 

### Sample selection

**Figure 2.** PRISMA plot of sample selection

[Figure 2 HERE]

We selected our sample as outlined in Figure 2. Data from the Registrar General Weekly Reports on Notifiable
Diseases only contains information on England and Wales, UK Biobank participants born outside these nations (n = 39 488) were therefore excluded. We linked regional disease incidence rates using birth coordinates so excluded participants (n = 57 799) when these were not available.   

Scarlet fever is treatable with penicillin which was introduced for public use in 1946 but had also been used in limited situations before this in hospitals^[@Gardiner2016]^. Individuals born before the introduction of penicillin would have faced a different disease environment compared to those born after. The Second World War also complicates the assignment of individuals to districts. Almost 1.5 million citizens, mostly children, pregnant women, and the disabled were evacuated to rural areas of the country from 1939^[@Smallman-Raynor2015]^. 

To reduce measurement error relating to the incorrect assignment of districts, as well as the differing disease environment individuals would have faced pre-penicillin, individuals born before penicillin’s introduction to the civilian population in June 1946 are excluded (n = 122 177). Finally, as we construct averages to age ten, we require all individuals to have ten years of disease incidence data. We therefore, only include individuals born between 1946 and 1961, leading to our analysis sample of 215 492. 

### Statistical analysis

We estimated the association of regional incidence of scarlet fever and each later life outcome using linear regression clustering the standard errors to the district. As shown in Figure 1, scarlet fever was much more common in the earlier years of our sample, potentially confounding our estimates. We controlled for this using year of birth indicators. We define the year to start in September of year t until August of year t+1. This ensures that each year is specific to the scarlet fever season^[@Lamagni2018]^, potentially capturing particular strains of scarlet fever that are in circulation in that year. We also control for month of birth and gender. 
 
Furthermore, scarlet fever is more common in lower socio-economic and rural areas^[@Falkingham2016]^. Hence, the estimate from a regression that controls for year and month effects may be partially driven by the variation of the socio-economic composition between local areas that is correlated with scarlet fever infections. To address this, we add in indicators for each of the 1472 districts of birth, allowing us to compare individuals exposed to a high rate of scarlet fever to those born in the same district, but exposed to a lower rate of scarlet fever due to their month of birth and birth cohort.
