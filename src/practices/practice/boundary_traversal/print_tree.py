import sys

import sys
sys.setrecursionlimit(100000)
from collections import deque


def print_tree(arr: list):
    levels = []
    i = 0
    level = 0

    start = 0
    end = 1
    while i < len(arr):
        levels.append(arr[start:end])
        level += 1
        start = end
        end += pow(2, level)
        i = end

    print()
    first_place = 2
    level_strs = ["" for i in range(len(levels))]
    for i in range(len(levels)):
        l = levels[len(levels) - i - 1]
        str_level = " "*(first_place - 1)
        for j in l:
            str_level += (str(j) + " "*( pow(2, i+1) - 1))
        level_strs[len(levels) - i - 1] = str_level
        first_place += pow(2, i)

    for l in level_strs:
        print(l)

if __name__=="__main__":
    s=input()
    print_tree(list(map(str,s.split())))
