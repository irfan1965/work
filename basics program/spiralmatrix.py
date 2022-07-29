
p=[[1, 2, 3,8], [4,9, 5, 6], [7,0, 8, 9],[8,6,4,3]]
n=len(p)
# for i in range(n):
#     l=list(map(int,input().split()))
#     p.append(l)
for i in p:
    print(i)
k=n*n
#print(k)
i=0
j=t=i
t1=n-1
#print(t1)
while k!=0:
    if (i==t and j<=t1):
        print(p[i][j],end=" ")
        if j==t1:
            i=i+1
        else:
            j=j+1
    elif (j==t1 and i<=t1):
        print(p[i][j],end=" ")
        if i==t1:
            j=j-1
        else:
            i+=1
    elif i==t1 and j>=t:
        print(p[i][j],end=" ")
        if j==t :
            i-=1
        else:
            j-=1
    elif j==t and i<=t1:
        print(p[i][j],end=" ")
        if i==t+1:
            j+=1
            t+=1
            t1-=1
        else:
            i-=1
    k-=1