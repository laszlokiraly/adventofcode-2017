"""
solution to day 7 part 1
"""
import re
import util

class Program(object):
    """
    Program node of the tree
    """
    def __init__(self, name=None, weight=None, parent=None):
        self.name = name
        self.parent = parent
        self.programs = set()
        self.weight = weight

    def __repr__(self):
        return self.name + "(" + str(self.weight) + ")"

def build_tree(lines):
    """
    build the tree from given lines
    """
    programs = dict()
    for line in lines:
        program = Program()
        for index, part in enumerate(re.split(r'[ ]+', line)):
            if index == 0:
                if programs.get(part):
                    program = programs.get(part)
                program.name = part
                programs[part] = program
            elif index == 1:
                program.weight = int(part[1:-1])
            elif index > 2:
                subprogram_name = part.rstrip(',')
                sub_program = programs.get(subprogram_name)
                if not sub_program:
                    sub_program = Program(subprogram_name)
                sub_program.parent = program
                programs[sub_program.name] = sub_program
                program.programs.add(sub_program)
    any_program = programs.values()[0]
    root = any_program.name
    while any_program.parent:
        any_program = any_program.parent
        root = any_program.name
    return root

print build_tree(util.load_input('day7.input'))
