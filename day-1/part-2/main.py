#!/usr/bin/python

# find two entries that sum to 2020 and then multiply those numbers together
def main(input):
    for i in input:
        for j in input:
            for k in input:
                if i+j+k == 2020:
                    print(f'i: {i}, j:{j}, k:{k} mult: {i*j*k}')
                    # 'clean' way would be to only iterate half way throught the list forwards
                    # and half way throught the list backwards
                    return


if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = [line.replace('\n', '') for line in f.readlines()]
    valid_ints = [int(line) for line in input if line]
    main(input=valid_ints)

