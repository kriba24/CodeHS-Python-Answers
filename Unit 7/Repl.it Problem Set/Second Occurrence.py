def hello(name):
    int1 = name.find("p")
    if int1 == -1:
        return -2
    int2 = name.find("p", int1 + 1)
    if int2 == -1:
        return -1
    else:
        return int2