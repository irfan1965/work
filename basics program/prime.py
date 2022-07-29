n=int(input("enter number"))
for i in range(2,(n//2)+1):
    if n%i==0:
        print("Not Prime Number")
        break
else:
    print("prime number")