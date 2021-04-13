# Write a program that reads the length of the base and the height of a right-angled triangle and print the area. Every number is given on a seperate line.

length = int(input("Enter the value of the length: "))
height = int(input("Enter the height: "))

area = (length * height)//2

print(f"the area of triangle is {area}")