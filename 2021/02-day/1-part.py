'''
Multiply the final position coordinates (horizontal position and depth) of the submarine with:
- FORWARD X: increase x the horizontal axis
- DOWN X: increase x the vertical axis
- UP X: decrease x the vertical axis
'''
lst = [
    ('forward', 5),
    ('down', 5),
    ('forward', 8),
    ('up', 3),
    ('down', 8),
    ('forward', 2),
]

def main():
    x_axis = 0
    y_axis = 0
    with open('./input.txt', 'r') as f:
        raw_coordinates = f.read().split('\n')
        coordinates = [tuple(coordinate.split()) for coordinate in raw_coordinates if len(coordinate) != 0]
        for type, amount in coordinates:
            amount = int(amount)
            if type == 'forward':
                x_axis += amount
            elif type == 'down':
                y_axis += amount
            elif type == 'up':
                y_axis -= amount
    print(f'Result: {x_axis * y_axis}')
    return x_axis * y_axis


if __name__ == '__main__':
    main()

