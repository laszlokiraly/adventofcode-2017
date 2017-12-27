"""
solution for day 13
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
    solve day 13
    """
    layers = {}
    for line in input_data:
        data = re.split(r'[: ]', line)
        layers.update({int(data[0]):\
            {"scanner": 0, "direction": "down", "depth": int(data[2])}})

    position = 0
    score = 0

    while position <= max(layers.keys()):
        current_layer = layers.get(position)
        if current_layer is not None and current_layer["scanner"] == 0:
            score += position * current_layer["depth"]
        for layer in layers.items():
            scanner = layer[1]["scanner"]
            depth = layer[1]["depth"]
            if scanner == 0:
                layer[1]["direction"] = "down"
            if scanner == depth - 1:
                layer[1]["direction"] = "up"

            if layer[1]["direction"] == "up":
                layer[1]["scanner"] -= 1
            else:
                layer[1]["scanner"] += 1
        position += 1
    return score

print solve(TEST_INPUT)
print solve(DAY13_INPUT)
