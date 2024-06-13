
def validate_even_odd(n):
    if n < 0 or n == 0:
        print("Please enter valid positive number!")
    elif n % 2 == 0 :
        print(f"{n} is an even number!")
    else:
        print(f"{n} is an odd number! ")


num = int(input("Please enter a number\n"))
validate_even_odd(num)