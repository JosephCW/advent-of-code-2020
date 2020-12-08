#!/usr/bin/python

from math import prod

# Starting at the top-left corner of your map and following a slope of (-) 1, 1/3, 1/5, 1/7, 2?
def main(input):
    line_length = len(input[0])
    iterations = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]#down 2 over 1
    tree_hits_per_iteration = []
    for y_change, x_change in iterations:
        trees_hit = 0
        index = 0
        for i in range(len(input)):
            cl_index = i * y_change # how many lines to go down
            if cl_index >= len(input):
                break

            line = input[cl_index]
            if line[index] == '#':
                trees_hit+=1
            index += x_change
            index %= line_length

        tree_hits_per_iteration.append(trees_hit)

    print(f'Tree hits per iteration: {tree_hits_per_iteration}')
    print(f'Multiplied Tree Hits: {prod(tree_hits_per_iteration)}')


if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = [line.replace('\n', '') for line in f.readlines()]
    valid_input = [line for line in input if line]
    main(input=valid_input)

