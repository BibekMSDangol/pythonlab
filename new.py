'''# WAP to check a number given by the user is armstrong or not.'''
num = int(input("Enter any number"))
sum = 0
cube = num
while num>0:
    rem = num%10
    sum = sum + rem ** 3
    num = num//10
if sum == cube :
    print(f'The number is armstrong.')
else:
    print(f'The number is not armstrong')
print(sum)
print(cube)


