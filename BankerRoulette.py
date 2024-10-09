import random

members = ["Sai", "Charen", "Pooja", "Seenu", "Vj", "Priya"]
pay_bill = random.choice(members)

print(f"Bill will be paid by: {pay_bill}!")

#or

pay_bill = random.randint(0, 4)

print(members[pay_bill])
