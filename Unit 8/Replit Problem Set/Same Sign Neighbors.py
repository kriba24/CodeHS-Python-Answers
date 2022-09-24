def hello(name):
    newList = []
    for i in range(len(name) - 1):
        if (name[i] * name[i + 1]) > 0:
            newList.append(name[i])
            newList.append(name[i + 1])
            return newList
    if not newList:
        return 0