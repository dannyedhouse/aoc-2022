def check_fully_contains(s1, s2) -> bool:
    return int(s1[0]) <= int(s2[0]) and int(s1[1]) >= int(s2[1]) or int(s1[0]) >= int(s2[0]) and int(s1[1]) <= int(s2[1])

def check_overlaps(s1, s2) -> bool:
    return int(s2[0]) <= int(s1[0]) <= int(s2[1]) or int(s1[0]) <= int(s2[0]) <= int(s1[1])

with open('input.txt') as f: 
    lines = f.read().splitlines()
    section_count = 0
    overlap_count = 0
    
    for line in lines:
        sections = line.split(',')
        s1 = sections[0].split('-')
        s2 = sections[1].split('-')

        if check_fully_contains(s1, s2):
            section_count += 1

        if check_overlaps(s1, s2):
            overlap_count += 1

    print("Part A: ", section_count)
    print("Part B: ", overlap_count)