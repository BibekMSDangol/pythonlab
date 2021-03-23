import random

number= random.randint(1,10)
guess=int(input("Please guess the number"))
while number !=guess:
    guess = int(input('Try again'))
else:
    print('Congratulations!! You are right')