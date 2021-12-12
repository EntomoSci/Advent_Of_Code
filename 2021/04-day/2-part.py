'''Get the bingo board that win last'''

from modules import bingo_board_generator
from modules import get_winner_board_indexes
from functools import reduce


def main():
    file_path = './input.txt'
    boards = bingo_board_generator(file_path)
    with open(file_path) as f:
        sequence_nums = [str(num) for num in f.readlines(1)[0].strip().split(',')]
    winner_board_indexes, last_marked_number = get_winner_board_indexes(boards, sequence_nums)
    unmarked_nums = []
    marked_nums = []
    for row in boards[winner_board_indexes[-1]]:
        for num in row:
            if num[-1] != '!':
                unmarked_nums.append(int(num))
            else:
                marked_nums.append(num)
    final_result = reduce(lambda a, b: a + b, unmarked_nums) * last_marked_number[-1]
    print(f'\nLAST WINNER BOARD: {boards[winner_board_indexes[-1]]}\n')
    print(f'MARKED NUMS: {marked_nums}\n')
    print(f'UNMARKED NUMS: {unmarked_nums}\n')
    print(f'WINNER BOARD INDEXES: {winner_board_indexes}\n')
    print(f'LAST MARKED NUMBER: {last_marked_number}\n')
    print(f'FINAL SCORE BOARD: {final_result}\n')
    return final_result


if __name__ == '__main__':
    main()
