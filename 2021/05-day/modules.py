'''Functions to Advent Code 2021, day 5'''


def create_dots_map(x:int, y:int) -> list:
    '''Return a 2D array of "y" arrays and each array filled with "x" dots (".")'''

    dots_map = []
    i = 0
    while i < y: # Appending the rows filled with dots to the map.
        dots_map.append(['.' for j in range(x)])
        i += 1

    return dots_map


def find_largest_coordinate(sequence: list) -> tuple:
    '''Return a tuple with the largest numbers of 'x' coordinates (index 0) and 'y' (index 1)'''
    
    largest_x = 0
    largest_y = 0
    for outer in sequence:
        for inner in outer:
            x = int(inner[0])
            y = int(inner[1])
            if x > largest_x:
                largest_x = x
            if y > largest_y:
                largest_y = y

    return (largest_x, largest_y)
