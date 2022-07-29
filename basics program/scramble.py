import random
m=list(map(str,input("enter :  ").split()))
#m=['irfan','is','a','good','hoax!']
p=""
s=""
for n in m:
    if len(n)>3:
        if n[-1].isalpha():
            p=n[1:len(n)-1]
        else:
            p=n[1:len(n)-2]
        p=list(p)
        random.shuffle(p)
        g=n[0]
        for i in p:
            if i.isalpha():
                g+=i
            else:
                s+=i
        if n[-1].isalpha():
            g+=n[-1]
        else:
            g+=n[-2:]
        

        print(g,end=" ")
    else:
        print(n,end=" ")
print(s)