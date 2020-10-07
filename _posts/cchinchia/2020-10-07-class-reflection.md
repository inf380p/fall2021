---
layout: post
author: cchinchia
title: "Claire's Reflection on the class so far"
---

I really like learning how to do pair programming. I've never had an official programming class, so I experienced many struggles while I tried to learn to code by myself. Pair programming make the frustrating debugging process more adorable, and I learned a lot from my peers.

Through the exercises every week, I'm more familiar with different types of variables, and their features. For example, in the Lists Exercise, I learned to use "deepcopy" method to duplicate another list to store and make changes, instead of directly affecting the original list.

```python
def chop(input):
  if len(input) <= 2:
    return None
  # remove first
  another_list = copy.deepcopy(input)
  another_list.pop(0)
  # remove last
  last_index = len(another_list) - 1
  another_list.pop(last_index)
  return another_list
```

Besides, using for loop to draw graphics is something new for me. But when I wanted to create for loop on my own, I feel it's really hard, and not sure how to make it work. I think I'll search for more examples to get inspirations and learn how they did it.

```python
for i in range(size):
  tommy.speed(8)
  tommy.circle(5*i) 
  tommy.circle(-5*i) 
  tommy.left(i)
```

Overall, I enjoy the programming experience so far. Google Search is my best coding friend. I also really appreciate the discussion with my friend.
