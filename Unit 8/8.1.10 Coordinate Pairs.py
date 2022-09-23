import math


# fill in this function to return the distance between the two points!
def distance(first_point, second_point):
    diffX = math.pow(second_point[0] - first_point[0], 2)
    diffY = math.pow(second_point[1] - first_point[1], 2)
    result = math.sqrt(diffX + diffY)
    return result