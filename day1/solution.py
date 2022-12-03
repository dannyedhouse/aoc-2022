most_calories = {}

with open('input.txt') as f:
    elf_item_calories = f.read().splitlines()
    calories = 0

    for line in elf_item_calories:
        if line:
            calories += int(line)
        else:
            most_calories[len(most_calories)+1] = calories
            calories=0

print(max(most_calories.values()))
print(max(most_calories, key=most_calories.get))