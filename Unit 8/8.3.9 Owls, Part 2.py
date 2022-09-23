text = input('Enter some text: ')
text = text.lower()
text = text.split()
listIndex = []
count = 0
for i in range(len(text)):
    if "owl" in text[i]:
        listIndex.append(i)
        count += 1
print("There were " + str(count) + " words that contained \"owl\".")
print('They occurred at indices: ' + str(listIndex))