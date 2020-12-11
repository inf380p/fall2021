---
layout: post
author: pccisme
title: "Patrick's Final Project: New York Times News Analysis App"
---

# Code
<iframe src="https://trinket.io/embed/python/053ff5e2e1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>



# Reflection

## Introduction

I chose data analysis as the topic of my final project, and I wanted to analyze news-related data. Finally, I used the New York Times APIs to obtain the data I needed and wrote a program to analyze and visualize these News data.

## Select data source

Whether it is for data analysis or machine learning projects, I find that choosing the right dataset is the most difficult and important part. Because the content of this dataset will directly affect the functions that can be developed later. For example, if my data set does not indicate the reporter who writes each news item, even if I have strong development capabilities and experience, I will not be able to make a function related to reporters because I have no reporter data at all. Especially when all the functions have not yet been determined, I would hope that my data set can contain as many kinds of data as possible. But at the same time, I also hope that the data is of high quality, not a bunch of unorganized messy data.

So, I tried multiple news-related APIs on the Internet, and I paid special attention to those APIs services provided by large Internet companies and well-known news agencies. In addition, I must also understand the limitations of these APIs for free users. Some services limit the number of data requests per hour, and some services limit the amount of news that can be obtained. But I must emphasize that I think most services charge very reasonably. They provide reliable and comprehensive services. If you have a mature product, these services will be a good choice. However, because I will only use it on my final project, and I don't have a budget of several hundred dollars to pay for these services. Therefore, under the above premise, free access to high-quality data is my main demand.

In the end, I chose New York Times APIs. Their service limits the number of visits within a certain period of time, but I do not have the need to obtain large amounts of data in a short time. Moreover, this API allows me to access news data from now to 1851. I felt that I might be able to complete some very interesting analyses, so I was very excited.

## Preview Dataset

In addition to reading the instructions for each API, I also applied for their free account and tried to send data requests. In this step, I use Postman and Google Colab. First, Postman is a popular API client that allows users to test APIs. Therefore, I use Postman to send data requests and take a closer look at the data the server sends back to me. Second, Google Colab can run Python code and see the results instantly. I will use Google Colab to test some simple operations. For example, I want to know whether I can correctly collect the data I want in a dictionary, list and other data structures. In short, I want to test whether I can easily use this dataset with Python code.

## Developed in Python

I think I have some familiarity with loops and functions. Therefore, in this section, I want to explain how I use Dictionary and Classes learned in class.

### Dictionary

I remember when I first learned the concept of a dictionary, I thought the dictionary looked boring and the list looked more flexible and easy to use. But when I was reading some dictionary related articles, I found that it is a very efficient data structure. When retrieving from a dictionary with a key, the time complexity is O(1) in big-O notation. In addition, I heard that Google uses the concept of the dictionary to realize its powerful search engine. Also, I know more about dictionary by studying the classic leetcode question: "Two sum". These make me pay attention to the dictionary.

In my code, there are mainly two parts where the dictionary is used. The first is in my dataset. The dataset I get from New York Times APIs is a json file, and json itself is a dictionary. I access the data I need, so I must use the key to find them correctly. In addition, in the counting function, I also use a dictionary. Here I use a dictionary to complete the efficient counting function. And I would say that this function is the soul of this program. Without this efficient counting function, the parts of data visualizations would not be possible.

### Class

I must admit that I rarely used Classes before. I have completed Classes related assignments in some online courses, but I rarely use Classes in my previous projects. I may only use Functions for most data analysis tasks. Therefore, one of the difficulties for me is where I should use Classes in my project.

Finally, I have three Classes in my project: News, PopularNews and ArchiveNews. I turned the entire dataset into a Class, and in this Class, the main functions are also included, making the entire code very concise. It is worth mentioning that I used the concept of inheritance. I learned this concept from Java last summer, but it was hard for me to think where I could apply it. This time, in my code, I took out the two same functions in PopularNews and ArchiveNews, and put them in a Class named News, and let PopularNews and ArchiveNews inherit News. I think it’s a cool thing that I can use the concepts of Class and inheritance in my project.

## Process

As mentioned earlier, I spent a lot of time looking for suitable datasets and testing them one by one.

After finding a suitable dataset, because I have less experience in using Class, I tried to operate the dataset in Python on Google Colab. I also tried to write a few classes to try and make sure they can run. In the steps, I tried and made some mistakes, but these experiences are very valuable, and I have more confidence in the use of Class. At this stage, I also built the main text based GUI.

After finishing the preliminary test, I started to implement the functions I planned on Trinket. But I immediately found out that I could not use external libraries on Trinket. I originally used a Python library called “pynytimes” on Google Colab. This library allows me to easily obtain data from New York Times. But I think this is a challenge for me, and I must overcome it. Because in different situations, the resources available to you may be limited, and how to use the available resources to complete the original task is also a challenge, and I think I may encounter similar problems in my work in the future. 

Actually, I have had similar experience before.When I was serving in the military in Taiwan, my superior asked me to remove the background for a few photos. As an amateur photographer, I didn't think this was a difficult task at first. But then I discovered that due to information security considerations, all computers in the military are not allowed to connect to the Internet. And I only used Microsoft Powerpoint 2003 and Microsoft Paint. Finally, I used these tools to complete the task of removing the background from the photos. Before this, I never thought I could use these tools to remove the background.

In order to implement my program on Trinket, I read the user manual of New York Times APIs again and understand which libraries on Trinket are available to me. Then, I use urllib and json libraries to get datasets from New York Times APIs and read them in JSON format. In addition, I originally used the heapq library on Google Colab to quickly find the N largest. I once considered implementing nlargest by myself, but due to limited time, I had to give up and tried to achieve my function in other ways.

For the UI, I designed a two-layer UI menu. One of the problems that I spent a lot of time solving is: before returning to the top menu, I hope that the user can continue to operate on the dataset he or she just selected. In other words, my program does not need to re-acquire the dataset every single time it executes a function, which is unreasonable in terms of workflow and efficiency. In order to achieve this goal, I used a while loop. If the original user has already specified a certain topic or time dataset, before he or she returns to the top menu, other functions will be executed with the original dataset, and there is no need to ask the user topic or time again.

Finally, I re-run the program several times and added protections to the options at two layers. So, the program will not be terminated due to an invalid user input. And when receiving an invalid input, a warning text will show on the screen. The above is the process of creating my program.





