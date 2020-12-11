---
layout: post
author: cchinchia
title: "Claire's Final Project: Titanic Survival Prediction Tutorial App"
---

# Code
<iframe src="https://trinket.io/embed/python3/a408bdb9a2" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection

## Introduction

This is a program where I combined what I learned in this class and what I learned before. I took a machine learning class last semester. I want to tackle a challenge from the beginning to the end, and that is why I chose one of the most famous and entry-level challenges on Kaggle: Titanic Survival Prediction. The Kaggle website provides the dataset with several features such as gender, ticket fare, onboarding deck, and name title.
I built the model to generate the prediction. I also create the functions that users can interact with the app to customize their models and see the prediction rate immediately.

## My Process

My process can be separated into two phases. The first one is to build the machine learning model, and the other one is to make my app interactive.

I thought I would quickly jump into model training in the first phase, but I did not. Instead, I spent most of my time visualizing and cleaning data. I believe this is a precious experience for me. I get to understand the correct mindset to work on a machine learning project. Rushing into the building model is not a faster way, but having an overall understanding of what kind of data you're looking at is. At the same time, I gain the skills to create graphs that show what I want and to transform the data structure that can be better used for model training. The whole process of processing the data is snapshotted on my [Github](https://github.com/cchinchia/Titanic-Challenge/blob/main/snapshot-20201206.ipynb).

In the second phase, it is more fun, but I still experienced some struggles. The fun part is to ideate and create interactive functions, and to expect users to feel fun and engaging when playing with my app. I want to leverage python class in this part, and I went through many struggles while I tried to organize and break down the functions and code. I will elaborate on how I made it through in the later part.

## Dataset

My original dataset came from the Kaggle challenge, and the one used in my app is the one I have cleaned and processed. Most of the time, I worked on my project is to understand and transform the data structure. I cleaned the dataset that is well prepared for building the model. The cleaned dataset is without missing values, and all the contents in the cells are converted to integers. There are more variables in the original dataset and only the ones that affect the survival rate remain.

In total, there are three data files in my app. Two of them are used for machine learning models, and the other one is used for statistical analysis. The difference between them is whether the column of "Survived" exists or not.

## Visualize and clean data

In order to understand the data, I searched and used several different ways to create the graphs. I get more familiar with calling out certain parts of the data frame I want to look at and learning how to use different metrics to generate the plots.

One of the methods I find really useful and convenient when reforming the data frame is get_dummies(). It helps me convert string variables into integers in just a few lines of code. 

```
titles_dummies = pd.get_dummies(combined_df['Title'], prefix='Title')
combined_df = pd.concat([combined_df, titles_dummies], axis=1)
```

## Design

My app is designed for the users to understand this data challenge, how I tackle it, and most important of all, have a chance to try and build their own models. Therefore, when entering the app, users can choose options from the main menu. 

Some choices will be displayed only with texts, and some others will run functions that I write in other modules.

```
if choice == '2':
   main_model()
if choice == '3':
   sex_stats()
```

One of them is for users to play with models, and the other is to show statistical facts.
The first one is the most complicated part of my app. Here I combined classes, dictionaries, and functions to construct the whole feature.

First of all, I built the interface of the class of model. The fit() function is used for fitting in the dataset I provided for the machine to train the model, and the compute_score() function is used for computing and presenting the prediction score.

```
class Model:
 def fit(x, y):
  pass
 def compute_score(x, y, scoring):
  pass
"

I then created instances for different models and assigned them with distinct arguments that users will have the flexibility to input their own parameters.

```
class DecisionTreeModel(Model):
 def __init__(self, depth, split, leaf):
  self.decision_tree = DecisionTreeClassifier(random_state=2, max_depth=depth, min_samples_split=split, min_samples_leaf=leaf)
…
```

I chose the decision tree model and the random forest model because they have better prediction rates in my previous analysis. Also, I used the grid search method to find the best parameters. And I used them as default options to compute prediction score, while users can choose to input their own parameters and compete with me.

After this, I wrote the functions that gather and react to user inputs. Based on the users' inputs, different class objects will be created and then apply to model training and prediction. I spent a lot of time modifying and testing the code to make it work. Now I can see why the class is powerful, but it is tough for me to design the code that maximizes its value.

```
def set_up_decision_tree_model():
 …
 elif (param_choice.lower().startswith("n")):
  depth = input("What is the maximum depth of the tree (default=5)?\n")
  split = input("What is the minimum number of samples required to split an internal node (default=20)?\n")
  leaf = input("What is the minimum number of samples required to be at a leaf node (default=25)?\n")
  return DecisionTreeModel(int(depth), int(split), int(leaf))
```

I also used the dictionary to store the functions corresponding to the user inputs. I find it surprising that I can store functions in the dictionary, and I think doing so makes my code more readable and clean.

```
model_options = {
  '1': set_up_decision_tree_model,
  '2': set_up_random_forest_model
}
```

Other than playing with models, I used the for loops to calculate the survival rate for specific groups. Pandas data frame works differently from the way we learned in class. I found the pandas iterrows() method that is suitable and commonly used for looping through data frames.

```
for index, row in z.iterrows():
  if row['Survived']==1:
   if row['Sex_Code']==1:
    survived_female+=1
…
```

If I have more time, I will add more models for users to play around with and display more statistical results for reference. So far, I am satisfied with what I achieved, and I hope users like you would enjoy my app!

## Overall

Thinking back from what I created at the very beginning of the semester, there is a huge leap between what I can do now and before. Working on a programming project from scratch to finish forces me to think about how I should design the whole code to make it easily maintained and modified. Although I often just sat in front of my computer and kept deleting and rewriting a particular piece of code, I still enjoy the whole process. At first, I only write linear code that can only be executed once. But for now, I can break down my program into pieces and write individual functions that can be reused. Also, I feel more comfortable facing roadblocks and challenges. I can leverage the resources I have, including websites such as Stackoverflow and peers. 

Besides, I like how I can create a program that combines what I learned before. I bring what I learned from the previous class and leverage the new things I learned in this class to reach a higher goal. Coming with a UX background, I also adjust my code when I feel the adjustments can lead to better user experiences. For example, I added a line saying "computing score…" when it takes a few seconds for my program to compute the score. In the future, I hope I can apply all the things I have to create something different. After this individual project, I feel more confident in challenging myself with coding. Now I know I will figure out what the solution can be. This class provides a good environment for me to try things and feel safe, even encountering failures. 

Another thing I think I might try afterward is to collaborate with others to contribute to a bigger project within limits time frame. I have previously worked in a team setting for design projects. I learned from others and experienced different struggles while working together. I believe the programming project will be another kind of challenge for me, but I expect the result will be fruitful. 


