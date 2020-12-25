#!/usr/bin/env python3

'''
Input: một số nguyên trong range(1,13).
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
'''


def solve(input_data):
    '''Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February," 28)

    :param input_data: tháng bất kì
    :rtype: tuple
    '''
    # assert (input_data in range(1, 13)), "Tháng không tồn tại"
    result = None
    # li = list()
    # dic = {1: {"MONTH": "January", "DATE": 31}, 2: {"MONTH": "February", "DATE": 28}, 3: {"MONTH": "March", "DATE": 28}, 4: {"MONTH": "April", "DATE": 30},
    #         5: {"MONTH": "May", "DATE": 31}, 6: {"MONTH": "June", "DATE": 30}, 7: {"MONTH": "July", "DATE": 28}, 8: {"MONTH": "August", "DATE": 28},
    #         9: {"MONTH": "September", "DATE": 30}, 10: {"MONTH": "October", "DATE": 28}, 11: {"MONTH": "November", "DATE": 30}, 12: {"MONTH": "November", "DATE": 28}}
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # res = dic.get(input_data)
    # if not res:
    #     return ('sai', 'cmnr')
    # return res['MONTH'], res['DATE']
    # for k,v in dic.items():
    #     # print(v)
    #     for key, value in v.items():
    #         if k == input_data:
    #              li.append(value)
    #              print(value)
    # result = tuple(li)
    # print(type(result))
    # return result
    data = [("January", 31), ("February", 28), ("March", 31), ("April", 31),
            ("May", 31), ("June", 31), ("July", 31), ("August", 31),
            ("September", 31), ("October", 31), ("November", 31), ("December", 30)]

    for i in range(1, 13):
        if input_data == i:
            result = data[i - 1]
    return result


def main():
    # month, day = solve(12)
    print(solve(12))



if __name__ == "__main__":
    main()
