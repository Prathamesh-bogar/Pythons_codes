from datetime import datetime

user_input = input("Enter a goal with dealine as colon separated value!\n")
data_list = user_input.split(":")
goal = data_list[0]
deadline = data_list[1]
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

time_till_deadline = deadline_date - today_date

print(f"Time left to complete your goal: {goal} is {time_till_deadline.days} days")