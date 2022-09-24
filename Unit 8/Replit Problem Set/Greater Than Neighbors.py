def hello(name):
    name = name.split()
    count = 0
    for i in range(1, len(name) - 1):
        if (name[i] > name[i - 1]) and (name[i] > name[i + 1]):
            count += 1
    return count