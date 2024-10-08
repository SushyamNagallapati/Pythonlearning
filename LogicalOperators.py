height = int(input("Enter your height: "))

if height >= 120:
    print("You are eligible to ride!")
    age = int(input("enter your age: "))
    bill = 0
    if age < 12:
        bill += 5
        print("Your bill is $5")
    elif age < 18:
        bill += 7
        print("Your bill is $7")
    elif age >= 45 and age <= 55:
        print("Your ride is Free!")
    else:
        bill += 12
        print("Your bill is $12")


    want_photos = input("Type 'y' if you want Photos or type 'n' if you don't want: ")
    if want_photos == "y":
        bill += 3
    print(f"Your final bill is: ${bill}.")

else:
    print("You are not Eligible!")
