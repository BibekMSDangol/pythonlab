''' Given three integers, print the smallest one. (Three integers should be user input)'''

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
if num1 < num2 and num1 < num3:
    print(f"The first number is smallest: {num1}")
elif num2 < num1 and num2 < num3:
    print(f"The second number is smallesr: {num2}")
else:
    print(f"The third number is smallest: {num3} ")