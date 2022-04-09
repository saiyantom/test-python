import random

#lst = [random.randint(1,100) for n in range(10)]
new_lst = [ele*10 for ele in [random.randint(1,100) for n in range(10)] ]

#print(lst)
print(new_lst)
