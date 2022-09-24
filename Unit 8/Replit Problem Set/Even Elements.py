def hello(name):
    evenList = []
    for item in name:
        if item % 2 == 0:
            evenList.append(item)
    return evenList