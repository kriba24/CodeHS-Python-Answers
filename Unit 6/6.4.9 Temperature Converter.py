# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!
def celsiusToFahrenheit(tempCelsius):
    return (tempCelsius * 1.8) + 32



# Now write your function for converting Fahrenheit to Celsius.

def fahrenheitToCelsius(tempFahrenheit):
    return (tempFahrenheit - 32) / 1.8


# Now change 0C to F:
print(celsiusToFahrenheit(0))
# Change 100C to F:
print(celsiusToFahrenheit(100))
# Change 40F to C:
print(fahrenheitToCelsius(40))
# Change 80F to C:
print(fahrenheitToCelsius(80))