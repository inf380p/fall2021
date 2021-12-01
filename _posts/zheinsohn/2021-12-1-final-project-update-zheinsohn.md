---
layout: post
author: zheinsohn
title: Zoe's Final Project Update
---
Trinket Snapshot of Dictionaries:
<iframe src="https://trinket.io/embed/python/4dc8403329" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Given that I'm still working on interesting and useful ways of digesting the data, I thought it might be useful for me to see how Python works with the data itself when it comes to creating and using dictionaries. To stay on track with my general schedule, I decdided to at least create the working parts of the program, so that if I change my data, I will still have the code necessary to easily create dictionaries, and can add complexity once I have a more complete idea of how to best use the data. To help with creating the dictionary, I thought about what kind of output I would want from it. I knew that I would want users to be able to see the word they were looking for and the numerical frequency data associated with it. Writing the output first helped me conceptualize what the code should do.

Given the structure of my data (a column of words with associated information stored in other columns) it made sense to me to create a nested dictionary, with a single word from the column of words as the inner key, and a second dictionary as the outer key. The second dictionary would have an inner key of the column name (like Frequency, for example) and an outer key of the corresponding value (5,for example).

I created a tiny test dictionary to make sure I was on the right track.
```python
wordinfo = {'supertest':{'Rank': '5', 'common': '1', 'caps': '6', 'blogPM': '1', 'webPM': '1', 'TVMPM': '1',	'spokPM': '1', 	'ficPM': '1', 'magPM': '1', 'newsPM': '1', 'acadPM': '1'}}
for lemma, l_column in wordinfo.items():
  print("Word:", lemma)
  
  for key in l_column:
    print(key+':', l_column[key])
```

The next challenge was populating the dictionary with hundreds of words and associated data without having to enter each key and value myself. To do this, I tried to split the txt file with all of my data into lines, where each line would become a nested key-value pair, then use the str.split() method to split on the whitespace that divided each value.

It returned each line of the text file as a sequence of individual strings. I then used a variable to store the lemma and column info of each line.
```python
  splitvalues = str.split(line)
  lemma = splitvalues[0]
  rank = splitvalues[1]
  common = splitvalues[2]
  caps = splitvalues[3]
  blogPM = splitvalues[4]
  webPM= splitvalues[5]
  TVMPM = splitvalues[6]
  spokPM = splitvalues[7]
  ficPM = splitvalues[8]
  magPM = splitvalues[9]
  newsPM = splitvalues[10]
  acadPM = splitvalues[11]
  print('lemma:', lemma, 'rank:', rank, 'commonality:', common)
```
This is the part where I got stuck. I really didn't want to have to add thousands of lines to the dictionary myself, but I struggled to figure out how to add new values to existing keys to a nested dictionary. I tried some different lines and I kept getting 'not responsive' errors, so this whole process took a while. I eventually decided to shorten the number of key-value pairs I added at once to just three total:
```python
info = ('rank:', rank, 'commonality', common)
for lemma in splitvalues:
  if lemma not in wordinfo.keys():
  wordinfo[lemma] = info
  else:
    continue
  print(wordinfo)
```
The above code block did eventually return a populated dictionary, and was a lot more simple than I was imagining. I ended up having several different test trinkets full of tiny pieces of code that I eventually was able to bring together. Each step in the process took a while to click, and creating the basic dictionary took me longer than I thought it would. I think it was difficult for me to go from a nice idea in my head to actual execution. My milestones from last time were:

1. Finalize basic regex expression that will reliably account for line structure and different categories of word frequency.
2. Determine keys and values of dictionaries
3. Create dictionaries
4. Complete user interface refinement options
5. Complete user interface input search functionality, including any data visualizations

So far, I'm pretty happy with the regex expression from last time, especially since it will be simplified by having the dictionaries with individual keys and values. I determined the keys and values for my nested dictionaries and was able to create the base code and populate with about 100 test key-value pairs. The dictionaries are not fully created and populated, but I feel confident that I will be able to extrapolate to incorporating the entire file. So that leave the majority of work to be done on the user interface. What I will be working on next is:

2. Overhaul user interface sketch to include the appropriate number of options, define acceptable user input, and account for a range of input.
3. Incorporate regex/search functions
4. Add complexity through digested data and additional comparision information and finish dictionary population
5. Visualizations
