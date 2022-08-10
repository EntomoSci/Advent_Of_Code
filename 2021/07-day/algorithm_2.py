'''2022/08/09 by smv7'''


def calc_total_fuel(positions: list[int], middle: int) -> int:
    '''
    Return total fuel needed for all `positions` to go to `middle`.'''

    return sum([abs(middle-pos) for pos in positions])


if __name__ == '__main__':
    # Importing the horizontal positions.
    with open('./input.txt', 'rt') as f:
        positions: list[str] = [int(pos) for pos in f.read().split(',')]
        # print(type(positions[0]))

    # Gettings the smallest and largest positions. 
    smallest = min(positions)
    largest = max(positions)
    # print(smallest, largest)

    # Getting the middle value.
    # NOTE: The median can be calculated with module "statistics.median".
    r = sorted(positions)
    rl = len(r)
    middle = r[rl//2-1] if rl % 2 == 1 else (r[rl//2-1] + r[rl//2]) / 2
    print('Middle value:', middle)

    # Calculating total fuel needed to go to middle point.
    total_fuel = calc_total_fuel(positions, middle)
    print(f'Total fuel: {total_fuel}')

    # Brute force solution:
    # Calculating all total fuels needed for each possible position.
    cheapest = None
    for i in r:
        total = calc_total_fuel(positions, i)
        if cheapest is None:
            cheapest = i, total
        if total < cheapest[1]:
            cheapest = i, total
    print(f'Cheapest position: {cheapest[0]}')
    print(f'Cheapest fuel: {cheapest[1]}')
