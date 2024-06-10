#Import validate function from demo module which contains the code.
from module_demo import validate_input

user_input = ""
while user_input != "exit":
     user_input = input("Hey User, enter number of days and units for conversion\n")
     days_and_units = user_input.split(":")
     my_dict = {"no_of_days":days_and_units[0],"units_of_conversion":days_and_units[1]}
     days = my_dict["no_of_days"]
     units = my_dict["units_of_conversion"]
     validate_input(days, units)