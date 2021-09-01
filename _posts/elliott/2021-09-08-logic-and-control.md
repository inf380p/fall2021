---
layout: post
category: notes
title: "Logic and the flow of Control"
author: elliott
published: true
mode: Remote
---

Forthcoming.

{% comment %}


# Welcome Form review


# Survey responses & code reflections

{% comment %}
Highlights from the welcome survey:
* "I tried to learn python from my brother and then through CodeAcademy. I followed along but lost interest and forgot what I learned quickly."
* Goal: "A decent understanding of python and python's application in the real world and where to go next to learn more."
* "I tend to be a perfectionist, so learning that getting things wrong as part of the learning process makes me a bit anxious, but I really hope to become more comfortable with that as the semester goes on. "
* "From the little experience that I have, I have navigated coding simply by doing and not really understanding what I am coding."
* "...quite a lil bit of imposter syndrome..."
* "I like the feeling of success when I've been working on something for a long time and finally get it to work. That's such an exciting feeling :) "
* "I would really really like some projects for my portfolio/resume"
* "I’m fairly worried that I won’t be able to keep up since I’m starting from scratch and this is not my academic strong suit."
* "I struggle with learning on my own, so I hope that the structure and community in this course will help alleviate those difficulties."
* "My understanding is that you can get hung up on parts of code and I hope I don’t spend the majority of my time backtracking and trying to figure out where I went wrong."
* "I am excited about learning a tangible new skill."
* "I hope to gain technical base where I build from and become more proficient in years to come."
* " Using open source lectures to learn code does not work for me because I do not have the instructor to go to to ask questions or help how he/she will solve a coding error."

Highlights from the first exercise reflections:

* "I was absolutely overwhelmed in class (and only coded a bunch of lame pre-figured shapes/colors), but once I relaxed and took the time to work through a slightly more complicated project later on, I learned a lot more and was happier with the result. The moral of this story is that I probably won’t get stuff right off the bat and will probably have to mess around with things alone/ in silence later on for it to click. It's going to take a while. That’s ok with me!"
* "I had a lot of trouble with the move forward and backward and using the x and y coordinates was much easier on my brain."
* "It seems simple but turns out to be difficult."
* "Although my piece is fairly simple, I'm happy with how it turned out and I feel confident I could make other shapes and pictures much more easily now."
{% endcomment %}


# Final Project Discussion

It's posted. We'll talk more about it later, but take a look to see where we're headed.  Short version: you'll use everything we're learning to write an awesome program!

# In Class: Make Sure You Can Access Protected Panopto Content

This brief in-class assignment is also in our [how tos]({{ site.baseurl }}/how-to.html) if you ever run into a situation where these videos aren't displaying for you.

We're doing it this week because next week is remote!



[Zoom Room for Remote Classes]({{site.zoom_url}}). Also in the menu bar above.

# Today's Class Schedule

Times are approximate.

Part I - Conditionals and Homework
* 15 minutes: Zoom: Intro
* 15 minutes: Conditionals
* 15 minutes: Zoom: Discussion & Homework. Introduce Part II
* 10 minutes: Break

Part II
* 15 minutes: Work on your own. Check-in for breakout discussions
* 15 minutes: Zoom: Breakout discussions
* 10 minutes: Work on your own
* 10 minutes: Break
* After Break: Zoom: Code talks & screenshares. Introduce Part III

Part III
* 15 minutes: Zoom then on your own: Make a pull request
* 10 minutes: Zoom: Pair up to review and merge that pull request
* 10 minutes: Zoom: Wrap up and on your own Github cleanup if needed

# Announcements and Q&A

* Check out the People page! You'll soon be able to update these bios, and they'll appear on your posts automatically.
* There was an incorrect due date on the trinket assignments. Don't worry about it!
* Community engagement - Get started now! Here are [some webinars](https://guides.lib.utexas.edu/data-and-donuts) from the UT libraries.
* Open Source contributions: Extra Credit
* blocks in python
* Vocab?
* How's it going so far?

# Review Last Time

*Turtle & Python*
* We went through and discussed Turtle Basics and saw that everyone came up with very different programs, using simple building blocks
* We reviewed Chapter 2 Exercises
* We used Zoom screenshares to see and discuss code
* We discussed the importance of reflections embedded into various assignments. Reflections are for me, your peers, and *YOU* to have a window into where you are in terms of understanding.


*Problem Solving Resources*
* We talked about problem solving *attitudes* of self-awareness, calm, and determination.
* We talked about problem solving *strategies* of Stopping, Going in the Right Direction, Working Smart, and Using Resources.
* We talked about problem solving *tactics* in Python, including commenting code, `print`ing variables, and using the `type()` function to figure out what kind of data something is.

*Github*
* We talked about how to edit a pull request
* We discussed Github reviews
* We made sure everyone could access Panopto Protectedcontent for this class
* We made a new post for the Custom Turtles exercise, and then edited it to put a Trinket in it.

# Discussion: Logic and the Flow of Control

Boolean values are very simple but very powerful.  There are tons of useful ways to
construct **expressions** that evaluate to `True` or `False` in Python, and we use these
to change the behavior of our program.

Basic `if` statements act as 'gates' to control whether blocks of code get executed.
`elif` and `else` statements enhance this control.

Some specific concepts to understand:

* *Truithiness*: Everything can be evaluated to either true or false. Most things are true.
* *`try` and `except`*: expecting exceptions (also known as 'errors') in your code. This is *super helpful* for user input. Compare:

<iframe src="https://trinket.io/embed/python3/5cc539fe20" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

...with:

<iframe src="https://trinket.io/embed/python3/8333113d87" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

* *Flow of Control*: Python does things in a specific order. Sometimes it'll not execute some code, and any *runtime errors* in that code won't appear until or unless it does. Let's revisit [the section on short-circuiting](https://books.trinket.io/pfe/03-conditional.html#short-circuit-evaluation-of-logical-expressions).

# Homework Review

On [Zoom](https://utexas.zoom.us/j/93951295777) together, using screenshares of your Trinket exercises.


# Part II: In Class Python Exercise

Logical Turtles!

* 15 minutes: Work on your own. Check-in for breakout discussions
* 15 minutes: Zoom: Breakout discussions
* 10 minutes: Work on your own
* 10 minutes: Break
* After Break: Zoom: Code talks & screenshares. Introduce Part III

# Logical Turtles code talks

* Story of your approach
* Your triumphs
* Your despairs
* Problem Solving attitudes and strategies




# Part III: Merging on Github from Now On

Re-join [Zoom](https://utexas.zoom.us/j/93951295777)

* 15 minutes: Zoom then on your own: Make a pull request
* 10 minutes: Zoom: Pair up to review and merge that pull request
* 10 minutes: Zoom: Wrap up and on your own Github cleanup if needed

Moving forward, you'll review and merge each others' work *in class*.

Review, fix, and merge pull requests. We'll have some catch-up time where
we can review any outstanding issues.

# Merging!

With great power comes great responsibility

* Never merge your own pull request (our settings make that impossible, but it's a general rule)
* Never commit directly to the `production` branch
* Never merge broken or failing code
* Always be explicit with your reviews:

![screenshot 2018-05-22 at 5 24 53 pm](https://user-images.githubusercontent.com/1702745/40391297-c084aa2e-5de5-11e8-9eee-54c79744b2b8.png)


# Review & Merge Posts

Volunteer: Merging with Tommy Tester.

* Reviewing PRs - comment on them directly
* Create a formal Review to **Approve** or **Request Changes**.  Leave comments on a specific line if needed.  Request changes on an open PR.  Open an issue if the code has already been merged - that way, issues are with the current site, and problems with new code say in the PR.
* Merging - Your responsibility to make sure your partner's post works! Check that it shows up on our site afterwards.  Code > Commits will let you see whether the site has been rebuilt (takes ~1 minute)
* Assigning issues - already merged work with problems

~10 minutes reviewing & merging posts with a partner.


# Github cleanup

Taking turns with a partner, find *all* your pull requests (open and closed), and review what's happened to them. For the ones that are merged,

# Functions & Refactoring for Next time

Read up on functions and then use the power of custom functions to make your previous code more concise and more awesome!

{% endcomment %}