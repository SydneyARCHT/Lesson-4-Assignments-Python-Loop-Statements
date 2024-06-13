#Lesson 4: Assignments | Python Loop Statements
#1. The Range Riddle
#Task 1:
#index            0           1         2           3            4         5          6
import random
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for days_of_week, day in enumerate(days_of_week):
  if days_of_week % 2 == 0:
    print(day)

print()

#2. Loop Condition Logic
#Task 1:
x = 10
while x <= 100:
  print(x)
  x += 10

print()

#Task 2:
x = 1
while x <= 6:
  print(x)
  if x == 5:
     break
  x += 1

print()

#3. Python's Random Game Night
import random
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_number = random.choice(nums)
while True:
    user_input = input("Guess the number I am thinking of from 1 to 10: ")
    if int(user_input) == random_number:
        print("You got it! Seems like luck to me...")
        break
    else:
        print("Ha! Guess again!")



