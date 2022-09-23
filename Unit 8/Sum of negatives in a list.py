def sumOfNegs(list1):
    sum = 0
    for num in list1:
        if num < 0:
            sum += num
    return sum