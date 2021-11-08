---
layout: post
author: scyrill 
title: "Stephanie's Final Project Idea"
---

For my final project, I want to try making a medical dictionary using Python. I am hoping to do this using MIMIC-III data, which is a free dataset on patients that were hospitalized at Beth Israel Deaconess Medical Center between 2001-2012. In this data, there is a downloadable CSV file called ’NOTEEVENTS’ that is basically patient notes. These notes provide valuable information on what the patient went through as they were in the hospital, the progression of their illnesses, medication they received, and the final diagnoses. Though there is a wealth of information here, I wanted to focus on the final diagnoses to use in my medical dictionary. By having them, I wanted to define what the diagnoses were using what we learned in the dictionaries section of class. To find this, I would have to get Python to do the following: 

- Read through the file 
- Search for the term ‘Discharge Diagnosis’ and print the diagnoses underneath it, but have it stop at the last diagnosis (some are in a list) —> this might have to be stopped at ‘Discharge Condition’
- Make sure that only the diagnoses are returned
- Count the number of times a certain diagnosis comes up as it would give insight into the top illnesses, but also lets me know which diagnoses will need to be defined 
- Have a dictionary that defines each diagnosis
- Have the users put in a diagnosis or illness that they are curious about and Python returns it 

As the end product of this project, I would like for the user to be able to input a diagnosis into Python and have it return the diagnosis definition, along with symptoms associated with the disease. I wanted to do data analysis because I am interested in finding a way to use Python to parse through a large text file, extract key words (in this case the diagnosis), take note of them, and define them. If time allows for it, I would also like to explore ways that I can use Python to make predictions on what the disease diagnosis might be based on the symptoms listed, or at least the top five illnesses it could be based on the symptoms that are input by the user. Though this would be interesting, this might require some tuning to get right. 
