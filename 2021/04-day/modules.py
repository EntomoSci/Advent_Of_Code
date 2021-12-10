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


def bingo_board_generator(file_path:str) -> list[list[list[str]]]:
    '''Return 5x5 2d-array with all the bingo boards'''
    with open(file_path, 'r') as f:
        raw_list = f.read().split('\n') # Refactor using f.readlines() insted.
    row_list = list()
    for i in range(len(raw_list)): # Fill a 2D array with all bingo board rows (list of 5 numbers by row).
        line = raw_list[i].strip()
        if len(line) == 0 or \
           i == 0:
            continue
        row_list.append(line.split())
    board_list = multi_array_generator(len(row_list) / 5) # Create a empty 2D array with the same lenght as the amount of bingo boards.
    index = 0
    for row in row_list: # Fill each list of the empty 2D array of bingo boards with 5 rows (5 number list).
        board_list[index].append(row)
        if len(board_list[index]) == 5: # When current bingo board is a 5x5 array, go to the next board.
            index += 1
        if index == len(board_list):
            break
    # print(f'Board  1: {board_list[0]}')
    # print(f'Board  1: {type(board_list[0][0][0])}')
    # print(f'Board  2: {board_list[1]}')
    # print(f'Board  3: {board_list[2]}') 
    # print(row_list)
    # print(board_list)
    return board_list


# def locate_winner_board(tensor:list[list[list[str]]]) -> int or bool:
#     '''If a winner bingo board was found, return his index. Otherwise return bool 'False'.'''
#     dimensions = {
#         'x_axis': len(tensor[0]),
#         'y_axis': len(tensor)
#     }
#     print('X axis: ',dimensions['x_axis'])
#     print('Y axis: ',dimensions['y_axis'])
#     input('Enter to continue')
#     matches = 0
#     for board_index, board in enumerate(tensor):  # Iterate over each bingo board in tensor.
#         # Horizontal iteration on x axis in current board (regular iteration)
#         for row in enumerate(board): # Iterate over each row index in current bingo board.
#             # print(f'Matches: {matches}')
#             for num in enumerate(row): # Iterate over each num in current row.
#                 if not num[-1] == '!':
#                     matches = 0
#                     break
#                 matches += 1
#             if matches == dimensions['x_axis']: # Return the location of the winner board if all numbers in row are marked.
#                 print(tensor[board_index])
#                 return tensor.index(tensor[board_index])
#         # Vertical iteration on y axis in current board (by index)   
#         x_index = 0 # Control what index to target in the board row's (horizontal position).
#         y_index = 0 # Control what row to target in the board (vertical position).
#         while (x_index < dimensions['x_axis']) and (y_index < dimensions['y_axis']): # Iterate vertically in numbers from index
#             for num_index, num in enumerate(tensor[board_index][y_index][x_index]):
#                 # print(f'Current iteration: {tensor[y_index][x_index]}')
#                 if not tensor[board_index][y_index][x_index][num_index][-1] == '!': # Go to next bingo board column if current number is not marked.
#                     matches = 0
#                     y_index = 0
#                     x_index += 1
#                     continue
#                 # print(f'Number {tensor[y_index][x_index]} IN sequence!')
#                 # print('Before:',matches)
#                 y_index += 1
#                 matches += 1
#                 if matches == dimensions['y_axis']: # Return the location of the winner board if all numbers in column are marked.
#                     print(tensor[board_index])
#                     return tensor.index(tensor[board_index])
#     return False


def get_winner_board(tensor:list, sequence:list[str]) -> list[str]:
    '''Return the winner bingo board index. First the function marks every number
       from tensor present in sequence (analyzed linerly) and finally checks if any
       bingo board wins.'''
    
    
    def locate_winner_board(tensor:list[list[list[str]]]) -> int or bool:
        '''If a winner bingo board was found, return his index. Otherwise return bool 'False'.'''
        dimensions = {
            'x_axis': len(tensor[0][0]),
            'y_axis': len(tensor[0])
        }
        # print('X axis: ',dimensions['x_axis'])
        # print('Y axis: ',dimensions['y_axis'])
        # input('Enter to continue')
        print('==================BEGIN TO LOCATE WINNER BOARD==================')
        matches = 0
        for board_index, board in enumerate(tensor):  # Iterate over each bingo board in tensor.
            # Horizontal iteration on x axis in current board (regular iteration)
            for row in enumerate(board): # Iterate over each row index in current bingo board.
                # print(f'Matches: {matches}')
                for num in enumerate(row): # Iterate over each num in current row.
                    if not num[-1] == '!':
                        matches = 0
                        break
                    matches += 1
                if matches == dimensions['x_axis']: # Return the location of the winner board if all numbers in row are marked.
                    print(tensor[board_index])
                    return tensor.index(tensor[board_index])
            # Vertical iteration on y axis in current board (by index)   
            x_index = 0 # Control what index to target in the board row's (horizontal position).
            y_index = 0 # Control what row to target in the board (vertical position).
            while (x_index < dimensions['x_axis']) and (y_index < dimensions['y_axis']): # Iterate vertically in numbers from index
                print(f'======================== BEGIN VERTICAL ITERATION {x_index} =========================')
                for num in tensor[board_index][y_index]:
                    # print(f'Current iteration: {tensor[y_index][x_index]}')
                    print(f'=============== {tensor[board_index][y_index][x_index]} ==============')
                    if not tensor[board_index][y_index][x_index][-1] == '!': # Go to next bingo board column if current number is not marked.
                        matches = 0
                        y_index = 0
                        x_index += 1
                        continue
                    # print(f'Number {tensor[y_index][x_index]} IN sequence!')
                    # print('Before:',matches)
                    y_index += 1
                    matches += 1
                    if matches == dimensions['y_axis']: # Return the location of the winner board if all numbers in column are marked.
                        print(tensor[board_index])
                        return tensor.index(tensor[board_index])
        return False


    # Begin to mark the announced numbers from sequence
    iterations = 0
    result = None
    for seq_num in sequence: # Iterate over each num in sequence, marking each equal num in tensor
        seq_num = str(seq_num)
        # print(seq_num)
        for board_index, board in enumerate(tensor): # Iterate over each bingo board.
            for row_index in range(len(board)): # Iterate over each row index in bingo board.
                num_index = 0
                while num_index < len(tensor[board_index][row_index]): # Iterate over each number in row, marking the numbers equals to current num in sequence.
                    num = str(tensor[board_index][row_index][num_index])
                    print(num)
                    if num == seq_num:
                        tensor[board_index][row_index][num_index] = num + '!'
                        print(tensor[board_index][row_index][num_index])
                    num_index += 1
        if iterations > 4: # After mark all numbers equals to current sequence num, checks if any board wins.
            result = locate_winner_board(tensor)
            if result:
                return result
        iterations += 1
    return False
