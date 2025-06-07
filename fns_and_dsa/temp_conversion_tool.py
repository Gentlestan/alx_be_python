# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature and validate numeric input
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)

        # Prompt user for temperature unit and validate input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit not in ('C', 'F'):
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

        # Perform conversion based on unit
        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature:.2f}°F is {celsius:.2f}°C")
        else:  # unit == 'C'
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature:.2f}°C is {fahrenheit:.2f}°F")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
