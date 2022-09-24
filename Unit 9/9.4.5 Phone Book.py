phonebook = {}
human_input = ""
while True:
    human_input = input('Enter a name: ')
    if human_input == "":
        break
    elif human_input in phonebook:
        print(phonebook[human_input])
    else:
        phone_number = input('Enter a phone number: ')
        phonebook[human_input] = phone_number
print(phonebook)