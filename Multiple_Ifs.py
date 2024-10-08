height = int(input("What is your height: "))
bill = 0
if height >= 120:
    print("You can ride!")
    age = int(input("What is your age: "))
    if age < 12:
        bill = 5
        print("Ticket rate is $5")
    elif age <= 18:
        bill = 7
        print("ticket rate is $7")
    elif age >= 18:
        bill = 12
        print("Ticket rate is $12")

    want_photo = input("If you want photos type 'y' for Yes and 'n' for No: ").lower()

    if want_photo == "y":
        bill += 3

    print(f"The total bill is ${bill}")

else:
    print("You can't ride!")
