def hello(name):
    index1 = name.find("h")
    index2 = name.rindex("h")
    name1 = name[index1 + 1:index2]
    name1 = name1.replace("h", "H")
    return name[:index1 + 1] + name1 + name[index2:]