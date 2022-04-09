import pandas as pd
from tabulate import tabulate

student = {'Mary':{'English':70,'Chinese':90,'Maths':60},
           'John':{'English':43,'Chinese':67,'Maths':54},
           'Peter':{'English':80,'Chinese':35,'Maths':78}}

result_student = {}

for name,subj in student.items():
   total = subj['English'] + subj['Chinese'] + subj['Maths']
   average = float(total / 3)
   new_student = {name:{'Total':total,'Average':average}}
   result_student.update(new_student)

df = pd.DataFrame(result_student)
print(tabulate(df.T, headers="keys"))
