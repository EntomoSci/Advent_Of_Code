'''Functions of 4th day Advent Code 2021'''


def multi_array_generator(size:int) -> list:
    '''Return a empty multimensional array of the size specified by argument'''
    nd_array = list()
    i = 0
    while i < size:
        nd_array.append([])
        i += 1
    # print(nd_array)
    return nd_array 


def bingo_board_generator(file_path:str) -> list[int]:
    '''Return 5x5 2d-array with all the bingo boards'''
    boards = list()
    with open(file_path, 'r') as f:
        raw_list = f.read().split('\n') # Refactor using f.readlines() insted
    row_list = list()
    for i in range(len(raw_list)):
        line = raw_list[i].strip()
        if len(line) == 0 or \
           i == 0:
            continue
        row_list.append(line.split())
    board_list = multi_array_generator(len(row_list) / 5)
    print(board_list)
    index = 0
    for row in row_list:
        board_list[index].append(row)
        if len(board_list[index]) == 5:
            index += 1
        if index == len(board_list):
            break
    # print(f'Board  1: {board_list[0]}')
    # print(f'Board  1: {type(board_list[0][0][0])}')
    # print(f'Board  2: {board_list[1]}')
    # print(f'Board  3: {board_list[2]}') 
    # print(row_list)
    # print(board_list)
    return 0


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
