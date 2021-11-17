---
layout: post
author: lulomax
title: "finalproject 2"
---

  My plan has not changed, only finalized. I'm going to explore diversity or the lack thereof in the iSchool using graphs (mostly pie charts) that will reveal the actual numbers--not the promises--of minority students and faculty in the School of Information. I will write code using matlablib to graph the proportions of blacks, Latinos & men among student body and faculty including a breakdown, I think, of those who are tenured or tenure-track faculty. I will add a display of the races of the iSchool's extraordinary all-female Diversity & Inclusion Committee, and for comparison also do a visualization of the campus's numbers in these regards overall and at the Dell School of Medicine which has similar racial diversity challenges. I'll also need a comparison chart for Texas's own racial breakdown. My project will be option-driven with a menu that the user can choose from. It's in a while loop now but I don't know if I'll stick with that. I'm probably going to use dictionaries to store the data itself. I'm still trying to get all the data I need but the university has begun to respond to my open records requests. The only roadblock I've run into so far is that matlablib does not load properly.

  This is what I have so far but as I said above I'm having a problem loading matlablib so it doesn't run
  
  https://trinket.io/python/3028acdcff
  
  This is the option code that I'm working on:
  
  ```python
  
  def menu():
  print("[Option 1] Get a gender breakdown of students at the iSchool")
  print("[Option 2] Get the racial breakdown of students at the iSchool")
  print("[Option 0] Exit the program")
  
menu()
option = int(input("Enter your option: "))

while option != 0:
  if option == 1:
    print("Option 1 has been selected")
    # Creating dataset
    
 ```
 
 
  
