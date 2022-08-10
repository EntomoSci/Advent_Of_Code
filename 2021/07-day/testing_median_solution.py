'''12-27-2021, AdventCode day 7 part 1 by smv7'''


def create_dict(input: str) -> dict[int, int]:
    '''Return a dictionary with the counts of each number from input'''
    with open(input) as f:
        crab_list = f.read().split(',')
        crab_dict = {} # Key (Horizontal position) : Value (amount of crabs in that position).
        for num in crab_list: # Initializing new keys.
            num = int(num)
            if num not in crab_dict:
                crab_dict[num] = 0
        for num in crab_list: # Counting the existing keys.
            crab_dict[int(num)] += 1
    return crab_dict


def main():
    crab_dict = create_dict('input.txt')
    
    with open('input.txt') as f:
        raw_nums = f.read().split(',')
        nums = sorted([int(num) for num in raw_nums])
        # nums = [int(num) for num in raw_nums]
        # print(len(nums)//2)
        median = nums[(len(nums)//2) - 1]
        # if len(nums) % 2 == 0:
        #     median = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
        # else:
        #     median = nums[len(nums) // 2]
        sum
        print(median)
        print(nums[499])
        print(nums[500])
        return median

if __name__ == '__main__':
    main()
