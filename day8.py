"""
solution for day 8 part 1 and 2
"""
import re
from enum import Enum
from enum import unique
import sys
import util


DAY8_INPUT = util.load_input('day8.input')

@unique
class Operator(Enum):
    """
    operator enum
    """
    LT_ = '<'
    GT_ = '>'
    EQ_ = '=='
    NEQ = '!='
    LTE = '<='
    GTE = '>='

def evaluate_condition(first_value, operator, second_value):
    """
    evaluate given condition
    """
    if operator == Operator.LT_:
        return first_value < second_value
    elif operator == Operator.GT_:
        return first_value > second_value
    elif operator == Operator.EQ_:
        return first_value == second_value
    elif operator == Operator.NEQ:
        return first_value != second_value
    elif operator == Operator.LTE:
        return first_value <= second_value
    elif operator == Operator.GTE:
        return first_value >= second_value

def solve(input_data):
    """
    solve day 8 part 1 and 2
    """
    register = {}
    highest_value_ever = -sys.maxint
    for line in input_data:
        modifier = 1
        variable = None
        value = 0
        condition_variable = None
        condition_value = 0
        condition_operator = None
        for index, part in enumerate(re.split(r'[ ]+', line)):
            if index == 0:
                variable = part
                if not register.get(variable):
                    register[variable] = 0
            elif index == 1:
                if part == 'dec':
                    modifier = -1
            elif index == 2:
                value = int(part)
            elif index == 4:
                condition_variable = part
                if not register.get(condition_variable):
                    register[condition_variable] = 0
            elif index == 5:
                condition_operator = Operator(part)
            elif index == 6:
                condition_value = int(part)
                if evaluate_condition(register.get(condition_variable),\
                    condition_operator, condition_value):
                    register[variable] = \
                        register[variable] + modifier * value
                    highest_value_ever = max(register.get(variable), \
                        highest_value_ever)
    highest_value = -sys.maxint
    for value in register.values():
        highest_value = max(highest_value, value)
    return highest_value, highest_value_ever

print "part 1: %d, part 2: %d" % solve(DAY8_INPUT)
