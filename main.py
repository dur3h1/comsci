def display_menu():
    print("Binary Unit Conversion Program")
    print("1. Convert Mebibyte to Kibibyte")
    print("2. Convert Mebibyte to Byte")
    print("3. Convert Mebibyte to Gibibyte")
    print("4. Exit")

def convert_mebibyte_to_kibibyte(mebibyte):
    return mebibyte * 1024

def convert_mebibyte_to_byte(mebibyte):
    return mebibyte * 1024 * 1024

def convert_mebibyte_to_gibibyte(mebibyte):
    return mebibyte / 1024

def main():
    while True:
        display_menu()
        
        # Get user input and validate it
        try:
            choice = int(input("Please select an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        # if user input is 4 then we end the program
        if choice == 4:
            print("Exiting the program. Goodbye!")
            break
        
        try:
            mebibyte = float(input("Enter the amount in Mebibyte: "))
        except ValueError:
            print("Invalid input. Please enter a valid number for Mebibytes.")
            continue

        if choice == 1:
            result = convert_mebibyte_to_kibibyte(mebibyte)
            print(f"{mebibyte} Mebibyte = {result} Kibibytes")
        elif choice == 2:
            result = convert_mebibyte_to_byte(mebibyte)
            print(f"{mebibyte} Mebibyte = {result} Bytes")
        elif choice == 3:
            result = convert_mebibyte_to_gibibyte(mebibyte)
            print(f"{mebibyte} Mebibyte = {result} Gibibytes")
        else:
            print("Invalid option. Please select between 1 and 4.")

main()