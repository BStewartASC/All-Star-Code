from random import *




wife = ["your girl", "Beyonce", "Niki Minaj"]

job = ["bum", "football player", "engineer"]

car = ["mazerati", "honda civic", "lambo"]

home = ["mansion", "apartment", "shack", "house"]

wife = raw_input("Who do you want to be your wife:")

job = raw_input("What do you want you job to be:")

car = raw_input("What car do you want to drive:")

home = raw_input("What do you want to live in:")

print("Your wife will be " + choice(wife))

print("You will be a " + choice(job))

print("You will drive a " + choice(car))

print("You will live in a " + choice(home))
