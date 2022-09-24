def hello(name):
    index1 = name.find("h")
    index2 = name.rindex("h")
    name1 = name[index1:index2 + 1]
    return name[:index1] + name1[::-1] + name[index2 + 1:]