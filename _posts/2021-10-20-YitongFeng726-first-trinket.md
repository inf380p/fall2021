---
layout:
title:

---

<iframe src="https://trinket.io/embed/python3/e4d4dd346f" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

```
phrase = "Exeggcute evolves into Exeggutor which are two extraordinary Pokemon"
def calc_count(str):
    letter_count={}
    for i in str.lower().replace(' ',''):
        if i not in letter_count:
            letter_count[i]=1
        else:
            letter_count[i]+=1
    return letter_count
letter_count=calc_count(phrase)
e_counter=letter_count['e']
print(e_counter) 


```
this question is interesting.
