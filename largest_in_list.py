def find_largest(lst):
    largest = lst[0]

    for num in lst[1:]:
        if num > largest:
            largest = num
    
    return largest

list = input("Enter the numbers separated by comma\n")
new_list = [int(i) for i in list.split(", ")]
result = find_largest(new_list)
print(f"The largest element is {result}")



