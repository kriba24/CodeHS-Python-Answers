# Write your function here...

def safe_int(item):
    try:
        return int(item)
    except:
        return 0


list_of_strings = ["a", "2", "7", "zebra"]


# Your code here...

print([safe_int(i) for i in list_of_strings])