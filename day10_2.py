"""
solution for day 10 part 2
"""

DAY10_INPUT = "206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3"

def convert_to_ascii(input_data):
    """
    convert input data to ascii representation
    """
    result = [ord(c) for c in input_data]
    result += [17, 31, 73, 47, 23]
    return result

def hash_knot(input_data):
    """
    for use in day 14
    """
    return solve(input_data, 256)

def solve(input_data, list_length):
    """
    solve day 10 part 2
    """
    numbers = [i for i in range(list_length)]
    current_position = 0
    lengths = convert_to_ascii(input_data)
    skip_size = 0
    for _ in range(64):
        for length_as_string in lengths:
            length = int(length_as_string)
            start_index = current_position
            end_index = (start_index + length - 1) % len(numbers)
            for _ in range(0, length / 2):
                numbers[start_index], numbers[end_index] = \
                    numbers[end_index], numbers[start_index]
                start_index = (start_index + 1) % len(numbers)
                end_index = (end_index - 1) % len(numbers)
            current_position = (current_position + length + skip_size) % len(numbers)
            skip_size += 1
    result = xor(numbers)
    return ''.join(result)

def xor(numbers):
    """
    execute xor operator on all numbers of given array in steps of 16
    """
    result = []
    for x_1 in range(16):
        xored = 0
        for x_2 in range(16):
            xored = xored ^ numbers[16*x_1+x_2]
        result.append(hex(xored)[2:].zfill(2))
    return result

def xor_test():
    """
    test the xor function
    """
    test = []
    for _ in range(16):
        test.extend([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22])
    return int(xor(test)[0], 16)

def main():
    """
    main
    """
    print "unittest convert_to_ascii('1,2,3'): %s" % convert_to_ascii('1,2,3')
    print "unittest xor(65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22): %d" % xor_test()
    print ""
    print "test \"\": %s" % solve("", 256)
    print "test \"AoC 2017\": %s" % solve("AoC 2017", 256)
    print "test \"1,2,3\": %s" % solve("1,2,3", 256)
    print "test \"1,2,4\": %s" % solve("1,2,4", 256)
    print ""
    print "DAY10_INPUT: %s" % solve(DAY10_INPUT, 256)

if __name__ == "__main__":
    main()
