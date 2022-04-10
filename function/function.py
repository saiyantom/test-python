#Pass by positional arguments
def area(l,w,h):
    return 2*((l*w)+(w*h)+(l*h))


#Pass by keyword arguments
def area2(l,w,h):
    return 2*((l*w)+(w*h)+(l*h))


#Pass by variable positional arguments
def area3(*args):
    for para in args:
        return [round(ele**2,2) for ele in para]

#Pass by variable keyword arguments
def volume(**kwargs):
    result=1
    for (para,v) in kwargs.items():
        result *= v
    return result 


s=(2.3,4.6,3.2,5.08,7.41)
side={'l':6,'w':5,'h':2}

print(f'Area1: {area(10,20,15)}')
print(f'Area2: {area2(h=30,l=20,w=15)}')
print(f'Area3 Square: {area3(s)}')
print(f'Volume: {volume(**side)}')
