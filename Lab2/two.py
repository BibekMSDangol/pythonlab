'''#WAP which accepts marks od four subjects and display total marks, percentage and grade.'''
WAP1=int(input("Enter the marks of the first subject: "))
WAP2=int(input("Enter the marks of the second subject: "))
WAP3=int(input("Enter the marks of the third subject: "))
WAP4=int(input("Enter the marks of the fourth subject: "))
total_marks=(WAP1+WAP2+WAP3+WAP4)
print(f" the total marks {total_marks}")
percentage = total_marks/400*100
if percentage>=80 and percentage<=100:
    print( "You have scored A+")
elif percentage>=60 and percentage<=79:
    print("You have scored A")
elif percentage>=40 and percentage<=59:
    print("You have scored B+")
else:
    print("You have failed")