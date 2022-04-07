import random

lst = []

for i in range (20):
    n = random.randint(0,100)
    lst.append(n)

print(f'The generated list: {lst}\n')

number = int(input("Enter the number: "))

if lst.count(number)>0:
    print(f'Position of number in list: {lst.index(number)+1}\n')
else:
    print('Number is not in the list\n')
