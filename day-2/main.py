#!/usr/bin/python

import re

# Count the number of passwords that are valid based on the given rule
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# where ex 1 and 3 are valid becuase there were 1-3 a characters, and 2-9 c characters
def is_valid(input):
    count_min, count_max, character, password = (a for a in re.split(r'-|\s|:', input) if a)
    # print(f'min:{count_min} max:{count_max} char:{character} pass:{password}')
    char_count = password.count(character)
    return char_count <= int(count_max) and char_count >= int(count_min)
    

def main(input):
    #valid = 0
    #for line in input:
    #    if is_valid(line):
    #        valid+=1
    valid = sum([is_valid(line) for line in input])
    print(f'Valid passwords: {valid}')


if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = [line.replace('\n', '') for line in f.readlines()]
    valid_input = [line for line in input if line]
    main(input=valid_input)

