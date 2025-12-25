from typing import List


def abs_key(x: int) -> int:
    return abs(x)


data: List[int] = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]


def main():
    # Без lambda
    result: List[int] = sorted(data, key=abs_key, reverse=True)
    print('Без lambda:')
    print(result)

    # lambda
    result_with_lambda: List[int] = sorted(
        data, key=lambda x: abs(x), reverse=True)
    print('\nС lambda:')
    print(result_with_lambda)


if __name__ == '__main__':
    main()
