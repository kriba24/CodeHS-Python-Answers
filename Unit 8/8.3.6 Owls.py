def owl_count(text):
    text = text.lower()
    text = text.split()
    count = 0
    for i in range(len(text)):
        if "owl" in text[i]:
            count += 1
    return count