# WAP to print the multiplication table of a given number using functions.

def mul(a):
    for i in range(1, 11):
        mul = a * i
        print(f" {a} * {i} = {mul}")

mul(5)