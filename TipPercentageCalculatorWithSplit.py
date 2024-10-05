# Tip Percentage calculator with split
print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill? "))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

people_share = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_tip = total_bill * tip_percent
total_bill_with_tip = total_bill + total_tip
bill_split = total_bill_with_tip / people_share

final_amount = round(bill_split, 2)

print(f"Each person should pay: ${final_amount}")
