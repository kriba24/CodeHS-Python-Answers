def hello(name):
    newList = []
    name = name.split()
    for item in name:
        newList.append(int(item))
    maxlist = max(newList)
    minlist = min(newList)
    indexMin = newList.index(minlist)
    indexMax = newList.index(maxlist)
    newList[indexMin] = maxlist
    newList[indexMax] = minlist
    return newList