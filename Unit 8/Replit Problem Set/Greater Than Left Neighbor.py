def hello(name):
    newList = []
    for i in range(len(name) - 1):
        if name[i] < name[i + 1]:
            newList.append(name[i + 1])
    return newList