---
author: elliott
layout: post
title: "Why Python?"
categories: reading
canvas: false
---

# Why Python?
This may be your first experience with programming, so I want to give you a sense of why we're using Python, some of its advantages, and when you might want to use another language.

tl;dr: It's a very readable language, is powerful enough for almost anything you want to do with it, and lots of people use it.

Further reading:

* [Why I Push for Python](http://lorenabarba.com/blog/why-i-push-for-python/) by George Washington University prof. Lorena Barba
* [Why Python is a great language for teaching beginners in introductory programming classes](http://pgbovine.net/python-teaching.htm) by Rutgers prof. Philip Guo
* [Why Python is a Great First Language](http://blog.trinket.io/why-python/) by yours truly

## Dynamic vs Static (Types)
In statically typed languages such as Java, you have to declare the data type of
every variable (such as numbers vs text).  This makes compilers happy and can prevent bugs, but tends to
involve a lot of boilerplate.  When you're frustrated with Python, remember, the
language is managing all the data types for you, so cut it a break.

Compare the Java and Python versions of a simple program that prints "Hello, World!":

**Java**

```java
public class HelloWorld {

    public static void main(String[] args) {
        System.out.println("Hello, World");
    }

}
```

**Python**

```python
print("Hello, World!")
```

Phew, that was easy!


Further reading:

* [Introduction to Static and Dynamic Typing](http://www.sitepoint.com/typing-versus-dynamic-typing/)
* [List of Dynamically Typed Languages](https://en.wikipedia.org/wiki/Category:Dynamically_typed_programming_languages)
* [List of Statically Typed Languages](https://en.wikipedia.org/wiki/Category:Statically_typed_programming_languages)

## Interpreted vs Compiled
Every programming language is an interface for controlling your computer.  It uses the RAM, CPU, and Hard Drive to perform calculations.
How is it that the magical code you type can do this? Well, it's either a compiler or an interpreter.

**A compiler takes computer code and processes it into binary instructions for a CPU.**  Very literally, ones and zeros.
Compiled programs are very fast, but they only work for a limited set of computer architectures (see Note below), since different
CPUs speak different dialects of binary.  One of the most frustrating parts of working with a compiled languages is
getting a program to compile without errors.  It can be hard to find bugs because you can't run the program to see
what it does until you've run it.  These kind of programs have major benefits, though, in that they're very fast and
very unlikely to crash.  There are even some languages that are guaranteed not to crash once they've compiled.  This
is great for ubernerds and many of you may go on to code with compiled languages. But, luckily, we get to start with Python instead.

Compiled languages you may have heard of include C, C++, Java, FORTRAN, and Haskell.

**An interpreter is a program that knows how to read a certain type of code and can translate that code into instructions for
a certain CPU type on the fly.**  It has a general set of instructions and uses those to convert computer code into instructions
for the CPU.  So an interpreter only needs to be made once for a given CPU type- then the CPU can run all the programs in
that interpreted language.  Python falls in this category.  Your Python code will run on any system that has an Python
interpreter installed on it.

Interpreted Langauges you may have heard of include Python, Ruby, Javascript, R, and Perl.

Python programs will run even if they have bugs in them.  They'll run up until the point where the bug causes them
to crash.  This is a very useful feature, since it gives you important clues as to when and why the bug is happening.
When you get frustrated with Python, remember that at least you don't have to make your program compile before finding
out what the bug is!

**Note:** There is great variability in the ways that languages are designed and executed. For instance,
Java is a compiled language that uses a Virtual Machine to try to get around this limitation.  A virtual machine (VM)
is kind of like an interpreter, in that it takes instructions and translates them for the CPU, and you need one for each CPU
type. You still have to compile Java programs, though once you do they (should) run on any Java VM.
This is one of the reasons it became more popular than C as a teaching language.  But Python is now overtaking Java because
intepreters are so much more convenient for programmers than compilers are.

Further Reading:

* Chapter 1 of our textbook has more on this subject.
* [Discussion about this on Quora](https://www.quora.com/What-is-the-difference-between-compiled-and-interpreted-programming-languages)
wherein the top commenter says that since every language *can* be interpreted or compiled (which is true), it makes no sense to speak of them in
such terms.  Which means that what I wrote above is a bunch of hogwash. See if you agree.  You'll find lots of very precise answers like
this on the Internet.  In this course I'll often give you less precise (but more useful) answers.
I hereby grant you permission (not that you need it) to come up with your own conclusions!
* [List of Interpreted Languages](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type#Interpreted_languages)
* [List of compiled Languages](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type#Compiled_languages)

## Whitespace-based syntax
Python uses whitespace (spaces, tabs, newlines, and other things that aren't typically displayed to the user)
to delineate the start and stop of its major pieces.  Many other languages use a verbose syntax,
which involves a lot of special characters.

The more explicit syntax is great for compilers and interpreters- it helps unambiguously tell them
what to do.  But it's not so great for humans, since special characters have been shown to
impede the comprehension of code's meaning, especially for beginners.

Whitespace-based syntax tends to be very readable, since humans are good at seeing things spatially.
For instance, in this Python program, it's easy to grok, without knowing anything else, that
lines 2 through 4 are 'inside' line 1, and that line 3 is 'inside' line 2.

{% highlight python linenos=table %}
def a_function():
    for i in range(10):
        print("something")
    print("something else")
{% endhighlight %}

Python used to be even easier to read: the `print()` function used to not require parentheses. But
as of Python 3, it does, which makes the language more syntactically correct but harder for beginners.
This is a rare misstep from the people who write the language.  Trinket continues to support both
forms of print, but we'll be using the Python 3 version. Apologies for the loss in readability.

Further reading:

* [An argument against Python](http://colintmiller.com/python/) mentioning whitespace, amongst
other grievances.
* [Python Whitespace Discussion](http://c2.com/cgi/wiki?PythonWhiteSpaceDiscussion), a collection of
snippets Pro and Con python's whitespce design.  It's a little disjointed but will give you a sense
of some of the conversation surrounding Python as it rose to popularity.  With the dominance of
Python and Ruby (another language that uses whitespace as syntax) in Web programming, much of this
discussion has faded into obscurity.
* (for giggles) There is actually a programming language where **all** components of its syntax
are whitespace.  [More here](https://en.wikipedia.org/wiki/Whitespace_(programming_language)).
While it's neat to see just how many kinds of programming languages there can be, I recommend
against actually trying to use one that's entirely invisible.