'''12-17-2021, AdventCode day 6 part 1 by smv7'''


def main(days:int=None) -> int:
    # Creating the initial fishs list.
    file_path = './input.txt'
    with open(file_path) as f:
        initial_fishs = [int(fish) for fish in f.readlines(1)[0].strip().split(',')]
        print(initial_fishs)

    # Processing the fishs cycle.
    day = 0
    while day < days:
        new_fish_indexes = []
        for fish_index, fish in enumerate(initial_fishs):
            if fish == 0:
                initial_fishs[fish_index] = 6
                initial_fishs.append(8)
                new_fish_indexes.append(len(initial_fishs)-1) # Add last index.
            elif (fish > 0) and (fish_index not in new_fish_indexes):
                initial_fishs[fish_index] -= 1
        day += 1
    
    # Returning the final results.
    final_result = len(initial_fishs)
    print(f'After {days} are {final_result} lanternfishs')
    return final_result


if __name__ == '__main__':
    main(80)
