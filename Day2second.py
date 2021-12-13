horizontal = 0
depth = 0
aim = 0

# if the line starts with down x, then add x to aim
# if the line starts with up x then substract x from aim
# if the line starts with forward then add x to horizontal AND increase the depth by aim multiplied with x

# open the file Day2test.txt
with open('Day2b.txt') as f:
    for line in f:
        # if the line starts with down x, then add x to aim
        if line.startswith('down'):
            aim += int(line[4:])
        # if the line starts with up x then substract x from aim
        elif line.startswith('up'):
            aim -= int(line[3:])
        # if the line starts with forward then add x to horizontal AND increase the depth by aim multiplied with x
        elif line.startswith('forward'):
            horizontal += int(line[7:])
            depth += aim * int(line[7:])
    print(horizontal, depth)
    print(horizontal * depth)
