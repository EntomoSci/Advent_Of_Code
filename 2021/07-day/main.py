'''12-22-2021, AdventCode day 7 part 1 by smv7'''


def create_dict(input: str) -> dict[int, int]:
    '''Return a dictionary with the counts of each number from input'''
    with open(input) as f:
        crab_list = f.read().split(',')
        crab_dict = {}
        for num in crab_list:
            if num not in crab_dict.keys(): # Initializing new key and counting the existing ones
                crab_dict[num] = 0
            else:
                crab_dict[num] += 1
    return crab_dict


def main():
    crab_dict = create_dict('test.txt')
    


if __name__ == '__main__':
    main()
