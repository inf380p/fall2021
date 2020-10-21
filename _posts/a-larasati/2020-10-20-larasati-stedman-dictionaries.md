---
layout: post
author:
- a-larasati
- brianna-stedman
title: "Paired Dictionary Exercises"
---
#### Trinket Code

<iframe src="https://trinket.io/embed/python3/436ddb2759" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

#### Ayu's Reflection
This exercise took quite a bit of time to do, and finding a time that we could both work on it together was also quite difficult, so we ended up trying to work on it individually and then getting together to talk about it. Some parts of the chapter helped, some parts I had to actually Google to figure it out. This exercise had multiple moving parts, and the comments from the original code helped chunk it out, but my brain still seizes up when I finished a chunk of the problem and starting the next. 

The first chunk was building a list of lists data structure and appending new items, which was similar to an exercise we've done before. This portion of the code didn't really get reused in the later parts of the exercise though (at least in the code I wrote).

The next chunk is broken into two parts: identifying the states a transaction happened and the number of times a transaction happened and printing out a table with the information as its content.

```python
# Build a dictionary containing each state and the number of transactions that happened in it
transactions_by_state = {}
for line in sales_lines[1:]:
  state = line.split(",")[state_index]
  if not state in transactions_by_state:
    transactions_by_state[state] = 1
  else:
    transactions_by_state[state] = transactions_by_state[state] + 1

# Print an alphabetized table of each state and its # of transactions, separated by tabs
for state in sorted(transactions_by_state.keys()):
  print(state + '\t' + str(transactions_by_state[state]))
```

At it's core, we wanted to count the number of times a state name appears because each appearance of a state indicates a transaction in that state. If a `state` hasn't been added to the dictionary, the code adds the `state` to the dictionary and gives it a count of 1 as the number of transactions that has happened. Once a `state` has been added to the dictionary, the next instances that the specific `state` appears, the code adds 1 to the count.

I had to look up how to print a table separated by tabs, and that was just adding `'\t'` into the print statement.

The last big chunk was a little similar to the previous one, except now it also wants to calculate the sum of the transactions that happened in each state.

```python
# Build a dictionary containing a dictionary for each state containing 
# number of transactions and total transaction value (the sum of Prices
# of all transactions that happened in that state)
transactions_by_state2 = {}
for line in sales_lines[1:]:
  items = line.split(",")
  state = items[state_index]
  amount = items[amount_index]
  if state in transactions_by_state2:
    transactions_by_state2[state] = { 'count': transactions_by_state2[state]['count'] + 1,
                                      'total': transactions_by_state2[state]['total'] + int(amount)}
  else:
    transactions_by_state2[state] = { 'count': 1,
                                      'total': int(amount)}

# Print an alphabetized table of each state, the number of transactions in the 
# state, and the total value of all transactions in the state, separated by tabs
for state in sorted(transactions_by_state2.keys()):
  print(state + '\t' + str(transactions_by_state2[state]['count']) + '\t' + str(transactions_by_state2[state]['total']))
```

I had to look up how to write a dictionary within a dictionary, or at least what the code looks like. The approach is a little similar in terms of how to count each instance, but now I also made sure to take into account the amount of each transaction by setting up a dictionary with it. 

I think remembering the differences between a `string` and a `variable` as related to dictionaries and when to call each one when using a dictionary was something I struggled with. I can't say for sure if I figured out a surefire way to remember which one to call because I kind of brute-forced my way through parts of the code.

#### Brianna's Reflection
