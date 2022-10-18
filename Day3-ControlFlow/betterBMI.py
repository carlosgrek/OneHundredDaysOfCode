height = float(input("Enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2
round(bmi)

if bmi < 18.5:
    print("You are underweight!")
elif bmi < 25:
    print("You are normal weight!")
elif bmi < 30:
    print("You are overweight!")
elif bmi < 35:
    print("You are obese!")
else:
    print("You are clinically obese!")
