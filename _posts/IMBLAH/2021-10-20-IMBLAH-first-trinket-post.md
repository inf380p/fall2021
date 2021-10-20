---
layout: post
author: IMBLAH
title: "IMBLAH's first trinket post!"
---

Here's a an example about parsing using `cityState.split(",")` and `values[2]`.

<iframe src="https://trinket.io/embed/python/fd5f1e89b0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

```
def avg_PM25(state):

    # get the lines from the file
    inFile = open("uspoll.txt","r")
    lines = inFile.readlines()
    inFile.close()

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

print(avg_PM25('OH'))
```

In this case, when using split method, it returns a list.
