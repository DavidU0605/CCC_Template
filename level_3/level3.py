import utils
import string
import math
import re
import itertools
import operator
import functools
from random import randint
from pprint import pprint

def get_coins(currency, value):
    # get the least number of coins to make up the value

    # create a list of the number of coins for each value from 1 to value
    coins = [0] + [math.inf] * value
    for i in range(1, value + 1):
        for j in currency:
            if j <= i:
                coins[i] = min(coins[i], coins[i - j] + 1)

    # get the coins used
    res = []
    i = value
    while i > 0:
        for j in currency:
            if j <= i and coins[i] == coins[i - j] + 1:
                res.append(j)
                i -= j
                break


    values  = []

    pprint(res)

    # for each arr in res, print the amount of the distinct values in tgat array
    for line in res:
        values_in_line = {}
        print(line)

        pprint(values_in_line)

    return " ".join([f"{res.count(x)}x{x}" for x in sorted(set(res))])




def solve(lines):
    res = []

    # each line is a currency with coins, every line has the value one
    # generate all values from 1 to 100 for every currency with the least number of coins
    # a string in res is "1x1 2x3" where 1x1 is 1 coin of value 1 and 2x3 is 2 coins of value 3
    # each line in res is one value for one currency

    for i in range(1, len(lines)):
        currency = [int(x) for x in lines[i].split()]
        for j in range(1, 101):
            if j in currency:
                res.append(f"1x{j}")
            else:
                res.append(get_coins(currency, j).strip())

    return res

if __name__ == "__main__":
    example = False
    lines = []
    level = 3

    if example:
        lines = utils.read_example_file(level)
        res = solve(lines)
        pprint(res)
        # check if
    else:
        for i in range(1, 6):
            lines = utils.read_file(level, i)
            res = solve(lines)  # Do something with the lines
            utils.write_file(level, i, res)
