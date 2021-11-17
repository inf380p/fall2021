---
layout: post
title: "Stephanie's Project Interface"
author: scyrill
---

# Pre-Project Cleanup → Reflection on Data Clean-Up 11/10
Since I had a very large dataset from MIMIC-III (~1M entries), I had to do some data cleanup to make it usable for my project. To clean up my dataset, I deleted some of the columns as I just wanted to focus on the doctor’s notes on the patient’s file. Then I searched the dataset to see how many of these entries actually used the word ‘diagnosis’. I did this because I wanted to know if this could be a way to condense the dataset that I had and it turned out that only 30% of the data actually used the word ‘diagnosis’, so I considered finding ways to remove the rows that didn’t have that word. I knew that this might be possible in Excel, so I exported the dataset to Excel and looked at ‘Conditional Formatting’ to see if I could create some if-then statement that would power through the deleting of rows for me. However, I soon found that it was also too much information for Excel and I didn’t know how to write my if-then statement out in Excel to make it do exactly what I wanted. Because of this I asked the professor and he suggested that since the data is not sequential, I could just remove some of the rows, so I selected the first 3k rows to use in this project. After this, I exported the file as .txt so that I could use it in my data analysis. 

# 1. Reading the file: 
To tackle this component of the project, I started by rereading chapter 8.2 on opening files in Python because it was something that I hadn’t had to actually write myself in a while, and this was the result. 

```python 
#open the file 
pt_notes = open(‘MIMIC-III Data.txt’)
print(pt_notes) #testing to see if it will even work, also this is what the book said to do 
```

This was a good start for me and it told me how to open my file, but then I ran into a problem when I moved to testing it on Trinket. When I input what I did, I quickly realized that I didn’t know how to import a file to Trinket, which led me to look up ‘how to import files to Trinket’ and it led me to the Trinket blog (https://blog.trinket.io/add-files-python-trinkets/). This laid out the steps I needed to upload my txt file to Trinket, in which it said I had to press ‘+’ then I uploaded the txt file from my computer. I then moved to opening the file in the main.py tab. I tried this many times, but each time it didn’t work. Since it didn’t work, I thought that maybe the issue lied in the size of my txt file, in which it had over 550k lines to accommodate the 3k patient notes that I uploaded, so I decided to cut down some empty lines on the file in trinket, but it still didn’t work. I kept going to the file to fix things but it turns out that the original file had never saved as a .txt file, so I duplicated it on my computer, saved it as a .txt, and uploaded that to Trinket. After this, I rewrote the name of the file in single quotation marks and changed the title to match what I saved the file as on my computer, and it worked!

```python 
pt_notes = open('Dataset for Python Proj 2k.txt')
print(pt_notes)
```

With this basic step out of the way, I moved to having Python read the file. Again, I found that I forgot the ordering that it should be written to have it read the file because I remembered ```readlines()```, but I forgot where it would go. To solve this, I went back to chapter 8.4 to read about how to write code that reads files and this was the result: 

``` python
note_events = open('Dataset for Python Proj 2k.txt')
pt_notes = note_events.read()
print(pt_notes)
```

# How it is going so far...
![image](https://user-images.githubusercontent.com/92882368/142267543-afed5947-2937-4b34-ac5a-eb70931c8c6b.png)

# Text File 
![image](https://user-images.githubusercontent.com/92882368/142267594-4fe3420b-8cde-4165-8a4b-afbaf03e0632.png)

Though this was a good start, I noticed that it was taking Trinket a long time to return the ```pt_notes```, and this was a problem that kept persisting. I figured that it might have something to do with the amount of rows that I had (3k), so I decided to chop it down by 1k and re-upload it to Trinket and hope that it would work, and it worked! From here, I could get Trinket to open the file, read it, and print out the entire thing, but I ran into problems again when it came to saving it. Continually I got the error that it couldn't be saved and I couldn’t figure out why, so I reached out to the professor to see why this might be. He suggested making a blank file and then uploading the file a few lines at a time, which I plan to do next. 

# Copy of my code
<iframe src="https://trinket.io/embed/python/d081208c70" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Next Steps…
For the next steps in my project, I plan to tackle the following before the next class: 
1. Upload a blank file, then upload a few lines at a time to see where the problem is arising, and see if it can be saved 
2. Have Python read through the file and find everywhere that the phrase ‘Discharge Diagnosis’ comes up and print the lines that follow it
3. When it finds the phrase ‘Discharge Diagnosis’, ‘Final Diagnosis’ or ‘Final Diagnoses’ it should return the list of diagnoses that follow it, add it to the dictionary (or make a list of these things), and stop printing lines when it finds the phrase ‘Discharge Condition’ 
Upon finding these lines that detail the diagnosis, I should be able to find out the exact diagnoses that need to be defined in the dictionary. 

# Interface Sketch
![image](https://user-images.githubusercontent.com/92882368/142267937-2393f887-2e4c-4c54-81c3-6c35b2384796.png)
![image](https://user-images.githubusercontent.com/92882368/142267960-6984cd67-09ec-4bc2-a162-e59fd96cf40c.png)
