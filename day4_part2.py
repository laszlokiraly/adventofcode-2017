"""
solution to day 4 part 2
"""
import re
from collections import Counter

def solve():
    """
    solve day 4 part 2
    """
    with open('day4.input') as input_file:
        content_lines = [x.strip('\n') for x in input_file.readlines()]
        count = 0
        for line in content_lines:
            word_list = []
            valid = True
            for word in re.split(r'[ ]+', line):
                next_word_counter = Counter(word)
                for word_counter in word_list:
                    if word_counter == next_word_counter:
                        valid = False
                        break
                if not valid:
                    break
                word_list.append(next_word_counter)
            count += 1 if valid else 0
        print count

solve()
