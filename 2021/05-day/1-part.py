'''12-13-2021, AdventCode day 5 part 1 by smv7'''


def main():
    file_path = './input.txt'
    vent_lines = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            coor_1, coor_2 = line.split(' -> ') # Coordinates (x1,y1) and (x2,y2)
            vent_line = (tuple(coor_1.split(',')), tuple(coor_2.split(',')))
            vent_lines.append(vent_line)
    print(vent_lines)


if __name__ == '__main__':
    main()
