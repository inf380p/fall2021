---
layout: post
author: samandalib
title: "Final project progress"
---
When I started this project, I was sure that I have to gather the data that I need to work on. So the first task was to find the right API to get data from. I explored different options and decided to go with [Finnhub.io](http://finnhub.io) because it has a good documentation and easy workflow. 
I spend a couple of days working on the data that I can get from API and making sure how I can use the data. 

The first challenge was understanding UNIX timestamps that exists in the dataset and converting those to human readable timestamps and vice versa. After searching for the solution on the internet, I created two functions to do this job for me:

```python
def date_convertor(date):
    #convert the time to UNIX timestamp
    import time
    result = int(time.mktime(time.strptime(date, "%d/%m/%Y")))
    return result #Returns Integer type
    


def timestamp_convertor(timestamp):
        import datetime
        result = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')
        return result #Returns String type
```
Next step for me was to get all the data that I need and save it on my computer so that I don't need to call the API each time the program runs. To do this, I needed a list of company symbols that I was going to work on. I wanted to work on the first 100 companies in the SP500. So I looked for a source to get symbols and found the following lines that helped me to end up with a list of SP500 companies information:

```python
table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df.to_csv('S&P500-Info.csv')
df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])
```

At this point of project, I think the main challenge for me is to clean data and prepare what I can gather to be usable for my purpose. I think my milestones can be even tougher from what I was thinking of at the begining of the project. My program so far is mostly consisted of some helper functions for this program:
<iframe src="https://trinket.io/embed/python/080268889c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here are my milestones that I have submitted last week:
- [ ] Finding appropriate datasets that I can get data from
- [ ] Cleaning up data as necessary
- [ ] Learning and using Numpy, Panda and Matplotlib for analyzing
- [ ] Write the code to use data for analyzing using data science libraries
- [ ] Visualizing the output with Matplotlib
and my strech goal was to consider using a REST API to keep the data updated whenever the user wants to try it. But after a week of work I am in a different direction. Actually I started with my strech goal and captured all the data that I need from an existing REST API and started refining the data. 
My new list of milestones will be as follows:
- [x] Find the appropriate API to get data from
- [x] Refine data and make it ready for doing some calculations
- [ ] Do calculations on data to get data ready for visualization
- [ ] learn basics of Numpy, Pandas and Matplotlib to be able to work with my data
- [ ] Visualize data gathered
- [ ] make the program responsive to user inputs
