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


# Final Project Discussion

It's posted. We'll talk more about it later, but take a look to see where we're headed.  Short version: you'll use everything we're learning to write an awesome program!


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