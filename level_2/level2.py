import utils
import string
import math
import re
import itertools
import operator
import functools
from random import randint
from pprint import pprint

def solve(lines):
    res = []
    # Get two lines at once
    for i in range(2, len(lines), 2):

        a = [int(x) for x in lines[i].split()]
        b = [int(x) for x in lines[i + 1].split()]

        # With the coins in a, construct the values in b with exactly two coins
        # Add the two coins as a string "coin1 coin2" to the res

        for x in b:
            for y in a:
                if x - y in a:
                    res.append(f"{y} {x - y}")
                    break


    return res

if __name__ == "__main__":
    example = False
    lines = []
    level = 2

    if example:
        lines = utils.read_example_file(level)
        res = solve(lines)
        print(res)
    else:
        for i in range(1, 6):
            lines = utils.read_file(level, i)
            res = solve(lines)  # Do something with the lines
            utils.write_file(level, i, res)
