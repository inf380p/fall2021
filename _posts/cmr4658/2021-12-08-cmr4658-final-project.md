---
 layout: post
 author: cmr4658
 title: "Chase's Final Project and Reflection"
---

# Final Project

<iframe src="https://trinket.io/embed/python/b11a025afc" width="100%" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Project Overview

For my final project, I decided to make a Hangman-style game. My goal was to have the program select a random word from an external text file and let the player guess which letters are in the word using the keyboard. I also wanted the program to keep track of the player's guesses and let them know if they tried to guess a letter they had already guessed previously. After the player had guessed all the letters in the word (or ran out of guesses) I wanted to give them the option to play again. Finally, if there was enough time, I planned to add in a graphical representation of the hangman--since I came up with the project idea in October, my plan was to use a skeleton for this and make the game Halloween-themed. Overall, I was able to achieve my goals for this project, and I'm proud of how it turned out even though it's no longer seasonally appropriate. :)

I chose a Turtle game rather than a data analysis program for my final project because I love games in general (and making them). Even though it's relatively small in scope as far as games go, it was very satisfying to make one from start to finish. I think part of the reason I was ahead of schedule throughout the project was because I genuinely had a lot of fun working on it and felt motivated to keep trying new things. Both that motivation and the general Python skills I had the opportunity to practice (like dictionaries, functions, and class inheritance) will be just as useful to me on more practical projects.

Something interesting I noticed while working on this project was that I felt two distinct types of frustration. The first type was a more negative feeling that usually came up after I'd been working on the same problem for too long or if I was tired in general--it led to me trying the same thing over and over and could only really be solved by working on something else or just walking away for a while. The other type was a positive feeling that motivated me to keep pushing through difficult problems by thinking about them from different angles. Learning to recognize what kind of frustration I was feeling helped me decide what I should do in situations where I was feeling stuck--limiting the negative frustration where I knew I wasn't going to make any progress and harnessing the positive frustration to focus and get things done.

## Planning Process

I used this list of milestones to break down the project into manageable tasks and make sure I would be able to complete it on schedule:

### Basic Functionality
- [x] Set up a class for text display boxes
- [x] Get the game to recognize keypresses and display them on the screen
- [x] Keep track of previously guessed letters and display them
- [x] Start making the word dictionary

### Iterative Interface
- [x] Put the game functions inside a while loop (and leave the setup functions outside)
- [x] Make an input function to select the difficulty
- [x] Fix the lives counter so the game ends when it hits 0
- [x] Create the win/lose/play again screen

### Presentation
- [x] Put the Display class in an external module
- [x] Add the skeleton picture
- [x] Tie the skeleton picture to the lives counter

### Stretch Goals
- [x] Add more words to the word dictionary
- [x] Make the interface resize evenly or lock to one size

When I was deciding what my project milestones would be and how I would schedule them, I prioritized making something that functioned the way I wanted it to without worrying too much about what it looked like. The last thing I wanted to do was to spend a lot of time making the interface look nice only to have to redo everything when I started on the gameplay--and potentially run out of time to make something that worked at all. It was also important to me to identify a variety of things I could work on at the start, so that if I got stuck on a certain part, I could take a break from it and work on something else that would still be just as productive. I think this approach was the right balance of structure and flexibility for me.

## Challenges, Strategies, and Solutions

The first challenge (and to me, the hardest) came up right at the beginning of the project, just as I was starting on the basic functionality of the game. From what we'd gone over in class and in the textbook, I knew that I could use the `onkey` function in Turtle to bind another function to a specific key. My first instinct was to write a function that would pass in the letter of the key being pressed, but that didn't work, since the function called by the `onkey` function couldn't take any parameters. At this point, I was a little concerned that I wouldn't be able to get this type of game to work--all the online resources I could find on `onkey` used it as something like arrow keys to move the character around the screen instead of text input. That was when I knew I needed to break down the problem further. I already knew that I wanted each key to do something like this, but I didn't want to write it out 26 times:

```
def guess(letter):
    if letter in guessed:
      status_display.update('You already guessed that letter! Guess again.')
    else:
      guessed.append(letter)
      guess_display.update('Guesses: ' + ", ".join(guessed))
      update_progress()
      if letter not in current_word:
        lose_life()
```

Then I remembered something I did for one of the Runestone exercises where I added a variety of functions to a list and then used them later by accessing them in the list. If that was possible, I realized I could probably do the same thing in this situation by using a for loop to create the functions and just appending them all to the list. The one issue was that I couldn't name the functions that were generated by the for loop, which resulted in me having to call the functions by index instead of letter. I got around this by using a dictionary instead of a list, setting the key to the letter being pressed, and setting the value to the corresponding function. Finally, I added two more functions to activate the keys at the beginning of the game and deactivate them so they wouldn't do anything if the player wasn't in the middle of a game. Here is what I ended up with:

```
def create_function(letter): # This will be the onkey function for every letter
  def function():
    if letter in guessed:
      status_display.update('You already guessed that letter! Guess again.')
    else:
      guessed.append(letter)
      guess_display.update('Guesses: ' + ", ".join(guessed))
      update_progress()
      if letter not in current_word:
        lose_life()

  return function

def activate_keys():  
  for letter in all_letters: # Activate the onkey functions at start of game
    keyboard[letter] = create_function(letter)
    screen.onkey(keyboard[letter], letter)
    
def deactivate_keys(): # Deactivate the onkey functions (after game over)
  for letter in all_letters:
    screen.onkey(None, letter)
```

The other challenge I faced was organizing my code. This one was interesting because at first glance it didn't effect how the end product looked or worked at all, but I think it made an enormous difference in how easy the code was to work with (as far as adding new features and changing things around) and how readable it was in the end. After I finished the basic functionality, my project definitely worked, but the functions weren't really in any particular order and it was hard to read:

<iframe src="https://trinket.io/embed/python/bd61a725fe" width="100%" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

It was so unmanageable that for the next iteration, I decided it would actually be easier to rewrite the whole thing from scratch. First, I used comments to delineate different sections for the code based on what it did. Then, I thought about what order the components needed to run in, and what the code was supposed to do from start to finish (instead of just tacking on new functions at the end as I wrote them). Originally, I was just going to copy and paste the individual functions over, but while I didn't change a whole lot, looking at what I'd already written with fresh eyes made it easier to see places where I could improve it. For example, originally I had three separate functions to update the word, guess, and lives displays:

```
def update_guesses(): # update the guess display
  guess_display.text.clear()
  message = 'Guesses: ' + ', '.join(guessed)
  guess_display.text.write(message, align='center')
  
def update_lives(): # update the lives counter
  lives_display.text.clear()
  message = 'Lives: ' + str(lives)
  lives_display.text.write(message, align='center')
  
def update_word(): # update the word display
  word_display.text.clear()
  msg = []
  for letter in current_word:
    if letter in guessed:
      msg.append(letter)
    else:
      msg.append('_')
  result = ' '.join(msg)
  word_display.text.write(result, align='center', move=False, font=font)
```

I took these out and replaced them with an `update` method on the `Display` class itself, which all the display objects are instances of:

```
  def update(self, message, alignment='center'):
    self.text.clear()
    self.text.write(message, align=alignment, move=False, font=self.font)
```

Now, instead of messing with three different functions, I could use the `update` method for all the displays:

```
status.display.update('Text goes here')
```

I'm very glad I caught this early, since so much of the game revolves around updating the text in the displays on screen. Taking the extra time to make this really simple and readable probably saved me a lot of time I would have spent debugging down the road.

## Final Thoughts

Overall, I'm happy with how this game came out, and working on it definitely helped me solidify the Python skills I've learned in this class and elsewhere. Surprisingly, even though most of the project is made up of things I've done at least once before, the fact that I needed to put them all together--not to mention planning the project and writing updates--makes me feel like I've learned a lot in a short period of time.

My concentration at the iSchool is in usability and accessibility, and I think games are a great place to practice skills in these areas--both Python and in thinking about the different ways different users might interact with the program. I'd really like to continue making projects like these outside of class on my own time to put what I'm learning in my other classes into practice. It's possible I'll also revisit this game in the future and see how I might be able to improve it.
