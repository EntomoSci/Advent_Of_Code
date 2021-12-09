'''Functions to extract data from binary number procesing'''


def proc_bit_by_file(file_path:str) -> int:
    '''Process a file and multiply the resulting binary numbers of gama and epsilon.'''
    gamma_rate = ''
    epsilon_rate = ''
    with open(file_path, 'r') as f:
        report = f.read().split()
    num_length = len(report[0])
    index = 0
    while index < num_length:
        zero_bit_count = 0
        one_bit_count = 0
        for num in report:
            if num[index] == '0':
                zero_bit_count += 1
            elif num[index] == '1':
                one_bit_count += 1
        if zero_bit_count > one_bit_count:
            gamma_rate += '0'
            epsilon_rate += '1'
        elif zero_bit_count < one_bit_count:
            gamma_rate += '1'
            epsilon_rate += '0'
        index += 1
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def get_ox_or_co2_rating(file_path:str, mode:str) -> int:
    '''Process a file of binary numbers to get a unique decimal who match
       the bit criteria of 3th day part 2 puzzle from 'Advent Code 2021'.'''
    with open(file_path, 'r') as f:
        report = f.read().split()
    num_length = len(report[0])
    index = 0
    while index < num_length:
        zero_bit_count = 0
        one_bit_count = 0
        for num in report:
            if num[index] == '0':
                zero_bit_count += 1
            elif num[index] == '1':
                one_bit_count += 1
        if mode == 'ox_rat': # Most common bit criteria
            if (one_bit_count > zero_bit_count) or \
               (zero_bit_count == one_bit_count):
                report = list(filter(lambda x: x[index] == '1', report))
            elif (zero_bit_count > one_bit_count):
                report = list(filter(lambda x: x[index] == '0', report))
        elif mode == 'co2_rat': # Least common bit criteria
            if (one_bit_count > zero_bit_count) or \
               (zero_bit_count == one_bit_count):
                report = list(filter(lambda x: x[index] == '0', report))
            elif (zero_bit_count > one_bit_count):
                report = list(filter(lambda x: x[index] == '1', report))
        if len(report) == 1:
            if mode == 'ox_rat':
                print('Results of Oxigen Generator')
            elif mode == 'co2_rat':
                print('Results of CO2 Scrubber')
            print(f'Binary rating: {report[0]}\nDecimal rating: {int(report[0], 2)}\n')
            return int(report[0], 2)
        index += 1


def get_ox_or_co2_rating_test(lst:list, mode:str=None) -> int:
    '''Process a lst of binary numbers to get a unique decimal who match
       the bit criteria of 3th day part 2 puzzle from 'Advent Code 2021'.'''
    num_length = len(lst[0])
    index = 0
    while index < num_length:
        zero_bit_count = 0
        one_bit_count = 0
        for num in lst:
            if num[index] == '0':
                zero_bit_count += 1
            elif num[index] == '1':
                one_bit_count += 1
        if mode == 'ox_rat': # Most common bit criteria
            if (one_bit_count > zero_bit_count) or \
               (zero_bit_count == one_bit_count):
                lst = list(filter(lambda x: x[index] == '1', lst))
            elif (zero_bit_count > one_bit_count):
                lst = list(filter(lambda x: x[index] == '0', lst))
        elif mode == 'co2_rat': # Least common bit criteria
            if (one_bit_count > zero_bit_count) or \
               (zero_bit_count == one_bit_count):
                lst = list(filter(lambda x: x[index] == '0', lst))
            elif (zero_bit_count > one_bit_count):
                lst = list(filter(lambda x: x[index] == '1', lst))
        if len(lst) == 1:
            if mode == 'ox_rat':
                print('Results of Oxigen Generator')
            elif mode == 'co2_rat':
                print('Results of CO2 Scrubber')
            print(f'Binary rating: {lst[0]}\nDecimal rating: {int(lst[0], 2)}\n')
            return int(lst[0], 2)
        index += 1
