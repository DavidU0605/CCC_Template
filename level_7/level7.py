import utils

if __name__ == "__main__":
    example = True
    lines = []
    level = 7

    if example:
        lines = utils.read_example_file(level)
        res = lines
        print(res)
    else:
        for i in range(1, 6):
            lines = utils.read_file(level, i)
            res = lines  # Do something with the lines
            utils.write_file(level, i, res)
