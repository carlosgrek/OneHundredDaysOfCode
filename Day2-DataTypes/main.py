# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# 90 years has
# days = 32850
# weeks = 4680
# months = 1080

days_left = 32850 - int(age) * 365
weeks_left = 4680 - int(age) * 52
months_left = 1080 - int(age) * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left to live.")

