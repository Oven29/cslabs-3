from typing import List, Dict, Any, Iterator, Union


def field(items: List[Dict[str, Any]], *args: str) -> Iterator[Union[Any, Dict[str, Any]]]:
    assert len(args) > 0

    if len(args) == 1:
        key: str = args[0]
        for item in items:
            value: Any = item.get(key)
            if value is not None:
                yield value
    else:
        for item in items:
            result_dict: Dict[str, Any] = {key: item.get(key) for key in args}
            if not all(value is None for value in result_dict.values()):
                yield result_dict


def main():
    goods: List[Dict[str, Any]] = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': 'Стул', 'color': 'white'}
    ]

    print('*** field(goods, \'title\') ***')
    for item in field(goods, 'title'):
        print(item)

    print('\n*** field(goods, \'title\', \'price\') ***')
    for item in field(goods, 'title', 'price'):
        print(item)

    goods_with_none: List[Dict[str, Any]] = [
        {'title': 'Кровать', 'price': 15000},
        {'title': None, 'price': 8000},
        {'title': 'Шкаф', 'price': None}
    ]

    print('\n*** field(goods_with_none, \'title\') ***')
    for item in field(goods_with_none, 'title'):
        print(item)


if __name__ == '__main__':
    main()
