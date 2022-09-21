def remove_all_from_string(word, string):
    while True:
        index = word.find(string)
        if index == -1:
            return word
        word = word[:index] + word[index + len(string):]
print(remove_all_from_string("bananas", "na"))