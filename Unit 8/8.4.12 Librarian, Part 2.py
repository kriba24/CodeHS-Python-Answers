name_list = []
for i in range(5):
    name = input('Name: ')
    name = name.split()
    name = name.pop() 
    name_list.append(name)
name_list.sort()
print(name_list)