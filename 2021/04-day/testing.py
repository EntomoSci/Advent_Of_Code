# Vertical iteration on 2D array
nums = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
# x_index = 0
# y_index = 0
# dimensions = (len(nums[0]), len(nums)) # x and y
# while (x_index < dimensions[0]) and (y_index < dimensions[1]):
#     print(nums[y_index][x_index])
#     y_index += 1
#     if y_index == len(nums):
#         y_index = 0
#         x_index += 1


def nums_in_sequence(ndarray:list[list], sequence:list[int], axis:str) -> bool:
    '''Return bool if all numbers in row or columns of ndarray are in sequence.'''
    dimensions = {
        'x_axis': len(ndarray[0]),
        'y_axis': len(ndarray)
    }
    matches = 0
    if axis == 'x': # Horizontal iteration on x axis (regular iteration)
        for arr in ndarray:
            # print(f'Matches: {matches}')
            for num in arr:
                if not num in sequence:
                    matches = 0
                    break
                matches += 1
            if matches == dimensions['x_axis'] : break
    elif axis == 'y': # Vertical iteration on y axis    
        x_index = 0
        y_index = 0
        while (x_index < dimensions['x_axis']) and (y_index < dimensions['y_axis']):
            # print(f'Current iteration: {ndarray[y_index][x_index]}')
            if not ndarray[y_index][x_index] in sequence:
                # print(f'Number {ndarray[y_index][x_index]} NOT in sequence!')
                matches = 0
                y_index = 0
                x_index += 1
                continue
            # print(f'Number {ndarray[y_index][x_index]} IN sequence!')
            # print('Before:',matches)
            y_index += 1
            matches += 1
            # print('After:',matches)
    # print(f'Matches: {matches}')
    return True if ((axis == 'x') and (matches == dimensions['x_axis'])) or \
                   ((axis == 'y') and (matches == dimensions['y_axis'])) \
                else False


seq = [2, 5, 8, 11]
print(nums_in_sequence(nums, seq, 'y'))
print('\n=============================================================\n')
seq_2 = [7, 7, 9]
print(nums_in_sequence(nums, seq_2, 'x'))
