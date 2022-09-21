def remove_all_from_string(word, letter):
    while True: # This is an infinite loop
        index = word.find(letter) # Finds the index of specified letter
        if index == -1: # If the index is -1 meaning that the word isn't found, it will just return the word.
            return word
        word = word[:index] + word[index + 1:] # This returns everything in the word except for this letter