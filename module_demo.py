
def days_to_units(num_of_days, conversion_unit):
        if conversion_unit == "Hours" or  conversion_unit == "hours":
             print(f"{num_of_days} days are {num_of_days * 24} hours")
        elif conversion_unit == "Minutes" or conversion_unit == "minutes":
             print(f"{num_of_days} days are {num_of_days * 24 * 60} minutes")
        else:
             print("Enter Valid unit of conversion between Hours/hours and Minutes/minutes!")
        
    


def validate_input(user_input, conversion_unit):
    try:
         user_input_num = int(user_input)
         if user_input_num > 0:
              days_to_units(user_input_num, conversion_unit)
         elif user_input_num == 0:
              print("You entered 0, please enter a valid number for conversion!!")
         else:
              print("You entered a negative number, no conversion for you!!")  
    except ValueError:
        print("Error! Yout input is not valid..Don't ruin my program!")