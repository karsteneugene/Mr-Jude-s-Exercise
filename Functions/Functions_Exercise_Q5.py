# Made the function convert temp()
def convert_temp():
    # Asks user to input temperature in Fahrenheit in integers
    fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
    print("")

    # Displays the temperature in Fahrenheit
    print("The temperature in Fahrenheit is:", fahrenheit)

    # Made the helper function convert to celsius()
    def convert_to_celsius():
        # Returns calculated value of temperature in Celsius to convert to celsius()
        return 5 / 9 * (fahrenheit - 32)

    # Displays the temperature in Celsius and calls the function convert to celsius()
    print("The temperature in Celsius is:", convert_to_celsius())

    # Made the helper function convert to kelvin()
    def convert_to_kelvin():
        # Returns calculated value of temperature in Kelvin to convert to kelvin()
        return convert_to_celsius() + 273.15

    # Displays the temperature in Kelvin and calls the function convert to kelvin()
    print("The temperature in Kelvin is:", convert_to_kelvin())


# Calls the whole convert temp() function
convert_temp()
