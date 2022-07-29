p=1
while p:
    l=[2,5,8,12,16,23,38,56,72,91]
    l=sorted(l)
    print(l)
    o=int(input("enter which element to be search"))
    f=0
    h=len(l)-1
    m=(f+h)//2
    if o not in l:
        print('enter the correct numbver')
    else:
        while l[m]!=o:
            if l[m]<o:
                f=m+1
            else:
                h=m-1
            m=(f+h)//2
        print(m)
    p=int(input("enter the valid number\n for YES press 1\n for NO press 0\n"))
            