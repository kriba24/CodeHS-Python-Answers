def retrieve_positive_number():
    num = 0
    while num <= 0:
        try:
            num = int(input("Enter a positive number: "))
        except ValueError:
            print("That isn't a number!")
        if num > 0:
            return num
        elif num <= 0:
            print("That wasn't a positive number!")
print(retrieve_positive_number())