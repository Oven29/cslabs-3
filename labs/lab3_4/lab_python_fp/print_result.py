import functools
from typing import Callable, Any, List, Dict, TypeVar

F = TypeVar('F', bound=Callable[..., Any])


def print_result(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result: Any = func(*args, **kwargs)

        print(func.__name__)

        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f'{key} = {value}')
        else:
            print(result)

        return result
    return wrapper  # type: ignore


@print_result
def test_1() -> int:
    return 1


@print_result
def test_2() -> str:
    return 'iu5'


@print_result
def test_3() -> Dict[str, int]:
    return {'a': 1, 'b': 2}


@print_result
def test_4() -> List[int]:
    return [1, 2]


def main():
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()
