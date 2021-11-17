---
layout: post
author: zheinsohn
title: Zheinsohn Interface Draft and Project Update
---
My interface draft:
<iframe src="https://trinket.io/embed/python/4efd7c4a8e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My regex experiment:
<iframe src="https://trinket.io/embed/python/8ea089993f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I initially started thinking about the interface draft before I found the data I'm currently using, which caused me to rethink my program. I found an Excel file with the 5000 most common english words that contained a lot of additional data about frequency, which helped me think about interface options.

The spreadsheet included word frequency by total frequency, category (movie/tv, spoken, fiction, etc), part of speech and frequency of capitalization, and beyond, which might be useful to help solve or create puzzles, since you might be able to use the context of crossword clues to narrow down your options (i.e if a clue is a title of a book with one word missing, you could choose fiction, or searching by capitalization frequency to find proper nouns and acronyms). The options won't necessarily exclude many words from the search, but will change the order in which results are returned. If searching by fiction, a word that appears more commonly in fiction than newspapers will return higher up the Fiction results list than it would the Newspaper results list.

To allow users to explore these options, my user interface will provide a way to narrow down the number and type of results returned through a menu. I created my basic user interface with three initial options:

```python
while search:
  print(options)
  search = input("How would you like to begin your search?")
  if search == "Genre":
    print("Select from the following genres:")
  elif search == "POS":
    print("Select from the following parts of speech:")
  elif search == "Acronym":
    print("Enter any known letters of acronym")
  elif search == "cancel":
    search = False
```

I then defined the option functions for those options, which would allow users to further narrow results and eventually lead to an input by the user of any letters that are already known for a particular crossword clue:

```python
mode = ""
#add option functions
def Genreoption():
  print("Fiction, Newspaper, Spoken Word")
  mode = input("What is your genre selection?")

def Posoption():
  print("Noun, verb, adjective, adverb, proper noun")
  mode = input("What is your part of speech selection?")
  
def Acoption():
  mode = input("Enter any known letters of acronym:")
```
To begin to test my regex ideas, I imported a txt version of the Excel file to experiment with. My original regex experiment crashed, likely due to the file size. I decided to use just a small portion of the file to test the regex statments.  My initial successful statement then returned the whole file. This was the initial statement I used:

```python
import re
hand = open('wordfreq.txt')
for line in hand:
  line = line.rstrip()
  if re.findall('\S+[call]\S+', line):
    print(line)
 ```
After many tiny modifications that continued to return large portions of the txt file, including trying to accomodate the fact that nearly all lines in the file contained differing amounts of digits and white space before the english word, I decided to test a regex function to search the one line in the text document I knew for sure did not begin with a digit: the line that held the column titles. 
```python
import re
hand = open('wordfreq.txt')
for line in hand:
  line = line.rstrip()
  if re.findall('^rank', line):
    print(line)
```

This was a success, so I knew it was just a matter of working out a specific enough regex function to be able to call words. This was difficult, because the Excel file had a lot of columns, and I'm not entirely sure that the formatting of the file was correctly carried over into the txt version, which might have had an impact on the regex statement being able to find what I was looking for. I decided to export the Excel file into a txt file myself, which helped with formatting, and I was able to write a successful regex statement.


Some Roadblocks

I initially thought with all of the word frequency data included in the spreadsheet, it might be less necessary to assign a crossword frequency rate and use the included word frequency rates instead. 
However, upon further digging, there was a big difference between the most common words in general English and the most common English crossword words. For example, the most common word in the "Shortz era" crosswords is era, but it's the 2044th most common general English word. This amount of difference makes me think that it's more necessary to continue with my initial idea of including a "crossword frequency" number for the english words.

The matching of crossword frequency and words/word frequency will probably come with the creation of the dictionary, though I am working to find a less time-consuming way of performing this data entry task. It may be something that turns into an extra feature, but I would really like to include it. Another task is to remove or exclude any words less than three letters.

Milestones

I think my initial milestones were a little over-generalized, and be cause of this vagueness were a little too ambitious. My initial plan:

  1. Locate at least two data files: A simple English language dictionary and a data file of a to-be-determined number of the words that most often appear in crosswords.
  2. Assign "commonality score" to the dictionary words and create main data file.
  3. Write and test regex code to successfully return words with a particular pattern and score.
  4. Plan user interface for both user input and visual returns. Ideally, I would love for this to be more than the basic user input text box and screen if possible, but I want to ensure that the user is able to input a request and the results return properly.
  5. Test on crossword puzzle solving and create a simple puzzle using this tool.


My revised milestones are as follows:

1. Finalize basic regex expression that will reliably account for line structure and different categories of word frequency.
2. Determine keys and values of dictionaries
3. Create dictionaries
4. Complete user interface refinement options
5. Complete user interface input search functionality, including any data visualizations
	
Visualizations might include: dividing frequency values into tiers, and using a number of asterisks in a returned result to represent the frequency tier.
  
I think I am a little off-plan, just due to the richness of the data source I found, which has reshaped both my design of the user interface and my idea for the project. However, it's also given me a more concrete idea of the user interface and general design of the program. Before next class, I want to make progress on creating a useful working dictionary or dictionaries and solidify data visualization ideas and execution.
