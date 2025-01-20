print("!!welcome to the tip calculator!!")
bill = float(input("what was your total bill"))
tip = float(input("what percentage tip would you like to give ( do not enter % sign ) "))
number = int(input("how many people to split the bill"))


tip_as_percent = tip /100
total_tip = tip_as_percent * bill
total_bill = bill + total_tip
per_person = total_bill/number

print(f"each person should pay : {round(per_person, 2)}")
