'''
Calculate the life support rating multiplying this two ratings:
    1. Oxigen generator rating:
        - Extract the most common bit by index calculations (1 if equals)
        - Conserve only the binary numbers with the returned bit in that position
        - Repeat the process until there is only one binary number left
        - That number is the Oxigen generator rating
    2. CO2 scrubber rating:
        - Extract the least common bit by index calculations (0 if equals)
        - Conserve only the binary numbers with the returned bit in that position
        - Repeat the process until there is only one binary number left
        - That number is the CO2 scrubber rating
'''

from modules import get_ox_or_co2_rating as gr
# from modules import get_ox_or_co2_rating_test as grt
# from testing import test_list


def main():
    # result = grt(test_list, 'ox_rat') * grt(test_list, 'co2_rat')
    result = gr('./input.txt', 'ox_rat') * gr('./input.txt', 'co2_rat')
    print(f'Result: {result}')
    return result
    

if __name__ == '__main__':
    main()
