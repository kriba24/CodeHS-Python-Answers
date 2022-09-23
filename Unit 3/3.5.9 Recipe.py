"""
This program asks the user for three ingredients,
three amounts, and a number of servings, and
determines how much of each ingredient is needed
to serve the specified number of servings.
"""

# Write program here...
ing1 = input("What is the first ingredient? ")
amountOfIng1 = float(input("How much " + ing1 + " do you want? "))
ing2 = input("What is the second ingredient? ")
amountOfIng2 = float(input("How much " + ing2 + " do you want? "))
ing3 = input("What is the third ingredient? ")
amountOfIng3 = float(input("How much " + ing3 + " do you want? "))
numServings = int(input("How many servings? "))
totalIng1 = numServings * amountOfIng1
totalIng2 = numServings * amountOfIng2
totalIng3 = numServings * amountOfIng3
print("Total " + ing1 +": " + str(totalIng1))
print("Total " + ing2 +": " + str(totalIng2))
print("Total " + ing3 +": " + str(totalIng3))