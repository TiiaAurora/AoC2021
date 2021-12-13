# Take the list of numbers from Day1.txt and compare each row with the next row and increase the counter "increase" to 1 if the number in the next row is larger.

increase = 0
previous_measurment = None

# opening file with the "with open" function, so we don't have to close it manually
with open('Day1data.txt', 'r') as measurements:

    # reading each line with a for loop
    for measurement_text in measurements:
        measurement = int(measurement_text)

        # compare mesasuremenent to previous
        if previous_measurment is not None and measurement > previous_measurment:
            increase += 1

        previous_measurment = measurement

# print the numbers of how many times the measurement is larger.
print(increase)
