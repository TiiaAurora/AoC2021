# Position is 0, 0
# forward x = horizontal + x
# up x = depth - x
# down x = depth + x
# read instructions out of the file
# add or substract depending on the direction

# set the coordinates if horizontal (x) and depth (y) to 0, 0
horizontal = 0
depth = 0

# if line says forward x, add x to horizontal
# if line says up x, substract x from depth
# if line says down x, add x to depth

# open the file Day2test.txt and read the first line
with open('Day2b.txt') as f:
    for line in f:
        if line.startswith('forward'):
            # isolate the number in the string
            x = int(line[8:])
            horizontal += x
        elif line.startswith('up'):
            # isolate the number in the string
            x = int(line[3:])
            depth -= x
        elif line.startswith('down'):
            # isolate the number in the string
            x = int(line[5:])
            depth += x
    print(horizontal, depth)
    print(horizontal * depth)
