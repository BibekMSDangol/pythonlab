''' A school decided to replace the desks in three classrooms. Each desks sits two students. Given the number of
# students in each class, print the smallest possible number of desks that can be purchased.'''

no_student_class1 = int(input("Enter the number of student in first class : "))
no_student_class2 = int(input("Enter the number of students in second class : "))
no_student_class3 = int(input("Enter the number of students in third class : "))

desk_class1 = (no_student_class1 // 2)
print(f"The required number of desk for first class is {desk_class1}")
desk_class2 = (no_student_class2 // 2)
print(f"The required number of desk for second class is {desk_class2}")
desk_class3 = (no_student_class3 // 2)
print(f"The required number of desk for third class is {desk_class3}")

remain_class1 = (no_student_class1 % 2)
print(f"Remaining desk for first class is {remain_class1} ")
remain_class2 = (no_student_class2 % 2)
print(f"Remaining desk for second class is {remain_class2} ")
remain_class3 = (no_student_class3 % 2)
print(f"Remaining desk for third class is {remain_class3} ")
total_desk = desk_class1 + desk_class2 + desk_class3 + remain_class1 + remain_class2 + remain_class3
print(f"The total number of desks that can be purchased is {total_desk} ")




