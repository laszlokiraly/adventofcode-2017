"""
solution to day 7 part 2, messy & manual steps involved
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
        self.sub_programs = set()
        self.weight = weight

    def calculate_balance(self):
        """
        calculate the balance
        """
        balance = self.weight
        for sub_program in self.sub_programs:
            balance += sub_program.weight
        return balance

    def find_anomalies(self):
        """
        find programs which contain unbalanced subprograms
        """
        balance = self.weight
        first_sub_balance = -1
        count_mismatch = 0
        for sub_program in self.sub_programs:
            sub_program_balance = sub_program.find_anomalies()
            if first_sub_balance == -1:
                first_sub_balance = sub_program_balance
            if first_sub_balance != sub_program_balance:
                count_mismatch += 1
            balance += sub_program_balance
        if count_mismatch >= 1:
            print self.name + ":" + str(count_mismatch)
        return balance

    def calculate_sub_programs_balances(self):
        """
        get a representation of program and all of its sub programs
        """
        balance = self.name + ":" + str(self.weight)
        for sub_program in self.sub_programs:
            sub_program_balance = sub_program.calculate_sub_programs_balances()
            balance += " + (" + str(sub_program_balance)+ ")"
        return balance

    def __repr__(self):
        return self.name + "(" + str(self.weight) + "" + \
            " " + str(self.calculate_sub_programs_balances()) + \
            " = " + self.calculate_balance() + ")\n"

def build_tree(lines):
    """
    buid the tree
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
                program.sub_programs.add(sub_program)
    any_program = programs.values()[0]
    while any_program.parent:
        any_program = any_program.parent
    return (any_program, programs)

ROOT, PROGRAMS = build_tree(util.load_input('day7.input'))

print "part 1: %s" % ROOT.name

ROOT.find_anomalies()
print PROGRAMS['anygv'].calculate_sub_programs_balances()

# anygv:3678 +
#     (tghfe:89 +
#         (usddqi:170 + (fgokr:19) + (mdznc:19) + (psynxr:19)) +
#         (zuphhfa:199 + (pkagrvq:14) + (ospcnv:14)) +
#         (rjzbhh:91 + (sarppfb:68) + (nhyhkq:68))) + # = 770
#     (fabacam:305 +
#         (dlcxjg:17 + (mhwqim:70) + (jcrmny:70)) +
#         (dlactl:127 + (lizkruo:15) + (jkhruz:15)) +
#         (falrf:97 + (sdezdnz:20) + (zttpfsd:20) + (zfaog:20))) + # = 776 -> 770 -> 305 -> **299**
#     (ybzqi:395 +
#         (ewifyk:25 + (sxino:50) + (vgwxuan:50)) +
#         (pcfotkv:23 + (pqdoti:51) + (cszltz:51)) +
#         (uredmot:55 + (zmjzmyq:35) + (ghnldf:35)))) # = 770
# with help from
# https://www.reddit.com/r/adventofcode/comments/7i7q5l/2017_day_7_part_2_help_for_solving/,
# quote: "Following the nested towers you'll find "fabacam" to have a different total weight
#         than its neighbors (776 instead of 770)."
# since tghfe==770, ybzqi==770, but fabacam==776, subtract the 6 from fabacam's weight ->
# 305 - 6 = 299
print "part 2: %d" % 299
