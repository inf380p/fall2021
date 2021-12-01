---
layout: post
author: vannyyeh
title: "(Extra Credit) Homework Revisions/Reflections III"
---


# Snapshot on Trinket

<iframe src="https://trinket.io/embed/python3/05b3e14bc8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


# Reflection

It's a good chanch to learn OOP, and some of the exercise in the Runestone is helpful but challenging. 
For example:
```
class Pokemon():

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def stringPokemon(self):
        print(f"Pokemon name is {self.name} and type is {self.type}")

class GrassType(Pokemon):

    # overrides the stringPokemon() function on 'Pokemon' class
    def stringPokemon(self):
        print(f"Grass type pokemon name is {self.name}")

poke1 = GrassType('Bulbasaur', 'Grass')
poke1.stringPokemon
poke1.stringPokemon()
poke2 = Pokemon('Charizard', 'Fire')
poke2.stringPokemon
poke2.stringPokemon()
```

I learn the method `__init__ ` that is called at the moment when a class is being used to construct an object. This is used to set up initial values for the object.

I stuck with those codes a long while ago, and I can't see the bug (since it's an optional chapter, I didn't solve it at that moment.) However, I saw the bug this time when I came back and tried it again. The bugs are just from some tiny attributes that are missing. For instance, the `class` keyword is used to define the data and code that will make up each of the objects, and `self` is used to represent the current instance of the class. I forgot to look up the details last time. Thus, the real power in object-oriented programming happens when we construct multiple instances of our class. Each constructor is linked with each attribute which makes the object complete. 

Although I think I still have confusion about what constructors really are and how to set up different initial values for each of the objects, I believe. At the same time, I construct multiple objects from our class, I will understand them clearly.

This exercise not only taught me the details and the OOP but also reminded me of the details of the codes inside and outside of the `()`. 

