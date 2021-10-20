---
layout: post
author: AU-turtledragon
title: "Aaron's Trinket Post"
---

Here's my example about parsing and manipulating data from a text file. The exercise asked us to define a function that will return the average PM 2.5 value for a particular state based on city pollution data contained in the document uspoll.txt. 

<iframe src="https://trinket.io/embed/python/3c22a3abaa" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

So...
This code defines a function `avg_PM25()`, which will take the argument `(state)`.
```python
def avg_PM25(state):
```
When called and provided with an argument, the function will call upon the file handle `inFile`, opening the file "uspoll.txt" in `r`ead mode. Variable `lines` is then created and assigned a value equivalent to a list of all the lines within the open text file (using the `.readline()` method). Then the file is closed.  See below:
```python
     inFile = open("uspoll.txt","r")
     lines = inFile.readlines()
     inFile.close()
```
Next, the function will create two new variables - `total` and `count`, both assigned an initial value of zero. 
```python
     total = 0
     count = 0
```
Then begins a for loop, which will traverse every element (`line`) in the list `lines`.  With each traversal, the string 'line' will be split into apart into a new list of separate elemements delimited by a colon and assigned as the value to variable `values`.  
```python
     for line in lines:
          values = line.split(":")
```
The value of the oneth element in new list `values[]` is recast as a floating point number (float) and assigned to variable `curr25`.  Likewise, the value of the zeroth element in the new `values[]` is assigned to variable cityState. 
```python
          values = line.split(":")
          curr25 = float(values[2])
          print(curr25)
          cityState = values[0]
```
Then, the `.split()` method is applied to `cityState` to break its string value into separate list elements delimited by a comma — so the city becomes the zeroth element and the state becomes the oneth element — and assigns that list to a new variable `cityStatevalues`.
```python
          cityStatevalues = cityState.split
```
The function now extracts the oneth element (the state) from the list `cityStatevalues[]`, remove any spaces from the beginning and end it via the `.strip` mehod, and assignes the resulting cleaned up string value to a new variable `curr_state`. 
```python
          curr_state = cityStatevalues[1].strip()
```
Now that the function has sufficiently parsed and isolated the data segments of interest within the document, it moves to the next stage of collecting the particular values the user is looking for. First it uses a conditional statement `if curr_state.find(state) >= 0:` to determine whether the line of text in the "uspoll.txt" being parses in this `for` loop iteration contains the state they're interested in. If so, it adds the current `curr25` value to the `total` variable's existing value _and_ increases the `count` variable by one - this will continue to increase for each loop iteration that contains the state in question.  As such, we're creating a running total of `curr25` values for each city within that state, as well as counting how many city samples exist for that state. 
```python
          if curr_state.find(state) >= 0:
              total += curr25
              count += 1
```
This all repeats for each line of text in the "uspoll.txt" document.  Once every iteration is completed, all that's left is to crunch the numbers and return the state's PM 2.5 value; which is accomplished by dividing the cumulative value of variable `total` by variable `count` - after which a final value is returned and function `avg_PM25()` is completed. 
```python
     return total / count
```
The last line serves as a test, requesting the PM 2.5 value for the state of Ohio by feeding a `state` value of 'OH' to the function `avg_PM25(state0` and then printing the returned value. 
```python
print(avg_PM25('OH'))
```


