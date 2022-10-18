print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        total_cost = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        total_cost = 7
    else:
        print("Adult tickets are $12.")
        total_cost = 12

    wants_photo = input("Do you want a photo taken fro $10? Yes or No? ")
    if wants_photo == "Yes":
        total_cost += 10
        print(f"Your total cost comes to ${total_cost}.")

    else:
        print(f"Your total cost comes to ${total_cost}.")

else:
    print("Sorry, you have to grow taller before you can ride.")


