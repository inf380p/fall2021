---
layout: post 
author: daiblej
subject: "Janet's Final Project 2nd Update"
---

2020-11-18
This week, I used google colab to clean the dataset. By using different functions, I now have a clearer understanding on the dataset. Google colab is easy to check each step outcome. However, there are some differences between colab and trinket. I have to figure out how to transfer the file to trinket. 

When I reviewed the final project material, I found there are some requirements that I need to meet:
*- Include more than one data file in the trinket
- Have help text available somehow. For instance, if the user types ‘Help’, explain what they program can do.
- have an iterative interface. That is, the user should be able to perform any number of supported actions and then exit the program.
- Visualize data via text printouts. 
…or, if you prefer, use a third-party module such as matplotlib, pygal, bokeh, etc. to produce graphical output*

Thus, I revised my milestone again:
- [x] find ~~a~~ two proper datasets
      * I use [google_play_store](https://www.kaggle.com/lava18/google-play-store-apps) and [apple_store](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps)
- [x] import the data into trinket
- [x] clean the data
    [x] delete wrong data
    [x] delete duplicated data
    ~[x] delete non-english data~

- [ ] calculate the categories/geners
- [ ] make a dictionary for different categories
- [ ] rank the list by rates, downloads, reviews
- [ ] minimize the list to 10 apps for one category
- [ ] use loop to find the highest rate and the most popular app
- [ ] ask users to choose the type
- [ ] random choose one as recommendation
- [ ] ask user whether they are satisfied wth this recommendation
interface
- [ ] help function
- [ ] a clear layout

Snapshot
<iframe src="https://trinket.io/embed/python3/17b9813812" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
