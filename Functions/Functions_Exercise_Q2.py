#Made the function calc weight on planet() with 2 parameters, one of them is "weight on earth" and the other one is an optional parameter for
#"surface gravity, which has a default value of 23.1
def calc_weight_on_planet(weight_on_earth, surface_gravity=23.1):
    
    #Calculated mass by divind "weight on earth" with the surface gravity of Earth, which is 9.8.
    mass = weight_on_earth / 9.8
    
    #Returns the value of the weight on a desired planet
    return mass * surface_gravity

#Triggers the function with a weight on Earth of 120 pounds and displays the weight on Jupiter
print(calc_weight_on_planet(120))
