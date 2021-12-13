'''Functions to Advent Code 2021, day 5'''


def create_dots_map(x:int, y:int) -> list:
    '''Return a 2D array of "y" arrays and each array filled with "x" dots (".")'''

    dots_map = []
    i = 0
    while i < y: # Appending the rows filled with dots to the map.
        dots_map.append(['.' for j in range(x)])
        i += 1

    return dots_map
