#First, made the function convert to days()
def convert_to_days():
    
    #Added some input boxes for hours, minutes and seconds and converts them into integers
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))

    #Made the get days() function inside the convert to days() function to return the converted value
    def get_days():
        return hours / 24 + minutes / 1440 + seconds / 86400

    #Displays the converted value
    print("")
    print("The number of days is:", round(get_days(), 4))


#Triggers the function    
convert_to_days()
