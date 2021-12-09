--
layout: post
author: alueker
title: "Andrew L's Final Project"
---
<iframe src="https://trinket.io/embed/python/7d6244c2c0?showInstructions=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

How I Made a Replica of Bop It Playable in Python

When I was a kid growing up in the early 2000s, me and my sister had any number of non-cellphone toys and one of my sister’s favorite toys was a game called Bop It. The objective of the game is simple: do what the toy tells you to do as fast as you can. This may seem relatively easy at first, but the game will progressively get harder and faster, which could mean having to react to the game in the span of a second. My sister was the best at the game and managed to beat the game (which is done by completing 100 commands in a row). 

What do my random memories of childhood pastimes have to do with anything, you might ask? Well, I took Bop It and turned it into a functional game using nothing but Python and Trinket! The road to Bop It was full of twist and turns, so let me take you through the creative hell that I put myself through in the past month. 

Bold Roots

My initial project plan was to create a playable game where users could go into an environment and play several smaller mini games. It was admittedly far too ambitious for the month window I was given to code.  I stepped back and thought of a game that would be possible to implement within the span of a month, but also hasn’t been done to death as a student project (as in, stay away from classics like Pong or Space Invaders). That’s when the idea of Bop It came to mind. 

From what I saw, no one had attempted to code Bop It into turtle yet, excluding a few people who coded it into physical hardware and one guy who made it a text-based game. This provided a good opportunity to come up with something original, as there was no available help as to the specific steps that I’d have to take on the internet, meaning that anything that I’d come up with would be from pure ingenuity. 

Attempts in Python3 and PyGame

To start off explaining the process of coding Bop It into Python turtle, I’d like to first talk about my experiences in attempting to code using the advanced features of flick it. Each Trinket that I created had their own bugs that made coding the game more challenging than it probably need to be. I’ll start with Python 3: simply put, the turtle module would not work in Python 3. I have no idea why; it just didn’t want to be imported and apparently conflicted with something called tkinter. 

PyGame was where I developed about half of the full game and to be fair it did a decent job running the program. However, it ran into a problem that ended up effecting the usability of the game, largely because PyGame does not interact with the time module in the same way that a traditional trinket would. For some reason, whenever time.sleep() is activated, it ends up pausing the entire program, and because of this the cursor cannot move until it is already too late. Bop It is a rhythm-based game: this genre of game lives and dies by how well the game controls. Simply put, I couldn’t risk the playability of the game and had to go back to what worked. I know there are native functions within the PyGame library, but simply put, I did not have time to learn PyGame and moved back onto the traditional trinket platform. 

Coding Bop It: The Process

Before I even began coding the original game, I wrestled with the idea of how to code the game. If you look at some of the initial prototypes I developed of the game, they didn’t do much of anything other than have a turtle that responded to button presses. I knew later that the turtle would have to respond to mouse clicks because of how fast the turtle needed to get from point a to point b. But before coding the interaction, I started with the fundamentals of the problem.

I knew that to produce the same effect that the original toy had I needed a function that spat out other functions in a random fashion on an iterative loop. Immediately, I imported the random module and created a function that successfully spat out other functions. The syntax of the function was somewhat tricky, but in the end I managed to get the run() function up and running. 

Secondly was creating the game board. The initial board itself was not hard to develop because it only required a series of turtles drawing buttons, but later down the road I would add an additional turtle that repeated the instructions. I found that this turtle, while somewhat repetitive made the game more enjoyable as users no longer had to look between the screen and the output log while playing the core game. The hardest part of the game screen was undoubtedly coding a system in which the game allows the turtle to move while the game was running. I already mentioned the time kerfuffle that I had with PyGame but imagine my horror when I realized that the regular trinket module had much of the same issues. In the ended, I had to put a screen.listen() loop in every command function in order to get the game to work in my desired fashion. 

Once I completed this, I had the makings of a functional game, but as with the original game, it needed a score. This is where I ran into the conflict between local and global variables. In a sense, Python functions are prejudice and refuse to acknowledge native variables outside of the function until they have been declared in the function as a global variable. This made coding a score into the game tricky; while it was mostly painless establishing a function that ticked to create a score, the score would carry over from a previous game. I ended up creating a separate function that wiped the score at the beginning of every attempt in Bop It. 

At this point, I’ve figured out most of the game’s intricacies and bugs, and it’s time to add some polish to the game. One of my favorite bits of polish I added was background colors depending on the phase the game is in, yellow if the game is waiting, green if the user is successful, and red if the user loses. I found that, although a very minor feature, it makes the game more enjoyable. 

Closing Thoughts and Further Developments

This semester ended up being one of my hardest semesters in my academic career, not because of workload, but because I was dealing with severe burnout. I didn’t complete any of my classes with the amount of energy I generally expect of myself and overall, just feel like I’m reaching the end of my academic rope (for the time being at least). This project ended up being therapeutic to me as it reaffirmed my belief that with hard work and determination you CAN overcome any obstacle, no matter where it lies. 

Future Developments

The win screen is fairly barebone, especially with the hardest difficulty. In the future, I would like to program a fun win screen to reward anyone who sticks with the game that much. 

Because I stuck to a regular trinket format, I lost out on the ability to plug the original sound effects from the game into the program. While I don’t think it’s necessary as the lack of audio provides its own unique challenge, it would be a welcome quality of life upgrade on some of the lower difficulties. 

Program Dictionary and In-Detail Structure

Modules

Turtle

Random - The random.choice() command is used to cycle between command functions (randomly of course)

Time - time.sleep() is used to create the game’s difficulty. Harder difficulties have less forgiveness.

Turtles!

mike, don, raph, april, splinter - These turtles are only drawing turtles and have no impact on the game past creating the board. In the future I’d like to add these turtles to a more complete win screen.

leo - Leo is the cursor in the game and is the star of the show. In every command function, there is a protocol that will look at the position of leo after z amount of time has passed (we’ll explain z later). If leo is in the correct spot, the game progresses and a point is added. If leo is not in the expected spot, the game ends.

writer - Writer illustrates which areas of the game are which for beginners or people that did not grow up with Bop It. If hard or master difficulty are chosen, writer’s input is removed. Think of writer as training wheels that get removed once you mastered the game.

casey - Lastly is casey, who prints output onto the screen. I added Casey later in development as a way to reduce the need for the user to look anywhere other than the screen during the main game. 

Functions and Variables

x,y – Do nothing, there as backups in case leogo() fails.
z – The sleep timer. Z’s value is changed based upon the difficulty setting
addscore() – The counter function that creates a game’s score. 
reset() – Set’s score back to 0 at the beginning of a new game.
difficulty – an input function used to set the games difficulty. Because z’s default value is 2, the game is set to easy by default.
leogo() – this function is bound to onscreenclick to move leo to anywhere on the map.
rules() – redirects users to the instructions, the rules changed a lot and I got tired of updating them.
intro() – sets the difficulty and connects to the run() function
fail() – The fail protocol. If a user loses, they are sent here to either restart the game of change the difficulty. Once writer is removed, help text will not be available until the program is restarted. Leo will reappear if you change from master difficulty.
bopit(), twistit(), spinit(), flickit(), pullit() – The command functions. Each command function is cycled between randomly during an active game. Each function is identical to one another: command will print, will sleep for z seconds, will judge success, or fail based on leo’s position.
game – game is a list of all command functions that is cycled between.  
run() – The function that runs the game, cycles between game functions.

<iframe src="https://trinket.io/embed/python/f1243d14f7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The above trinket is an example of map testing I did to make sure I had exact coordinates.

<iframe src="https://trinket.io/embed/pygame/195507348f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The failed Pygame Trinket
