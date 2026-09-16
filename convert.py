def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose 1 or 2: ")

    temp = float(input("Enter the temperature: "))

    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {result:.1f}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {result:.1f}°C")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()