---
layout: post
author: samandalib
title: "Final Project and Reflection"
---

## Final Project Trinket
<iframe src="https://trinket.io/embed/python3/b063dd06b1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Reflection
**I did most of my work on Jupyter notebook but for the purpose of the class I refactor a portion of it to the Trinket. However, what I am explaining here is the reflection and process for the project not only the Trinket part.You can see the Jupyter version with explaingi slides here:
https://github.com/samandalib/Stock_analysis_python/blob/master/StockAnalysis_presentation.ipynb**

The ultimate goal of this project is to get some visuals that convey an insight and help stock brokers to manage their investment portfolio in a more comprehensive way. By considering the changes in the stock price of a company and comparing those changes with other companies, I hope to get some insights on the relations between companies that cannot be easily understood by following news or studying historical data  of that company.  

This project had been passed 4 stages of progress to get to this point:

### Stage 1: Gather data
for gathering required data, I was trying to use [finnhub.io](http://finnhub.io) API as the source where I can get data from. This API had a good documentation and I was able to connect to the API and get the data easily by using the following lines of code and save the data in .csv files on my computer:

```python
import finnhub
# Setup clientm
finnhub_client = finnhub.Client(api_key ="b#########50")
  
try:
  
      # Stock candles
      res = finnhub_client.stock_candles(company, 'D', start_date, end_date)
      #res is a dictionary type

      #Convert response to Pandas Dataframe 
      response = pd.DataFrame(res)  
      
      #Write the CSV file out of data frame
      response_csv = response.to_csv(f"{company}.csv")
except:
      print('no company found ...')

```
The challenge here is that we want to get for example the data for top 100 companies in a period of time. To have the symbol of top 100 companies, I used a csv file to get S&P500 companies' symbols from using the following code:
```python
with open ("data_sets\\S&P500-Info.csv","r") as f:
        companies = f.readlines()
     
    company_list = []
    company_dictionary = {}#This is the main dictionary that I store company information
    
    for line in companies:
        line_list = line.strip('\n').split(",")
        company_list.append(line_list)     
   
		#Get the list of top 100 companies
    for company in company_list[0:101]:
        company_dictionary[company[1]]=company[2:]
 
```
Now that I have symbols of top 100 companies, I can get data from the API for each of them by using a for loop and the API code that I already used before:

```python
for company in companies:
        try:   
            # Stock candles
            res = finnhub_client.stock_candles(company, 'D', start_date, end_date)
            
            #Convert to Pandas Dataframe 
            response = pd.DataFrame(res)  
            
            #Write the CSV file out of data frame for each company
            response_csv = response.to_csv(f"{company}.csv")
        except:
            print('no company found ...')
```

### Stage 2: Cleaning Data
the output of the last step is 100 csv files saved on the computer. These files contain stock price of each company for each day within the timeframe specified. However, what I need is the price change from day to day. For this purpose I considered the 'closing' price as the one that I need. Now I have to read each file, get the closing price of each day and calculate the 

(c_day(n) - c_day(n-1)) where 'c' is the closing price.

To do the job, I first defined a function for reading each file and used a for loop to go over all the files and read them:
```python
def get_company_data(company):
    '''
    Function for returning information about specific company
    '''
    os.getcwd()
    with open (f"{company}.csv", "r") as c:
        company_data = c.readlines()
    return company_data[1:]
```

```python
#Dictionary to store price changes for each company
companies_records = {}
for company in companies:
        
        if (company + '.csv') in files:
            company_data = get_company_data(company)
            
            #get close prices in a list
            close_price_list = []
            for line in company_data:
                date_price = []
                line = line.strip('\n').split(',')
                date_price.append(line[1])
                date_price.append(line[6])
                close_price_list.append(date_price)
            
            #calculate the change in prices each day
```
By this step in my cleaning process, I will have a list of lists with name `close_price_list` in which each item is a list of `[<closing price>, <date>]`

But I cannot do anything unless I use this list to do my calculations on prices and have the difference of price changes between each two consecutive days. For this purpose, I found it easier to define an object (data structure) that I can easily reuse wherever I need it. I defined the class as below:

```python
#Object for having a data structure for the type of information that I want to store for my 
#furthur calculations in the program

class DeltaObject:
    def __init__(self, delta_change, percent_change, dates):
        self.change = delta_change
        self.percent = percent_change
        self.dates = dates
    def __repr__(self):
        return f'{self.change},{self.percent},{self.dates}'
```

At the next step, I calculate price changes in each two consecutive dates and store them in list called `change_list` using my `DeltaObject` data structure:

```python
change_list = []
for i in range(1,len(close_price_list)):
    
                delta_change = float(close_price_list[i][0]) - float(close_price_list[i-1][0])
                percent_change = delta_change / float(close_price_list[i-1][0])
                dates =(close_price_list[i-1][1],close_price_list[i][1])
                
                
                change_list.append(DeltaObject(delta_change,percent_change,dates))
            
companies_records[company]= change_list
```
Now company records is a dictionary that has companies' symbols as keys and a list as value that inside the list we have `DeltaObject`s.

### Stage3: Converting Data to Create Graph
As I said before, the goal of this project is to distill the data into a simple graph that shows the interdependencies between companies' stock prices. 

Up to this point, I have a dictionary named `companies_records` that  entails all the information needed for price changes for each couple of existing dates in the specified timeframe.

For each  DeltaObject that I defined before and its values exist in the company_data dictionary, I can define a color tuple. For example, if we want to get the first colored square of company 'C' in comparison with company 'A', we have to do the following:
```python
company_data = {'A':[DeltaObject0, DeltaObject1, ...], 'B': [DeltaObject0, DeltaObject1, ...], ...}

selected_company = 'C'
date_0_c = company_data['C'][0].dates
change_0_c = company_data['C'][0].change
percent_0_c = company_data['C'][0].percent

#data for company A
date_0_A = company_data['A'][0].dates
change_0_A = company_data['A'][0].change
percent_0_A = company_data['A'][0].percent

change = change_0_c * change_0_A#for determining the color
percent = percent_0_A/percent_0_c#for determining the color opacity

if change >0:
	color = (0,1,0, percent)#Green color with aplpha = percent
else:
	color = (1,0,0,percent)# Red color with alpha = percent
```

With keeping the idea explained above, the following function was used to calculate all the datapoints in the time range specified by the user:

```python
def get_compared_datapoints(company_data):
    '''
    function that takes the company data as a list of objects from the Deltaobject class and makes a nested
    dictionary in this format {time:{company_1:(Color tuple,..., company_n:(color_tuple))}}
    ''' 
    #let's compare data for the company with it's corrosponding data point in other companies
    data_points = []
    dict_of_dates = {}
    
    for i in company_data:
        date = i.dates
        change = i.change
        percent = i.percent
        
        lc=[]
        
        for symbol in companies_records:
            company_to_compare = companies_records[symbol]
            
            for k in company_to_compare:
                date_k = k.dates
                change_k = k.change
                percent_k = k.percent
                
                #set color of the comparison result
                if date == date_k:
                    if (change*change_k)<=0:
                        same_change = [1,0,0]#False #show in Red color
                    else:
                        same_change = [0,1,0]#True #show in Green color
                
                    # Set Color Opacity
                    try:
                        relational_opacity = round(abs(percent_k/percent),2)
                        if relational_opacity >=1:
                            relational_opacity = 1
                        
                    except:
                    
                        relational_opacity = 0
                  
                    same_change.append(relational_opacity)
                    data_point = tuple(same_change)                      
                    data_points.append(data_point)
       
                    company_date_dict = {symbol:data_point}

                    lc.append(company_date_dict)

        dict_of_dates[date] = lc
        
    results = dict_of_dates
    
    #merge separate dictionaries that are created in the last step
    for date in results:
        merged_dict={}
        for d in results[date]:
            merged_dict.update(d) 
        results[date] = merged_dict
    #returns a nested dictionary {time:{company_1:(Color tuple,..., company_n:(color_tuple))}}
    return results

```

### Stage4: Graph 
Creating a graph out of the data was the most challenging part of this project. I had very limited exposure to third party libraries like Matplotlib, Pandas and NumPy but the only thing I knew was that these libraries work together very well to create a graph out of data. 

In the first step, I tried to change my dictionary type data to a Pandas dataframe. It wasn't a hard work. I used the following line of code to do so:
```python
import pandas as pd
dataframe = pd.DataFrame(<dictionary>)
```
For taking the next steps, I was really confused. I was looking through [matplotlib.org](http://matplotlib.org) documentation to find a way to plot my data but they were more confusing than problems solving. 

After struggling with my data and matplotlib for a couple of days, I realized:

- The type of plot that I am trying to make is not of any standard type. Usually graphs are made of intersection of two measurable values (eg time vs. power) that we can expect to get linear graphs or scatter plots from them. The other type is when we have a measurable value such as company value and a label on the other axis such as companies' names. This type of data is usually reflected on bar charts or pie charts. However, the type of data that I am using is not measurable on either of axis. I want to show companies' names on one axis and deltatime objects on the other axis and the intersection of a company with a deltatime will be a colored square.  That requires some creativity and hacking skills to get something meaningful out of the existing functionalities of matplotlib
- Another roadblock on my way to get a plot of the data was the existence of `NaN` data in my dataframe. I had limited knowledge about pandas dataframe. To fill the gap, I took an online course on LinkedIn learning to understand the basics and it worked pretty well. The biproduct of this process was also learning some Jupyter Notebook as well that I really liked to work with but never had the chance.

    [Basics of Matplotlib - Python for Data Visualization Video Tutorial | LinkedIn Learning, formerly Lynda.com](https://www.linkedin.com/learning/python-for-data-visualization/basics-of-matplotlib?u=36306084)

    for cleaning the data out of `NaN` value, I first checked the existence of these values with the following line of code:

    ```python
    dataframe.info()
    ```

    Then I filled the gaps using the 'backfill' method. This method will use the next available data for the missing datapoint and fills the gap.

    ```python
    new_dataframe= dataframe.fillna(method = 'bfill')
    ```

Now that I have the data cleaned, I can go with my creative plan of making a graph from these data. I decided to go with bar chart as the base of my plot but instead of having one bar for each company, I will have as many as needed for my `delta_time` values with the height of 1 and I will stack them on top of each other to represent a single bar that color changes within its way going up. 

After struggling with my code for a couple of days and doing a lot of trial and error, I was able to achieve my goal using the following code:
```python
dataframe = pd.DataFrame(result)           

#Replace NaN values with valid values  
new_dataframe= dataframe.fillna(method = 'bfill')

#Ask the user to select how many companies they want to compare with selected company
selection = int(input("Number of companies to compare: "))

x_companies = companies[:selection]
y_date = 1 #height of the bar for each data point is eqaul to 1

colors_data = new_dataframe.values[:selection]

for j in range(colors_data.shape[1]):
    for i in range(selection):
        print(i,j,colors_data[i][j])
        plt.bar(x_companies[i], y_date,bottom=j, color=colors_data[i][j])
```

It was successful to get a meaningful graph out of this code. For example for company with symbol 'A', I selected 5 companies to compare with. 
