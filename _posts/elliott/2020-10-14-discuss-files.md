---
author: elliott
category: notes
layout: post
title: "Let's learn files & review dictionaries"
mode: Remote
published: true
---

# Q&A

**MEETUPS** - Do you have one?

# Python 3

We'll be using Python 3 in Trinket for all text-based work.  Remember your `print()` functions.

`sep=" "` lets you specify what the seperator between arguments is.  It defaults to a space.

`end='\n'` lets you specify what to do at the end of the print functin.  It defaults to a newline.

You can make anonymous Python 3 trinkets on Trinket for free.  If you want the convenience of saving your
Python 3 trinkets to your account, you should use code `INF380P` to get our premium plan at a huge discount of $4.50 a month.

# Part I: Files

There are a few core actions you should be able to perform on files:

* Open them (Dr. Chuck)
* Search/extract information from them (Dr. Chuck)
* Build a data structure from them (not really Dr. Chuck)
* Explore your data (not really Dr. Chuck)
* Print a table from your data (not Dr. Chuck)

We'll review all of these today.

Something Dr. Chuck didn't cover: the `with` statement.  This is the Pythonic way to open a file:

```python
with open("sales.csv") as file:
  sales_raw = file.read()
  # Or, if you need lines:
  sales_lines = file.readlines()
```

Otherwise you'll have to open and close the file handler and it's a pain.

# Lists of Lists

Making a list full of lists gives you some interesting powers.  First, you can think of each item in
the main list as a row and each item in the interior lists as a cell/column.  As long as you keep the lengths
constant you've got what amounts to a spreadsheet, but in Python!

Here's how you can visualize a list of lists:

```
[ [... , ... , ...]
  [... , ... , ...]
  [... , ... , ...]
  [... , ... , ...]
  [... , ... , ...] ]
```

This one has five rows and three columns.

To work with lists of lists you'll nee lots of **slicing** and **indexing**.  Remember the `list[x:y:z]` syntax.

Let's read over questions 1-3 briefly and then go straight to exercise 4.


# Part II: App project Milestones

In two weeks, your first multi-week project is due. Today we'll make milestones and next class we'll review your intiial progress.


Let's review the assignment.

Manual groups by Option 1, Drawing App, and Option 2, Blackjack App.

# Part III: Dictionaries

Dictionaries are like simple mini databases.  They're great at keeping track of statistics.

Today we'll use **dictionaries of dictionaries** that will let you store and retrieve multiple stats about a state. This
is a core data analysis skill.


# Dictionary exercises today

We'll spend much of the class working **together** on your homework.  I'm here. Use me.
It's not due until next class, but I recommend you finish as much as possible during class or make plans to coordinate.

