from pathlib import Path

data = Path('Day3b.txt').read_text().splitlines()

# filter the lines for the oxygen generator

oxygenlist = list(data)

for column in range(len(data[0])):

    zero = 0
    one = 0

    for line in oxygenlist:
        # print(line, column)
        if line[column] == '0':
            zero += 1
        else:
            one += 1
    if zero == one:
        gamma = "="
        epsilon = "="
    elif zero > one:
        gamma = "0"
        epsilon = "1"
    else:
        gamma = "1"
        epsilon = "0"

    # print(gamma)

    oxygenmatches = []
    for line in oxygenlist:
        if line[column] == gamma:
            oxygenmatches.append(line)
        elif gamma == "=" and line[column] == "1":
            oxygenmatches.append(line)

    oxygenlist = oxygenmatches
    if len(oxygenlist) == 1:
        break


# Do the same with the CO shizzle

COshizzlelist = list(data)

for column in range(len(data[0])):

    zero = 0
    one = 0

    for line in COshizzlelist:
        # print(line, column)
        if line[column] == '0':
            zero += 1
        else:
            one += 1
    if zero == one:
        gamma = "="
        epsilon = "="
    elif zero > one:
        gamma = "0"
        epsilon = "1"
    else:
        gamma = "1"
        epsilon = "0"

    # print(COshizzlelist)
    # print(epsilon)

    COshizzlematches = []
    for line in COshizzlelist:
        if line[column] == epsilon:
            COshizzlematches.append(line)
        elif epsilon == "=" and line[column] == "0":
            COshizzlematches.append(line)

    COshizzlelist = COshizzlematches
    if len(COshizzlelist) == 1:
        break

oxydec = int(oxygenlist[0], 2)
COdec = int(COshizzlelist[0], 2)

print(oxygenlist)
print(COshizzlelist)

print(
    f"Oxyshmoxy is {oxydec}, COshmoxy is {COdec} and the whole Shmoxy together is {oxydec * COdec}")
