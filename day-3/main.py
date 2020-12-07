#!/usr/bin/python

# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
def main(input):
    trees_hit = 0
    index = 0
    line_length = len(input[0])
    print(f'Line Length: {line_length}')
    for line in input:
        if line[index] == '#':
            trees_hit+=1
        index += 3
        index %= line_length

    print(f'Hit {trees_hit} tree(s)')


if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = [line.replace('\n', '') for line in f.readlines()]
    valid_input = [line for line in input if line]
    main(input=valid_input)

