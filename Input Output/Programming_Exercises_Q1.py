print("Enter your height.")
height_feet = int(input("Feet: "))
height_inches = int(input("Inches: "))

board_length = 0.88 * (height_feet * 30.48 + height_inches * 2.54)
print("Suggested board length:", board_length, "cm")
