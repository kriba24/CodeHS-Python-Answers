def hello(name):
    newList = []
    name = name.split()
    count = 0
    for item in name:
        newList.append(int(item))
    for i in range(len(newList)):
        for j in range(i + 1, len(newList)):
            if name[i] == name[j]:
                count += 1
    return count