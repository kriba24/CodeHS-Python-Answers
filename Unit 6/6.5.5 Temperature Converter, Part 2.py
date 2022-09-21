def fToC():
    try:
        tempF = float(input('Enter a temperature in degrees Fahrenheit: '))
    except ValueError:
        print("Try again, that didn't work!")
    tempC = (tempF - 32) / 1.8
    print(tempc)
def cToF():
    try:
        tempC = float(input('Enter a temperature in degress Celsius: '))
    except ValueError:
        print("Try again, that didn't work!")
    tempF = (tempC * 1.8) + 32
fToC()
cToF()