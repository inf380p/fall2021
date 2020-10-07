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

Reflection (Audrey): This was a fun exercise to complete and my first time working with a partner. Ayu started out "driving" while I "navigated" and after a couple of short sessions we were able to successfully complete the three prompts.
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
---
Reflection (Ayu):



Co-authored-by: a-larasati
Co-authored-by: intjnotinfp
