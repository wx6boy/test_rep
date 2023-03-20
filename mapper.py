#! /user/bin/python3
import sys

values = []
sum = 0
for current_line in sys.stdin:
    line = current_line.strip().split(",")
    if len(line) > 8:
        price = float(line[-7])
        values.append(price)
        sum += price

dispersion = 0
avg = sum / len(values)
for current_value in values:
    dispersion += (current_value - avg) ** 2

if values:
    dispersion = dispersion / (len(values) - 1)
    print("1\t" + (str(len(values)) + "," + str(avg) + "," + str(dispersion)))

