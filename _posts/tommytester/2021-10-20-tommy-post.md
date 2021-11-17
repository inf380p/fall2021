---
layout: post
author: tommytestertwo
title: "Tommy's Trinket Post"
---


Here is the trinket I selected:
<iframe src="https://trinket.io/embed/python/82c4707fea" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This code uses an accumulator/incrementer pattern to calculate the average:
```
def avg_PM25_count(state):

  # calculate the average
  total = 0
  count = 0
  for line in lines:
    values = line.split(":")
    curr25 = float(values[2])
    cityState = values[0]
    values = cityState.split(",")
    curr_state = values[1]
    if curr_state.find(state) >= 0:
      total += curr25
      count += 1

  return total / count
```

This code stores the values in a list and then calculates the average from that list using `sum()` and `len()`:

```
def avg_PM25_list(state):
  statelist = []
  for line in lines:
    values = line.split(":")
    curr25 = float(values[2])
    cityState = values[0]
    values = cityState.split(",")
    curr_state = values[1]
    if curr_state.find(state) >= 0:
      statelist.append(curr25)
  return sum(statelist) / len(statelist) , statelist
```

This code builds a dictionary containing a list for every state. The interface to the function is a little different: it returns a dictionary rather than an average. By accessing a particular state in that dictionary to get its resulting list, you can calculate the average of any state:

```
def get_PM25_dict():
  statedict = {}
  for line in lines:
    values = line.split(":")
    curr25 = float(values[2])
    cityState = values[0]
    values = cityState.split(",")
    curr_states = values[1].strip()
    split_states = curr_states.split("-")
    for curr_state in split_states:
      if curr_state not in statedict:
        statedict[curr_state] = [curr25]
      else:
        statedict[curr_state].append(curr25)
  return statedict
```

After saving the return value of the function into a variable, say `polldict`, the average of the state of Ohio would be calculated like this:

```
sum(polldict['OH'])/len(polldict['OH']
```

The dictionary could have just stored the average as well. But, by storing the list, it would be possible to add more data to the program later on and recalculate the average, so this is the most flexible approach for a long-lived program.
