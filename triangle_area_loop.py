import math
import triangle_area

def triangle_area_loop():
    '''() -> number

    Return the area of a triangle with dimentions base and height given by the user.

    '''
    base = int(input("enter the triangle's base: "))
    height = int(input("enter the triangle's height: "))

    area = triangle_area.triangle_area(base, height)
    return area
