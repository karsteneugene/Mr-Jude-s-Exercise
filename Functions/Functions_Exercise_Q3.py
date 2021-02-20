#Made the function num atoms() with 2 parameters, one which is amount of element in grams and another parameter, which is optional, atmoic weight,
#which has a default value of 196.97
def num_atoms(amount_of_element, atomic_weight=196.97):
    
    #Made a variable for Avogadro's constant
    avogadro_constant = 6.022 * 10 ** 23
    
    #Returns the calculated value of the number of atoms by diving amount of element in grams with atomic weight and multiply it with the
    #Avogadro's constant
    return (amount_of_element / atomic_weight) * avogadro_constant


#Triggers the function with 10 grams of an element, and displays the calculated value
print(num_atoms(10))
