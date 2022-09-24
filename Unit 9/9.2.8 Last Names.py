names = [
    "Maya Angelou",
    "Chimamanda Ngozi Adichie",
    "Tobias Wolff",
    "Sherman Alexie",
    "Aziz Ansari"
]
# Your code here... 

name = [names[i].split() for i in range(len(names))]
names = [name[i][-1] for i in range(len(names))]
print(names)