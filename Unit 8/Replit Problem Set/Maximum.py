def hello(name):
    newList = []
    name = name.split()
    for item in name:
        newList.append(int(item))
    num = max(newList)
    index = newList.index(num)
    return num, index