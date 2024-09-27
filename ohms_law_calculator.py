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