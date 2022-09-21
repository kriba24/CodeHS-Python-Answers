age = int(input("Age: "))
citizen = input("Born in the US? ")
residency = int(input("Years of residency: "))
if age >= 35 and citizen == "Yes" and residency >= 14:
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")