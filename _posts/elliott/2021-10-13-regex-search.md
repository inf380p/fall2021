---
author: elliott
category: notes
layout: post
title: "Regex & basic search"
mode: Remote
published: true
---

# Q&A and Vocab

* Group up and let's get these on the board.

Resources:

* [Pythex](https://pythex.org/) is a nice way to build out regular expressions while testing them visually
* [Regex Crossword](https://regexcrossword.com/) can be a fun way to learn regexes by producing text that will match multiple regexes, like crossword puzzles have overlapping words.

# The Wild Wonderful World of Wegexes

Regexes are super powerful. It takes a lot of practice to be able to parse the complicated ones. But it's also OK to start simple:

* `this` is a regex that matches these exact characters: `this`
* `(t)?his` is a regex that matches `his` and, optionally, `this`. The parentheses plus the `?` indicate that the `t` is optional.
* `[th]is` matches `his` OR `tis`. The square brackets indicate either/or.

[Here's this example on Pythex](https://pythex.org/?regex=%5Bth%7Cbr%5Dis&test_string=his%0Athis%0Athat%0Atis%0Awhich%0Awish%0Abris%0A&ignorecase=0&multiline=0&dotall=0&verbose=0)

## Character Classes

_Note: Regex character classes are different from the Classes used to make objects in Python._

The above examples add in some regex **syntax** but use characters. Regex also provides special symbols which indicate a range of characters. `\d` indicates a **d**igit, for instance.

So, the pattern of a typical US phone number would be written

* `\d\d\d-\d\d\d-\d\d\d\d`

This would match string like `555-867-5309`, since there are digits and hyphens that follow the pattern above.

* `\d` indicates **d**igit characters, 0-9
* `\w` indicates **w**ord characters, a-z, A-Z, 0-9, and _
* `\s` indicates **s**pace characters, like ` `, `\t` (tab), and `\n` (newline)

The capitalized versions of each of these match _everything not in the classes_.

## Selecting

Let's say we only wanted the area code of a phone number. We can use parentheses to select just that portion of a match:

* `(\d\d\d)-\d\d\d-\d\d\d\d`

Why not just use `\d\d\d`? well, that would also find other instances of three digits in a row. We want three digits in a row only when they're followed by the rest of a phone number. So we write the pattern of a phone number and select what we want out of it.

# Specific examples from the homework

* TBD

# Getting Set Up Trinket

1. Create a free Trinket account
2. Create your first new trinket (any trinket)

That's it: you can now make and share your own Python programs. We'll embed python trinkets into the class website next week as we go deeper with talking about code.

If there's time, we'll walk through getting a Write Code exercise into Trinket. If we can all get through this, there's no homework for next class!

That said, some of you might want to execute on the strategies for resolving fuzziness you identified in your reflections during this 'week off'. It's a week for catching our breath and catching up where needed.