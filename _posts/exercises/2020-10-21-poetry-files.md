---
layout: post
author: elliott
category: exercise
title: "Poetry Slam Files"
published: false
---

**Make a Copy of your Poerty Slam Trinket for this exercise.**

Submit a well-formatted pull request to our blog with a modification of your Poetry Slam trinket.  The modified trinket should:

* Allow the user to save their poem to a file in the trinket when they're done.
* Allow the user to specify a file name

Optional (push yourself!):

* Allow the user to choose to load a file instead of typing a poem
* Display the poem from the selected file as if they'd typed it in.  `.readlines()` might be helpful to produce a list of all the lines in the file.
* After the user is done entering their poem and it is written to the screen, the
program keeps going, asking for another poem.  Make sure the old poem is cleared when
the next begins.  The user can potentially generate and/or read from any number of files, depending on what else you implement.