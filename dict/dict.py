import operator

d={'Kiwi':34.67,'Apple':12.08,
'Pear':30.34,'Banana':54.5,
'Orange':97,'Lemon':81.5}

student1 = {'Mary':24,'John':60,'Alex':43}
student2 = {'David':12,'Canny':52,'Fanny':73}

print(f'Original dict: {d}\n')

#Get dictionary values
print(d.get('Pear'),30)
print(d.get('Pfdear'),5)

#Print dictionary key,values
#for (k,v) in d.items():
#    print(k,v)

#Print dictionary key,values in sorted order (asc,desc)
#print(f'Sorted order asc:')
#for (k,v) in sorted(d.items()):
#    print(k,v)

#print(f'Sorted order desc:')
#for (k,v) in sorted(d.items(),reverse=True):
#    print(k,v)

#Print dictionary key,values in sorted order by values (asc,desc)
#print(f'Sorted order asc by values:')
#for (k,v) in sorted(d.items(),key = operator.itemgetter(1)):
#    print(k,v)

#print(f'\nSorted order desc by values:')
#for (k,v) in sorted(d.items(),key = operator.itemgetter(1), reverse=True):
#    print(k,v)

#Sort dictionary by key (default)
#d1 = sorted(d.items())
#d2 = sorted(d.items(),reverse=True)
#print(f'Sorted dict in asc. order by key: {d1}\n')
#print(f'Sorted dict in desc. order by key: {d2}\n')

#Sort dictionary by values (require operator pkg)
#d1 = sorted(d.items(),key = operator.itemgetter(1))
#d2 = sorted(d.items(),key = operator.itemgetter(1), reverse=True)
#print(f'Sorted dict in asc. order by values: {d1}\n')
#print(f'Sorted dict in desc. order by values: {d2}\n')

#Unpack Dictionary
#student_new = {**student1, **student2}
#print(f'New Student: {student_new}')
