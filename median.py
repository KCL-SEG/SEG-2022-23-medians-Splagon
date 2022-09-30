"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort();

median = 0;

if (len(numbers) > 0):
    midpoint = (len(numbers) + 1) / 2 - 1;
    if (len(numbers) % 2 == 1): #odd
        median = numbers[int(midpoint)]
    else:
        lowerOfMedian = numbers[int(midpoint - 0.5)]
        upperOfMedian = numbers[int(midpoint + 0.5)]
        median = (lowerOfMedian + upperOfMedian) / 2

print(median)
