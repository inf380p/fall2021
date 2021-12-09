---
layout: post
author: zheinsohn
title: zheinsohn final project reflection
---

Here is my trinket:
<iframe src="https://trinket.io/embed/python/b2fd756eb9" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Program I chose:
I chose to do a data analysis program that involves users being able to search for incomplete words and return the results by how common the words are, ostensibly to aid in the completion of crossword puzzles. This was not what I ended up with, for a variety of reasons. I initially started this project because I wanted to use regex, which I felt comfortable with. At the time, I felt more comfortable with doing this kind of data analysis than I did with turtles. However, since I ended up not even using regex at all and struggling to make the data analysis tool work, I think I should have attempted a turtle program instead. I think the data analysis idea I had needed to be more grounded and started smaller, especially when it came to the user input aspects of the program. Though I am pretty embarrassed by the lack of success of this program, I felt it was better to turn some functioning code in than none at all.

Process:
My process was somewhat disjointed and consisted of several small but unrelated pieces of code that eventually needed to be put together.
Once I decided on the type and direction of my data analysis project, I looked around for appropriate data that met the requirements. Once I found some workable data, which was a .csv file containing 60,000 words and associated statistics, I spent some time trying to understand what exactly it was communicating and how I might be able to pull meaning from it. As I mentioned previously, I started this project because I wanted to practice my regex skills, so I made some workable regex code to account for all the spaces and numbers in the .txt file that I converted the file to after I realized Trinket wouldn’t be able to parse a .csv file.
Next came the user interface sketch, which provided potential options for users to select from and then would incorporate a text search. This quickly got complicated, as I was trying to account for several tiers of selections. Initially I started with the search/mode style with options:

```python
options = """Main Menu
Genre (search by media type)
POS (search by part of speech)
Overall (search without specifications)"""

selection = ""
#add option functions
def Genreoption():
  print("Fiction, Newspaper, Spoken Word")
  genre_input = input("What is your genre selection?")
```

Then I worked on populating the dictionaries. It was a little time-consuming, but it felt good to get something to not return errors. I was actually a little nervous, because I knew I needed a nested dictionary, but creating one out of so much data felt like it was going to take ages!
With my dictionaries in mind, I rewrote my interface draft. After watching the lecture in which you mentioned the get_input method, it seemed like a more efficient way of passing input and output for all my options. I didn’t get it to work fully, as it often didn’t run correctly after the first round of input, despite many tweaks. It led to bits of code like this:

```python
  def Genre_input():
  genre_selection = get_input("Enter the number of your preferred genre:", ["Fiction","Newspaper", "Spoken Word"])
  if genre_selection == "1":
```

Which ended up being stubs that I couldn’t use.
After scrubbing through some more of the recorded lectures, I realized my dictionaries weren’t exactly what I wanted them to be, so I worked on refining them and was able to successfully create a nested dictionary that printed well and was able to have information extracted from it.
Lastly, I tried to combine interface, dictionaries, and the search and user input code into one and essentially broke everything. It didn’t occur to me to use the code that we would use to pull key-value pairs from a dictionary as part of the user interface by adding the ability to take user input. Like I said previously, sometimes I get stuck on code being a certain way and have a hard time seeing other ways to reach the same outcome. Adding in the options to select a preferred stat from a list rather than have a bunch of different options first also was new to me! Unfortunately, by the time I was able to reach this point, my restarts, rewrites, and failed code bits were so frequent that I had very little time to try to elaborate further. It was at this point where I think the fatigue from not only looking at this code but also my other finals projects set in. It felt like every idea I had was incorrect and broke something else in the code I already had working. Every new implementation felt like a risk that would end up preventing the program from running at all.

Skills and attitudes:

Though I ultimately did not create a fully successful program, and was often stressed and frustrated, I tried to employ the problem-solving skills and strategies we discussed at the beginning of the course as much as possible, including stepping away from the code, talking through it, commenting things out, etc. I am disappointed with my program because although there is functioning code, generating what little there is was very difficult. The past few months it has felt like there was a wall between my understanding of what needed to be done and actually getting the code written and running. I felt like I had learned enough to conceptualize and outline the code I wanted, but writing it was so challenging. I did have a lot of determination though, and used pomodoros for hours! I stepped away and came back, started fresh, reread chapters, searched Stack Overflow, and watched videos, because it really felt like there was something I was missing, and if I just read a little bit more it would all fall into place. I felt like it was just out of reach, and with a little more time I would remember exactly what I needed to do. It’s frustrating that I only got a small amount of code working for all the time I put into it. I really can’t put my finger on exactly what makes it so difficult for me to generate my own code, but it’s something I really would like to work on. I’d like to continue to work to understand and feel comfortable with Python and the logic that goes into making the code work.

One thing I definitely made a mistake on was the way I approached creating the program. It has been repeated when writing a program to start small and get something working, which is what the milestones were, but my milestones ended up being separate pieces of code that weren’t easy for me to put together. Having the user interface be designed completely separate from the dictionary itself was, upon reflection, my biggest mistake. Once I had a design, it was difficult for me to abandon the piece of code structure entirely until I absolutely had to. To me, having code that works is like a lifeboat for me. I don’t want to leave it!

Overally, though this assignment left me feeling very panicked and stressed at some points, it’s actually driven me to continue working on it after the semester is over out of spite (and because I still want to learn). This semester in particular has been difficult for a number of reasons, but the challenge of this program really absorbed me, and the small wins when code did work felt gigantic. I really feel with a little more time and resources for me to learn at my own pace, I will be able to reach the desired functionality.

General
I know the time I spent thinking, reading, and working on this code doesn’t come through in its complexity. Where the code logic and syntax used to click, they suddenly didn’t, but it felt temporary (until it obviously wasn’t). However, I am absolutely not discouraged from continuing to try to become comfortable with using Python. I’ve bought a few books, including one that you had mentioned in class called “Automate the Boring Stuff”. Though I struggle to generate original code, I learned so much about the vocabulary and syntax of Python that I find it much easier to read programs and understand Stack Overflow posts. I want to build on this foundation, even if it takes me a little longer than other students, because even if I don’t end up writing Python code in the course of my future job, it has already made it easier for me to complete some assignments in my archival classes this semester. Encoding a finding aid in Encoded Archival Description/XML and generating metadata for a document was so much less daunting than I think it would have been had I not taken this class. Python is still somewhat opaque to me, but I’m not so afraid of it. I see it as a challenge and something to keep me on track over the winter break.
