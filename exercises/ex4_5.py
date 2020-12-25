#!/usr/bin/env python3


def solve(numbers):
    '''Tính tổng và tích của dãy số `numbers`

    Return một tuple (sum, product)
    Không sử dụng hàm `sum`
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    list = []
    sum = 0
    multi = 1
    for num in numbers:
        # print(type(num))
        sum += num
        multi = multi * num

    # print(sum)
    # print(multi)
    list.append(sum)
    list.append(multi)
    # result = list
    result = tuple(list)
    return result


def main():
    # Cho list numbers chứa các giá trị từ -10 đến 10, trừ số 0.
    numbers = range(-10, 11)
    numbers = list(numbers)
    numbers.remove(0)

    print(solve(numbers))


if __name__ == "__main__":
    main()
