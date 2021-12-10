'''Get the bingo board that win first'''


from modules import bingo_board_generator as bbg
from modules import get_winner_board as gwb


def main():
    file_path = './input_tiny.txt'
    boards = bbg(file_path)
    with open(file_path) as f:
        numbers = [str(num) for num in f.readlines(1)[0].strip().split(',')]
        # print(numbers)
        # print(type(numbers))
    result = gwb(boards, numbers)
    print(result)
    # print(boards[0][0][0])
    # print(boards[0][0][0][0])


if __name__ == '__main__':
    main()
