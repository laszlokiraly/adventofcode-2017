"""
"""
from functools import reduce

def id(input_data):
    return reduce(lambda a, b: a+b, [str(x).zfill(2) for x in input_data])

def solve(input_data):
    """
    """
    memory_configurations = {}
    steps = 0
    while True:
        maximum_value = 0
        maximum_index = 0
        for index, value in enumerate(input_data):
            if value > maximum_value:
                maximum_value = value
                maximum_index = index
        memory_to_spend = maximum_value
        pointer = maximum_index
        memory_configurations.update({id(input_data): steps})
        input_data[pointer] = 0
        while memory_to_spend > 0:
            pointer = (pointer + 1) % len(input_data)
            input_data[pointer] += 1
            memory_to_spend -= 1
        steps += 1
        steps_first_appearance = memory_configurations.get(id(input_data))
        if steps_first_appearance:
            return ("part 1: " + str(steps), "part 2: " + str(steps - steps_first_appearance))
 
print solve([0, 2, 7, 0])
print solve([11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11])
