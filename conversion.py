def kms_to_miles(num):
    miles = num * 0.6213711922
    return miles

def cel_to_farenheit(num):
    faren = (num * 9/5) + 32
    return faren

n = int(input("Enter number to convert\n"))

print(f"Conversion of {n} KMs is {kms_to_miles(n)} Miles")
print(f"Conversion of {n} Celcius is {cel_to_farenheit(n)} Farenheit")

