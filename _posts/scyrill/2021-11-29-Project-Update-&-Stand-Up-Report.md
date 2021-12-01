---
layout: post
author: scyrill 
title: "Project Update"
---

On my last update I mentioned that I wanted to tackle the following goals for the next part of my assignment: 

1. Go through the terms and remove anything that might be duplicates or making one common term for both of them (ex. COPD exacerbation and Chronic Obstructive Pulmonary Disease Exacerbation
2. Create a dictionary for diagnoses
3. Look for the definitions of the illnesses and input them as strings
4. Create an area for the user to input the diagnosis that they want to know more about  and if there is no entry for what they want to know, including an option for them to enter something else

However, after meeting with the professor, we discussed how while these were good goals, my overall end goal was outside of the scope of our course and that there was still a way to do text analysis, but simplified. During office hours last week, he and I went through what I already had and he introduced new methods that I could try, starting from the beginning. 

Initially I used `pt_notes = notes.read()` to read the file, but he suggested that I switched to `readlines()`. However, since this was an area I went back and forth on last time, I explained what the issue with that was (i.e. Trinket would crash when I used `readlines()`) and why I decided to use `read()` instead, led to us trying `readlines()` again, testing it by printing lines, and me finding out that it worked! After this, we moved on to my txt file and noticed that there were separations for the notes in my file, and suggested that I could find a way to count the number of notes in my txt file by finding key words and having Python print portions of the note based on them. 

Though this was good, I still wanted to find a way to define diagnoses in the file because that’s what I was working towards in the beginning. However, while working on the file with the professor, it was concluded that since my data was pretty complex and semi-structured, the best route would be to try structuring it so that meaningful material could be extracted by the user. From there, we began looking for ways to give it more structure while building on the aspect of pulling information from the notes versus the entire file. When looking through the txt file, we found out that new notes were indicated by 'Admission Date', so he recommended that I look for that in my data and based on that, finding things like how many notes there are in the file. 

After the professor suggested checking out `readlines()`, we also change the variable `pt_notes` into `pt_lines = notes.readlines()` and creating an index for it, so I could analyze the lines in the file. After this, a loop was created to go through the files to see the beginning and end of a note by looking for 'Admission Date' since it was more consistent for differentiating the number of notes. By finding this, it would then be possible to slice the index into the notes. He modeled it like this:  

```python
notes_dict = {}
notes_dict["medications"] # => list of medications
notes_dict["prior_history"] # => string of narrative history
notes_dict["word counts"] # => list of all narrative sections with word counts
notes_dict["condition_list"] # => only the conditions that appear in this note
```

He mentioned that introducing dictionaries would be a good way to deconstruct data in Python, but also give more structure to the user interface. By introducing these dictionaries, it would help the user get more of an overview of each note also, instead of being bombarded with information. Some additions that were also made were creating a for loop followed by if statements that would skip lines that weren’t pertinent to my focus and when there was a new note, adding it to the `notes_list` and then setting the `current_note` to a blank dictionary. 

``` python
for line in pt_lines:
  if line.startswith('"Admission Date:'):
    # We have a new note
    if current_note != {}:
      notes_list.append(current_note)
```

By continually looping through this, I would know where new notes would begin and I would clean it up by adding them to the `notes_list` as this logic is basically saying that if the dictionary has something in it, it should be put in the `notes_list`. 

It was suggested that I use regex in my code because it would be very useful to me, especially since I have a lot of inconsistent data (i.e. Final Diagnoses and Diagnosis, Discharge Diagnoses and Diagnosis), so I will implement that in the next part of this project, especially since it would help me catch those inconsistencies that I encountered. 

Some of the inconsistencies that arose when looping through all the lines, a couple of results were printed for the final diagnoses, but when going through the file to see if this was true, this was not the case. Some results were left out since it was Diagnosis, so it was changed to `FINAL DIAGNOS`, which returned a lot of results! However, it returned more than just the final diagnoses because there were periods in the file, and we coded for newline characters. 

``` python
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
```

By doing this, we accounted for lines that were blank, but we didn’t think about what would happen if the line started with or contained any other kind of character, thus explaining why more than just the final diagnoses were returned. To build a list of things that indicate the end, `.\n` was added to the line of stuff to look out for. This returned less results, which was more accurate. 

I thought that this was good progress, but I still wanted to make it interactive for the user because I wanted them to type something they wanted to know more about, so I asked how can I make this interactive for the user? I was told that I had to be more pragmatic and adapt what I want to do with what the dataset would allow me to do. Because my dataset is idiosyncratic, it would be better to decompose the notes into data structures, extract what I think are the most important kind of items, and combining that with an interface where the user can either compare across notes or get an overview of a certain note then that becomes a tool for understanding this dataset. I thought that this was a good idea because considering what I had before this, to try making a large scale dictionary at this point would not be wise, so it would be better to scale down to get more out of the data. 

# Here is my code so far
<iframe src="https://trinket.io/embed/python/6144d7845c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

With the ways things were going, I scrapped my original goals and decided to do the following: 

1. Build the dicts so that the user can explore the data that is in the dictionaries
2. Grab all the headers from the notes so that the user can broadly know what is in each note 
3. Having it return requested information based on the header (?)
4. Return the number of words in a given note and word frequency (if time permits)
5. Write a list of all the capital letters, using regex
6. Using the code that was previously written, building a dictionary from the condition list that I made and count how many times a condition shows up in a given note 
7. Extracting out the text of each note into a list and looping through that list and doing that would show me that i am only working with one note at a time and then the multi-line regexes could extract things in a more powerful way and it would be extensive so that you are taking only what you want
