'''Get the bingo board that win first'''


from modules import multi_array_generator as mag
from modules import bingo_board_generator as bbg
from modules import nums_in_sequence as ninseq


def main():
    file_path = './test.txt'
    with open(file_path) as f:
        numbers = [str(num) for num in f.readlines(1)[0].strip().split(',')]
        # print(numbers)
        # print(type(numbers))
    boards = bbg(file_path)



if __name__ == '__main__':
    main()
