# WAP to find the factorial of a number by using functions.

def factorial(a):
    factorial = 1
    num = int(input("Enter a number: "))
    for i in range(num, 1, -1):
        factorial = factorial * i
    return factorial

x = factorial(5)
print(f"The factorial of given number is {x}")

