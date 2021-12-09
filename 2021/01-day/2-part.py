'''Count the number of three-measurements window who are larger than the previous one.'''


def main():
    counter = 0
    with open('./input.txt', 'r') as f:
        measures_in_str = f.read().split()
        measures = [int(i) for i in measures_in_str]
    for i in range(len(measures)):
        if len(measures) - i == 2:
            # print(f'{measures[-2]} == {measures[i]}')
            print(counter)
            return counter
        if (measures[i] + measures[i+1] + measures[i+2]) > \
           (measures[i-1] + measures[i] + measures[i+1]):
            counter += 1


if __name__ == '__main__':
    main()
