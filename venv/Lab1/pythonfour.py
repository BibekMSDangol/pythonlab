# N students take K apples and distribute them among each other evenly. The remaining part remains in the basket.
# How many apples will each single student get? How many apples will remain in the basket?
# The program reads the number N and K. It should print two answers for the questions above.

N=int(input("enter the number of students in class:"))
A=int(input("enter the number of apples:"))
D=(A//N)
R=(A%N)
print(f"each student got {D} ")
print(f"the remaining apples are {R}")
