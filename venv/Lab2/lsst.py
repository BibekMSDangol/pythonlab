def mul(dot):
    lst=[2,4,6,8]
    for i in lst:
        if lst == 2:
            return lst(1)
        else:
            return lst[i] +mul(dot - 1)
print(mul())