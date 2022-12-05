def get_priorities(str):
    count = 0
    for char in str:
        count += ord(char) - 38 if char.isupper() else ord(char) - 96
    return count

def part_a(lines) -> int:
    priorities = 0

    for line in lines:
        part_a = set(line[:len(line)//2])
        part_b = set(line[len(line)//2:])

        intersection = "".join(part_a.intersection(part_b))
        priorities += get_priorities(intersection)
    
    return priorities

def part_b(lines) -> int:
    badges = 0

    for i in range(0, len(lines), 3):
        group_1 = set(lines[i])
        group_2 = set(lines[i+1])    
        group_3 = set(lines[i+2])    

        intersection = "".join(group_1.intersection(group_2).intersection(group_3))
        badges += get_priorities(intersection)

    return badges

with open('input.txt') as f:
    lines = f.read().splitlines()
    print("Part A: ", part_a(lines))
    print("Part B: ", part_b(lines))