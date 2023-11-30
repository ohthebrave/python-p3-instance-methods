#!/usr/bin/env python3

class Dog:
    # Class body goes here

    #Instance method definition
    # bark becomes a method of all instances of Dogs.
    def bark(self):
        print('whoof!')

    # sit becomes a method 
    def sit(self):
        print("The dog is sitting.")


fido = Dog()
fido.bark()
# output =>> Woof!

snoopy = Dog()
snoopy.sit()