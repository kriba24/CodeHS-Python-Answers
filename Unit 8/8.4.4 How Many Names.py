name = ""
numNames = int(input("How many names do you have? "))
for i in range(numNames):
    name += input("Name: ") + " "
name = name.split()
print("First name: " + str(name[0]))
print("Middle names: " + str(name[1:numNames - 1]))
print("Last name: " + str(name[-1]))