age = int(input("Age: "))
citizen = input("Born in the US? ")
residency = int(input("Years of residency: "))
if age < 35 or citizen == "No" or residency < 14:
    print("You are not eligible to run for president.")
if age < 35:
    print("You are too young. You must be at least 35 years old.")
elif citizen == "No":
    print("You must be born in the U.S. to run for president.")
elif residency < 14:
    print("You have not been a resident for long enough.")
else:
    print("You are eligible to run for president!")