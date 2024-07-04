n = int(input("Enter a number\n"))
count = 0

while n > 0:
    n = n // 10
    count += 1

print(f"Number of digits is {count}")