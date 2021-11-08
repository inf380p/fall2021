---
layout: post
author: agunnells
title: "Ali's Project Idea & Work Plan"
---
I plan to pursue the data analysis track for my final project. I have recently been pursuing research related to text analysis for my English MA degree. In particular, I am interested in looking at short stories specifically at the level of language; in other words, a lot of my research involves comparing the words used in a text and the number of times that each word appears. While there are some Python scripts that mathematically measure the similarities of two or more texts, they do not actually provide information about which words appear the most frequently in a text. Therefore, I would like to see if I can figure out how to create a project that can provide information about how often certain words appear in a text and compare that to other texts. 

I plan on using .txt files for my project; there are many .txt versions of short stories available on Project Gutenberg. I will likely use short stories written by Charlotte Perkins Gilman, as I have worked with her writing before, although any short story available in .txt format can be used. The goal for my project is to be able to create a dictionary for each file that includes a count of how many times each word in a text appears. Then, I plan to include the third-party module `pygal` to produce visuals that compare the word counts of multiple texts. For instance, I might have the module produce a bar chart that compares the top five most used words from two different texts. Ultimately, the individual words will be the data that I work with, and the text files will be the data sets. 

My initial work plan consists of the following milestones:
	1.	Identify texts to use in the project; write code to open and read the text file, as well as remove all punctuation marks
	2.	Create a dictionary for each text file; write a function that uses a `for` loop to count each instance of each word in the text file and add each new instance to the text file’s corresponding dictionary 
	3.	Create a custom module that provides a variety of actions for the user to perform on a text file’s dictionary, such as returning the top five most used words for one text or providing the number of times a word appears across a variety of texts
	4.	Incorporate `pygal` so that the user can produce visuals from the data
	5.	Create help text and determine how the user will access it
