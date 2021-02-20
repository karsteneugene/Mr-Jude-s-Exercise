# Made function calc new height()
def calc_new_height():
    # Asks the user to enter current width and height and the user's desired width in integers
    current_width = int(input("Enter the current width: "))
    current_height = int(input("Enter the current height: "))
    desired_width = int(input("Enter the desired width: "))

    # Calculates the ration
    ratio = current_height / current_width

    # Apply ratio to desired width
    return desired_width * ratio


# Triggers and displays the new height from desired width
print(calc_new_height())
