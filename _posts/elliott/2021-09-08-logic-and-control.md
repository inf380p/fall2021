---
layout: post
category: notes
title: "Logic and the flow of Control"
author: elliott
published: true
mode: Remote
---

# Part I: Intro

## Announcements

Grading is a work in progress

## Vocab Palette

What things have you encountered, in the readings or elsewhere, that you'd like to make sure I cover in class today?

* Here's a resource on [Python's escape characters](https://www.w3schools.com/python/gloss_python_escape_characters.asp) (thanks, Misha!)

## Welcome Survey Review

Whoever you are, you belong here! And you can probably relate to many of the things your classmates said in the welcome survey:

What excites you about coding or learning to code?
* It can be a great way to creatively express myself
* I view learning to code (and, I suppose, coding itself) as a type of creative problem solving
* I am excited to learn a subject that has always intimidated me
* I love the idea of being able to engage more with technology
* I like the idea of being able to create or edit programs so they work for the specific way I want to do things.
* I think what excites me most about learning to code is just that, when I feel like I'm truly learning.

Do you have any apprehensions about code or learning to code?
* I don't like that coding is literal. If you're off infinitesimally, you're wrong
* I have some experience but no formal training
* One thing that I find really daunting is the amount of jargon and terminology that you need to remember
* I am nervous about learning something so new to me
* I worry that the way I solve problems through code isn't necessarily the most efficient or straightforward.

What are your goals for this class?
* Looking forward to developing a cool extended project to represent my skills
* I hope that I will be able to use this course knowledge in my future profession (multiple responses: academic librarian, UX designer)
* I want to become competent at the processes of learning to program
* My primary goal is to become comfortable with the language of programming.
* I'd like to learn more about how to collaborate with other people/how to "be a programmer" in general.

Students indicated a range of prior experience with Python and programming, from "None" to having completed a project or two. Almost everyone said they wanted to feel more confident in writing their own programs, as opposed to just doing what someone said to do.

## Final Project

The final project will have you complete a program of your own design over the course of a few weeks, integrating everything you've learned by then. Many of you stated that being able to make your own program was one of your goals for the class, which is great!

There's nothing you need to do now, so this is just an FYI. It will be due on our final exam day, **Thursday**, December 9th. A draft of the assignment is up. **Don't panic**


![Don't panic]({{site.baseurl}}/img/dontpanic.jpg)

The final covers lots of concepts and skills and even platforms we haven't touched yet. You'll be familiar with all of these by the time we get there.

The meetup writeup and optional open source extra credit are due the same day as well.


## Pomodoros today

Pomodoros are a productivity technique to ensure that you're taking regular breaks. We're going to use them today!

![pomodoro visual explanation](https://luxafor.com/wp-content/uploads/2020/07/the-Pomodoro-Technique-3-1024x576.png)

If you find pomodoros help you, you can use them yourself, for anything. There are fancy apps and such, but all you need is a clock or timer and some discipline.

## Schedule

Pomodoro 1: Intro (in progress). 5m break

Pomodoro 2: 20m Conditionals exercises in pairs. 5m discussion. 5m break

Pomodoro 3: 20m Conditionals exercises in pairs - switch roles. 5m discussion. 5m break

Long break

Pomodoro 4: 20m Loops exercises in pairs. 5m discussion. 5m break

Pomodoro 5: 20m Loops exercises in pairs - switch roles. 5m discussion 5m break

Wrap up & Next class discussion. **In person** next week.

Finish anything you don't get to on your own tonight.

{% comment %}
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

{% endcomment %}