n=list(map(int,input().split()))
n=sorted(n)
print(n)

o=int(input("enter which element to be found"))
for i in range(len(n)-1):
    if o==n[i]:
        print(o,"is found at index of ",i)
