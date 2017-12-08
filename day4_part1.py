"""
solution to day 4 part 1
"""
import re

def solve():
    """
    solve day 4 part 1
    """
    with open('day4.input') as input_file:
        content = [x.strip('\n') for x in input_file.readlines()]
        counter = 0
        for line in content:
            word_dict = {""}
            valid = True
            for word in re.split(r'[ ]+', line):
                if word in word_dict:
                    valid = False
                    break
                word_dict.add(word)
            counter += 1 if valid else 0
        return counter

print solve()
