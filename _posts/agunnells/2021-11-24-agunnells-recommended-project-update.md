---
layout: post
author: agunnells
title: "Ali's (Recommended) Project Update"
---

# My Updated Project Interface

<iframe src="https://trinket.io/embed/python3/8f0f42d10a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Project Reflection and Update

I was able to make a pretty good deal of progress on my project since the last update. I was working in a lot of individual Trinkets beacuse I was trying to get the individual components of my project to work. For instance, I was working on a Trinket that dealt only with creating a dictionary from "The Yellow Wallpaper":

<iframe src="https://trinket.io/embed/python3/81b69bfe1f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I realized that I would probably need to create a more generalized function that I could plug any file name into. So, I restructured the Trinket above into a function that could take any filename as its argument and create a dictionary from that file. This is the trinket I ended up with: 

<iframe src="https://trinket.io/embed/python3/140476926f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I turned that into a custom module, which can be seen in my updated project interface Trinket. I repeated this process with several other custom modules; now, my project has custom modules that will provide the total word count, individual word counts, individual word frequeuncies, and a visualization of the top five most used word for each text. 

The other major update I made to this project was incorporating these custom modules into my project interface. This was something that I tried to do completely on my own; I wanted to see if I could figure it out before looking it up. I decided to incorporate an `if` statement for the options a user can select for the individual texts. In other words, once the user selects their text from the main menu, they have a list of possible options they can run on that text. This is where I used the `if` statements. Each `if` statement connects to a part of one of my custom modules:

```python
#create option 2, which is about The Yellow Wallpaper
def option2():
  print("""What would you like to see? Select one of the following:
  1: Dictionary
  2: Word count
  3: Count an Individual Word
  4: Word frequency
  5: Visualize the Top 5 Most Used Words""")
  selection = input("Enter your selection:")
  if selection == '1':
    create_story_dict('theyellowwallpaper.txt')
  elif selection == '2':
    print('The total word count of this story is:', get_total_word_count('theyellowwallpaper.txt'))
  elif selection == '3':
    print('The count of your selected word is:', get_individual_word_count('theyellowwallpaper.txt'))
  elif selection == '4':
    print('The frequency of your selected word is:', calculate_word_frequency('theyellowwallpaper.txt'))
  elif selection == '5':
    create_a_visual('theyellowwallpaper.txt')
```
Overall, I made a lot more progress on my project this past week than I was expecting. I think the fifth option in my main menu, which compares the individual texts together, will be my focus for the next project update. I think this may create some roadblocks for me because it is the most ambitious aspect of my project. I am hoping to create a series of options for the user to compare top words or selected words across texts, as well as create some visualizations with `pygal`. I got the basics of `pygal` down for the individual texts, but I don't yet know how to compare certain words across multiple texts in a stacked bar graph. However, I am still confident that I can complete my project by the deadline. 

# Project Milestones

Completed Milestones:
1. Identify texts to use in the project; write code to open and read the text file, as well as remove all punctuation marks 
2. Create a dictionary for each text file; write a function that uses a `for` loop to count each instance of each word in the text file and add each new instance to the text file's corresponding dictionary
3. Create a custom module that provides a variety of actions for the user to perform on a text file's dictionary 
4. Incorporate `pygal` so that the user can produce visuals from the data

In-Progress Milestones:
1. Work on the fifth option provided in my user interface, which focuses on comparing the texts; create some custom modules that will compare words/word counts across the texts
2. Work on incorporating `pygal` visualizations into the fifth option
3. Create help text and determine how the user will access it
