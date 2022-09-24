def hello(name):
	name = name.split()
	newList = []
	if len(name) % 2 == 0:
		for i in range(len(name)):
			if i % 2 == 0:
				newList.append(int(name[i + 1]))
			else:
				newList.append(int(name[i - 1]))
	else:
		for i in range(len(name) - 1):
			if i % 2 == 0:
				newList.append(int(name[i + 1]))
			else:
				newList.append(int(name[i - 1]))
		newList.append(int(name[-1]))
	return newList