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
    return res


if __name__ == "__main__":
    example = True
    lines = []
    level = 5

    if example:
        lines = utils.read_example_file(level)
        res = solve(lines)
        print(res)
    else:
        for i in range(1, 6):
            lines = utils.read_file(level, i)
            res = solve(lines)
            utils.write_file(level, i, res)
