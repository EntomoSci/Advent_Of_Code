'''Functions of 4th day Advent Code 2021'''


def multi_array_generator(size:int) -> list:
    '''Return a empty multimensional array of the size specified by argument'''
    nd_array = list()
    i = 0
    while i < size:
        nd_array.append([])
        i += 1
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
    return board_list


def get_winner_board(tensor:list, sequence:list[str]) -> tuple:
    '''Return a tuple with the winner bingo board index and the last marked number.
       1. The function marks every number in each board from tensor present in sequence (one by one).
       2. Checks if any bingo board wins with the inner function.
       3. Repeat the process with the next sequence number until a winner bingo board is found.'''

    def locate_winner_board(tensor:list[list[list[str]]]) -> int or str:
        '''If a winner bingo board was found, return his index. Otherwise return string "Winner board not found".'''
        dimensions = {
            'x_axis': len(tensor[0][0]),
            'y_axis': len(tensor[0])
        }
        matches = 0
        for board_index, board in enumerate(tensor):  # Iterate over each bingo board in tensor.
            # Horizontal iteration on x axis in current board (regular iteration)
            for row_index, row in enumerate(board): # Iterate over each row index in current bingo board.
                for num_index, num in enumerate(row): # Iterate over each num in current row.
                    if not num[-1] == '!':
                        matches = 0
                        break
                    matches += 1
                if matches == dimensions['x_axis']: # Return the location of the winner board if all numbers in row are marked.
                    return tensor.index(tensor[board_index])
            # Vertical iteration on y axis in current board (by index)   
            x_index = 0 # Control what index to target in the board row's (horizontal position).
            y_index = 0 # Control what row to target in the board (vertical position).
            while ((x_index < dimensions['x_axis']) and (y_index < dimensions['y_axis'])): # Iterate vertically in numbers from index
                if not tensor[board_index][y_index][x_index][-1] == '!': # Go to next bingo board column if current number is not marked.
                    matches = 0
                    y_index = 0
                    x_index += 1
                    continue
                else:
                    matches += 1
                    if matches == dimensions['y_axis']: # Return the location and last marked number if all numbers in column are marked.
                        print(f'\nWINNER BOARD:\n{tensor[board_index]}')
                        return tensor.index(tensor[board_index])
                y_index += 1
        return 'Winner board not found'

    # Announce the first number in sequence, mark all numbers in all boards equal
    # to current sequence num and checks if a winner board exist after five iteration.
    # Repeat the process with each sequence number until get a winner board. 
    iterations = 0
    for seq_num in sequence: # Iterate over each num in sequence, marking each equal num in tensor.
        for board_index, board in enumerate(tensor): # Iterate over each bingo board.
            for row_index in range(len(board)): # Iterate over each row index in bingo board.
                num_index = 0
                while num_index < len(tensor[board_index][row_index]): # Iterate over each number in row, marking the
                    num = tensor[board_index][row_index][num_index]    # numbers equals to current num in sequence.
                    if num == seq_num:
                        tensor[board_index][row_index][num_index] = num + '!'
                    num_index += 1
        if iterations > 3: # After mark all numbers equals to current sequence num, checks if any board wins.
            winner_board_index = locate_winner_board(tensor)
            if not winner_board_index == 'Winner board not found':
                return (winner_board_index, int(seq_num))
        iterations += 1
    return False
