"""
solution for day 12 part 2
"""
import re
import util

DAY12_INPUT = util.load_input('day12.input')

def visit_programs(program, program_dict, visited_programs):
    """
    recursively visit connected programs remembering visited programs
    """
    connected_programs = program_dict[program]
    for connected_program in connected_programs:
        if not visited_programs[connected_program]:
            visited_programs[connected_program] = True
            visited_programs = zip_or(
                visited_programs,
                visit_programs(connected_program, program_dict, visited_programs))
    return visited_programs

def zip_or(visited_programs_1, visited_programs_2):
    """
    item wise or operation on two lists
    """
    return [x or y for x, y in zip(visited_programs_1, visited_programs_2)]

def solve(program, input_data):
    """
    solve day 12 part 2
    """
    programs = {}
    for raw_line in input_data:
        line = re.split(r'( <-> )', raw_line)
        programs.update({int(line[0]): [int(i) for i in re.split(r',', line[2])]})

    visited_programs = [False for _ in range(len(programs.keys()))]
    groups = 0
    next_program = program
    while next_program is not None:
        groups += 1
        visited_programs[next_program] = True
        visited_programs = zip_or(
            visited_programs,
            visit_programs(next_program, programs, visited_programs))
        try:
            next_program = visited_programs.index(False)
        except ValueError:
            next_program = None
    return groups

print solve(0, DAY12_INPUT)
