def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

def rankine_to_fahrenheit(rankine):
    fahrenheit = rankine - 459.67
    return fahrenheit

def main():
    print("..........................Selecct Temperature to Convert................................")
    print("1. Celsius (°C)")
    print("2. Kelvin (K)")
    print("3. Rankine (°R)")

    choice = int(input("Enter the scale (1/2/3): "))
    temperature = float(input("Enter the temperature: "))

    if choice == 1:
        fahrenheit = celsius_to_fahrenheit(temperature)
        scale = "Celsius"
    elif choice == 2:
        fahrenheit = kelvin_to_fahrenheit(temperature)
        scale = "Kelvin"
    elif choice == 3:
        fahrenheit = rankine_to_fahrenheit(temperature)
        scale = "Rankine"
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        return

    print(f"{temperature} {scale} is equal to {fahrenheit} Fahrenheit.")

if __name__ == "__main__":
    main()
