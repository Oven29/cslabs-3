import json
import sys
import os
from typing import List, Dict, Any, Iterable

from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import CmTimer1


def f1(arg: List[Dict[str, Any]]) -> List[str]:
    return sorted(list(Unique(field(arg, 'job-name'), ignore_case=True)), key=str.lower)


def f2(arg: List[str]) -> List[str]:
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


def f3(arg: List[str]) -> List[str]:
    return list(map(lambda x: f'{x}, с опытом Python', arg))


def f4(arg: List[str]) -> List[str]:
    num_count: int = len(arg)
    salaries: Iterable[int] = gen_random(num_count, 100000, 200000)
    return list(map(lambda x: f'{x[0]}, зарплата {x[1]} руб.', zip(arg, salaries)))


@print_result
def process_data_pipeline(data: List[Dict[str, Any]]) -> List[str]:
    return f4(f3(f2(f1(data))))


def main():
    path = os.path.join(os.path.dirname(__file__), 'data_light.json')

    data: List[Dict[str, Any]] = []
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}", file=sys.stderr)
        sys.exit(1)

    with CmTimer1():
        process_data_pipeline(data)


if __name__ == '__main__':
    main()
