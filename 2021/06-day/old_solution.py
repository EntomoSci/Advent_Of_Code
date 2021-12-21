'''12-17-2021, AdventCode day 6 by smv7'''


def main(days:int=None) -> int:
    # Creating the initial fishs list.
    file_path = './input.txt'
    with open(file_path) as f:
        initial_fishs = [int(fish) for fish in f.readlines(1)[0].strip().split(',')]

    # Processing the fishs cycle.
    day = 0
    while day < days:
        new_fish_index = None
        for fish_index, fish in enumerate(initial_fishs):
            if fish == 0:
                initial_fishs[fish_index] = 6
                initial_fishs.append(8)
                if new_fish_index == None:
                    new_fish_index = len(initial_fishs) - 1 # First new fish index.
            elif fish_index == new_fish_index: # Skip fishes spawned in the same day.
                break
            else:
                initial_fishs[fish_index] -= 1
        day += 1
    
    # Returning the final results.
    final_result = len(initial_fishs)
    print(f'After {days} days are {final_result} lanternfishs')
    return final_result


if __name__ == '__main__':
    main(80)
