def hello(name):
    name = name.split()
    name = [int(i)for i in name]
    newlist = []
    name2 = []
    for item in name:
        name2.append(int(item))
        
    for i in range(len(name2)):
        count = 0
        x = name2[i]
        for j in range(len(name2)):
            if x == name2[j]:
                count += 1
        if count == 1:
            newlist.append(name[i])
    return newlist