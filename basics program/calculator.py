r=0
f=int(input("enter :  "))
k=[]
n=0
while n!=1:
    s=input("enter opertions : ")
    l=int(input("enter : "))
    if s=="-":
        r+=f-l
        print(r)
    elif s=="+":
        r+=f+l
        print(r)
    elif s=="*":
        r+=f*l
        print(r)
    elif s=="%":
        r+=f%l
        print(r)
    elif s=="/":
        r+=f/l
        print(r)
    else:
        print("undefine symbol")
        break
    k.append(r)
    f=r
    r=0
    print("press s to continue or n to stop")
    n=input()
    if n=="s":
        n=0
    else:
        n=1
    print(k)

    



