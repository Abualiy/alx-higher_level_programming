#!/usr/bin/python3

def no_c(my_string):
    update = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            update += i
    return (update)
