def hello(name):
    firstf = name.find("f")
    if firstf == -1:
        return -1
    lastf = name.rindex("f")
    if firstf == lastf:
        return firstf
    else:
        return firstf,lastf