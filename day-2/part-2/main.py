#!/usr/bin/python

import re

# Count the number of passwords that are valid based on the given rule
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# part 2: 1-3 means either position 1 OR position 3 has that character, 1 indexed
def is_valid(input):
    pos1, pos2, character, password = (a for a in re.split(r'-|\s|:', input) if a)
    # use XOR logic against char check
    return (password[int(pos1)-1] == character) ^ (password[int(pos2)-1] == character)
    

def main(input):
    valid = sum([is_valid(line) for line in input])
    print(f'Valid passwords: {valid}')


if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = [line.replace('\n', '') for line in f.readlines()]
    valid_input = [line for line in input if line]
    main(input=valid_input)

