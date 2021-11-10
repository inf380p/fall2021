---
layout: post
author: acreese
title: "Alex Reese's final project idea and work plan"
---

### Project Idea

I plan to pursue a data analysis-based final project, focusing specifically on native plant data from the USDA’s PLANTS Database which provides standardized information about the vascular plants, mosses, liverworts, hornworts, and lichens of the U.S. and its territories. Plant Science was one of my undergraduate majors, and I am still very passionate about native plant botany, taxonomy, and gardening. 

The specific datasets I plant to use are comma-separated “NRCS State Plants Lists” for each U.S. American state and territory – found at <https://plants.usda.gov/home/downloads>. Each file contains structured information for every native plant species including Symbol, Synonym Symbol, Scientific Name (genus and species) with Authors, preferred State Common Name, and taxonomic Family. By parsing the data in these files, my program will allow users to return information like the number of unique families and species, the number of species with and without common names, the most prevalent/diverse plant families and genera, and perhaps even the most common elements of common names of the native plants of  individual states and perhaps even compare the date from different states. 

### Initial work plan

1. Pick model file to build code around. 
2. Write code to open and read in the text file, write loops to read file line-by-line and split on commas
3. Develop and apply regex formula to separate Scienctific Name from Author information
4. Build dictionaries and lists to enumerate and store data
5. Incorporate a third-party data visualization module
6. Create functions that allow users to retrieve/output summary statistics and data visualizations
7. Create help function and text
