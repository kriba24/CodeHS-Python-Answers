weather = input('What is the weather? (sunny, rainy, snowy): ')
def rainy():
    print("Wear galoshes. It's wet outside!")
def snowy():
    print("Make sure to wear boots. It's cold!")
def sunny():
    print("Good day to wear sandals!")
if weather == "sunny":
    sunny()
else:
    if weather == "snowy":
        snowy()
    else:
        if weather == "rainy":
            rainy()
        else:
            print('Invalid option!')