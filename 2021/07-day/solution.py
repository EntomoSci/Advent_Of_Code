'''2022/10/08 by smv7

Solutions of day 7'''


import pathlib
import math
import statistics as stats


def part_1(positions: list[int]) -> int:
    '''
    Solution for day 7, part 1.
    '''
    middle = stats.median(positions)
    return sum([abs(middle-pos) for pos in positions])


def part_2(positions: list[int]) -> int:
    '''
    Solution for day 7, part 2.
    '''
    # middle = math.ceil(stats.mean(positions))
    middle = stats.mean(positions)
    return sum([sum(range(1, abs(int(middle)-pos)+1)) for pos in positions])


if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.joinpath('input.txt')
    with path.open('rt') as f:
        positions = [int(pos) for pos in f.read().split(',')]

        # positions = [16,1,2,0,4,2,7,1,2,14]
        # for i in range(min(positions), max(positions)+1):
        #     cost = sum([sum(range(1, abs(int(i)-pos)+1)) for pos in positions])# + float_part
        #     print(f'{i}: {cost}')
        # print(f'Median: {stats.median(positions)}')
        # print(f'Mean: {math.ceil(stats.mean(positions))}')

        print(f'Solution 1: {part_1(positions)}')
        print(f'Solution 2: {part_2(positions)}')

