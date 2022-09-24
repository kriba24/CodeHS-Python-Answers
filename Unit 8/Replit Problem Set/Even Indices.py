def hello(name):
    newList = []
    for i in range(len(name)):
        if i % 2 == 0:
            newList.append(name[i])
    return newList