---
author:
- intjnotinfp
- KJEZ35
title: "Kevin and Audrey's Dictionary Exercises Pair Programming Post"
---

Take a look at our Trinket code:
<iframe src="https://trinket.io/embed/python3/2058485220" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

First, to create the list of data structures, Kevin discovered the handy dictreader string method which maps the dictionary information onto output rows. That was used to jumpstart getting the lines into separate lists.

Later, code for an if/else conditional with yes/ no input was added at the top to account for making a choice between using the sales.csv or homes.csv files. The different naming styles between files were also addressed by defining price_key and state_key “Price”/“price” and “State”/“state” respectively, so that one variable for each would get the job done. I thought that was really clever, and it was my favorite part of the code. Here’s what that looks like:

```
if user_input == "yes":
  csv_file = "homes.csv"
  price_key = "price"
  state_key = "state"
else:
  csv_file = "sales.csv"
  price_key = "Price"
  state_key = "State"
```

We found this instance of pair programming to be a bit difficult, particularly we both got completely stuck on our first try. We had to take a break, dive deeper into it individually, and make plans to regroup. I drove to start, then Kevin drove until it was finished. We both had to put the brakes on to slow down and consult outside resources, demonstrating one of the limitations of pair programming – it’s logistically difficult to coordinate using the “take a break method” when two people have to turn to it multiple times! Overall, this was a helpful exercise though, and it’s cool to see different highly practical Python applications. 
