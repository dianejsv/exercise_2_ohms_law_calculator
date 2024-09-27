# State the program
print("Ohm's Law Calculator")
# Provide the program's functions
print("What would you like to calculate?")
print("1. Current (I)\n2. Voltage (V)\n3. Resistance (R)")

# Ask the user to choose what to calculate
choice = input("\nEnter the letter you want to calculate (I, V, or R): ").strip().upper()

# Calculate Voltage if user entered 'V'
if choice == "V":
    current = float(input("Enter the current (I) in amperes: "))
    resistance = float(input("Enter the resistance (R) in ohms: "))
    voltage = current * resistance  # Calculate the voltage using Ohm's Law: V = I * R
    print(f"Voltage (V) = {round(voltage, 2)} volts")

# Calculate Current if user entered 'I'
elif choice == "I":
    voltage = float(input("Enter the voltage (V) in volts: "))
    resistance = float(input("Enter the resistance (R) in ohms: "))
    if resistance == 0:  # Check for division by zero
        print("\n\033[0;31mResistance cannot be zero. Division by zero error.\033[0m")
    else:
        current = voltage / resistance
        print(f"Current (I) = {round(current, 2)} amperes")

# Calculate Resistance if user entered 'R'
elif choice == "R":
    voltage = float(input("Enter the voltage (V) in volts: "))
    current = float(input("Enter the current (I) in amperes: "))
    if current == 0:  # Check for division by zero
        print("\n\033[0;31mCurrent cannot be zero. Division by zero error.\033[0m")
    else:
        resistance = voltage / current
        print(f"Resistance (R) = {round(resistance, 2)} ohms")
# Handle invalid choice with an error message
else:
    print("Invalid choice. Please enter 'I', 'V', or 'R'.")
