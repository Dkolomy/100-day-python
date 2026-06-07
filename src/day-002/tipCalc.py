print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = total_bill * (tip_percentage / 100)
total_amount = total_bill + tip
amount_per_person = total_amount / people

print(f"Each person should pay: ${amount_per_person:.2f}")