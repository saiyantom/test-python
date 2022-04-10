def create_array(x,y,z):
    lst=list()
    return [[[k for k in range(z)] for j in range(y)] for i in range(x)]

print(create_array(3,3,4))

