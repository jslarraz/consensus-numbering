import os
import re
import sys


def main() -> int:
    next_number = -1

    pattern = re.compile("^SN-(\\d+)(:?-.)?$")

    for entry in os.listdir("./sn/"):
        count = int(pattern.match(entry).group(1))
        next_number = max(next_number, count)

    print(next_number + 1, file=sys.stdout)
    return next_number + 1


if __name__ == '__main__':
    main()
