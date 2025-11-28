def convert_length():
    print("Length Converter")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Meter to Centimeter")
    print("4. Foot to Meter")
    print("5. Inch to Centimeter")

    choice = int(input("Choose option: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value / 1000, "km")
    elif choice == 2:
        print("Result:", value * 1000, "m")
    elif choice == 3:
        print("Result:", value * 100, "cm")
    elif choice == 4:
        print("Result:", value * 0.3048, "m")
    elif choice == 5:
        print("Result:", value * 2.54, "cm")
    else:
        print("Invalid Option!")

def convert_mass():
    print("MASS CONVERTER")
    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")
    print("3. Kilogram to Pound")
    print("4. Pound to Kilogram")
    print("5. Ounce to Gram")

    choice = int(input("Choose option: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value * 1000, "g")
    elif choice == 2:
        print("Result:", value / 1000, "kg")
    elif choice == 3:
        print("Result:", value * 2.20462, "lbs")
    elif choice == 4:
        print("Result:", value / 2.20462, "kg")
    elif choice == 5:
        print("Result:", value * 28.3495, "g")
    else:
        print("Invalid Option!")


def convert_temperature():
    print("TEMPERATURE CONVERTER")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")

    choice = int(input("Choose option: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", (value * 9/5) + 32, "°F")
    elif choice == 2:
        print("Result:", (value - 32) * 5/9, "°C")
    elif choice == 3:
        print("Result:", value + 273.15, "K")
    elif choice == 4:
        print("Result:", value - 273.15, "°C")
    elif choice == 5:
        print("Result:", (value - 32) * 5/9 + 273.15, "K")
    else:
        print("Invalid Option!")


def convert_currency():
    print("CURRENCY CONVERTER")
    print("1. INR to USD")
    print("2. USD to INR")
    print("3. INR to EUR")
    print("4. EUR to INR")
    print("5. USD to EUR")
    
    choice = int(input("Choose option: "))
    value = float(input("Enter value: "))
    
    INR_TO_USD = 0.012
    USD_TO_INR = 83.0
    INR_TO_EUR = 0.011
    EUR_TO_INR = 89.0
    USD_TO_EUR = 0.92

    if choice == 1:
        print("Result:", value * INR_TO_USD, "USD")
    elif choice == 2:
        print("Result:", value * USD_TO_INR, "INR")
    elif choice == 3:
        print("Result:", value * INR_TO_EUR, "EUR")
    elif choice == 4:
        print("Result:", value * EUR_TO_INR, "INR")
    elif choice == 5:
        print("Result:", value * USD_TO_EUR, "EUR")
    else:
        print("Invalid Option!")

while True:
    print("UNIT CONVERTER")
    print("1. Length")
    print("2. Mass")
    print("3. Temperature")
    print("4. Currency")
    print("5. Exit")

    main_choice = int(input("Choose category: "))

    if main_choice == 1:
        convert_length()
    elif main_choice == 2:
        convert_mass()
    elif main_choice == 3:
        convert_temperature()
    elif main_choice == 4:
        convert_currency()
    elif main_choice == 5:
        print("Good-Bye!")
        break
    else:
        print("Invalid Category!")
