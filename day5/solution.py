import re

def build_stacks(stack):
    stacks = [[] for x in range(len(stack[-1].strip().split()))]
    for stack in stack[:-1][::-1]:
        stack = stack[:-1]
        for i in range(9):
            if len(stack) < 1 + 4 * i:
                continue
            crate = stack[1 + 4 * i]

            if crate!= " ":
                stacks[i].append(crate)

    return stacks
    
def move_crate(instructions, stacks):
    for i in range(len(instructions)):
        stack_num, origin, to = re.findall(r"\d+", instructions[i])

        for i in range(0, int(stack_num)):
            stacks[(int(to)-1)].append(stacks[(int(origin)-1)].pop())

    print("".join([stack[-1] for stack in stacks])) #Part A
    return stacks

with open('input.txt') as f: 
    lines = f.read().splitlines()

    stacks = []
    instructions = []
    count = 0

    for line in lines:
        count += 1
        if line == "":
            instructions = lines[count:len(lines)]
            break
        stacks.append(line)

    built_stacks = build_stacks(stacks)
    move_crate(instructions, build_stacks(stacks))