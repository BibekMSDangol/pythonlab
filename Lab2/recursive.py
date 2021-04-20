def mul(n):
    if n==1:
        return 3
    else:
        return 3+mul(n-1)
for i in range(1,11):

    print(mul(i))