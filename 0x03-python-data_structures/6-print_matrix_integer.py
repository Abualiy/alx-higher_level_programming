#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in i:
            if x == i[-1]:
                print('{:d}'.format(x), end='')
            else:
                print('{:d}'.format(x), end=' ')
        print()
