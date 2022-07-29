import csv
from random import sample
x=open("sample.csv")
j=csv.reader(x)
print(next(j))
r=[]
for  i in j:
    r.append(i)
print(r)
x.close()