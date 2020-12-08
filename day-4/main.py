#!/usr/bin/python

# Verify that all required properties are found for passport
def main(input):
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')#, 'cid' # optional)
    passports = []
    new_user = {}
    valid = 0
    for line in input:
        if not len(line):
            passports.append(new_user)
            new_user = {}
            continue

        # Split on spaces, gives K:V
        line_props = dict(l.split(':') for l in line.split(' '))
        new_user.update(line_props)

    for user in passports:
        if all(k in user for k in required_fields):
            valid+=1

    print(f'Valid passports: {valid}')

if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = [line.replace('\n', '') for line in f.readlines()]
    main(input=input)

