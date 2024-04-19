import utils
import string
import math
import re
import itertools
import operator
import functools
from random import randint
from pprint import pprint
from collections import Counter


def get_coins_old(currency, value):
    res = {}

    for i in range(1, value + 1):
        coins = [math.inf] * (value + 1)
        coins[0] = 0
        for j in range(1, i + 1):
            for coin in currency:
                if coin <= j:
                    coins[j] = min(coins[j], coins[j - coin] + 1)
        res[i] = coins[i]

    return res


from collections import Counter

def get_coins(currency, value):
    coins = {1: value}

    for coin in currency:
        for i in range(1, value + 1):
            if i - coin in coins:
                coins[i] = min(coins.get(i, math.inf), coins[i - coin] + 1)

    return " ".join([f"{coins.get(x, 0)}x{x}" for x in sorted(set(currency))])


def solve(lines):
    res = []

    # each line is a currency with coins, every line has the value one
    # generate all values from 1 to 100 for every currency with the least number of coins
    # a string in res is "1x1 2x3" where 1x1 is 1 coin of value 1 and 2x3 is 2 coins of value 3
    # each line in res is one value for one currency

    for i in range(2, len(lines), 2):
        currency = [int(x) for x in lines[i].split()]
        values = [int(x) for x in lines[i + 1].split()]
        for value in values:
            res.append(get_coins(currency, value).strip())
            pprint(res)

    return res


if __name__ == "__main__":
    example = True
    lines = []
    level = 4

    if example:
        lines = utils.read_example_file(level)
        res = solve(lines)
        print(res)
    else:
        for i in range(1, 6):
            lines = utils.read_file(level, i)
            res = solve(lines)  # Do something with the lines
            utils.write_file(level, i, res)
            print(f"-----------------------------------------------------{i}")
