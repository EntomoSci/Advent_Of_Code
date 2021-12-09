'''Count the number of sonar sweep measures who are larger than the previous one.'''


def main():
    counter = 0
    with open('./input.txt', 'r') as f:
        measures_in_str = f.read().split()
        measures = [int(i) for i in measures_in_str]
        for i in range(len(measures)):
            if measures[i] > measures[i-1] and i > 0:
                counter += 1
    print(f'Measures: {counter}')
    return counter


if __name__ == '__main__':
    main()
