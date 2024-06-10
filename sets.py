calculation_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
        print(f"{num_of_days} days are {num_of_days * calculation_unit} {name_of_unit}")
    


def validate_input():
    try:
         user_input_num = int(num_of_days)
         if user_input_num > 0:
              days_to_units(user_input_num)
         elif user_input_num == 0:
              print("You entered 0, please enter a valid number for conversion!!")
         else:
              print("You entered a negative number, no conversion for you!!")  
    except ValueError:
        print("Error! Yout input is not valid..Don't ruin my program!")
    
    

user_input = ""
while user_input != "exit":
     user_input = input("Please enter number of days as comma separated list and we will convert it to hours \n")
     user_list = user_input.split(", ")
     for num_of_days in user_list:
          validate_input()
        









