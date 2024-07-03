str = input("Enter\n")

l = len(str) - 1
rev = ""
for i in range(l, -1, -1):
    rev = rev + str[i]

if str == rev:
    print("palindrome!")
else:
    print("not palindrome!")