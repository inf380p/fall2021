---
layout: post
author: areiter18
title: Project Update and Standup Report (12/1/2021)
---

Since my update on November 22, I have not done a lot with my project because of travel, other course obligations, and my job. I plan to return and finish my project this coming weekend, tweaking and adding components where applicable. 

I am pleased with my project so far. I feel that the goals I set for myself have been exceeded, mainly because I have had not had trouble recently since I went to office hours and received input. I felt that asking questions really helped me develop realistic goals for this assignment.

Over the weekend, I did tweak and edit my code a little bit, discovering a problem here: 

```
  elif option == "3":
    selection = option3
    print(countrydict.get(5))
    print("So what does this mean?")
    print("This data includes several pieces of information:")
    print("1.) Country")
    print("2.) Revenues")
    print("3.) Expenditures")
    print("4.) Surplus (if a positive number) or Deficit(if a negative number)")
    print("and 5.) Surplus as a Percentage of GDP.")
    print("***************************")
    print("All amounts of money are in thousands of United States Dollars(USD). ")
    print("***************************")
    print("If you see a negative number for the 3rd value it means that particular country has a budget deficit. A positive number means they have a budget surplus.")
 ```

<p>Essentially, I forgot to include the phrase ```break``` at the end, causing the code to continually loop and ask the same thing repeatedly if you selected a particular input. This was an important reminder to remove yourself from the project (I had not noticed this before) and then return to closely edit line-by-line. </p>

<p>This weekend, I am going to work on custom modules and incorporating them into the project. I have already incorporated the following into my project:</p>

<li> csv file </li>
<li> dictionary </li>
<li> definite loops </li>
<li> custom functions </li>
<li> Python 3 Trinket </li>
<li> <b> Need:</b> Custom Modules </li>

<b> Stretch goal:</b>  I’d also like to create a section with user input to look at the max, min, mean, and median values for a particular column of data in my csv file. That will require some research so I plan to see if this if feasible this coming weekend when I have time to work on this.
  
<b>Timeline </b>:
<p> <i>By December 6 </i>: add custom modules </p>
<p> <i>By December 7 </i>: see if my stretch goal is feasible </p>
<p> <i>By December 7 </i>: Have the reflection written </p>
<p> <i>By December 8 </i>: Edit code/reflection and get ready to publish to a pull request </p>
<p> <i>By December 9</i>: Turn in </p>
  
<p>Overall, I am feeling good about this project. My knowledge has vastly expanded and while my project isn’t perfect, I think I have definitely learned a lot this semester.</p>
 
<b> Here is my project as of 11/30: </b>
<iframe src="https://trinket.io/embed/python3/ffbc2ef790" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
  
  
