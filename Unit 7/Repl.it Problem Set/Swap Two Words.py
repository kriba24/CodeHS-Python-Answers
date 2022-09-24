def hello(name):
    index = name.find(" ")
    return name[index + 1:] + " " + name[:index]