num = int(input("Enter a number to check!\n"))

original = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if rev == original:
    print(f"{original} is a palindrome number!")
else:
    print(f"{original} is not a palindrome number!")