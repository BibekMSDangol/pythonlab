''' Write a function called showNumbers that take a parameter called limit. It should print all the numbers between 0
and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print
0 Even
1 Odd
2 Even
'''

def showNumbers (limit):
    if (limit%2==0):
        print(f'It is even')
