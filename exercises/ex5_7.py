#!/usr/bin/env python3


def solve(input_data):
    '''
    Trả về string biễu diễn tương ứng ở hệ thập phân (decimal),
    hệ nhị phân (binary), bát phân (octal), thập lục phân (heximal)

    Gợi ý: sử dụng bin(), oct(), hộ rộng là 8, các giá trị thẳng nhau căn lề phải.
    Output :ex(), string method `rjust`
    Mỗi dòng 1 số, với đ

       1       1     0o1     0x1
       2      10     0o2     0x2
       ...
    '''
    result = None
    list = []
    t = ''
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")
    for i in input_data:
        t = (str(i).rjust(8) + bin(i)[2:].rjust(8) + oct(i).rjust(8) + hex(i).rjust(8)+'\n')
        list.append(t)
    result = ''.join(list)
    return result




def main():
    input_data = range(1, 20)
    print(solve(input_data))


if __name__ == "__main__":
    main()
