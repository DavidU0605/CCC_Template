import utils
import string
import math
import re
import itertools
import operator
import functools
from random import randint
from pprint import pprint


def solve(lines_arr):
    result = []
    for line in lines_arr[1:]:
        nums = [int(x) for x in line.split()]
        for i in range(nums[0], nums[-1] + 1):
            if i not in nums:
                result.append(i)
                break

        result.appendnums[0] + nums[-1]


if __name__ == "__main__":
    example = True
    lines = []
    level = 1

    if example:
        lines = utils.read_example_file(level)
        res = solve(lines)
        print(res)
    else:
        for i in range(1, 6):
            lines = utils.read_file(level, i)
            res = solve(lines)  # Do something with the lines
            utils.write_file(level, i, res)
