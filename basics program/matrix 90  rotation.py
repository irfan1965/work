n=int(input("enter row"))
n2=int(input("enter column"))
p=[]
for i in range(n):
    l=list(map(int,input().split()))
    p.append(l)
print(p,"original matrix")
k=[]
o=[]
for i in range((n2)):
  for j in range((n)):
    k.append(p[j][i])
  o.append(k)
  k=[]
for i in o:
  print(i)
