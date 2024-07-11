def fibonacci(num):
    a = 0
    b = 1

    if num < 0:
        print("Incorrect Input!")
    elif num == 0:
        return 0
    elif num == 1:
        return b
    else:
        for i in range(1, num+1):
            c = a + b
            a, b = b, c
        return b
    
n = int(input("Enter a number to get the fibonacci series term\n"))
print(fibonacci(n))