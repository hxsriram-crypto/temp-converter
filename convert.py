def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose 1 or 2: ")
    while choice not in ("1", "2"):
        choice = input("Invalid choice. Please enter 1 or 2: ")

    try:
        temp = float(input("Enter the temperature: "))
    except ValueError:
        print("Invalid temperature. Please enter a number.")
        return

    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {result:.1f}°F")
    else:
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {result:.1f}°C")

if __name__ == "__main__":
    main()