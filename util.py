"""
utility helper
"""

def load_input(filename):
    """
    load the input
    """
    with open(filename) as input_file:
        return [x.strip('\n') for x in input_file.readlines()]
