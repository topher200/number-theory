#!/usr/bin/python3

from random import randint

def choose_randomly():
  return randint(1,6)

def roll_die():
  return choose_randomly()

def play_randomly():
  roll1 = roll_die()
  roll2 = roll_die()

  guess1 = choose_randomly()
  guess2 = choose_randomly()

  return ((roll1 == guess1) and (roll2 == guess2))

print(play_randomly())
