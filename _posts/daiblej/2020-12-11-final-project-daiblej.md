---
layout: post
author: daiblej
title: "Janet's Final Project and Reflection"
---

2020-12-11
##Project Introduction
This code mainly help users understand the data itself. 1. know how many columns and rows does the original dataset has 2. discover wrong data and duplicated data 3. discover categories and look for most rated, installed and reviewed 
A little different from a normal data analysis project, I used two different ways to do the same data analysis, trying to understand the differences between different analysis ways. 

##The Process
The process is much harder than I expected. I had to debug the code again and again without others' help. I have to say I was frustrated several times during the process. When I googled some data analysis projects online in the beginning, I found people most use jupyter notebook and pandas modules to analyze data. Unfortunately, I'm not familiar with any of them. However, data analysis looks so simple by using these two tools so I started learning google collab, which is a similar tool to the jupyter notebook. But, again, it's much harder than I expected. As I was not familiar with pandas and any other modules outside the class, I have to spend a lot of time understanding others' code. It wasted me a lot of time. I also noticed the code runs differently in the notebook and in the trinket. This made me much more confused. I talked about the problem with the professor in the class. He said I should focus on the code itself, not the data analysis quality as it's a programming class. Finally, I realized if I want to better apply the knowledge I learned to practice, I should avoid using the notebook. I had to first better understand how the code runs in a normal way before going advanced.:disappointed_relieved:
This is the reason why I start use the basic Python language writing the data analysis code. I really want to share this experience to you because knowing my limitation is also something I learned from this class. Fortunately, you could see how I improve myself step by step in the later process. 

:one:
**1st update**
<iframe src="https://trinket.io/embed/python3/fd7fe26ceb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
My first step is to clean the data. Sorry to say so, but, again, it's not that easy than I expected. Actually, I spent most of my time in this project cleaning the data. I have two dataset. One is [google_play_store](https://www.kaggle.com/lava18/google-play-store-apps) and another is [apple_store](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps). I developed a class to analysis the two different dataset without copying similar code:
```python
class understand_data():
  def __init__(self,dataset,titleline=[]):
    self.dataset = dataset
    # self.titleline = []
  # see all the titles  
  def titlename(self):
    for line in self.dataset[0:1]:
        self.titleline = line.split(",")
    print("Title name:", self.titleline)
    # print(len(self.titleline))
  # understand the row and column
  def row_column(self):
    print ("Row:",len(self.dataset))
    print ("Column:",len(self.titleline))
 ```

:two:
**2nd update**
<iframe src="https://trinket.io/embed/python3/17b9813812" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
By reading the discussion in kaggle.com, I noticed the row[10472] is a wrong input which we need to delete. But I wanted to prove we only have thi sonly wrong input in the dataset. I used ` len(row) != len(google_play[0])` to test my dataset but turned out that I haven't separate the list by ','. I could do so but I also noticed that csv is a style of file that seperate items by ','. I learned to import 'csv' module, which automatically separate the list.(reference:
# https://stackoverflow.com/questions/51644941/typeerror-csv-reader-object-is-not-subscriptable)
```python
import csv
with open("googleplaystore.csv") as f:
    google_play = list(csv.reader(f))
 
with open("AppleStore.csv") as f:
    apple = list(csv.reader(f))
```
finally, I developed two functions, helping recognize wrong input and duplicated data. I deleted these useless data from the dataset.

:three:
3rd update
<iframe src="https://trinket.io/embed/python3/ae0f472c40" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
At this stage, I have to wait for a while for the analysis result. I didn't execute the code line by line as it has to wait for a pretty long time. And since it had been already long enough, I thought maybe I should have another '.py' to save the classes and functions I created. I named it 'understand_data.py'.

:four:
4th update
<iframe src="https://trinket.io/embed/python3/939224b995" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
I didn't know why but the waiting time became longer and longer. The only possible answer I had is the code is too complicated to quickly go through each line. So, is there a better way to analysis this big dataset? The pandas module. 
I decided to rewrite the code using this commonly used module. But before that, I have to learn the commands of pandas. I wrote the same functions I had before.
For reading row and column, it's much easy to finish by using `dfg.shape`.
For wrong input:
```python
print(dfg.loc[[10472]])
dfg.drop(dfg.index[10472],inplace = True)
```
For duplicated data:
```python
dfg.drop_duplicates(subset = ['App'],inplace = True)
```
I ran the code locally on my laptop. It's much more quickly than the previous one I wrote.
I also learnt 
drop column:
```
dfg.drop(['Size','Content Rating','Last Updated', 'Current Ver','Android Ver'], axis=1, inplace=True)
```
sort value:
```
dfg.sort_values(['Category','Rating'], ascending = [True, False], inplace = True)
```
transfer a column to a list
```
app in dfg['Category'].tolist()
```
By using these new commands, I start another round of data analysis, trying to understand the categories by rates, installs and reviews.
##Final Milestones
- [x] find ~~a~~ two proper datasets
      * I use [google_play_store](https://www.kaggle.com/lava18/google-play-store-apps) and [apple_store](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps)
- [x] import the data into trinket
- [x] clean the data
    -[x] delete wrong data
    -[x] delete duplicated data
    ~~-[ ] delete non-english data~~
- [x] data analysis
  - [x] calculate the categories/geners
  - [x] make a dictionary for different categories
  - [x] rank the list by rates, downloads, reviews
~~- [ ] minimize the list to 10 apps for one category~~
interface
- [ ] help function
- [x] a clear layout

##Features need to include:
-[x] External data files.
-[x] Dictionaries
-[x] Custom modules
-[x] definite (for) loops
-[x] Custom functions
-[x] Custom classes - Extended or created from scratch.
-[x] A Python 3 Trinket

-[x] Include more than one data file in the trinket
-[x] Have help text available somehow. For instance, if the user types ‘Help’, explain what they program can do.
-[x] have an iterative interface. That is, the user should be able to perform any number of supported actions and then exit the program.
-[x] Visualize data via text printouts.
-[x] use a third-party module(I choose pandas)

##Final Code
#code with pandas
<iframe src="https://trinket.io/embed/python3/28968cdfc8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
