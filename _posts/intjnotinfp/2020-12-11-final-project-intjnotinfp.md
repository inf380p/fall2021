---
layout: post
author: intjnotinfp
title: "intjnotinfp’s Final Project and Reflection"
---

Code for Final Version of Data Analysis Utility:

<iframe src="https://trinket.io/embed/python3/1de23ebe8e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For my final project, I selected the text-based data analysis utility. The reason for choosing the second option was because I never felt very comfortable using Turtle for the various assignments earlier in the semester. It’s easier for me to work towards more “black and white” requirements that are either obviously accomplished or not because I can tell if I’m on track or not, and it also requires less creative energy. In other words, for a beginner like me, it’s harder to figure out how to do stuff if you’re not clear on what exactly you need to be doing. I knew I had to choose a topic I was either interested or personally invested in, so I started by searching the web for Python uses in a library setting. One article called “ Do Library Stuff Faster with Python” mentioned a handy library holdings lookup that uses the Beautiful Soup library to check a CSV of book records against the library’s own catalog to eliminate the possibility of accepting duplicate copies as donations. This sparked my interest and made me think about making CSVs of my own personal holdings, then visualizing the different types of data that are typically included in a MARC record. I had been poking around on Texas Data Repository but didn’t find any data sets similar enough to what I wanted to work with so I moved forward with the personal catalog idea.

After I had decided what information to include within each record (title, author_last, author_first, year, publisher, ISBN, format, genre), the first step was to create (2) CSVs with records for all the books I own. This took A LOT longer than expected, although it worked out pretty well. It was cool to learn how to create a CSV because I’d never done that before and it was a lot easier than expected! It made me feel like a programmer despite the ease. I used Excel to create two workbooks, one for English holdings and one for Spanish. Next, I exported them separately as CSV files and then pasted the values into different pages on Trinket. As I ran my first function “process_line(line)” which splits the line at each comma, I realized that some of my titles had commas in them and that was messing up the split. I went back to Excel, deleted them from there, and put the cleaned up files back into Trinket. I also had to remove new line characters by replacing them with empty strings.

My main strategy was to try to work with the tools I already had, because 1) I didn’t have the time to learn entirely new things like how to use Pandas or myplotlib and 2) I didn’t realize that at the time I made that decision, those might have actually been the more efficient routes. As I kept looking up documentation for dictionary problems, I realized that Pandas seemed like the prevalent way to go. Unfortunately, the work-with-what-you-know approach also spilled over into classes. I had worked through a large part of my project before sitting down to try to understand the concept. It never clicked for me and I decided the best option for me and best use of my time was to focus on hitting all the other requirements at the expense of that one. For that reason, I mention that project deficiency in this strategy section. 

The main data structure, aka the bread and butter of the project, was created by taking the individual records and turning them into a list of dictionaries where the column headers, or “attributes” served as dictionary keys and the unique values became the dictionary values. This was the part that took the longest for me, and required multiple sessions and lots of looking up dictionary tips on sites like stack overflow, etc. I ultimately had to get help from a friend (not classmate, per instructions!) with this particular function because I stalled out and wasn’t making progress. I knew what I wanted to do but couldn’t locate any documentation to help me accomplish it. What I ended up doing was using a while loop to iterate throught the records and 
just pull out column headers from list the first time (on the very top line), and after that create dictionaries with headers as the keys and the values and specific values. I also added an optional encoding for UTF-8-SIG which I found out was necessary to clean up the records because they included non-English characters which were the accent marked letters from the Spanish catalog. I split the catalog into English and Spanish records to satisfy the multiple text file requirement, but since I wanted to aggregate all the records to do visualizations on the set as a whole, I concatenated the two CSV files via a function called load books. I used them joined like this for most of my user options, with the exception of the language breakdown option. 

One specific challenge I encountered was an instance where my program was running without errors but not returning anything. I couldn’t figure out why that kept happening, so I had to go line by line and check all the changes I had made since the last time I was able to run it properly. What I came up with was this:

def print_asts(col, val):
    count = count_col_values(books, col, val)
    stars = ''
    i = 0
    while i < count:
        stars = stars + '*'
    print(val, ': ', stars)

I realized that it wasn’t incrementing because I forgot to add i += 1 after stars = stars + '*'. The program was running through an infinite number of stars because it kept adding a star to the string sum before it. Oops! Once I corrected that, I got back on track.

I also got super frustrated with the multitude of parentheses used in this function and trying to keep straight how many I needed and where they ought to have gone to avoid syntax errors. That was a good old guess and check moment:

eng_freq = str(round((english / combined), 2) * 100) + '%'
    span_freq = str(round((spanish / combined), 2) * 100) + '%'

My overall process was to work through each column name/attribute to create the functions needed to display the data for that type, and it got easier as I went on because I felt like I understood the pieces better and also how to manipulate them. My easiest functions were the two for format and language because they were pretty much just basic math, dividing the number of times a specific value appeared by the total records. I got tired of printing stars every time, so that’s why I switched to percentages for a couple. The ‘visualization’ is admittedly underwhelming because it’s just numbers, but at least it’s something a little different than the previous functions.

One of the last steps was to go back and “clean up” my code by deleting code that was commented out (which I had used to test along the way), removing functions that I didn’t end up using in the main loop, and making sure that overall the code was well-commented. 

Here’s a glimpse of how I modified, added to and executed different milestones:

[X] Determine which fields to include in CSVs
[X] Audit personal library
[X] Create (2) CSVs listing entire collections
[X] Clean up and normalize data fields
[] Define a “book” class that assigns column headers as attributes
[] Instantiate the class for each holding
[X] Create various dictionaries for personal holdings
[X] Make a comprehensive list of those dictionaries
[X] Add “help” text
[] Return a line graph that displays each publication year with # of titles
[] Set up functions that return text that displays: - 
[X] # of books per publisher 
[X] Ratio/percentage of paperbacks/hardbacks/ fine bindings to total 
[X] Percentage of each genre represented in collection - percentage of Spanish to English 
[X] Percentage of Spanish v. English books
[X] Most popular genre
[X] Visualize data via prinouts
[X] Create iterative interface via main loop with if clauses

** Outside the scope of project, but potential to continue by: **

[] Somehow automate a “checker” that runs dictionaries against UT holdings
[] Return data about each item: yes/no in regards to whether or not library would accept the donation
[] Visually represent that data with either a graph or chart

I didn’t end up accomplishing any of my strech goals, but if I wanted to expand on this project in the future and develop a checker function with an API that connects my catalog to the UT libraries, I already have a good chunk of that done. I still feel like I only understand a tiny fraction of what Python has to offer, but I’m amazed that I could do so much with so few tools! I’m happy with the final product, especially because I didn’t know a lick about Python or computer programming at all on the first day of class. The process was a lot harder than I expected it to be and I’m proud that I got this far despite not learning classes in time to incorporate that into the project.

REFS:

https://acrl.ala.org/techconnect/post/do-library-stuff-faster-with-python/
https://stackoverflow.com/questions/17912307/u-ufeff-in-python-string 
https://www.geeksforgeeks.org/python-ways-to-concatenate-two-lists/ 
https://www.freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854/
https://stackoverflow.com/questions/45198869/create-dictionary-from-csv-with-headers 
https://stackoverflow.com/questions/44105375/how-to-create-a-dictionary-of-key-column-name-and-value-unique-values-in-col
https://www.xspdf.com/resolution/53291127.html
