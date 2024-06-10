calculation_unit = 24*60
name_of_unit = "minutes"


def days_to_units(num_of_days):
        print(f"{num_of_days} days are {num_of_days * calculation_unit} {name_of_unit}")
    


def validate_input():
    if user_input.isdigit():
        user_input_num = int(user_input)
        if user_input_num > 0:
            days_to_units(user_input_num)
        elif user_input_num == 0:
            print("You entered 0 days, please enter valid number of days!!!")     
    else:
        print("Error!!!! Enter a valid number of days!!!!")


user_input = input("Please enter number of days and we will convert it to minutes \n")
    
validate_input()








