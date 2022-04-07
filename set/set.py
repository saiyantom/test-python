import random

s=set()
c=b=0

while len(s)<10:
    #for k in range (10):
    n = random.randint(15,46)
    s.add(n)

print(f'Before operation: {s}')

#my_list=list(s)
#print(f'After conversion: {my_list}\n')

#for i in range(len(my_list)-1):
#    if my_list[i] < 30:
#        c+=1
#        continue
#    if my_list[i] > 35:
#        b+=1
#        my_list.remove(my_list[i])
#        print(f'list after removal: {my_list}')
 
#print(f'After operation: {my_list}')
#print(f'Number of elements<30: {c}')
#print(f'Number of elements>35: {b}')
