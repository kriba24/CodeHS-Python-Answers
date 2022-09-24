def hello(name):
    name1 = ""
    for i in range(len(name)):
        if i % 3 != 0:
            name1 += name[i]
    return name1