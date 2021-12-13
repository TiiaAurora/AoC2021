from pathlib import Path
from collections import Counter
# Read the file Day3test.txt
# Find the most common character on position 0, 1, 2, 3, 4 of each line.


data = Path('Day3data.txt').read_text().splitlines()

epsilon = []
gamma = []

print(len(data[0]))

for column in range(len(data[0])):
    zero = 0
    one = 0

    for line in data:
        # print(line, column)
        if line[column] == '0':
            zero += 1
        else:
            one += 1

    if zero > one:
        gamma.append("0")
        epsilon.append("1")
    else:
        gamma.append("1")
        epsilon.append("0")

    # print(zero, one)


gammabin = ''.join(gamma)
epsilonbin = ''.join(epsilon)

print(gammabin)
print(epsilonbin)

gammadec = int(gammabin, 2)
epsilondec = int(epsilonbin, 2)

print(
    f"Gamma decimal is {gammadec}, epsilon decimal is {epsilondec}. Both combined are {gammadec * epsilondec}")

#  print(int(gamma) * int(epsilon))
