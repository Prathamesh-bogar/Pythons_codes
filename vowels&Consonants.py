str = input("Enter a string\n")

v = 0
c = 0

for i in str:
    if i in ('a','e','i','o','u'):
        v+=1
    else:
        c+=1

print(f"Number of vowels are {v} and consonants are {c}")
