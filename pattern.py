n = int(input("Enter the number of rows\n"))
#right angled triangle
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     print()

#reverse right angled triangle
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("*", end=" ")
    print()