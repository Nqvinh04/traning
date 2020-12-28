#!/usr/bin/env python3


data = {
    'xanh lá': '#3cba54',
    'vàng': '#f4c20d',
    'đỏ': '#db3236',
    'xanh da trời': '#4885ed',
}

def solve(colors):
    '''Ghi ra file index.html code HTML để tạo ra logo của Google với màu sắc
    chính xác.
    Biết cách để tạo chữ G màu xanh da trời dùng code HTML sau::

      <span style="color:#4885ed">G</span>

    Return list chứa các tuple, mỗi tuple  chứa chữ cái trong 'Google' và màu
    của nó.
    Gợi ý: dùng `zip`

        In [1]: list(zip(['xanh', 'do'], ['XXX', 'YYY']))
        Out[1]: [('xanh', 'XXX'), ('do', 'YYY')]
    '''

    result = []
    color = [c for c in colors.keys()]
    listColor = []
    listString = []
    # print(color)
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")
    str = 'Google'
    for i in range(len(str)):
        listString.append(str[i])
        if str[i] == 'G' or str[i] == 'g':
            listColor.append(color[-1])
        elif str[i] == 'o' and str[i + 1] == 'o':
            listColor.append(color[-3])
        elif str[i] == 'o' or str[i] == 'e':
            listColor.append(color[-2])
        elif str[i] == 'l':
            listColor.append(color[-4])

    # print(listColor)
    v = zip(listColor, listString)
    resultSet = set(v)
    result = list(resultSet)
    return result


def main():
    '''Biết mã hex của các màu trong Google logo là:
    '''
    colors = data
    print(solve(colors))


if __name__ == "__main__":
    main()
