from art import *
import random
import time
from game_data import *
import replit
print(logo)

score = 0
game_over = False
question_a = None
question_b = None

while game_over == False:
  if score == 0:
    question_a = random.choice(data)
    # print(question_a)
  else:
    replit.clear()
    question_a = starting_question
    print(f"That's corrent! Your current score is {score}")
    
  print(f"Compare A: {question_a['name']}, a {question_a['description']} from {question_a['country']}.")
  print(vs)

  question_b = random.choice(data)
  while question_a == question_b:
    question_b = random.choice(data)
    
  print(f"Compare B: {question_b['name']}, a {question_b['description']} from {question_b['country']}.")
  
  selected_input = input("\nWho has more followers? type A or B.\n")
  
  if selected_input == 'A' and question_a['follower_count'] > question_b['follower_count']:
    score += 1
    # print(f"Correct! {question_a['name']} has more followers than {question_b['name']}.")
    correct_answer = 'A'
    starting_question = question_b
  elif selected_input == 'B' and question_b['follower_count'] > question_a['follower_count']:
    score += 1
    # print(f"Correct! {question_b['name']} has more followers than {question_a['name']}.")
    correct_answer = 'B'
    starting_question = question_a
  else:
    print(f"That's wrong, unfortunately. Your final score was {score}. Run again to play again.")
    game_over = True
  
  time.sleep(1)