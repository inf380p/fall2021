---
layout: post
author: samandalib
title: "Update on the final project"
---

The ultimate goal of this project is to get some visuals that convey an insight and help stock brokers to manage their investment portfolio in a more comprehensive way. By considering the changes in the stock price of a company and comparing those changes with other companies, I hope to get some insights on the relations between companies that cannot be easily understood by following news or studying historical data  of that company.  

The update for my milestones is now like this:
- [x] Find the appropriate API to get data from
- [x] Refine data and make it ready for doing some calculations
- [x] Do calculations on data to get data ready for visualization
- [x] Learn basics of Numpy, Pandas and Matplotlib to be able to work with my data
- [ ] Visualize data gathered
- [ ] Make the program responsive to user inputs

For connecting to API, I found a good API to easily connect to and retrieve required data for my project. I called the API and saved the result in `.csv` format on the local machine. The code that I used for this purpose is as below:
```python
import finnhub
# Setup client
finnhub_client = finnhub.Client(api_key ="########")
  
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

Though my initial plan was to work on Trinket,I was not able to do so because as you can see in the code above, I need to `import finnhub` to the program and Trinket didn't support Finnhub. So I had no way but to continue my work on the local machine. When I wanted to import my code into Trinket, I found it the best to creat a portion of my work in the Trinket so that it can be managable. 
The following code shows a snapshot of what I did so far to get to a point where I can visualize data by using Panda's dataframe:
<iframe src="https://trinket.io/embed/python3/2bd145dae8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Reflection
I think setting the initial milestones helped me to be able to manage my time and have the status of my goals during the project implementation. I think the main roadblock for me is to get a clear and understandable visualization of the data that I managed to get so far. Learning `Matplotlib` is one of the prerequisites of this step. I believe my milestones were ambitious enough that it takes to much time and iteration to get to the point where I am right now. I think I need to dedicate more time and effort to this project to be able to meet the final deadline mostly because I didn't anticipitated that cleaning and transforming data takes this amount of time.
If I want to do this project again, I will design the process from the final output back to the required inputs so that I prevent wasting my time on things that are not really important for this project.
