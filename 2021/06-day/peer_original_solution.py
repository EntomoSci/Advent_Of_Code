def generate_fish_dict(input: list[int]) -> dict[int, int]:
    fish_dict: dict[int, int] = {num: 0 for num in range(9)}
    for num in input:
        fish_dict[num] += 1
    return fish_dict


def part_one(input: list[int], days: int = 18) -> int:
    fish_dict = generate_fish_dict(input)
    print(f"Initial state: {fish_dict}")
    for day in range(1, days + 1):
        original_0 = fish_dict[0]
        for index, age in fish_dict.items():
            if index != 0:
                fish_dict[index - 1] = age
                fish_dict[index] = 0

        fish_dict[6] += original_0
        fish_dict[8] += original_0

        print(f'After {day} {"days" if day > 0 else "day"}: {fish_dict}')

    return sum(fish_dict.values())


if __name__ == "__main__":
    with open("input.txt") as f:
        raw_input: str = f.readline()
        input = [int(num) for num in raw_input.split(",")]
        print(part_one(input, 256))
