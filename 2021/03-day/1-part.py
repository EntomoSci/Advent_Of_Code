'''Calculate the gamma rate and epsilon rate of the submarine binary report'''

from modules import proc_bit_by_file as pbf
# from testing import test_list


def main():
    result = pbf('./input.txt')
    print(f'Result: {result}')
    return result


if __name__ == '__main__':
    main()
