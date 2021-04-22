''' #Write a python program to find the max of three numbers.'''

def maxnumber(one,two,three):
    if one>two and one>three:
        print("the first number is maximum")
    elif two>one and two>three:
        print("the second number is greater")
    else:
        print("the third number is greater")

first_number=int(input("enter the first number"))
second_number=int(input("enter the second number"))
third_number=int(input("enter the third number"))
maxnumber(first_number,second_number,third_number)