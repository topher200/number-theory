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

wins = 0
losses = 0
for i in range(10000):
  # Play, and record the outcome
  if play_randomly():
    wins += 1
  else:
    losses += 1

total_games = wins + losses
win_percentage = wins / total_games
print(wins, losses, win_percentage)
  
