from collections import Counter

s = input('Enter the string: ')
occ_dict = dict(Counter(s))

#print(f'{occ_dict}\n')

for k,v in occ_dict.items():
    print(k,v)
