userinput = input('Enter some text: ')
userinput = userinput.split()
myDict = {}
def update_counts(count_dictionary, word):
    for item in word:
        if item in count_dictionary:
            count_dictionary[item] += 1
        else:
            count_dictionary[item] = 1
    return count_dictionary
print(update_counts(myDict, userinput))