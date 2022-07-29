import csv
from random import *
import pandas as pd
from random import randrange
from timee import *
from lot import *
from random_deallocation import *
from random_allocation import *

ind=0
cou=0

j=csv.reader(open("lot.csv"))
df = pd.read_csv("lot.csv")
o1=(next(j)[1:])
for i in range(4):
    for j in range(1,11):
        df.iloc[i, j]="free"
        df.to_csv("lot.csv", index=False)
r=open("lot.csv")
k=csv.reader(r)
j=[]
rw=0
for i in k:
  j.append(i)
g=(j)
dic={ }
c=0
x=[]
for i in range(1,len(g)):
  x.append(g[i][0])
temp={}
td={}
for i in x:
  temp[i]=[]
  td[i]=[]
u=[]

for i  in g[1:]:
  dic[i[0]]=i[1:]

while(1):
  print("enter 1 for random allocations enter 2 fro de allocations and 3 for reset ")
  nn=int(input("enter "))
  if nn==1:
      al1(dic)
  elif nn==2:
      print("random deallocatio")
      rd(dic)


    


