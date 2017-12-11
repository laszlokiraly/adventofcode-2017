"""
solution for day 9
"""
import util

DAY9_INPUT = util.load_input('day9.input')

OPEN_GROUP = '{'
CLOSE_GROUP = '}'
OPEN_COMMENT = '<'
CLOSE_COMMENT = '>'
IGNORE = '!'

def solve(input_data):
    """
    solve day 9 part 1 and 2
    """
    group_depth = 0
    comment_mode = False
    ignore_next = False
    score = 0
    garbage = 0

    for char in input_data[0]:
        if ignore_next:
            ignore_next = False
            continue
        elif comment_mode:
            if char == IGNORE:
                ignore_next = True
            elif char == CLOSE_COMMENT:
                comment_mode = False
            else:
                garbage += 1
        elif char == OPEN_GROUP:
            group_depth += 1
        elif char == CLOSE_GROUP:
            score += group_depth
            group_depth -= 1
        elif char == OPEN_COMMENT:
            comment_mode = True
    return score, garbage

print('part 1: %d, part 2: %d' % solve(DAY9_INPUT))
