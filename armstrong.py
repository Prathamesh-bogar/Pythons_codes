def validate(num):
    str_n = str(num)
    no_of_digits = len(str_n)
    temp = num
    sum_of_powers = 0

    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** no_of_digits
        temp //= 10
    
    if sum_of_powers == num:
        print(f"{num} is an armstrong number!")
    # else:
    #     print(f"{num} is not an armstrong number!")

start = int(input("Enter a range start: "))
stop = int(input("Enter a range stop: "))
for i in range(start, stop+1):
    validate(i)