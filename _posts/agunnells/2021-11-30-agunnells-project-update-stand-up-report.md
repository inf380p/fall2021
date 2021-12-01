---
layout: post
author: agunnells
title: "Ali's Project Update & Stand-Up Report"
---

# My Updated Project Interfact

<iframe src="https://trinket.io/embed/python3/5af4e521d4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Project Reflection

Overall I am feeling pretty happy with my project progress; I have no concerns about completing it by the deadline. As I mentioned in my previous update, the primary thing I wanted to work on was the fifth option in my main menu. I've had a mixed experienced so far, as this was where I knew I would have to stretch myself. I first just wanted to make sure that I was able to create some comparisons between the stories, and I did end up figuring out how to do that. I started off by trying to figure out a way to create a visual that shows how the words counts of each short story compare to one another. I had already created a custom module, `word_count.py` that could calculate the total word count of each text: 

```python
#create a function to calculate the total word count of a story
def get_total_word_count(filename):
  #open and read the file
  file = open(filename, "r")
  #strip all of the punctation marks and line breaks from the story
  string_without_line_breaks = " "
  for line in file:
    stripped_line = line.strip()
    string_without_line_breaks += (stripped_line + ' ')
  #set the total word count to zero and create a word list to add each word to
  word_count = 0
  word_list = []
  words = string_without_line_breaks.split()
  #for each word in the story, add a count of +1 to the word count
  for word in words:
    stripped_word = re.sub(r'\W+', '', word)
    lowercase_word = stripped_word.lower()
    word_count += 1
  return word_count
  ```
  I wanted to see if there was any easy way that I could build off of this code, rather than starting from scratch for my comparisons. I decided to create a second function, `compare_total_word_counts` within the same custom module so I could build off of my function `get_total_word_count`:

```python
  def compare_total_word_counts():
  bar_chart = pygal.Bar()
  bar_chart.add('The Yellow Wallpaper', get_total_word_count('theyellowwallpaper.txt'))
  bar_chart.add('Kew Gardens', get_total_word_count('kewgardens.txt'))
  bar_chart.add('Story of an Hour', get_total_word_count('storyofanhour.txt'))
  bar_chart.render_to_file('Total_Word_Counts.svg')
 ```

Ultimately, creating a second function to build off of my first provided an easy way to get a visualization without writing out a ton of code. In addition, I also figured out how to create a visual that compares the individual count of a word across the three short stories. I created a function called `compare_individual_word_counts` that prompts the user to enter a word, and then provides a visualization of how often that word appears across each text. While I did get my code to work, it is currently incredibly verbose. I want to challenge myself to continue working on that portion of my code and hopefully find a less verbose way of making that visualization. 

Despite figuring out some basics for comparing the stories, I have hit a few roadblocks. In particular, I was hoping that I could use `pygal` to create a stacked bar chart that would compare the top five most common words from each story. However, not all three stories have the same top five words. I am currently unsure of how to work around that issue with Pygal. This task is certainly one of my stretch goals, and while I hope that I can figure it out before the project deadline, I am not totally confident. 

# Project Milestones

Complete Milestones:
1. Identify texts to use in the project; write code to open and read the text file, as well as remove all punctuation marks
2. Create a dictionary for each text file; write a function that uses a `for` loop to count each instance of each word in the text file and add each new instance to the text file's corresponding dictionary
3. Create a custom module that provides a variety of actions for the user to perform on a text file's dictionary
4. Incorporate `pygal` so that the user can produce visuals from the data
5. Work on the fifth option provided in my user interface, which focuses on comparing the texts; create some custom modules that will compare words/word counts across the texts
6. Work on incorporating `pygal` visualizations into the fifth option

In-Progress Milestones:
1. Create help text and determine how the user will access it 
2. Add in more detailed comments for my code 
3. Create a visual to compare the top five most used words across the texts (if possible)
