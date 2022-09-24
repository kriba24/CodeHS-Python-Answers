myList = []
for i in range(5):
    x = int(input('Enter an x value: '))
    y = int(input('Enter a y value: '))
    myList.append((x, y))

for i in range(4):
    p1 = myList[i]
    p2 = myList[i + 1]
    x1, y1 = p1
    x2, y2 = p2
    slope = (y2 - y1)/(x2 - x1)
    print('Slope between ' + str(p1) + ' and ' + str(p2) + ': ' + str(slope))