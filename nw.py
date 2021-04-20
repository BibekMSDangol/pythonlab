'''#WAP to find am or pm from the time given by the user.'''

user_time = int(input("Enter the time: "))
if (user_time >= 1 and user_time <= 12):
    print('The time is am')
else:
    print("The time is pm")