import random

#lst=[random.randint(-100,100) for n in range(10)]
#print(lst)

#Two List
#lst_positive=[ele for ele in lst if ele>0]
#lst_negative=[ele for ele in lst if ele<0]
#print(f'Positive list: {lst_positive}')
#print(f'Negative list: {lst_negative}')

#+ve and -ve in one list
#num_lst=[ [ele for ele in lst if ele>0],[ele for ele in lst if ele<0] ]
#print(f'Number list: {num_lst}')

odd_lst=[2*n+1 for n in range(20)]
even_lst=[2*n for n in range(1,21)]
print(f'Odd list: {odd_lst}')
print(f'Even list: {even_lst}')


