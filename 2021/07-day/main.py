'''12-22-2021, AdventCode day 7 part 1 by smv7'''


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


def find_duplicate_largest_values(input: dict[int, int]) -> list[int]:
    '''Return the keys on input with the highest numeric values'''
    highest_value_key = max(input, key=input.get) # Get the first highest value to compare against.
    high_value_keys = [highest_value_key]
    for key, value in input.items():
        if key != highest_value_key:
            if value == input[highest_value_key]: # Adding keys with crabs amount equal to the highest key.
                high_value_keys.append(key)
    for num in high_value_keys:
        print(input[num])
    return high_value_keys


def main():
    crab_dict = create_dict('input.txt')
    meeting_point_keys = find_duplicate_largest_values(crab_dict) # Get the meeting point number keys.
    
    # print(crab_dict)
    # print(meeting_point_keys)
    # print(f'Highest value: {max(crab_dict.values())}')
    # print(f'Max position: {max(crab_dict.keys())}')
    # print(f'Min position: {min(crab_dict.keys())}')
    # input()
    # meeting_point_key = max(crab_dict, key=crab_dict.get) 
    # print(f'Meeting point number: {meeting_point_key}')

    total_fuel_costs = [] # Contains fuel costs for several meeting points (if any).
    for index, meeting_point_key in enumerate(meeting_point_keys): # Iterate over all meeting points.
        total_fuel_costs.append(0)
        for key, amount in crab_dict.items(): # Calculate the fuel cost of crabs in current horizontal position.
            if key == meeting_point_key: # Skip the meeting point key.
                continue
            # Calculate the single fuel cost of a crab in horizontal position (key)
            # and then multiply that cost by the amount of crabs in that position (amount).
            if key > meeting_point_key:
                total_fuel_costs[index] += (key - meeting_point_key) * amount
                # result = (key - meeting_point_key) * amount
                # print(f'Calculating ({key} - {meeting_point_key}) by {amount} = {result}')
                # print(f'Total fuel cost: {total_fuel_costs}\n')
            else:
                total_fuel_costs[index] += (meeting_point_key - key) * amount
                # result = (meeting_point_key - key) * amount
                # print(f'Calculating ({meeting_point_key} - {key}) by {amount} = {result}')
                # print(f'Total fuel cost: {total_fuel_costs}\n')

    lower_fuel_cost = min(total_fuel_costs)
    print(f'Total fuel costs: {total_fuel_costs}')
    print(f'Meeting point numbers: {meeting_point_keys}')
    print(f'Lower total fuel cost: {lower_fuel_cost}')
    return lower_fuel_cost


if __name__ == '__main__':
    main()
