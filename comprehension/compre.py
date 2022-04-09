
#List Comprehension
lst2 = ['OK' if n%22==0 else (2*n+1) for n in range (100)]
print(lst2)

#Set Comprehension
s1 = {1,3,5,7,9}
s2 = {n**3 for n in s1}
print(s2)

#Dictionary Comprehension
d = {'Mary':60,'John':80,'Jenny':40,'Peter':30,'Mavis':76}
d2 = {k:('Pass' if v>50 else 'Fail') for (k,v) in d.items()}
print(d2)
