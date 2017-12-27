"""
solution for day 13 part 2
"""
import re
import util

DAY13_INPUT = util.load_input('day13.input')
TEST_INPUT = [\
    '0: 3',\
    '1: 2',\
    '4: 4',\
    '6: 4']

def solve(input_data):
    """
    solve day 13 part 2
    """
    layers = []
    for line in input_data:
        data = re.split(r'[: ]', line)
        # item with (duration of scan, position)
        layers.append(((int(data[2]) - 1) * 2, int(data[0])))

    delay = 0

    # sort by duration ascending to fail faster at uncaught check
    layers = sorted(layers, key=lambda x: x[0])

    while True:
        uncaught = True
        for item in layers:
            if (item[1] + delay) % item[0] == 0:
                uncaught = False
                break
        if uncaught:
            break
        delay += 1
    return delay

print solve(TEST_INPUT)
print solve(DAY13_INPUT)
