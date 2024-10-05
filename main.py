# Conversion factors for binary and decimal units
CONVERSION_FACTORS_BINARY = {
    "B": 1,            # Byte
    "KiB": 1024,        # Kibibyte
    "MiB": 1024**2,     # Mebibyte
    "GiB": 1024**3,     # Gibibyte
    "TiB": 1024**4,     # Tebibyte
    "PiB": 1024**5,     # Pebibyte
}

CONVERSION_FACTORS_DECIMAL = {
    "B": 1,             # Byte
    "KB": 1000,         # Kilobyte
    "MB": 1000**2,      # Megabyte
    "GB": 1000**3,      # Gigabyte
    "TB": 1000**4,      # Terabyte
    "PB": 1000**5,      # Petabyte
}

def display_menu():
    print("Binary and Decimal Unit Conversion Program")
    print("Available Units: ")
    print("1. Bytes (B)")
    print("2. Kibibytes (KiB)")
    print("3. Mebibytes (MiB)")
    print("4. Gibibytes (GiB)")
    print("5. Tebibytes (TiB)")
    print("6. Pebibytes (PiB)")
    print("7. Kilobytes (KB)")
    print("8. Megabytes (MB)")
    print("9. Gigabytes (GB)")
    print("10. Terabytes (TB)")
    print("11. Exit")

def convert_units(value, from_unit, to_unit):
    """Convert value from one unit to another, handling both binary and decimal conversions."""
    if from_unit in CONVERSION_FACTORS_BINARY:
        value_in_bytes = value * CONVERSION_FACTORS_BINARY[from_unit]
    else:
        value_in_bytes = value * CONVERSION_FACTORS_DECIMAL[from_unit]
    
    if to_unit in CONVERSION_FACTORS_BINARY:
        return value_in_bytes / CONVERSION_FACTORS_BINARY[to_unit]
    else:
        return value_in_bytes / CONVERSION_FACTORS_DECIMAL[to_unit]

def get_unit_input():
    """Get and validate user input for unit choice"""
    while True:
        try:
            unit_choice = int(input("Choose a unit (1-10): "))
            if unit_choice in range(1, 12):
                units = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "KB", "MB", "GB", "TB"]
                return units[unit_choice - 1]
            else:
                print("Invalid option. Please select between 1 and 11.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 11.")

def main():
    while True:
        display_menu()

        # Get user input for from and to units
        print("Select the unit to convert FROM:")
        from_unit = get_unit_input()

        if from_unit is None:
            continue
        
        print("Select the unit to convert TO:")
        to_unit = get_unit_input()

        # Exit option
        if from_unit == "11" or to_unit == "11":
            print("Exiting the program. Goodbye!")
            break

        try:
            value = float(input(f"Enter the amount in {from_unit}: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Perform conversion
        result = convert_units(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")
        print('')

main()