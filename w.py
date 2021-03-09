'''#WAP to take an input from the user to ask the user age. If the user age is below 15, print a message
 "You are a child." If the users age in above 15, print a message "You are an adult." If the users age is above
  48 then print a message "You are old."'''

age = int(input("Enter your age:"))
if age<15:
    print('You are a child.')
elif age > 15 and age < 48:
    print('You are an adult.')
else:
    print("You are old.")