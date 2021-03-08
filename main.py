print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_num = int(input("How many people to split the bill? "))

total_bill_w_tip = round(total_bill + (total_bill * (tip_percentage / 100)), 2)
each_person_pay = "{:.2f}".format(total_bill_w_tip / people_num)

print(f"Each person should pay: ${each_person_pay}")