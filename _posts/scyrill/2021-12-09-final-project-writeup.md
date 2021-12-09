---
layout: post
author: scyrill
title: "Stephanie's Final Writeup"
---
Last time, the professor helped me build a dictionary for the final diagnoses, so I attempted to begin building out others that would return other things from the patient notes. I started by creating dictionaries that were almost the same, but would only open up if we were collecting for that information. For example, ```collecting_medications``` would only be True if the line started with ‘Medic’, and so on. I started with the basic structure that was made when I last met with the professor because I thought it would be easy to implement these changes and that all I had to do next was creating similar logic with a chain of elif statements where I would say if line starts with (blank) then some information would be stored in my other note dictionaries, but this would all be contained in the same initial for statement.  After writing out what the previous code did, I got a better grasp on what it was doing and tried writing the same logic to find medications: 

```python 
for line in pt_lines:
  if line.startswith('"Admission Date:'):
    # We have a new note
    if current_note != {}:
      notes_list.append(current_note)
    
    #current_note = {}
  else:
    # We're continuing a note
  if line.startswith("Med"):
    medications = []
    collecting_medications = True
  elif collecting_medications and line not in ['\n','.\n']:
    medications.append(line)
  elif collecting_medications and line in ['\n','.\n']:
    collecting_medications = False
    current_note["medications"] = medications

for note in notes_list:
  print("Medications used were:\n"," ".join(note["final_diagnoses"]))
```

While this did end up printing the medications, it was just repeating the same set of medicines when there were more in the text file. Because of this, I went back to the original code to see why there were repetitions because this didn’t happen before. Tracing back my code, I found out that since I commented out ‘current_note = {}’, there was no dictionary that it was entering the medications into, so I re-introduced it and it began to run well, but I did get a syntax error as well when I reintroduced my code for medications into the program. I didn’t understand why this was, so I printed out the ```notes_list``` to see if it was at least finding the medications in the file like I wanted it to and it was. I knew that I needed to pull them out of the list, so I thought the best way to do this would be creating a new medical dictionary that’s not ```current_note```. In the meantime, I decided that it would be easier to write some prompts outside of the loop that could correlate with the user choosing what they would like to know from the patient notes. As I did this, however, I knew that I still had a long way to go for creating the other dictionaries, and doing this in the meantime was only prolonging the inevitable. Therefore, after entering the new prompts around the code, I tried address the medications dictionary again in the following way:

```python
#!/bin/python3
import re
#open and read the file 
notes = open("MIMIC-IIIData.txt", "r")
#prompt the user to enter in a number that relates to something they'd like to know 
welcome = input("Hello, what would you like to know about the patient notes today? Enter a number that corresponds with a field.")

notes_list = []
current_note = {}
collecting_diagnoses = False
collecting_meds = False

pt_lines = notes.readlines()
for line in pt_lines:
  if line.startswith('"Admission Date:'):
    # We have a new note
    if current_note != {}:
      notes_list.append(current_note)
    
    current_note = {}
  else:
  # We're continuing a note
    if line.startswith("FINAL DIAGNOS"):
      diagnoses = []
      collecting_diagnoses = True
    elif collecting_diagnoses and line not in ['\n','.\n']:
      diagnoses.append(line)
    elif collecting_diagnoses and line in ['\n','.\n']:
      collecting_diagnoses= False
      current_note["final_diagnoses"] = diagnoses
#make a dictionary for medications within pt_notes for loop   
for note in notes_list:
  print("Final Diagnoses for this patient were:\n"," ".join(note["final_diagnoses"]))
  
if line.startswith("Med"):
  medications = []
  collecting_meds = True
elif collecting_meds and line not in ['\n','.\n']:
  medications.append(line)
elif collecting_meds and line in ['\n','.\n']:
  collecting_meds = False
  current_note["medications"] = medications

#for note in notes_list:
 # if input == '1': 
  #  print(notes["diagnoses"])
  #elif input == '2': 
   # print(notes["medications"])
#  elif input == '3':
 #   print(notes["condition_list"])
  #elif input == '4':
   # print(notes["word_frequencies"])
#else: 
 # print(input("Sorry, looks like we don't have that information yet. Would you like to enter a different number?"))

#response = input == 'Y' or 'Yes':
    #print('What would you like to know more aboout?')
  #print("Final Diagnoses for this patient were:\n"," ".join(notes["medications"]))

input()

notes_dict = {}
notes_dict["medications"] # => list of medications
notes_dict["prior_history"] # => string of narrative history
notes_dict["word counts"] # => list of all narrative sections with word counts
notes_dict["condition_list"] # => only the conditions that appear in this note

medical_bank = []

#read through the pt notes and have it recognize 'Discharge Diagnosis'
diagnoses = pt_notes.split("Discharge Diagnosis:")

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

However, when I did this, the medication dictionary was still not printing. Because I thought there might have been a problem with my code, I moved all that information to another Trinket and tried starting from a blank slate, only including the code that I had written for medications. I did this because I wanted to see if there was a bug in the specific block of code that I wrote and figured this would be a good way of quickly seeing what was going on without encountering major errors from the larger code. When I isolated the block of code, it worked!

```python
#!/bin/python3
import re

notes = open("MIMIC-IIIData.txt", "r")

notes_list = []
meds = []
current_note = {}
collecting_diagnoses = False
collecting_meds = False
collecting_frequencies = False
collecting_conditions = False

pt_lines = notes.readlines()
for line in pt_lines:
  if line.startswith('"Admission Date:'):
    # We have a new note
    if current_note != {}:
      notes_list.append(current_note)
      
      current_note = {}
  
  else:
    if line.startswith("Med"):
      meds = []
      collecting_meds = True
    elif collecting_meds and line not in ['\n']:
      meds.append(line)
    elif collecting_meds and line in ['\n','.\n']:
      collecting_meds = False
      current_note["medications"] = meds
  
for note in notes_list: 
  print("Here are some medications used:\n"," ".join(note["medications"]))
```
    
While this was nice, I began to think about using nested for loops or if statements so that I could just return information for that dictionary (i.e. having it return diagnoses when the notes for it was called, conditions, etc.). I am not sure if this can all be in the same loop, but I thought I could do it, so that it could be connected with the user input later on, so for the time being, since all the code would be relatively the same, I divided it into different tabs so that I could focus better and find a way to pull it all together later on. Splitting the parts of the code up was helpful for me because I didn’t get overwhelmed and it was easy to figure out what was going on in each one because I could run it. This gave way into me creating the different blocks of code that would eventually be in the larger code and attain my goals. 

# Return word frequency, the number of words in a given note, the section headers, and the total number of words in a file
I went back to the textbook to find out how to make a counter in a dictionary and found that that was covered in 10.2 and 10.3, but since I was more interested in the number of words in a note, 10.3 was more helpful for extracting that information. I ended up with the following code for this: 
```python
counts = {}
for line in notes:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] + 1
for w in sorted.counts[int(begin):int(end)]:
  print("Here is the words and frequencies for the index you entered:\n", w)
```
This achieved the goal of returning the frequency of words, and I decided to arrange the numbers in ascending order based on the frequency. This meant ordering the dictionary by the values and I thought this could be achieved by adding another for loop, but when Trinket crashed a couple of times, it made me ask myself, how many for-loops can I introduce? How many are too many? After googling it, I found that while there was around 500 loop limit, maybe there was another way that I could go about ordering by values. I remembered doing coding exercises on this in the past, so I went to the book again and came upon how to order dictionaries by values in 11.6. From the examples, it turned out that I didn’t need to include another for loop, but that I could use ```sort()``` outside of the for loop and that would return the values in descending order. From this, I learned what words were used the most in the notes, but I wanted to build on it more, so I created an input command from the user so that they could select the index start and end points and had Python print out the words that fell in that index. At first, I didn’t think it would work, but to my surprise, it did! While it did work, I wanted Python to politely return the words selected by having a message followed by the words and their counts. I tried doing this by adding

```python
print("Here is the words and frequencies for the index you entered:\n", w)
```

However, since it was in a for loop, this line printed for every word when I really just wanted the phrase to appear once and have the words under it. I knew how to do this because it’s what I worked on with the professor for the diagnoses, so I went back to it to see what he did to print that information out nicely in Python. That previous one printed nicely because it was looping through the notes in the file, and while it was still analyzing lines like this one was, it wasn’t the same. To solve this, I took the print statement out of the for loop and put it above it, so that the user would just the phrase and the list of words that are in the range that they selected. 

I then moved on to finding out how to count the number of words in the patient note, but to do that, I would first have to find a way to isolate/split patient notes from one another. I already knew that each patient note was divided by the phrase ```”Admission Date:```, so building off of that, I created a function called ```assigning_notes``` that would look for the lines that had the phrase '"Admission Date:' and split the file up into separate components, or notes. To do this, I would prompt the user to input a random number, and when they do so, Python would open up the entire txt file that I am using, read through the lines, split the lines in the file based on the key phrase '"Admission Date:', convert the user’s input into a number and return the requested note. 

```python
def assigning_notes():
  patient_num = input("Enter a number to return a patient note:")
  notes = open("MIMIC-IIIData.txt", "r")
  pt_lines = notes.read()
  notes_assigned = []
  splitter = pt_lines.split('"Admission Date:')
  print(splitter[int(patient_num)])
  return splitter[int(patient_num)]
```

This function was primarily created so that the user could look at and explore one patient note at a time in the file, but I soon found that it could also be used to find other information as well. I created two other functions that would return the total number of words in a patient note, along with the headers in the notes, called ```word_totals``` and ```grab_headers```, respectively. To find the total number of words in a patient note, I wrote the following: 

```python
def word_totals(words): 
  x = words.split('\n') 
  words_inline = 0
  for line in x:
    split_lst = line.split(' ')
    for word in split_lst: 
      if word.isalpha():
        words_inline += 1
  print("The total number of words in this file is:", words_inline + 2)
  ```

The function takes in the argument ```words```, and it splits the words based on the newline character in the list. I had it split on the newline characters because this would indicate the start of the newline and since they were all over the file, I didn’t want it to contribute to the word count, ```words_inline```. I then moved on to creating a for loop that would go through this list again and split wherever there was a space in the list and I used the function ```isalpha()``` to only look for alphabet characters. This was done so that numbers and punctuation wasn’t included in the final count of words in a patient note. How does this tie in with the function ```assigning_notes()```? Well, when the user input that they wanted to know more about the word count in a patient file, it would first go through ```assigning_notes()``` to get a patient file and then it would count the number of words in the file. 

```python
   elif patient_info == '4':
     word_totals(assigning_notes())
```

This same idea of putting functions as arguments was something that I did with the other defined function, ```grab_headers```. When I wrote this code, I just wanted to return the number of headers in the file, but this returned a long list of section headers that would be useless to the viewer, so I found that there could be a way to just return headers in a patient note by similarly taking in ```assigning_notes()``` as an argument for ```grab_headers```. To first go to the function that I wrote for ```grab_headers```:

```python
def grab_headers():
  for line in pt_lines:
    line = line.rstrip()
    x = re.findall('^.[A-zZ].+:', line)
    if len(x) > 0:
      print(x)
```

Essentially in this function, I wanted to find a way to return all the headers in the file. I noticed when going through the file earlier that many of the headers were the same, but some were written with a combination of capital and lowercase letters, thus causing some of them to not be returned. To fix this, I used regex to go through each line, find where lines started with a capital letter, but was followed by any letter and a colon, and if the length of the word wasn’t 0, it would print. When applying this to the larger code, when the user would input that they wanted to know more about the headers in a patient note, ```grab_headers``` would call ```assigning_notes()``` as an argument. 

```python
    elif patient_info == '3':
      grab_headers(assigning_notes())
```

Doing this would prompt the user to input a specific patient note that they want the headers for and it would return that. I found that it was actually pretty fun to define functions and have them call one another as it made my job easier. Before, I thought that this would be super complicated to write out, but as I did it in small chunks, I found that it was easy and not that overwhelming. For my last, and ironically first function, I created the function that would look for the total number of notes in a file. I just wanted to return the total number of notes that were in my file as I thought it could be useful information for the user because many people may wonder how many patient notes are actually contained in this txt file. To find the total number of notes, I wrote the following: 

```python
def note_total():
  note_count = 0 
  pt_lines = notes.readlines()
  for line in pt_lines:
    if line.startswith('"Admission Date:'):
      note_count += 1
  print("The total number of notes in this file is:", note_count)
```

This was great at returning the number of patient notes, which was 244, as it specifically looked for lines that started with '"Admission Date:', which indicated a new note, and counted how many times it ran into that phrase, and that gave me the number of patient notes present. 

# Prompting the User
Having created all of these, the next step was to return back to the user prompts and write them out. I started by welcoming the user and having them select what they would like Python to return by assigning different parts to different numbers. Though I initially started with a short list, I found that there was so much more that the user could extract from the file, so I numbered different information from 1-8, with a subset of assigned numbers that the user could go through if they wanted to know more about patient notes. 

```python
  user_wants = input("""Hello, what would you like to know about today?
    \n 1  = Medications on Admission
    \n 2  = Illness History
    \n 3  = Final Diagnoses
    \n 4  = Discharge Medications
    \n 5  = Discharge Condition
    \n 6  = Discharge Diagnosis
    \n 7  = Word Frequencies
    \n 8  = Patient Notes
    \n """)
  
  if user_wants == '7':
    word_frequencies(notes)
  elif user_wants == '8':
    patient_info = input("""What would you like to know? 
    \n 1 = Number of Notes
    \n 2 = Explore a Patient Note!
    \n 3 = Sections of a Note
    \n 4 = Number of Words in a Patient Note
    \n""")
```

Once they selected what they wanted, they would either have that information returned to them, or, if they chose 8, they would get to further explore the patient notes in the file. If they did choose 1-6, they would be taken through an else statement to find what they are looking for. Within this statement, Python would specifically look for lines that started with certain words in the linestarter_list. The variable ```linestarter``` was created to take in the number that the user would input to know where to begin. Once this number was entered and converted into an integer, linestarter_list would take that as an index entry and it would go through the notes in the file, and look for places where the lines started with the index in the list. 

```python
else: 
    linestarter_list = ['MEDICATIONS', 'PAST MED', 'FINAL DIAGNOS', 'Discharge Med', 'Discharge Condit', 'Discharge Diagnosis:']
    linestarter = linestarter_list[int(user_wants)-1] 
    
    pt_lines = notes.readlines()
    for line in pt_lines:
      if line.startswith('"Admission Date:'):
        # We have a new note
        if diagnoses_dict != {}:
          notes_list.append(diagnoses_dict)
          
          diagnoses_dict = {}
          
      else:
        if line.startswith(linestarter):
          diagnoses = []
          collecting_diagnoses = True
        elif collecting_diagnoses and line not in ['\n','.\n']:
          diagnoses.append(line)
        elif collecting_diagnoses and line in ['\n','.\n']:
          collecting_diagnoses= False
          diagnoses_dict[linestarter] = diagnoses
```

Once it has gone through that, it would print different messages to the user that would easily present the information to them. 

```python
    for wants in notes_list:
      if user_wants == '1':
        print("Medications used:\n"," ".join(wants[linestarter]))
      elif user_wants == '2':
        print("The illness history for this patient was:\n"," ".join(wants[linestarter]))
      elif user_wants == '3':
        print("Final Diagnoses for this patient were:\n"," ".join(wants[linestarter]))
      elif user_wants == '4':
        print("Medications given to this patient upon discharge were:\n"," ".join(wants[linestarter]))
      elif user_wants == '5':
        print("The discharge condition for the patient was:\n"," ".join(wants[linestarter]))
      elif user_wants == '6':
        print("The discharge diagnosis for the patient was:\n"," ".join(wants[linestarter]))
```

Because I wanted the program to loop until the user exited, I went back to the beginning of the code, outside of the defined functions, and I introduced a variable called ```return_more_information```, which would essentially accomplish this goal. ```return_more_information``` would usually be ‘Y’, indicating that the user does want to know more information. This gave grounds to introduce a while loop that stated ```while return_more_information == 'Y'```, keep prompting the user to select a number and return information to them. However, if the user were to put ‘N’, that would end the program.

```python
   return_more_information = input("""Do you want to know more? 
  \n Y = Yes
  \n N = No
  \n""")
print("Goodbye!")
```

# My Finished Product!
<iframe src="https://trinket.io/embed/python/8434b8d34f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Though I had a lot of ups and downs while writing this program, I was glad that I got to power through it and find a way to return items from my text file that would be useful to those wanting to know more about MIMIC-III data.
