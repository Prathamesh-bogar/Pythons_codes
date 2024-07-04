def fibonacci(num):
    num1 = 0
    num2 = 1
    next_number = num2
    count = 1
    if num < 0:
        print ("Invalid input")
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        while count <= n:
            print(next_number, end=", ")
            count += 1
            num1 , num2 = num2, next_number
            next_number = num1 + num2
        print()

n = int(input("Enter a number to find fibonacci series\n"))
fibonacci(n)