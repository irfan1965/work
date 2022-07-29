from lot import *
from random import *
import pandas as pd
import time


def rl(sp,ep,name,dic):
                df = pd.read_csv("lot.csv")
                bn=["AP","TS"]
                nu=['01', '02', '03', '04', '05', '06', '07', '08', '09']
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

                               
def al1(dic):
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
                      rl(sp,ep,name,dic)
                  elif v=="bike" and bi<12:
                        sp=6
                        ep=9
                        name="bike"
                        number="123"
                        obj=bike(name,number)
                        bi+=1
                        i+=1
                        rl(sp,ep,name,dic)
                  elif bu<4:
                        bu+=1
                        i+=1
                        name="bus"
                        number=1234
                        obj=bus(name,number)
                        sp=9
                        ep=10
                        rl(sp,ep,name,dic)
          
          if i==40:
            break  