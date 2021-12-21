'''12-21-2021, AdventCode day 6 part 2 (based on peer work of smv7 with hvlds :))'''


def generate_fish_dict(input: list[int]) -> dict[int, int]:
    '''Create the initial lanternfish day timers.'''

    fishs = { num: 0 for num in range(9) } # Creating all posible day timers for the lanternfishs (0-8)
    
    # Counting the amount of initial lanternfish according to the day timer
    for num in input:
        fishs[num] += 1

    return fishs


def calculate_fishs(input: list[int], days: int = 18) -> int:
    '''Return the total amount of lanternfishs after n days.'''
    
    fishs = generate_fish_dict(input)
    for _ in range(1, days + 1):
        ready_to_multiply = fishs[0]
        for timer, amount in fishs.items():
            if timer > 0: # Slide the fish timers to the left (to 0 timer)
                fishs[timer - 1] = amount
                fishs[timer] = 0
        if ready_to_multiply: # Create new fishes and reset the creators if are any fish ready
            fishs[6] += ready_to_multiply
            fishs[8] += ready_to_multiply

    return sum(fishs.values())


def main():
    with open('input.txt') as f:
        initial_state = [ int(num) for num in f.readline().split(',') ] # Getting the initial state of the fishs
        n_days = int(input('Number of days: '))
        
        return calculate_fishs(initial_state, n_days)


if __name__ == '__main__':
    print(main())
