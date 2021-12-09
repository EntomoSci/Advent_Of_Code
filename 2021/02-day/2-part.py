'''
Multiply the final position coordinates (horizontal position and depth) of the submarine
with this new manual interpretation: A property "aim" is added now and he determinate if
"FORWARD" increases "depth" as well.
- FORWARD X:
    1. increase x the horizontal axis
    2. increase (x * aim) the submarine depth
- DOWN X: increase x the aim
- UP X: decrease x the aim
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
    horizontal_position = 0
    depth = 0
    aim = 0
    with open('./input.txt', 'r') as f:
        raw_coordinates = f.read().split('\n')
        coordinates = [tuple(coordinate.split()) for coordinate in raw_coordinates if len(coordinate) != 0]
        for type, amount in coordinates:
            amount = int(amount)
            if type == 'forward':
                horizontal_position += amount
                if aim > 0:
                    depth += (amount * aim)
            elif type == 'down':
                aim += amount
            elif type == 'up':
                aim -= amount
    print(f'Result: {horizontal_position * depth}')
    return horizontal_position * depth


if __name__ == '__main__':
    main()