---
author:
- intjnotinfp
- a-larasati
layout: post
title: "Ayu and Audrey's Pair Programming Reflection"
---

Exercise 4: split, sort and print
<iframe src="https://trinket.io/embed/python/56af39fdd2" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercise 5: parse, count and print
<iframe src="https://trinket.io/embed/python/96bd83d641" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercise 6: min, max, median
<iframe src="https://trinket.io/embed/python/f2528c4e15" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

#### Reflection (Audrey) 

This was a fun exercise to complete and my first time working with a partner. Ayu started out "driving" while I "navigated" and after a couple of short sessions we were able to successfully complete the three prompts.

Because Trinket kept crashing on us, we had to problem solve and use a different tactic such as working on our own respective Py text editors and sharing code that way.

Misha helped us figure out why Trinket kept crashing on us - we think it had to do with this code telling Python to parse all the lines in the mbox file, including potentially empty ones:

```python
words = line.split()
  if len(words) > 0: #safety line
    if len(words) > 2 and words[0] == 'From':
      print(words[1])
```
     
As you can see, we added a safety line in case any of the lines we were parsing had "0" words. Again, we assumed that was what was causing the problem, and once we added that we stopped crashing.

Later on, I tried driving and I was glad that we both tried both roles. It's a little bit more challenging to navigate in my opinion, although both of us contributed ideas while driving too. We just made sure as drivers to communicate and ask questions before "driving off". 

One thing that was really great about working with Ayu was how we could play off each other's suggestions to problem solve and find resources. Neither of us knew how to sort alphabetically, so we looked that up. We learned that capitalized items sort first and then lowercase items sort, so a capial-Z word would come before a lowercase-A word. Good to know!

#### Reflection (Ayu)

This was a really great first-hand experience in paired programming, and I learned a lot, especially the whole driver/navigator dynamics of the exercise. It might've not been the most "ideal" way to pair program because I heard it's typically done in-person while sitting side by side, but this virtual run isn't so bad. 

Like Audrey said, I agree that navigating was the more challenging of the two even though technically both drivers and navigators should be critically thinking of the problem and the approach to find the solution. I navigated for exercise 6, and we ran into trouble with getting the code to return a median. I knew off the top of my head that some math is involved in it, but I couldn't remember what the formula for finding a median was. After some Googling, at first we had tried to import the `statistics` module but we realized we actually needed a file with the module contents. Because we didn't know where to locate it, we looked at the documentation of the module to see what's actually included in hopes of finding the lines of code on how the `statistics` module runs the `median` function. And we did! We took that piece and defined it as a function in our exercise.

```python
def median(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        print("no median for empty data")
    if n%2 == 1:
        return data[n//2]
    else:
        i = n//2
        return (data[i - 1] + data[i])/2
```

Overall it was a really nice experience despite some technical difficulties we encountered along the way. I look forward to more opportunities to pair-program with her!


Co-authored-by: a-larasati
Co-authored-by: intjnotinfp
