#to check the number
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

#to check the string 1
str = input("Enter the string to check!\n")

rev = str[::-1]

if str == rev:
    print(str, "is palindrome!")
else:
    print(str, "is not palindrome!")

#to check the string 2
str = input("Enter\n")

l = len(str) - 1
rev = ""
for i in range(l, -1, -1):
    rev = rev + str[i]

if str == rev:
    print("palindrome!")
else:
    print("not palindrome!")



