n=input()
n=reversed((list(n)))
s=0
c=0
for i in n:
    i=int(i)
    s+=i*2**c
    #print(s,i,i*2**c)
    c+=1
print(s)
