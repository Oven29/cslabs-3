import time
from contextlib import contextmanager
from time import sleep
from typing import Iterator


class CmTimer1(object):
    def __init__(self) -> None:
        self.start_time: float = 0.0

    def __enter__(self) -> 'CmTimer1':
        self.start_time = time.time()
        return self

    def __exit__(self, *_) -> None:
        end_time: float = time.time()
        elapsed_time: float = end_time - self.start_time
        print(f'time: {elapsed_time}')


@contextmanager
def cm_timer_2() -> Iterator[None]:
    start_time: float = time.time()
    try:
        yield
    finally:
        end_time: float = time.time()
        elapsed_time: float = end_time - start_time
        print(f'time: {elapsed_time}')


def main():
    print('*** CmTimer1 (класс) ***')
    with CmTimer1():
        sleep(0.5)

    print('\n*** cm_timer_2 (contextlib) ***')
    with cm_timer_2():
        sleep(0.3)


if __name__ == '__main__':
    main()
