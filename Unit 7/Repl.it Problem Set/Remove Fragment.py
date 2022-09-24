def hello(name):
    index1 = name.find("h")
    index2 = name.rfind("h")
    return name[:index1] + name[index2 + 1:]