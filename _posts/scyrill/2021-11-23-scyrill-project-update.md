---
layout: post
author: scyrill 
title: "Project Update"
---

# Goal 1: Upload a blank file, then upload a few lines at a time to see where the problem is arising, and see if it can be saved
After the last course, I began copying and pasting small chunks of the txt file into Trinket and it actually started saving! However, because I wanted to get started on writing code, I pasted 6K/550K lines of the txt file, and figured that I could either just work with lines there or paste the rest of the txt file later. I moved on to actually writing out the code and I wrote the following to see if it would open the file and at least print it out: 
```python 
import re
#open and read the file 
pt_notes = open("MIMIC-IIIData.txt", "r")
#print(pt_notes)
```
It worked! This was a small step, but considering that there were issues pasting the txt file, saving it, and opening it in the past, it was something that I was thankful for. From here, I began tackling my goals that I set out to do at the end of class.

# Goal 2: Have Python read through the file and find everywhere that the phrase ‘Discharge Diagnosis’ comes up and print the lines that follow it

To address this goal, I decided to break it up into smaller steps, as reading the file, finding the phrase, and printing the lines that followed it were all different. I began with trying to find the phrase ‘Discharge Diagnosis’  because I thought that it would be the easiest to do because it would just be looking for instances of lines starting with it and it was throughout the entire txt file. I created a for loop so that it would iterate through the entire file and used the `startswith()` function to look for lines that started with ‘Discharge Diagnosis’ and printed the line to make sure that it would work. 
```python 
#look for the lines that have discharge diagnosis 
for line in pt_notes: 
  #figure out why this isn't printing 'final diagnosis'
  If line.startswith(‘Discharge Diagnosis’):
  print (line)
```
It would print all the lines that had ‘Discharge Diagnosis’, which I thought was good, but then I realized that in the file, it also had ‘Final Diagnosis’, ‘Final Diagnoses’, and ‘Discharge Diagnoses’. I learned that the reason why the other phrases weren’t being included was because some of them were in in all capital letters. To solve this, I just included them in a long line that tried to grab all the instances of the word. 

```python 
#look for the lines that have discharge diagnosis 
for line in pt_notes: 
  #figure out why this isn't printing 'final diagnosis'
  If line.startswith(‘Discharge Diagnosis’) or line.startswith(‘Discharge Diagnoses’) or line.startswith(Final Diagnosis’) or line.startswith(‘Final Diagnoses’):
  print (line)
```
I didn’t like the list of ors in the line because it was long, so I thought the best way to capture it in just a few words would be by making all the phrases uppercase and then catching the lines that way. 

```python 
#look for the lines that have discharge diagnosis 
for line in pt_notes: 
  #figure out why this isn't printing 'final diagnosis'
  If line.startswith.upper(‘Discharge Diagnosis’) or line.startswith.upper(‘Discharge Diagnoses’) or line.startswith.upper(Final Diagnosis’) or line.startswith.upper(‘Final Diagnoses’):
  print (line)
```
Not only was this longer, it didn’t work. Therefore, I turned to ```regex``` because I knew that it would at least be able to get it. Since it wasn’t catching the other ‘(blank) Diagnos(i/e)s’, I tried using regex to get all the instances where it begins with ______ Diagnos(i/e)s to get all the instances. To get a regex to do this, I searched the file for lines that started with any character, have a whitespace, accepted ‘diagnos’, followed by any character being acceptable to account for i/e, and end with ‘s’. I turned back to chapter 12 on Regular Expressions, and figured that the way to write the code would be using `re.findall()`. I had used it in the past for homework and exercises, so I figured that it could be used here too.  My code looked something like this: 
```python 
for line in pt_notes: 
  #figure out why this isn't printing 'final diagnosis'
  re.findall(‘.+\s Diagnos.s’):
  print (line)
```
This didn’t work and I thought that it was because of what I put in the parentheses. I changed it to ‘discharge diagnos.s’, but once I did this, the page would not load, so I switched back to the code I had before and gave up on doing this task because I figured that it was something that I could figure out later on. I moved on to making a dictionary or list for the diagnoses to go into later on and went to ch. 9 to see how I could create an empty list. After a couple of tries, I decided to make a list for now, so I introduced one that I intended to take in the diagnoses on the file, but I soon found that I couldn’t append anything into it yet because I still hadn’t found a way to tell Python to get the diagnoses that were usually listed between the final/discharge diagnos(i/e)s and the discharge condition.

This left me kind of fed up with Python and I had to retreat. After doing so, I went to a friend to see how I could break up lines of text in Python and she directed me to https://careerkarma.com/blog/python-attributeerror-list-object-has-no-attribute-split/, where I learned about how to split a list. I tried applying it to my code, this resulted in the the following error: “The attribute file has no split function”. This confused me, how could it not have this attribute when I just saw it used in the website? I asked her why this error was occurring and she said that it was because the file hadn’t been read yet and the file had to be converted to a string. I thought that it had already been converted, so I was doubly confused. I thought that I had that there with the `open((filename), "r")`.  So I scrapped everything and started looking for ways to get Python to read the file to turn it into a string. 

I turned to chapter 8 of our textbook to find out how to read and split the lines in python, along with the following websites: 

https://www.w3schools.com/python/ref_string_split.asp
https://www.kite.com/python/answers/how-to-split-a-file-into-a-list-in-python#use-str-splitlines

However, after doing exactly what the websites told me to do, I couldn’t get Python to read the file anymore and couldn’t figure out why nothing was printing, even though everything seemed to be running smoothly so far. 

I searched up the error and was led to a blog that also said that I needed to read the file also, so I tried introducing another variable that would read the lines in the txt file, and it looked like this: 
```python 
import re
#open and read the file 
notes = open("MIMIC-IIIData.txt", "r")
pt_notes = notes.readlines()

for line in pt_notes: 
  diagnosis = pt_notes.split(‘Discharge Diagnosis’)
  print(diagnosis)
```
This returned the same error, but I figured that it had to do with my putting line.split instead of pt_notes.split, but this was not the error, instead it turned out to be that `readlines()` makes a list, so it couldn’t be split at all because that is not an attribute that lists have, so I changed it from `readlines()` to `read()` and it began to work! However, I caused Trinket to crash once I reintroduced the for loop, so I reached out to my friend again to see why that might be. She mentioned checking if the discharge diagnosis is even in the pt_notes. I didn’t really understand what she meant, so I got rid of everything and went back to the beginning, reading the file. 
```python 
#open and read the file 
notes = open("MIMIC-IIIData.txt", "r")
pt_notes = notes.readlines()
pt_notes.close()
print(pt_notes)
```
This didn’t print anything, to my frustration, until I figured out that the reason it wasn’t printing anything was because I closed the file, so I left it open and changed `readlines()` to `read()`. Once I did this, the file printed everything again. From here, I moved on to putting everything into a list: 
```python 
#open and read the file 
notes = open("MIMIC-IIIData.txt", "r")
pt_notes = notes.read()
diagnosis = pt_notes.split(“Discharge Diagnosis:”)
print(diagnosis)
```
However, this is not what I wanted to do, so I asked my friend, and she told me that, as is, I am telling Python to print the entire file in a list and if I wanted to get python to grab everything after the first instance of ‘Discharge Diagnosis’, I would have to print that position, which resulted in me putting `print(diagnosis[1])`, which wound return the first line after ‘Discharge Diagnosis’ which is the list of diagnoses that I wanted. The next step was to get Python to stop printing right before the phrase ‘Diagnosis Condition’. To do this, I added the following lines: 
```python 
dc = pt_notes.split(“Discharge Condition:”)
print(dc[0])
```
This ended up returning all the lines before ‘Discharge Condition:’, which was partially what I wanted since it didn’t include the phrase ‘Discharge Condition:’, but it was not printing just the diagnoses that I wanted. Some learnings that I gained from this were that with `dc[0]`, it completely cuts ‘Discharge Condition:’ off from the file, whereas the `diagnosis[1]` included what I wanted, so I had to find a way to put them together. I ended up making `diagnosis[1]` a variable and then splitting it in a new variable called `dc`. To have a place to store all this information, I introduced an empty list called `bank` to put the diagnoses. From here, I added the diagnoses to `bank` by using the `append()` function, thus resulting in the following code: 
```python 
#open and read the file 
notes = open("MIMIC-IIIData.txt", "r")
pt_notes = notes.read()
bank = []
diagnosis = pt_notes.split(“Discharge Diagnosis:”)
dd = diagnosis[1]
dc = dd.split(“Discharge Condition:”)
bank.append(dc[0])
print(bank)
```
This finally worked! It returned all the diagnoses, but it included the whitespace character `\n`, which was something I wanted to get rid of. I knew that I could use `strip` to take out the whitespace, so I tried using `rstrip()` to do so. I chose to do this by introducing another variable called `entries`, attaching `rstrip()`, and putting into what I wanted it to strip out of the list. 
```python 
entries = bank.rstrip(“[0-9]\n”)
print(entries)
```
From this error, I learned that lists don't have the attribute `rstrip()`, so things cannot be stripped from lists like I thought they could be. Because of this, I had to scrap this idea and instead introduced another variable that would call `dc` and split it at the whitespace characters: 
```python 
d1 = dc[0].split("\n")
bank.append(d1)
print(d1)
```
# Goal 3: When it finds the phrase ‘Discharge Diagnosis’, ‘Final Diagnosis’ or ‘Final Diagnoses’ it should return the list of diagnoses that follow it, add it to the dictionary (or make a list of these things), and stop printing lines when it finds the phrase ‘Discharge Condition’ Upon finding these lines that detail the diagnosis, I should be able to find out the exact diagnoses that need to be defined in the dictionary.

I chose to modify this goal this little bit by just looking for 'Discharge Diagnosis' and creating a list that iterates through the entire file and returns the diagnoses that are between 'Discharge Diagnosis' and 'Discharge Condition'. To do this, I created a for loop that would go through the file and return the diagnoses.

```python 
#create a for loop that iterates through the file and pulls out the diagnosis
#start at the first position
for diagnosis in diagnoses[1:]: 
  discharge_diagnoses = diagnosis
  #recognize and stop once it sees the phrase 'Discharge Condition'
  discharge_condition = discharge_diagnoses.split("Discharge Condition:")
  
#iterate through the strings in the list and split them
  #split the whitespaces
  condition_list = discharge_condition[0].split('\n')
  
#create a for loop that goes through the conditions in the condition list and returns only the condition
  for condition in condition_list: 
    #create a statement that says if the condition isn't an empty string and is a numeric at 
    #the first position then proceed
    if condition != '' and condition[0].isnumeric():
      #use regex to find all the whitespace characters on the line
      term = re.findall('\s.+', condition)
      #pull out the spaces in the line 
      terms = term[0].strip()
      #print the conditions
      print(terms)
```


# Final Project Progress Copy
<iframe src="https://trinket.io/embed/python/d081208c70" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


After going through all of these errors, I think it helped me learn a lot both about writing code myself, in that things aren't as simple as I think they are and being able to see what the code is doing is important in solving issues. I did get to eventually use regex, but only after all the roadblocks that I ran into in doing this. 

# Next Steps
1. Go through the terms and remove anything that might be duplicates or making one common term for both of them (ex. COPD exacerbation and Chronic Obstructive Pulmonary Disease Exacerbation)
2. Create a dictionary for diagnoses 
3. Look for the definitions of the illnesses and input them as strings
4. Create an area for the user to input the diagnosis that they want to know more about  and if there is no entry for what they want to know, including an option for them to enter something else
