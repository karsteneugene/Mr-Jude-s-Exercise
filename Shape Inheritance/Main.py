from Shape import Shape
from Circle import Circle
from Rectangle import Rectangle
from Square import Square


def main():
    new_shape = Shape()  # Creates new shape
    print(new_shape.getColor())  # Prints the new shape's color
    print(new_shape.isFilled())  # Prints True or False depending on if the new shape is filled or not
    print(new_shape.toString())  # Prints a string with the color and whether if the shape is filled
    new_shape.setColor('red')  # Sets a new color for the new shape
    new_shape.setFilled(False)  # Sets filled to False on the new shape
    print(new_shape.getColor())  # Prints the new changed color of the shape
    print(new_shape.isFilled())  # Prints True or False depending on the change made with the fill
    print(new_shape.toString())  # Prints a string with the new color and fill

    print('')

    new_circle = Circle()  # Creates new circle
    print(new_circle.getColor())  # Prints the current color of the circle
    print(new_circle.isFilled())  # Prints True or False depending on if the circle is filled or not
    print(new_circle.getRadius())  # Prints the current radius of the circle
    print(new_circle.getArea())  # Prints the calculated Area with current radius
    print(new_circle.getPerimeter())  # Prints the calculated Perimeter with current radius
    print(new_circle.toString())  # Prints a string with the current radius together with the superclass string
    new_circle.setColor('blue')  # Sets a new color for the circle
    new_circle.setFilled(False)  # Sets filled to False on the circle
    new_circle.setRadius(5.0)  # Sets the new radius to 5.0
    print(new_circle.getColor())  # Prints the new color of the circle
    print(new_circle.isFilled())  # Prints True or False depending on the changed fill
    print(new_circle.getRadius())  # Prints the new radius
    print(new_circle.getArea())  # Prints the calculated Area with new radius
    print(new_circle.getPerimeter())  # Prints the calculated Perimeter with new radius
    print(new_circle.toString())  # Prints a string with new radius together with the changes in the superclass

    print('')

    new_rectangle = Rectangle()  # Creates new rectangle
    print(new_rectangle.getColor())  # Prints the current color of the rectangle
    print(new_rectangle.isFilled())  # Prints True or False depending on if the rectangle is filled or not
    print(new_rectangle.getWidth())  # Prints the current width of the rectangle
    print(new_rectangle.getLength())  # Prints the current length of the rectangle
    print(new_rectangle.getArea())  # Prints the calculated Area with current width and length
    print(new_rectangle.getPerimeter())  # Prints the calculated Perimeter with current width and length
    print(new_rectangle.toString())  # Prints a string with current width and length with superclass string
    new_rectangle.setColor('yellow')  # Sets a new color for the rectangle
    new_rectangle.setFilled(False)  # Sets filled to False on the rectangle
    new_rectangle.setWidth(2.0)  # Sets the new width to 2.0
    new_rectangle.setLength(3.0)  # Sets the new length to 3.0
    print(new_rectangle.getColor())  # Prints the new color of the rectangle
    print(new_rectangle.isFilled())  # Prints True or False depending on the changed fill
    print(new_rectangle.getWidth())  # Prints the new width
    print(new_rectangle.getLength())  # Prints the new length
    print(new_rectangle.getArea())  # Prints the calculated Area with new width and length
    print(new_rectangle.getPerimeter())  # Prints the calculated Perimeter with new width and length
    print(new_rectangle.toString())  # Prints a string with new width and length with changes in superclass

    print('')

    new_square = Square(1.0)  # Creates new square
    print(new_square.getColor())  # Prints the current color of the square
    print(new_square.isFilled())  # Prints True or False depending on if the square is filled or not
    print(new_square.getWidth())  # Prints the current width of the square
    print(new_square.getLength())  # Prints the current length of the square
    print(new_square.getSide())  # Prints the current side of the square
    print(new_square.getArea())  # Prints the calculated Area with current side
    print(new_square.getPerimeter())  # Prints the calculated Perimeter with current side
    print(new_square.toString())  # Prints a string with current side with superclass string
    new_square.setColor('white')  # Sets a new color for the square
    new_square.setFilled(False)  # Sets filled to False on the square
    new_square.setSide(4.0)  # Sets the new side to 4.0
    new_square.setWidth(4.0)  # Sets the new width to 4.0
    new_square.setLength(4.0)  # Sets the new length to 4.0
    print(new_square.getColor())  # Prints the new color of the square
    print(new_square.isFilled())  # Prints True or False depending on the changed fill
    print(new_square.getWidth())  # Prints the new width
    print(new_square.getLength())  # Prints the new length
    print(new_square.getSide())  # Prints the new side
    print(new_square.getArea())  # Prints the calculated Area with new side
    print(new_square.getPerimeter())  # Prints the calculated Perimeter with new side
    print(new_square.toString())  # Prints a string with new side with changes in superclass


if __name__ == '__main__':
    main()
