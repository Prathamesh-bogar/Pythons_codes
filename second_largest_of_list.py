n = input("Enter list separated by comma and space\n")
list = [int(i) for i in n.split(", ")]
list.sort(reverse=True)
print(f"The second largest value of list is {list[1]}")