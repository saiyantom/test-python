def compute(num):
#    n,m = 7,7
    change=num
    sum=0
    for i in range(num):
        sum+=change
        change=change*10+num
    return sum

print(compute(7))
