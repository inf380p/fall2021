---
layout: post
author:
- luznette
- jasfromnz
title: "Jasmine and Janette's Dictionary Exercise"
---
For this excercise, the first half was a lot easier than the second. We were able to use the chapters from our assignments, but eventually had to search up videos and search issues on stackoverflow. To solve the bad price data in sales.csv we did the following:
```python
for i in sales_table[1:]:
  if not i[6] in state_dict:
    state_dict[i[6]] = dict()
    state_dict[i[6]]["Num"] = 1
    state_dict[i[6]]["Value"] = i[2]
    state_dict[i[6]]["Value"] = state_dict[i[6]]["Value"].replace(',', '')
    state_dict[i[6]]["Value"] = state_dict[i[6]]["Value"].replace('"', '')
    state_dict[i[6]]["Value"] = int(state_dict[i[6]]["Value"])
  else:
    state_dict[i[6]]["Num"] = state_dict[i[6]]["Num"] + 1
    state_dict[i[6]]["Value"] = state_dict[i[6]]["Value"] + int(i[2])
```

We started to have issues when we got to the final step which requires us to "Modify your program to let the user choose between sales.csv and homes.csv." We could not figure out how to use the code we had written for the sales.csv to homes.csv since the latter had different columns and did not translate over well. We were hoping to have this cleared up during class. 

Our dictionary exercise:
<iframe src="https://trinket.io/embed/python/0fd355c641" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
