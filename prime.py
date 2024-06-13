def is_prime(num):
    if num <=1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
    
n = int(input("Enter a number\n"))
result = is_prime(n)

if result:
    print(f"{n} is prime!")
else:
    print(f"{n} is not prime!")