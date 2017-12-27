"""
solution for day 12 part 1
"""
import re
import util

DAY12_INPUT = util.load_input('day12.input')

def visit_programs(program, programs, visited_programs):
    """
    recursively visit connected programs remembering visited programs
    """
    connected_programs = programs[program]
    for connected_program in connected_programs:
        if not visited_programs[connected_program]:
            visited_programs[connected_program] = True
            visited_programs = [x or y for x, y in \
                zip(visited_programs,\
                    visit_programs(connected_program, programs, visited_programs))]
    return visited_programs

def solve(program, input_data):
    """
    solve day 12 part 1
    """
    programs = {}
    for raw_line in input_data:
        line = re.split(r'( <-> )', raw_line)
        programs.update({int(line[0]): [int(i) for i in re.split(r',', line[2])]})

    visited_programs = [False for _ in range(len(programs.keys()))]
    visited_programs[program] = True
    visited_programs = visit_programs(program, programs, visited_programs)

    return len([x for x in visited_programs if x is True])

print solve(0, DAY12_INPUT)
