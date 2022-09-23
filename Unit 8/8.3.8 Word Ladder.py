def get_index():
    global index
    while True:
        index = int(input("Enter an index (-1 to quit): "))
        if index > len(word):
            print("Invalid index")
        elif index < -1:
            print("Invalid index")
        elif index == -1:
            break
        else:
            break


def get_letter():
    global letter
    while True:
        letter = input("Enter a letter: ")
        if len(letter) != 1:
            print("Must be exactly one character!")
        elif letter != letter.lower():
            print("Character must be a lowercase letter!")
        else:
            break


index = 0
letter = ""
word = input("Enter a word: ")
while True:
    get_index()
    if index == -1:
        break
    get_letter()
    list(word)
    print(str(word[:index]) + letter + str(word[index + 1:]))
    word = str(word[:index]) + letter + str(word[index + 1:])