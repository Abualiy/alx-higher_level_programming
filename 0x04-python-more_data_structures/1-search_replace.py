#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def find(x):
        return x if x != search else replace
    return list(map(find, my_list))
