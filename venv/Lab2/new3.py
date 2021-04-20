''' Weight Conversion:
Inpput the weight of a person in either kg or lbs. If the person provides his/her weight in kg then convert it into lbs
else convert it to kg'''

user_weight=float(input("Enter your weight:"))
user_unit=input("Do you want to convert it into kg or pound\n")
if user_unit=='kg':
    print(f'The weight in pounds is {user_weight*2.20462262}')
elif user_unit=='lbs':
    print(f'The weight in kg is {user_weight*0.453}')
else:
    print("It is not recognized. Pick between kg or pounds.")