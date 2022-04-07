import random

def generate_list():
    l = []
    for i in range (5):
        n = random.randint(0,10)
        l.append(n)
    return l

print(generate_list())


