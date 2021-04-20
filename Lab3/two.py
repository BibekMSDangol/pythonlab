''' Write a funciton called fizz_buzz that takes a number.
If the number is divisible by 3, it should return "fizz"
If it is divisible by 5, it should return "Buzz"
It it is divisible by both 3 and 5, it should return "FizzBuzz"
Otherwise it should return the same number. '''

def fizzbuzz (num):
    if (num%3==0) and (num%5==0):
        return "Fizzbuzz"
    elif num%3==0:
        return "Fizz"
    elif num%5==0:
        return "Buzz"
    else:
        print(num)

num = int(input("Enter a number: "))
x = fizzbuzz(num)
print(x)
print("End")