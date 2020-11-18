---
layout: post
author: pccisme
title: "Patrick's Final Project Update"
---

## My Reflections

First, I was focusing on how I can play with "[News API](https://newsapi.org/)". At the beginning, I learned to use the request library to get data from an API service. I do not have to download the json format file and upload it again. Then, I found that there are mainly two ways to get the news data: by "everthing?" or by "top-headlines?". Later, I try to get the titles of each news and count how many times each word shows up by dictionary. However, it seems that there's limit that I could not really get every news from News API. In the next week, I want to try other API services and choose one to use in my final project. It should be reliable and free to use most of the functions I need.

### 2020.11.18 update: 
Second, I tried "[New York Times API](https://developer.nytimes.com/apis)". One thing really impressed me is their "[Archive API](https://developer.nytimes.com/docs/archive-product/1/overview)", which allows developers to get NYT articles data from 1851. I was excited and thinging about what I can with Achive API. Currently, I create two classes to achieve functions that we can count the number of articles, trending of keywords, section distribution, geographical distribution, etc. In the next step, I want my application can do more visualization with Bokeh, and also show some news urls as examples when I show the analysis results. 

## Code

I have used [Google Colab](https://colab.research.google.com/) for a couple of previous course projects. As I am more familiar with Google Colab, I use it to explore the APIs and compare their differnces.

You can check my first work [here](https://colab.research.google.com/drive/1j9oJiMGMYGFNhtdvK4MhkoPXtCrZm7Fz?usp=sharing).

### 2020.11.18 update: 
Here is the code working with New York Times API [here](https://colab.research.google.com/drive/156vbngdRs9TuTEOtDUW6Ku11sEy4ws5A?usp=sharing)

## Current Milestones

- [ ] Compare different options and select the API I want to use in my project
- [ ] Fetch news data in JSON format
- [ ] Get the titles and put every keywords in dictionary and count them
- [ ] Desgin an UI to show the result
- [ ] Work on building some data visualizations
- [ ] The applcation can work automatically update data every day
- [ ] Advanced features!

I did not update my milestones because I see that I am still in the very first section. Also, I feel that for any data analysis project, how to collect (or to choose/create) the right dataset is always the most difficult topic. If we don't find an ideal dataset, the quality of the project would be lower than expected.


### 2020.11.18 update: 
- [X] Compare different options and select the API I want to use in my project
- [X] Get articles data and use dictionaries to find the trendings
- [X] Design an text-based UI to show the results
- [ ] Work on building data visualizations with Bokeh
- [ ] Bring some news and their url as examples when display the analysis results.
- [ ] More advanced features!
