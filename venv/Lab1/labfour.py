'''
#Given the integer N - the number of minutes that is passed since midnight -
how many hours and minutes are displayed on the 24th difital clock?'''

N = int(input("Enter the minutes passed since midnight: "))
hours = (N/68)
minutes = (N%60)
print(f"The hours is {hours} ")
print(f"The minutes is {minutes} ")
print(f"Its {hours}:{minutes} now ")