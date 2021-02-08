from art import logo
from art import vs
from game_data import data
import random


game_data = data



def compare_followers(followers1, followers2):
  if(followers1 > followers2):
    return True
  else:
    return False


def generateNumber():
  randomNumber = random.randint(0,49)
  return randomNumber

score = 0

def game():
  global score

  itemA = random.choice(game_data)

  itemB = random.choice(game_data)

  if(itemA == itemB):
    itemA = random.choice(game_data)

  game_start = False


  while not game_start:
    print(logo)
    print(f"Compare A: {itemA['name']}, {itemA['description']}, from {itemA['country']} ")
    print(vs)
    print(f"Against B: {itemB['name']}, {itemB['description']}, from {itemB['country']}")
    choice = input("Who has more followers? Type 'A' or 'B' ").lower()

    result = False
    if choice == "A":
      result = compare_followers(itemA['follower_count'],itemB['follower_count'])

    if choice =="B":
      result = compare_followers(itemB['follower_count'],itemA['follower_count'])

    if result == True:
      score +=1
      print(f"You are right ! Current score {score}.")
      itemA = itemB
      itemB = random.choice(game_data)

      if itemB == itemA:
        itemB = random.choice(game_data)
      continue
    else:
      print(f"Sorry that's wrong. Final score: {score}")
      game_start = True


game()
