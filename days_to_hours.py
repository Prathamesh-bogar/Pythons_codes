calculation_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
        print(f"{num_of_days} days are {num_of_days * calculation_unit} {name_of_unit}")
    


def validate_input():
    try:
        user_input_num = int(user_input)
        if user_input_num > 0:
            days_to_units(user_input_num)
        elif user_input_num == 0:
            print("You entered 0 days, please enter valid number of days!!!") 
        else:
             print("You entered negative number, please enter a valid positive number!")   
              
    except ValueError:
        print("Error!!!! Enter a valid number of days!!!!")



user_input=""
while user_input != "exit":
     user_input = input("Please enter number of days and we will convert it to hours \n")
     validate_input()