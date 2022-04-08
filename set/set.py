import random

s=set()
gt_set=set()
c=0

while len(s)<10:
    n = random.randint(15,46)
    s.add(n)

print(f'Before operation: {s}')

for item in s:
    if item > 35:
        gt_set.add(item)
    elif item < 30:
        c+=1

print(f'No. of elements < 30: {c}')
print(f'No. of elements > 35: {gt_set}')
print(f'After operation: {s-gt_set}')
