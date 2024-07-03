num = input("Enter set of numbers separated by comma to find average of:\n")
list = num.split(",")

n = len(list)
sum = 0
for i in list:
    sum = sum + int(i)
    
avg = sum / n
print(f"Average of given numbers is {avg}")
                   