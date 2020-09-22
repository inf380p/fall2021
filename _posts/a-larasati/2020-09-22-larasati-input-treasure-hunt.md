---
layout: post
author: a-larasati
title: "Turtle Treasure Hunt & Reflections"
---
#### Turtle Treasure Hunt

Thankfully I didn't have to start from scratch for this exercise, though I think I can do it as long as the basic information re: what the game wants to do is there (might take a lot longer though...)

There are a couple of moving parts to this exercise that I needed to tackle aside from understanding what's been prepared on the starter pieces of code. I read up on what `random` was and what `random.randint` does to understand what they do and how they fits to the whole program. Aside from this, the base code had comments as instructions (which frustrated me at first but I'll get to that later), the frame for a `while` loop, and some variables defined. The rest was up to me.

The first thing I did was pick apart what I needed to do and look at the base code to see what's been covered. From there, I came up with this short list:

1. Get user input.
2. Make Tina go to user input.
3. Give feedback to the user re: their inputs and how close/far they are to the treasure.
4. Declare the user a winner when they find the correct coordinate combination.

##### Getting user input

If just asking for input, it's pretty straightforward (use `input()` ) but there's more to it that that because I have to anticipate invalid inputs like typing words or spelling out the actual number. I decided to tackle this problem one coordinate at a time because if I can do it for the X coordinate, it's just copy-paste for the Y (and changing the appropriate variables of course). Here's the piece I wrote for the X coordinate:

```python
user_x = raw_input("Choose an X coordinate between -100 and 100")
try:
	xcoord = int(user_x)
	if xcoord < -100 or xcoord > 100:
		print("Try again.")
		continue
except:
	print("Try again.")
	continue
```

The original code used `raw_input()` which takes all inputs as a string, so I added a line that changes the string input to integers. Combining it with a `try` and `except`, I wrote the code to anticipate 3 things:
1. if the input is appropriate (a number between -100 and 100), `continue` to the next piece of code (ask for the Y coordinates);
2. if the input is not appropriate because the user enters a number above 100 or below -100, prompt the user to try again;
3. if the input is not appropriate because the user spells out the number or types a word/random letters, prompt the user to try again.

Once I got this piece working the way I wanted to, I copied and pasted it for the Y coordinates.

##### Make Tina go user input

This one is relatively straightforward. Since I assigned `xcoord` and `ycoord` to the integer of the numbers the users entered, I used those variables instead of the original `user_x` and `user_y` variables.

##### Give feedback about turtle position relative to treasure and winning the game

This one was a little tricky because it came with a couple of stipulations. The instruction on the base code was:

```
 # Give the user feedback on how close they are to the treasure
 # If the user is within 5 pixels of the treasure, they win!
```

I had to write code that reads the input and somehow calculates the distance between the current input and the random coordinates that `randint()` has assigned for the run of the program and provide feedback based on that input. If the input is within 5 pixels of the actual coordinates, the user wins.

There were 2 parts of this section that was kind of left up to interpretation: the type/frequency of feedback and what "5 pixels" mean. Regarding the feedback, I decided to give the user feedback after ever set of coordinates they enter, meaning after the user enters a number for X and Y, the machine tells them something. Regarding the "within 5 pixels," that part was what tripped me up the most in the beginning. Because from the way the instructions in the base code was written, it made it sound like these 2 separate pieces. Technically, yes they are, but I figured why not combine them into one?

The first thing I did at this point was decide how to approach the "within 5 pixels" part because in the code I wrote, "5 pixels" was the deciding factor. But what exactly did "5 pixels" mean? Does it mean that if the treasure was hidden on (10,10) and the user enters (5,5) or (15,15) or any combination in between, they win? Or does it mean if the treasure was on (10,10) they can enter any number for X and Y coordinate so long as the sum of the square of the values equals to 25 i.e. the square of 5 (if that makes any sense? The pythagorean theorem??)?

I decided that "5 pixels" meant 5 steps: if the treasure is on (10,10) and the user enters (10,15) or (15,10) or (12,13) or (8,7) or any number combination that is a total of 5 steps away from the winning coordinates, the user wins the game. To do this, I decided to sum the absolute value of the `randint()` that was assigned to the run of the program and compare it to the sum of the absolute value of coordinate numbers the user enters. If the difference of these absolute values is less than or equal to 5, the user wins. I also normalized the value to reduce the chances of error in calculation by adding 100; the range of "correct" inputs taken is from -100 to 100, which means there are 201 possible numerical inputs (including 0), and adding 100 simply pushes the range from 0 to 200. Note: `treasure_x` and `treasure_y` are variables assigned to the `randint()` values from the base code, which represents the X and Y coordinates of the treasure.

Regarding the feedback, I wanted the feedback to be relatively straightforward: using a standard X,Y coordinate plane and a `if` `else` statement, if the X value the user inputs is too high or too low, the feedback tells them that they are too far to the right or left, respectively. For Y values too high or too low, the feedback tells them that they are too high or low, respectively. If they found one correct coordinate but not the other, the feedback tells them they found that correct coordinate and their position relative to the incorrect one.

```python
#Normalizing the coordinates to prep it for the checks
norm_xcoord = xcoord + 100
norm_ycoord = ycoord + 100
norm_treasurex = treasure_x + 100
norm_treasurey = treasure_y + 100

#Checks the input coordinates and compares it to the random X/Y generated
check_xcoord = abs(norm_xcoord - norm_treasurex)
check_ycoord = abs(norm_ycoord - norm_treasurey)

if check_xcoord + check_ycoord > 5:
	if xcoord > treasure_x:
		print("You're too far to the right.")
	if xcoord < treasure_x:
		print("You're too far to the left.")
	if xcoord == treasure_x:
		print("You found the x-coordinate!")
	if ycoord > treasure_y:
		print("You're too high.")
	if ycoord < treasure_y:
		print("You're too low.")
	if ycoord == treasure_y:
		print("You've found the y-coordinate!")
	continue
else:
	user_has_won = True
```

The rest of the code was already prepared and it was a matter of getting the formatting right to trigger the winning animation. Here's the results from creating this treasure hunt. I didn't experiment outside the requirements too much. Enjoy!

<iframe src="https://trinket.io/embed/python/6cc3f748dd?toggleCode=true&start=result&showInstructions=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

#### Exercise Reflection

This was a fun exercise, and I actually felt like I made something that did something. I also rubber-ducked! Which was nice because I rubber-ducked on my partner as I worked and he helped me tease out the tough bits and pieces. I bounced ideas with him, especially on the "5 pixels" part of the requirement and how to approach that, but ultimately I decided to use the normalizing method I had thought of after we went on a walk with his dog and played Animal Crossing.

While writing this reflection, I had to refer to my code a couple of times and I realized spots where I could do certain things differently, especially about that "5 pixels" thing. I couldn't taken the difference between the `randint()` values and the user input values to calculate the distance between the points using the Pythagorean formula and set the feedback to respond if the difference is more than 5. I think I also inadvertantly made a feedback system that essentially guides the user to the specific `randint()` coordinates.

Overall I learned a lot as a student and as a programmer on how to think and approach problems. I also learned that those inline comment instructions are a bit bothersome for me because it made me think that the code needed to be written a certain way in a certain sequence. To the next!
