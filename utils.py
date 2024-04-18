def read_example_file(level: int, skip_first: bool = True) -> list[str]:
    list_of_lines = []
    with open(f"./level{level}_example.in", 'r') as f:
        if skip_first:
            f.readline()
        for line in f:
            list_of_lines.append(line.strip())

    return list_of_lines


def read_file(level: int, stage: int, skip_first: bool = True) -> list[str]:
    list_of_lines = []
    with open(f"./level{level}_{stage}.in", 'r') as f:
        if skip_first:
            f.readline()
        for line in f:
            list_of_lines.append(line.strip())

    return list_of_lines


def write_file(level: int, stage: int, data: list[str]):
    with open(f"./level{level}_{stage}.out", 'w') as f:
        for line in data:
            f.write(line + "\n")