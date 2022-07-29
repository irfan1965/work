import csv
x=open("Student_Data.csv")
s=csv.reader(x)
r=[]
for i in s:
    r.append(i)
for i in range(len(r)):
    print(r[i][0])
x.close()