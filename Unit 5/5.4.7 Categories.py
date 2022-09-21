listThings = ""
category = ""
thing = ""
for i in range(3):
    category = input('Enter a category: ')
    for j in range(3):
        thing = input('Enter something in that category: ')
        listThings += thing + " "
    print(category + ": " + listThings)
    listThings = ""