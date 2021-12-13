# sum of 1,2,3 then one step down the list and sum of 2,3,4
# compare both sums increase counter by 1 and continue

increase = 0
previous_measurments = []
triplesums = []

# opening file with the "with open" function, so we don't have to close it manually
with open('Day1data.txt', 'r') as measurements:

    # reading each line with a for loop
    for measurement_text in measurements:
        measurement = int(measurement_text)

        # push this measurement onto the previous list
        previous_measurments.append(measurement)

        # if the list has 3 entries
        if len(previous_measurments) == 3:
            # do the sum
            triplesums.append(sum(previous_measurments))
            # then remove the first entry
            previous_measurments.pop(0)

print(triplesums)

# check triplesums
previous_measurment = None

for measurement in triplesums:

    print(measurement, previous_measurment)

    if previous_measurment is not None and measurement > previous_measurment:
        print("increase")
        increase += 1

    previous_measurment = measurement

# print the numbers of how many times the measurement is larger.
print(increase)
