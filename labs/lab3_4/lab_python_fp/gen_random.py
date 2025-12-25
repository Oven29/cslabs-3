import random
from typing import Iterator


def gen_random(num_count: int, begin: int, end: int) -> Iterator[int]:
    for _ in range(num_count):
        yield random.randint(begin, end)


def main():
    print('*** gen_random(5, 1, 3) ***')
    result = list(gen_random(5, 1, 3))
    print(result)


if __name__ == '__main__':
    main()
