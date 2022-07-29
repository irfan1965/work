l=[[1,2,3],[4,5,6],[7,8,9]]
k=len(l)
v=[]
for i in range(k-1,-1,-1):
    print(i)
    v.append(i)
print(v)
x=v[:2]
print(x)
for i in x[::-1]:
    print(i)
    v.append(-+i)

print(v,"jfk")
b=[]
n=[]
#print(l[2][1])
for o in v:
  for i in range(k):
    for j in range(k):
        if o==(i-j):
            b.append(l[i][j])
  n.append(b)
  b=[]             
print(n)