from typing import Iterator, Any, List, Set, Iterable


class Unique(object):
    def __init__(self, items: Iterable[Any], **kwargs: bool):
        self.ignore_case: bool = kwargs.get('ignore_case', False)
        self.items: Iterator[Any] = iter(items)
        self.seen: Set[Any] = set()

    def __next__(self) -> Any:
        while True:
            try:
                current_item: Any = next(self.items)
            except StopIteration:
                raise

            key: Any = current_item
            if self.ignore_case and isinstance(current_item, str):
                key = current_item.lower()

            if key not in self.seen:
                self.seen.add(key)
                return current_item

    def __iter__(self) -> 'Unique':
        return self


def main():
    from gen_random import gen_random

    data_int: List[int] = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    print('*** Unique(data_int) ***')
    print(list(Unique(data_int)))

    data_gen: Iterator[int] = gen_random(10, 1, 3)
    print('\n*** Unique(gen_random(10, 1, 3)) ***')
    print(list(Unique(data_gen)))

    data_str: List[str] = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    print('\n*** Unique(data_str) ***')
    print(list(Unique(data_str)))

    print('\n*** Unique(data_str, ignore_case=True) ***')
    print(list(Unique(data_str, ignore_case=True)))


if __name__ == '__main__':
    main()
