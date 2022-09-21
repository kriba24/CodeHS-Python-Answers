score = 0
scoreSum = 0
for i in range(3):
    score = int(input("Enter score " + str(i + 1) + ": "))
    scoreSum += score
average = scoreSum / 3
print("Average: " + str(average))