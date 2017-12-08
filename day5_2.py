"""
solution to day 5 part 2
"""

def solve(instruction_list):
    """
    solve day 5 part 2
    """
    goal = len(instruction_list)
    pointer = 0
    steps = 0
    while pointer < goal and pointer >= 0:
        offset = instruction_list[pointer]
        instruction_list[pointer] += -1 if offset >= 3 else 1
        steps += 1
        pointer += offset
    return steps

def prepare_input_test():
    """
    prepare the input for test
    """
    input_value = """0
3
0
1
-3
""".splitlines()
    return map(int, input_value)

def prepare_input():
    """
    prepare the input
    """
    with open('day5.input') as input_file:
        input_value = [x.strip('\n') for x in input_file.readlines()]
        return map(int, input_value)

print solve(prepare_input_test())

print solve(prepare_input())
