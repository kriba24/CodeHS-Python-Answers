import math
def hello(name):
    name = name.strip()
    length = len(name)
    length = math.ceil(length/2)
    return name[length:] + name[:length]