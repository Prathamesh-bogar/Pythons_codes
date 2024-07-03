n = int(input("Enter number\n"))
fact = 1
if n < 0:
    print("Enter valid positive number!")
elif n==0 or n==1:
    print(f"The factorial is {fact}")
else:
    for i in range(1,n+1):
        fact = fact * i
    print(f"The factotial is {fact}")