---
layout: post
author: agunnells
title: "Ali's Final Project"
---

# My Final Project Trinket

<iframe src="https://trinket.io/embed/python3/ad524eb4ce" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# My Final Project Reflection

For my final project, I opted for a text-based analysis utility. When brainstorming ideas for my project, I challenged myself to think of a tool that would be useful for my own research. I wrote a research paper for my digital humanities class last year that analyzed the similarities between various short stories written by Charlotte Perkins Gilman. In that paper, I conducted a text analysis of Gilman’s short stories via a similarity measures tool. The tool uses a Python script to represent each text as a series of word counts; it then uses those word counts to calculate the distance (or difference) between texts. However, I encountered one major roadblock when using this tool: it did not provide the user any way of viewing the specific words in each individual text. In other words, I could calculate the similarity between a series of a short stories, but I could not get a sense of which words appeared more frequently in certain texts and may have accounted for those similarities and/or differences. I decided that I would create a program that could essentially perform data analysis on a short story in a way that could complement some of these text analysis tools that I have been using in my research. 

The text-based analysis utility that I created for my final project essentially treats the words of each short story as the data set that a user can perform various actions on. I decided to build my project using three short stories: “The Yellow Wallpaper” by Charlotte Perkins Gilman, “Kew Gardens” by Virginia Woolf, and “Story of an Hour” by Kate Chopin. However, the program is constructed in a way that makes it fairly simple to switch out those three short stories with others. Each short story fed into the program is first stripped of all punctuation and line breaks; then, the individual words from the story are separated and counted. A dictionary of each short story is created in which the different words of the story are the keys and the number of times each word appears in the story are the values. In other words, the dictionary becomes a representation of the data set I am working with: individual words in a story and how many times they appear. Furthermore, the program creates a list of tuples from each dictionary, which allows the user to run a series of actions on each data set. To start, the user can perform multiple actions on the data set of each short story:
-	View the story dictionary 
-	Calculate the total word count of the story
-	Calculate the count of an individual word
-	Calculate the frequency of an individual word (the individual word’s count divided by the total word count of the story)
-	Produce a bar chart that shows the count of the top five most used words in the story

In addition, the user can perform a few actions that compare the data sets from each text:
-	Produce a bar chart that compares the total word count of the three stories
-	Create a line graph that compares the number of times an individual word appears in each text

My process when constructing my final project was largely focused on building up from a solid foundation. Since many of the actions I wanted to perform on the data sets required having a dictionary of each text, my first goal was to ensure that I could create these dictionaries. Therefore, I started by working with one single short story, "The Yellow Wallpaper," to see if I could create a dictionary. A great deal of the initial work on my program revolved around figuring out how to strip all line breaks and punctuation marks from the story. This was one of the more time intensive aspects of my project; I ended up with several Trinket drafts of my work on "The Yellow Wallpaper." When I successfully created a dictionary from this story, which used individual words as the keys and the number of times they appeared as the values, I replicated the process with "Kew Gardens" and "Story of an Hour." However, each of these dictionaries was created in a separate Trinket file, and I knew that I should ideally have one function that could take each short story’s file name as an argument and create a dictionary from that file. Luckily, I was able to use the code I wrote to create the individual dictionaries by assigning a variable called `file` that would take each file name and create a dictionary from the corresponding file. My original code for “The Yellow Wallpaper” looked like this:

```python
gilman = open("theyellowwallpaper.txt", "r")
string_without_line_breaks = " "
for line in gilman:
  stripped_line = line.strip()
  string_without_line_breaks += (stripped_line + ' ')
gilman_list = []
words = string_without_line_breaks.split()
for word in words:
  stripped_word = re.sub(r'\W+', '', word)
  lowercase_word = stripped_word.lower()
  gilman_list.append(lowercase_word)
 
gilman_dict = {}
for word in gilman_list:
  if word not in gilman_dict:
    gilman_dict[word] = 1
  else:
    gilman_dict[word] += 1

sort_words = sorted(gilman_dict.items(), key = lambda x:x[1], reverse=True)
  
for word in sort_words:
  print(word[0], word[1])
 ```

On the other hand, my rewritten code takes the basic structure of the previous code, but it is structured as a function that takes any file as an argument:

```python
def create_story_dict(filename):
  read_story = open(filename, "r")
  string_without_line_breaks = " "
  for line in read_story:
    stripped_line = line.strip()
    string_without_line_breaks += (stripped_line + ' ')
  story_list = []
  words = string_without_line_breaks.split()   
  for word in words:
    stripped_word = re.sub(r'\W+', '', word)
    lowercase_word = stripped_word.lower()
    story_list.append(lowercase_word)
  
  story_dict = {}
  for word in story_list:
    if word not in story_dict:
      story_dict[word] = 1
    else:
      story_dict[word] += 1
     
  sort_words = sorted(story_dict.items(), key = lambda x:x[1], reverse=True)
  
  for word in sort_words:
    print(word[0], word[1])
 ```
 
At this point, I transitioned from working on individual pieces of my project to considering it as a whole program with multiple components. This was around the time that we created a first draft of our project interface for a class assignment. The project interface draft redirected my focus towards how I would use the program foundation (aka my dictionaries, or data sets) to construct a program that would allow the user to perform multiple actions each data set. Earlier in this reflection, I listed out the actions that a user could perform on each individual story dictionary; when I started working on the user interface, I simultaneously worked on code that would perform those actions on each data set. Most of these actions were relatively easy to write code for, especially since I could draw on the code I wrote for my `create_story_dict` function. I created a custom module, `word_counts.py`, which takes the code I wrote to strip each story of line breaks and punctuation and uses it to build several other functions that allow the user to perform the listed actions. I also used this time to make sure that I was familiar with `pygal` so that I could incorporate visuals into my program. 

The final step in my process was to focus on the comparison options for the data sets. Once again, I was able to use a good deal of code that I had already written. For instance, one of the comparison options that I incorporated was a way for the user to produce a bar chart that compares the total word counts of the three texts. I already had code written that would calculate the total word count of a text, and I had the code written that would produce a visual using `pygal`. I created a function called `compare_total_word_counts` that performs the `pygal.Bar()` method on the results of the `get_total_word_count` in order to produce a bar chart of the total word counts of each text:

```python
def compare_total_word_counts():
  bar_chart = pygal.Bar()
  bar_chart.add('The Yellow Wallpaper', get_total_word_count('theyellowwallpaper.txt'))
  bar_chart.add('Kew Gardens', get_total_word_count('kewgardens.txt'))
  bar_chart.add('Story of an Hour', get_total_word_count('storyofanhour.txt'))
  bar_chart.render_to_file('Total_Word_Counts.svg')
```

In addition, I created one other comparison option for the user where they can input a word and the program will return a line graph comparing the word’s usage across the three texts. At this point, my last step was to create help text for the user to rely on. 

As I built my final project, I noticed that I relied on many of the attitudes/skills that I’ve learned over the course of the semester. I was definitely overwhelmed by this project at the start, and I thought back to prior moments in the semester when I was overwhelmed. I recalled writing in an earlier reflection that I had a habit of getting overwhelmed and shutting down, rather than stepping back, accepting those feelings, and working through them. Therefore, I tried to take a more active approach when I sensed that I was getting overwhelmed. I also remembered Elliott’s advice that we are not expected to have perfectly memorized everything we’ve learned this semester; rather, we should rely on the resources that we’ve cultivated. I revisited our textbook, as well as other resources I’ve relied on during the semester such as W3 Schools. Being able to jog my memory when building my project helped put those anxious feelings at bay. 

In addition, I noticed several lightbulb moments as I was working on my project. I think that many of these lightbulb moments came from an increased sense of confidence as I continued working on my program. For instance, although we discussed importing our custom modules into our interfaces, we did not necessarily discuss how to call the functions from those modules and use them in our interface. I decided to attempt to figure that out on my own as I worked on my project. I reasoned that, since the functions from our custom modules were already imported into the interface, I simply had to call each function when necessary:

```python
def option1():
  print("""
  You selected 'The Yellow Wallpaper.'
  What would you like to see? Select one of the following:
  1: Dictionary
  2: Word count
  3: Count an Individual Word
  4: Word frequency
  5: Visualize the Top 5 Most Used Words
  0: Main Menu
  Type "Help" to get help
  """)
  selection = input("Enter your selection:")
  menu = "1"
  while True: 
    if selection == '1':
      create_story_dict('theyellowwallpaper.txt')
      selection = input("Select another option or enter 0 to return to the main menu: ")
    elif selection == '2':
      print('The total word count of this story is:', get_total_word_count('theyellowwallpaper.txt'))
      selection = input("Select another option or enter 0 to return to the main menu: ")
    elif selection == '3':
      print('The count of your selected word is:', get_individual_word_count('theyellowwallpaper.txt'))
      selection = input("Select another option or enter 0 to return to the main menu: ")
    elif selection == '4':
      print('The frequency of your selected word is:', calculate_word_frequency('theyellowwallpaper.txt'))
      selection = input("Select another option or enter 0 to return to the main menu: ")
    elif selection == '5':
      top_5_words_visual('theyellowwallpaper.txt')
      selection = input("Select another option or enter 0 to return to the main menu: ")
    elif selection.lower() == 'help':
      print(short_story_help())
      selection = input("Select another option or enter 0 to return to the main menu: ")
    elif selection == '0':
      return options
    else:
      print("Please select a valid option.")
      selection = input("Enter your selection:")
```

Although this may seem pretty minor, it was nonetheless a signal to me of the progress that I’ve made during the semester. I was able to reason through the best course of action based on what I had learned and what seemed like the most logical next step. Lightbulb moments like this really increased my confidence as I felt like I was able to answer my own questions while creating my project. 

Ultimately, I am proud of the work that I did on this final project. There were some stretch goals that I set for myself which I was unable to complete. In particular, I really wanted to include a story comparison option that would produce a stacked bar chart comparing the top five most used words in each text. However, I hit some roadblocks with this goal. The set of top five words were not the same for each story, and I was not sure how to indicate that when using `pygal`. I ended up deciding to not include this option in my final project since I could not figure out how to make it work. Despite some of my stretch goals still requiring work on my part, I was very happy with the options that I did include in my program. I hope to use this tool in any future research that I conduct related to text analysis. 
