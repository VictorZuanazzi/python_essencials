import math

def triangle_area( base, height ):
    '''(number, number) -> number

    Return the area of a triangle with dimentions base and height.

    >>> triangle_area(10,5)
    25.0
    '''
    return base*height/2

def print_triangle_area(base, height):
    '''(number, number) -> number

    Returns and print the area of the triangle by base and height.
    
    >>> print_triangle_area(10,5)
    "The area of the triangle is 25"
    '''
    area= triangle_area(base, height)
    print ('The area of the triangle is', area)

def perimeter (side1, side2, side3):
    '''(number, number, number) -> number

    Reterun the perimeter of the triangle with sides of lenght side1, side2 and side3.

    >>> perimeter (1,2,3)
    6
    >>> perimeter (1.0,2.0,3.0)
    6.0
    '''
    return side1 + side2+ side3


def semiperimeter (side1, side2, side3):
    '''(number, number, number) -> float

    Reterun the semiperimeter of a triangle with sides of lenght side1, side2 and side3.

    >>> perimeter (1,2,3)
    3
    >>> perimeter (1.0,2.0,3.0)
    3.0
    '''
    return (perimeter(side1, side2, side3))/2

def area_hero (side1, side2, side3):
    '''(number, number, number) -> float

    Return the area of a triangle with sides of lenght side1, side2, side3.

    >>> area_hero(3,4,5)
    6.0
    >>> area_hero(10.5, 6, 9.3)
    27.731
    '''
    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi*(semi-side1)*(semi-side2)*(semi-side3))
    return area
    
