
n =int(input())
a=0
b=1
c=a+b
print(a)
print(b)
for i in range(2,n+1):
    a=b
    b=c
    print(c)
    c=a+b
    
