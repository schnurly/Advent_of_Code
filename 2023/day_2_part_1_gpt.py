def is_possible(game, red_count, green_count, blue_count):
    counts = {'red': 0, 'green': 0, 'blue': 0}

    for subset in game:
        for cube in subset:
            color = cube.split()[1]
            counts[color] += 1

    return counts['red'] <= red_count and counts['green'] <= green_count and counts['blue'] <= blue_count

def possible_games( red_count, green_count, blue_count):
    possible_sum = 0

    with open("C:\\temp\\Advent_of_Code\\2023\\02_input.txt.sample","r") as file:
        for line in file:
            parts = line.split(':')
            game_id = int(parts[0].split()[1])
            subsets = [part.strip().split(', ') for part in parts[1].strip().split(';')]
            game = subsets

            if is_possible(game, red_count, green_count, blue_count):
                possible_sum += game_id

    return possible_sum



red_count = 12
green_count = 13
blue_count = 14

result = possible_games( red_count, green_count, blue_count)
print(result)
