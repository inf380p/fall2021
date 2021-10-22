---
layout: post
author: acreese
title: "Alex's trinket post"
---

Here's an example about Regex:

<iframe src="https://trinket.io/embed/python/e9788651fb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This code creates a list of extracted email domains from a text file using a Regex pattern `@[A-z0-9.]+` and the `re.findall()` function inside of a for loop.

Because the `re.findall()` function returns a list of matched strings, I had to use a list index to extract each match. Otherwise I would create a list of lists.

```python
    domain = re.findall(pattern, line)
    if len(domain) > 0:
        domains.append(domain[0])
```

This is only sufficient if we are sure that there will be one match per line. If there are mutliple matches, it will only catch the first one. So I would rewrite this using a for loop:


```python
    for i in range(len(domain)):
      domains.append(domain[i])
```

Ths way we don't even need the if statement: `if len(domain) > 0:`

If we wanted to exclude the `@ ` sign from our match objects, we could also add a capturing group to our pattern to only return the domain, like this: `@([A-z0-9.]+)`

