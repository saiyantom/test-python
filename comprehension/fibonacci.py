fibon=[]
fibon.append(0)
fibon.append(1)
[fibon.append(fibon[i-1]+fibon[i-2]) for i in range(2,20)]
print(fibon)

