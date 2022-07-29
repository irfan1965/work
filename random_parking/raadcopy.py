import csv
from random import *
import pandas as pd
from threading import  *
from random import randrange
from datetime import timedelta
from datetime import datetime
import time 

ind=0
cou=0
bn=["AP","TS"]
nu=['01', '02', '03', '04', '05', '06', '07', '08', '09']
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

def tim():     
    d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
    m=random_date(d1, d2)
    m=int(str(m)[-8:-6]) 
    if m<=1 and m>0 :
        m=20
    elif m<=10:
        m=m*10
    else: 
        m=m*5   
    return m

for i  in g[1:]:
  dic[i[0]]=i[1:]
class Vehicle:
    def __init__(self,Name,Number):
        self.Name=Name
        self.Number=Number
class bike(Vehicle):
    def __init__(self,Name,Number):
        #print(Name,Number)
        Vehicle.__init__(self,Name,Number)
class car(Vehicle):
    def __init__(self,Name,Number):
        #print(Name,Number)
        Vehicle.__init__(self,Name,Number)
class bus(Vehicle):
    def __init__(self,Name,Number):
        #print(Name,Number)
        Vehicle.__init__(self,Name,Number)
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def rl(sp,ep,name):
                rw=0
                time.sleep(0.3)
                for z,j in dic.items():
                    flag = 0
                    for po in range(sp,ep):
                      time.sleep(0.01)
                      if j[po]=="free":                        
                        if z=="A":
                          rw=0                          
                          dic[z][po]="f"
                          num=str(choice(bn))+str(choice(nu))+str(chr(choice(range(65,90))))+str(chr(choice(range(65,90))))
                          cx=str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))
                          df.iloc[rw, po+1]="{}\{}".format(name,num+cx)
                          df.to_csv("lot.csv", index=False) 
                          flag = 1
                          break
                        elif z=="B":
                          rw=1                          
                          dic[z][po]="f"
                          num=str(choice(bn))+str(choice(nu))+str(chr(choice(range(65,90))))+str(chr(choice(range(65,90))))
                          cx=str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))
                          df.iloc[rw, po+1]="{}\{}".format(name,num+cx)
                          df.to_csv("lot.csv", index=False) 
                         # print(rw,"B")
                          flag = 1
                          break
                        elif z=="C":
                          rw=2                         
                          dic[z][po]="f"
                          num=str(choice(bn))+str(choice(nu))+str(chr(choice(range(65,90))))+str(chr(choice(range(65,90))))
                          cx=str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))
                          df.iloc[rw, po+1]="{}\{}".format(name,num+cx)
                          df.to_csv("lot.csv", index=False) 
                         # print(rw,"C")
                          flag = 1
                          break
                        else:
                          rw=3
                          dic[z][po]="f"
                          num=str(choice(bn))+str(choice(nu))+str(chr(choice(range(65,90))))+str(chr(choice(range(65,90))))
                          cx=str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))
                          df.iloc[rw, po+1]="{}\{}".format(name,num+cx)
                          df.to_csv("lot.csv", index=False) 
                          flag = 1
                          break
                          #print(rw,"D")
                    if flag == 1:
                        break
def rdl(sp,ep,name):
                rw=0
                #print(sp,ep,name) 
                for z,j in dic.items():
                    flag = 0
                    for po in range(sp,ep):
                      time.sleep(0.01)
                      if j[po]!="free":                        
                        if z=="A":
                          rw=0                          
                          dic[z][po]="free"
                          num=str(choice(bn))+str(choice(nu))+str(chr(choice(range(65,90))))+str(chr(choice(range(65,90))))
                          cx=str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))
                          print(rw,po+1,"posi")
                          df.iloc[rw, po+1]="free"
                          df.to_csv("lot.csv", index=False) 
                          print("|----------------------------------------------|")
                          print("vehicletype : ",name)
                          print("vehicle number : ",num+cx)
                          print("your charger  will be : ",tim())
                          print("|----------------------------------------------|")
                          print()
                          print()
                          flag = 1
                          break
                        elif z=="B":
                          rw=1                          
                          dic[z][po]="free"
                          num=str(choice(bn))+str(choice(nu))+str(chr(choice(range(65,90))))+str(chr(choice(range(65,90))))
                          cx=str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))
                          df.iloc[rw, po+1]="free"
                          df.to_csv("lot.csv", index=False) 
                          print("|----------------------------------------------|")
                          print("vehicletype : ",name)
                          print("vehicle number : ",num+cx)
                          print("your charger  will be : ",tim())
                          print("|----------------------------------------------|")
                          print()
                          print()
                         # print(rw,"B")
                          flag = 1
                          break
                        elif z=="C":
                          rw=2                         
                          dic[z][po]="free"
                          num=str(choice(bn))+str(choice(nu))+str(chr(choice(range(65,90))))+str(chr(choice(range(65,90))))
                          cx=str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))
                          df.iloc[rw, po+1]="free".format(name,num+cx,tim())
                          df.to_csv("lot.csv", index=False)
                          print("|----------------------------------------------|")
                          print("vehicletype : ",name)
                          print("vehicle number : ",num+cx)
                          print("your charger  will be : ",tim()) 
                          print("|----------------------------------------------|")
                          print()
                          print()
                         # print(rw,"C")
                          flag = 1
                          break
                        else:
                          rw=3
                          dic[z][po]="free"
                          num=str(choice(bn))+str(choice(nu))+str(chr(choice(range(65,90))))+str(chr(choice(range(65,90))))
                          cx=str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))
                          df.iloc[rw, po+1]="free"
                          df.to_csv("lot.csv", index=False)
                          print("|----------------------------------------------|")
                          print("vehicletype : ",name)
                          print("vehicle number : ",num+cx)
                          print("your charger  will be : ",tim()) 
                          print("|----------------------------------------------|")
                          print()
                          print()
                          flag = 1
                          break
                          #print(rw,"D")
                    if flag == 1:
                        break

                               
def al1():
      o=["car","bike","bus"]
      bi=bu=c=i=0
      while i<=40:
          if c+bi+bu<=40:
              if c<=24 and bi<=12 and bu <= 4:
                  v=choice(o)
                  if v=="car" and c<24:
                      sp=0
                      ep=6
                      name="car"
                      number=123
                      obj=car(name,number)
                      c+=1
                      i+=1
                      rl(sp,ep,name)
                  elif v=="bike" and bi<12:
                        sp=6
                        ep=9
                        name="bike"
                        number="123"
                        obj=bike(name,number)
                        bi+=1
                        i+=1
                        rl(sp,ep,name)
                  elif bu<4:
                        bu+=1
                        i+=1
                        name="bus"
                        number=1234
                        obj=bus(name,number)
                        sp=9
                        ep=10
                        rl(sp,ep,name)
          
          if i==40:
            break      
def rd():
      o=["car","bike","bus"]
      bi=bu=c=i=0
      while i<=40:
          if c+bi+bu<=40:
              if c<=24 and bi<=12 and bu <= 4:
                  v=choice(o)
                  if v=="car" and c<24:
                      sp=0
                      ep=6
                      name="car"
                      number=123
                      obj=car(name,number)
                      c+=1
                      i+=1
                      rdl(sp,ep,name)
                  elif v=="bike" and bi<12:
                        sp=6
                        ep=9
                        name="bike"
                        number="123"
                        obj=bike(name,number)
                        bi+=1
                        i+=1
                        rdl(sp,ep,name)
                  elif bu<4:
                        bu+=1
                        i+=1
                        name="bus"
                        number=1234
                        obj=bus(name,number)
                        sp=9
                        ep=10
                        rdl(sp,ep,name)
          #print(c,bi,bu,"fdg")
          if i==40:
            break      

while(1):
  print("enter 1 for random allocations enter 2 fro de allocations and 3 for reset ")
  nn=int(input("enter "))
  if nn==1:
      al1()
  elif nn==2:
      print("random deallocatio")
      rd()


    


