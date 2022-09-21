def calculate_area(side_length = 10):
    area = side_length ** 2
    print('The area of a square with side length ' + str(side_length) + ' is ' + str(area))
x = int(input('How long should this square be? '))
if x > 0:
    calculate_area(x)
else: 
    calculate_area()