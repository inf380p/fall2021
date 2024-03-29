---
layout : post
author : vannyyeh
title: "Vanny's Final Project Reflections and Trinket"
---

# Trinket

<iframe src="https://trinket.io/embed/python3/1fa7212a36" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

# Brainstorming

Before starting the project, I always wanted to create a system that could tell me the most real-time weather using the zip code. I felt the info I got from iPhone or any other platform is not as accurate and specific as the zip code searching. Therefore, when I realized that I needed to do a python 3 program, I was excited to turn my abstract concept into an actual application. In the beginning, I had an ambitus plan about fetching the IP address but not focusing on building the data structures in python. Therefore, I started to import existing data files from open-source platforms. After that, I begin to realize that my work is not only a weather fetching app but also a data analysis app!

# Introduction of the program

This is a weather-fetching data application. It pulls the data from the "open weather map" and gives users the most real-time weather information based on your input location, and it can also provide you with historical data of Texas state. Therefore, this program breaks into two parts. One is the current data, and the other one is the historical data. Users can easily switch between two functions by going back to the homepage. The `help` function has been implemented and guides the user when they lose in the game.  

The flowchart of the program:
![Flowchart copy](https://user-images.githubusercontent.com/70726508/145448947-5ddec08b-31f8-4822-8ce6-818f7073b290.png)


# Programming process 

The project had based on 2 main different components it, “CSV” and “API” but there are also some other challenges that I have encountered.
### API
The first challenge I faced was having the API settle up. It’s my first time to import a built-in function that hasn’t been covered in class before. After watching a couple of tutorials online, I quickly grabbed the concept of requesting the API. However, I kept looking for the API key until I realized that it should only be personal; everyone has its unique code. 
I am using the slimier idea of finding the ‘main’ column and ‘temp’ column, which matches those names, and it will return back the number. Because the value I got from openweathermap.com is Kelvin, so I used the formula to turn it into Fahrenheit and round it up to an integer. 
For example: `temp = round(((api_data['main']['temp'])- 273.15) * 9/5 + 32)`

### CSV & Dataset
Moving on to the CSV part is the most challenging part for me because I want to group and split the data to catch specific rows from the CSV file. I built a data structure of a data dictionary. I will need to pull the data from a particular date range from the dictionary. I was struggling with how to group the datetime. My goal is to filter out the “time” of the column and set up a time range. I did a lot of research and tried `datetime`, `groupby` and rows, etc. 
The groupby function was not working when I tried `pd.groupby('2020-01-01' : '2020-01-31')`, I think it’s because that it couldn’t recognize it as an item. Therefore, I end up using `pd.to_datetime('2020-01-01') and pd.to_datetime('2020-01-31')` 

Besides, I am using `.loc` to get values on a data frame with an index that has integer labels. `.loc` is primarily labeled based on pandas. 
For example: `sum_lt_1 = records.loc[records.time <= ts1, :]['temperatureLow'].sum()`
according to the datetime on the previous section, I am using it for setting the date range and then, I get the value of 'temperatureLow' from this time range.  This function helps me to organize all the data from specific columns and a requested rows. 

After I created the dictionary of months, I used a for loop to go through the data with the specific months that the user called. And the data of each specific month has already been organized by using pandas.
The below codes show how I implement the dictionary and for loop to print out the data.

```
#calling the function of the custom dictionary that ask Python to do the math!
def get_monthly_weather():
  print('Please follow the format of YYYY-MM')
  print("Choose a month:")
  for month in ["2020-01", "2020-02", "2020-03"]: #dictionary column
    print(month)
  month = input()
  print(Purple + "For the month of", month +":" + Color_Off)
  stat = months[month]
  for stat_name, value in stat.items(): #implement the for loop to output the data
    print(stat_name, ":", value, "°F")
```

### Recursion
The third challenge was allowing the user to perform any supported actions and then exit the program. It makes the program runtime slower if I make a while loop in every function. Thus, I want to enhance the program by using a better logic which is recursion. Therefore, I called itself function again at the end of the function. However, I met 2 new issues when I was doing this. 
First, import the function from the main file because I want to go back to the homepage. I solved the error by doing `from main import start_the_Game` in the custom function, not at the beginning of the .py file. I don't know the difference and why I can't import the main file at the beginning of the .py file. 
Second, I had to define the statement as true before breaking the loop. Otherwise, the loop can't be break. 
```
def start_the_Game():
  Api_or_historical = input(Blue + 'Do you want to know historical weather data of Texas of current weather OR all the city in the world?' + Green + '\n\npress [1] Current weather\n\npress [2] Texas historical data from Jan. to Mar.\n\nEnter No or exit to exit the program \n\nEnter Help for help' + Color_Off)
  while True: #define it to True 
    ...
    elif Api_or_historical in exit_answers:
      print("See you next time!")
      break  #leave the programe
    ...
```

### Color
After completing the flow of the program, I felt something missing, and the UI was not smooth enough. Before moving all the codes to the PySimpleGUI, I decide to do the simple color text and font at this moment. Therefore, I create a new module python file to save all the code for colors and bold fonts. I add the color in front of each print line, yet, there is a new concept that I need to be aware of. Because putting the color function in `print()` means starting from the word after the function will apply the color but it doesn't ask to stop using the color function. Therefore, I created a default reset code to use at the end of the print line. Remarkably, I can customize each print line by different colors efficiently without remembering what color has been used in the previous line. 
For example: `print(BIRed + 'text' + Color_Off)`



# Reflection

The first API punish me severely, I was middle of nowhere trying the API key and requesting the wrong data with an incorrect API key. Also, I didn’t expect there will be some unexpected disconnection error from the server that I tried to connect to before I had several terrible test cases. I kept using the wrong city name which I didn’t realize, so I was debugging the wrong way by using a different code to execute the `request.get(api)`. It cost me hours to figure out it’s my wrong input that caused the error. Of course, I end up using ` if api_data['cod'] == '404'` to prevent this situation. Therefore, this experience taught me to think about every single possible scenario of the program and I should write every possible test case so it would be easier to debug. 

I find it funny that out of all the progress I've made since then, I should make more data structures in the file than now. Looking back, perhaps I could have figured out a way to extend the dictionary to more sections that could be covered in the python file. However, the limitation of the CSV size of the trinket is one of an obstacle to doing this. I can't import a large file, it makes the trinket keeps running without any available output. Therefore, I kept squeezing my CSV file, from World historical data to the United States only then containing Texas with just three months. 

I also find the recursion part interesting because I need to consider all the cases when the user wants to jump back to the return page. I decide to make the user goes back to the homepage to quit the game because I don't like the user to leave in any specific function by mistake. If I make the quit function in the individual function, it might mistakenly tell the wrong message to a user for just leaving that function but not the game. Therefore, I set the quit function only in the main `start_the_Game()` function. 

Through the course of this project, using dictionaries played a critical role for me. Therefore, I appreciate the changes and progress that I am more able to create a nested dictionary and use the `for` loop to output the assigned value in the dictionary. Further, The API taught me how to locate the data by using the index and the parameters. Hence, after completing this project, I have more confidence to move on to the next step and become a better programmer. 
I aim to turn this project with GUI by importing `PySimpleGUI`, I believe this could be an excellent chance to evaluate what I’ve done and optimize this program in the future. 


# The skills and attitudes I used and will use

Overall, I felt confident and proud of making my final project. I think this is the most important and valuable milestone of becoming a programmer for me. The project gave me a good first impression when I made the brainstorming. However, when I dig more details and did the research furthermore, I realized that this project is more challenging than I expect. Therefore, I started to put more effort into this and it’s worthful. Nevertheless, I also put attention to writing a good styling code and keeping my name consistent like using the underline (start_the_game) instead of (startTheGame). I believe having this good habit could help me in my career. 

After going through the first challenge I mentioned previously of API, I felt more confident building something new that is not covered in class. I strongly feel that the most valuable skills I learn from this class and this project are not just using python itself but also how to utilize and carry the fundamental concept to apply on the new programming skills and other algorithm concepts. For example, I now know how to use and convert the code if I found a sample code on stackoverflow.com which is not in my skillset before doing this project. As well as, I heard "doing google search" is the essential daily life of being a programmer in career life from my meet-up. Therefore, I am delighted about myself of able to read and understand the new codes. 


# --- Update reflection after the code talks ---
After hearing my classmates discuss their work, it triggered my interest in doing the graph. Therefore, I tried to make a graph of catching the data from API. I hope I can make more graphs based on using the dictionary in the future when I have more time and knowledge. For all that, I also learn to put input inside the function while putting the assigned parameters. For example, `get_graph(a,b,c,d)` and I assign the parameters when I call the function `get_graph(temp,feel_temp,max_temp,min_temp)`.

Below is the screenshot of what I add:
<img width="461" alt="Screen Shot 2021-12-09 at 7 58 30 PM" src="https://user-images.githubusercontent.com/70726508/145505538-74f46e54-8860-4676-8b1b-83a6e2d7643c.png">

