"""
solution for day 10 part 1
"""
import re

DAY10_INPUT = "206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3"

def solve(input_data, list_length):
    """
    solve day 10 part 1
    """
    numbers = []
    for value in range(list_length):
        numbers.append(value)
    current_position = 0
    lengths = []
    for length in re.split(r'[,]+', input_data):
        lengths.append(length)
    skip_size = 0
    for length_as_string in lengths:
        length = int(length_as_string)
        start_index = current_position
        end_index = (start_index + length - 1) % len(numbers)
        for _ in range(0, length / 2):
            numbers[start_index], numbers[end_index] = \
                numbers[end_index], numbers[start_index]
            start_index = (start_index + 1) % len(numbers)
            end_index = (end_index - 1) % len(numbers)
        current_position = (current_position + length + skip_size) % len(numbers)
        skip_size += 1
    return numbers[0], numbers[1], numbers[0] * numbers[1]

print solve('3, 4, 1, 5', 5)

print solve(DAY10_INPUT, 256)
