---
layout: post
author: AU-turtlragon
title: "Aaron Ulmer's final project proposal and work plan"
---

### Description

As an academic administrator here at the iSchool, I have access to certain raw data reports which I use to inform various decisions about our current and future course scheduling and registration plans - among other things.  For this final project, I’ve chosen to focus my attention on the class manager “sections” report.  This report generates a list of all scheduled classes and their respective schedule/enrollment details for a given semester and field of study - in the case of the iSchool, that includes I (Informatics), ISP (Information Security & Privacy), and of course INF (Information Studies).  

I’ve chosen to work with this particular data for a few reasons:
1. Needless to say, it’s important that any University data that I disclose during class be safe for public consumption. Unlike many other datasets that I work with, none of the data generated here is subject to any restrictions or FERPA regulations.
2. I actually run this report quite regularly in my day-to-day work life and frequently pull data from it to assist with academic planning decisions based historical schedule/enrollment trends.  This process has thus far been a very manual process for me, so I have a personal vested interest in exploring ways to automate some of those repetitive and time consuming data analysis tasks.
3. The report contains a mix of textual and numerical data that present a variety of extraction and manipulation opportunities that I might play with.  How many total seats in INF XXX have we made available to students in the last academic year?  What are the names of all the instructors who have ever taught INF YYY?  Show me a graphical representation of the number of classes scheduled on a given day/time for this semester.  Etc. 
4. This report represents what I believe is a good sample of simple and well organized tab delimited data mixed with a sufficient amount of noise and formatting inconsistencies.  In other words, I’m confident that I can find ways to work with this data given my experience thus far with Python, but it certainly won’t be easy.  There will be a sufficient amount of data cleaning before I can even begin any sort of extraction and manipulation of the data. 
5. My previous experience working with this data via spreadsheets and whatnot provides me with a rather simple method for checking my coding work to verify that my results there align with my more manual calculations. 

Though I’m still brainstorming the specific ways I intend to play with this data, my goals from the outset are to:
- Import a group of text files to my Python trinket - one report per field of study/semester
- Merge the data of those reports into one dataset. 
- Clean the data and pare it down to only the portions that are useful for my own purposes.
- Modify certain portions of the data so that it’s more comprehensible to the reader - ex. Converting 24hr clock times to 12hr clock times, etc. 
- Pare this merged dataset into dictionaries/tuples/lists/etc that I can then use to query the data I’m interested in.
- Identify a handful of specific data extraction tasks that I want to focus on
- Build functions/methods to accomplish those tasks - most likely with an emphasis on making the user interface convenient - natural language argument inputs etc. 
- Produce a new report from my cleaned and merged data that’s more readable to non-expert users. 

### Work plan

My roadmap for right now is:

11/10-11/17: 
- Import data files to trinket and analyze how it looks from Python’s perspective. 
- Decide on specific data extraction tasks I want to focus on
- Clean data
11/18-11/24:
- Merge data from different files together
- Parse data into dictionaries, etc
11/25-12/1:  
- Build and test at least 2 extraction modules
12/2-12/8:
- Build and test 2 more extraction methods (I’ve admittedly arrived at 4 possible methods somewhat arbitrarily at this point)
- Build function for exporting new text file report based on cleaned data.
12/9:  Turn the project in and present. 

### Progress

My initial file import and sample of the data report I'll be working with can be seen here:

<iframe src="https://trinket.io/embed/python/ac27be96ba" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
