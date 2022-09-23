list_num = []
for i in range(5):
    num = int(input("Number: "))
    list_num.append(num)
    print(list_num)

total = 0
for i in range(5):
    total = total + int(list_num[i])

print("Sum: " + str(total))