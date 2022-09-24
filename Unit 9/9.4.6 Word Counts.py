userinput = input('Enter some text: ')
myDict = {}
userinput = userinput.split()
for item in userinput:
    if item in myDict:
        myDict[item] += 1
    else:
        myDict[item] = 1
print(myDict)