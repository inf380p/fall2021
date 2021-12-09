---
layout: post
author: spinachleaf
title: "spinachleaf final project reflection"
---

For my final project, I chose to do a turtle game. I was really drawn to turtle when we first started learning about it. To me, it’s a lot more intuitive than some of the other things we had been learning about in class at that time. When I learned that turtle was used to teach children about coding, that made total sense to me. As a former elementary school teacher with a little bit of experience with Girls Who Code (unfortunately canceled due to the pandemic), turtle reminded me of some of the things I saw in that program.

Looking back on my first version of this project, I can see how far I’ve come. It has been really easy for me to get discouraged throughout this process, but looking at my first version of my first interface draft has left me especially humbled. Some of the code survived:

```python
def advance():
    progress_bar.speed(3)
    progress_bar.forward(25)
```

I find it funny that out of all the progress I’ve made since then, I haven’t really changed the basic mechanics of the progress bar moving forward. Looking back, perhaps I could have figured out a way to move the bar differently depending on on the length of the word, but that is something that did not occur to me until now, as I am writing out my process.
  
My game is fairly simple: the user chooses a difficulty level, then types a word and moves a progress bar across the screen to reach the end. At that point, he can choose to play again, at either the same or a different difficulty. It sounds so easy to me.
  
Unfortunately, that was not the case. I spent more time on this project than anything else I have ever worked on, in this graduate degree or my first one. I racked my brain for solutions that just would not come. I felt so proud of myself when I figured out how to choose a difficulty, only to be told that it did not fit into the parameters of the assignment and I would have to change it. I did, but it took up a lot of time that I was hoping to get some guidance on my main issue with the project, one I never ultimately solved completely.
 
To say I was frustrated throughout this process would be an understatement. I spent countless hours poring over my textbook, reading every line of code out loud to find where an error occurred, and rewriting code blocks until they were unrecognizable from their original states. No amount of walking away and coming back later helped me to achieve the final goal of my project. I really wish I could have figured out how to reset the `.onkey()` function so that the screen would listen for the new word to be typed. Right now, it stops listening as soon as you finish the first word and does not reset when you hit ‘return’ to get a new word.

This is as far as I was able to get:

```python
#advance when user types a letter
def update_next_letter():
  letters = WordTurtle.word()
  incorrect = True
  correctcount = progress_bar.correctcount
  for letter in letters:
    incorrect = True
    screen.onkey(progress_bar.advance, letter)
    while incorrect:
      if (progress_bar.correctcount > correctcount):
        screen.onkey(None, letter)
        incorrect = False
        correctcount = correctcount + 1
      else:
        pass
```

When I finally figured out I could assign `WordTurtle.word()` to `letters` and have my program know what the letters were in those words, things got a lot easier. This was the most challenging part of my project and just being able to get this much accomplished from where I was last week was monumental for me. I decided to celebrate this small milestone as a win for myself, so I didn’t get too discouraged to continue.

Looking back on my reflection from last week, I see that I was even more frustrated than now. I wish I could have figured out the above code for `update_next_letter` a little sooner. I really think I could figure out how to reset for a new word if I had a few more days. The method of just walking away for a while and coming back with a fresh mind has really helped me to not get entirely overwhelmed throughout this class. I understand that deadlines exist, but it would have been nice to complete this project.

To talk more specifically about sections of my project and my process, I’ll try to walk through significant portions of my code from the final version, but give context from when I first conceptualized the section and how it changed from its original form.

Up first, I’d like to talk about when I figured out how to reset the progress bar to the beginning of the screen, or my basic user interface: 

```python
#reset level
def level_reset(progress_bar):
  if progress_bar.distance(winpoint) <= 1:
    return True
  else:
    return False
if level_reset(progress_bar):
  progress_bar.reset()

``` 

I played around for so long with `xpos()`, trying to get my program to work with it. Eventually, I accepted that I could not figure out how to make it work with my current skill level and opted to use `.distance` instead, after taking a nice retreating break and thinking about something else for a while. I think it still works for the purposes of this game, but I would like to have learned why the other method did not work. This is a common theme for me in this project and class in general. I want to know why something does or does not work, and I don’t always get the answer I was hoping for with my current technical understanding.

The next portion I’d like to talk about is the `WordTurtle`, which contributed heavily to my overall game logic:

```python
class WordTurtle(turtle.Turtle):
  def __init__(self, coordinates = [-30, 30], screen = screen):
    turtle.Turtle.__init__(self)
    self.hideturtle()
    self.penup()
    self.color(random.choice(colors))
    self.goto((random.randint(-30,30)),(random.randint(-30,30)))
    self.wordchoice = random.choice(words)
    self.write(self.wordchoice, align="left", font=("Arial", 20, "normal"))
  #choose new word
  def new_word():
    word_turtle.reset()
    word_turtle.hideturtle()
    word_turtle.penup()
    word_turtle.speed(0)
    word_turtle.color(random.choice(colors))
    word_turtle.goto((random.randint(-30,30)),(random.randint(-30,30)))
    word_turtle.wordchoice = random.choice(words)
    word_turtle.write(word_turtle.wordchoice, align="left", font=("Arial", 20, "normal"))
  screen.onkey(new_word, "return")
```

Why do I have `word_turtle.` instead of `self.` for my `new_word()` function? Because I could never get `.onkey` to work with `.self`. I played with this for hours. This was the only way I could get my program to run without errors. Does this have something to do with the reason I can’t get my program to reset for a new word when I press enter? Maybe it does. I’ve been thinking about this issue for so long that I can’t seem to come up with any better ideas. Unfortunately, the method of walking away and coming back fresh did not yield any answers for me this time around.

The next part of this project I would like to talk about is my level selection, another game logic component. The same logic I’m going to talk about applies to the help message. Here is the code for when the user selects level one:

```python
#user chooses a level
def select_one(x,y):
  game_state["level"] = 1
  hide_buttons()
one = turtle.Turtle()
one.hideturtle()
one.speed(0)
one.penup()
one.left(90)
one.setx(-180)
one.sety(140)
one.shape(image3)
one.showturtle()
one.onclick(select_one)
```
And here is my game state dictionary for reference:

```python
#major states of game tracked in a dictionary
game_state = {
  "level" : 1,
  "current_char" : 0
}
```

The level selection became so easy when I realized that you could use `.onclick` like this, in conjunction with the dictionary. I struggled for a long time to figure out how to even use a dictionary in a turtle game. Using it to keep track of game states was a suggestion from Professor Hauser, and it worked out perfectly.

The final part of this project I would like to talk about is the process as a whole. I may not have code blocks to talk about this, but I just want to walk through my thought process throughout it and what I have learned. Firstly, I learned that I am capable of more than I thought I was a month ago. My limitations are large, considering that I was exposed to python for the first time 4 months ago.

I’ve also learned that I take things too literally sometimes. When reading the textbook or the turtle python guide Professor Hauser showed us during class, I would try to apply sections of code that did what I wanted. However, I think there was often a piece missing from my code, or I was trying to do something that did not quite work with the parameters I gave. An example of this is when I tried to get the `.onkey` function to work with `.self`, and I got error messages about positional arguments. I’m sure there’s a way to make this work, but I do not currently have that knowledge.

Overall, this project was a learning experience. I’ve come really far from where I started on it nearly a month ago. If I could do it again, I would spend more time trying to figure out how to get the words to reset. I could have also benefited from partner work. The most beneficial learning I had in this class was from the beginning of the semester when I would go through the textbook chapters and compare answers to questions with other students. I am not the best independent learner. It always helps me to have time to work with others. The weekly updates we had were nice, but it was never enough time to really look closely at another’s project and troubleshoot with them. I think that the modeling Professor Hauser did at the beginning of the semester with paired programming was really helpful. Having an option like that for the final project would have helped me a lot.

This is the original plan I had for this project: “The game would be a typing game where typing the correct words advances the turtle to the other side of the screen in order to win. There would be 3 levels of difficulty, with each level having the same amount of time to complete but an increasing amount of letters to type in that time.” Considering these goals, I think I accomplished 95% of what I originally set out to do. I have a function written that advances the progress bar when the correct keys are pressed. I have three levels of difficulty, each untimed but so that the user has to type more for each level. I think that the “me” from a month ago would be fairly happy with my progress.

In conclusion, I’m proud of the work I did on this project and my only regret is not being able to bring my full idea to complete fruition. Below are two versions of my project for comparison. In version 10, the progress bar only advances when the correct letters are pressed in the correct order. The letters do not reset for a new word, so the game progress stops after one word is typed. In version 11, the user can press any letter to advance the progress bar. This version is to show full functionality of the program, since the user can complete the level and play again. I would like for both of these versions to be taken into consideration for evaluation purposes.

Version 10:
<iframe src="https://trinket.io/embed/python/17fde2471e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Version 11:
<iframe src="https://trinket.io/embed/python/f1cdda7ce1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
