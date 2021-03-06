#!/usr/bin/env python3


def solve(text):
    '''Kiểm tra text có phải là palindrome không.

    Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
    kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
    String phải dài hơn 1 chữ cái.
    Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

    :rtype: bool
    '''
    result = True
    # result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    # letters = list(text.lower())
    # for letter in letters:
    #     if letter == letters[-1]:
    #         letters.pop(-1)
    #     else:
    #         result = False
    #         break
    # text1 = text.lower()
    text = text.strip()
    if len(text) > 1:
        result = text[::-1].lower() == text.lower()
    else:
        return False
    return result

def main():
    print(solve('Able was I ere I saw Elba'))
    print(solve('civic'))
    print(solve('Noon'))
    print(solve('Nool'))
    print(solve(''))
    print(solve('P'))
    print(solve(' P  '))
    # print(solve(' P '))


if __name__ == "__main__":
    main()
