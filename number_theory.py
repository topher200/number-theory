#!/usr/bin/python3

from random import randint

def choose_randomly():
  return randint(1,6)

def roll_die():
  return choose_randomly()

def play(guess_function):
  roll1 = roll_die()
  roll2 = roll_die()

  guess1 = guess_function()
  guess2 = guess_function()

  return ((roll1 == guess1) and (roll2 == guess2))

wins = 0
losses = 0
for i in range(1000000):
  # Play, and record the outcome
  if play(choose_randomly):
    wins += 1
  else:
    losses += 1

total_games = wins + losses
win_percentage = wins / total_games
print(wins, losses, win_percentage)
  
