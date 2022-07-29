# # n=4
# # for i in range(n):
# #     for j in range(i):
# #         print("*",end="")
# #     print()                    
# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#             print("*",end=" ")
        
#     print()



n=5
k=0
for i in range(1,n+1):
    for j in range((n-i)+1):
        print(end="  ")
        
    while k!=(2*i-1):
        print("*",end=" ")
        k+=1
    
    k=0    
    print()
#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5
# rows = 5
# k = 0
# count=0
# count1=0

# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print("  ", end="")
#         count+=1
    
#     while k!=((2*i)-1):
#         if count<=rows-1:
#             print(i+k, end=" ")
#             count+=1
#         else:
#             count1+=1
#             print(i+k-(2*count1),end=" ")
#         k += 1
    
#     count1 = count = k = 0
#     print()
#rows = int(input("Enter number of rows: "))

# for i in range(rows, 1, -1):
#     for space in range(0, rows-i):
#         print("  ", end="")
#     for j in range(i, 2*i-1):
#         print("* ", end="")
#     for j in range(1, i-1):
#         print("* ", end="")
#     print()
