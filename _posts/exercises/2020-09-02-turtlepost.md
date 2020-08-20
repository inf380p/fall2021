---
layout: post
author: elliott
categories:
  - exercise
  - how-to
inclass: true
title: Embed Turtle Programs into our Class Blog
---

Use the instructions below to submit a post with your trinket embedded into it.

### Sharing your work

Programmers often need or want to share their work with others.  We're going to do that by making a
jekyll post with our code, a screenshot of our picture, and any thoughts or reflections we have on
the experience.

First you need a header:

<pre>
---
layout: post
author: tommytester
title: "Tommy's Turtle Exercise"
---
</pre>

Then, go to your Trinket programs and [follow the instructions here](https://docs.trinket.io/getting-started#/2-sharing-trinkets/embed-a-trinket)
to get the embed code.

Then, paste the code into the text of your post.  At this point your post will look something like this:


```
---
layout: post
author: tommytester
title: Tommy's Turtle Exercise
---

Here's the program I'm embedding:

    <iframe src="https://trinket.io/embed/python/c26c35e489" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```

## Static code blocks

If you want to display code that's not interactive (to talk about something you did, for instance)
, the cool grey boxes above come from telling Jekyll that we're about to write code using backticks: `

<pre>
```
# Look what I did here:
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.forward(50)
tess.left(120)
tess.forward(50)
```
</pre>

Here's that code rendered by Jekyll:

```
# Look what I did here:
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.forward(50)
tess.left(120)
tess.forward(50)
```


## Images

Finally, if you need to embed an image, do it thusly:

<pre>
![Turtle image](http://openbookproject.net/thinkcs/python/english3e/_images/tess03.png)
</pre>

That code looks like this:

![Turtle image](http://openbookproject.net/thinkcs/python/english3e/_images/tess03.png)


### Thoughts about the exercise

When submitting exercises, always include reflections, roadblocks you ran into, or
things you thought were cool. Always include links to example code if you use or are heavily influnced
by someone else's work. They should be at least a paragraph or two. Regardless of length, the best ones give me a sense of what you did
and why.  Here's [a post from a previous class](https://silshack.github.io/summer2017/zman7895-logic-turtle-exercise.html) that does a good job of this.

### Going deeper

Think the above is easy?  Try your hand at writing and calling **functions**. We'll get to these
later but an example from our very own Grant McLendon might help inspire you:
[Grant's Turtle post form Fall 2013](http://silshack.github.io/fall2013/gmclendon/2013/09/09/grants-turtle.html)
