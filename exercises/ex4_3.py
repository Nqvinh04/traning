#!/usr/bin/env python3


def solve(words):
    '''Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.
    (http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    '''
    result = None
    # import string
    # alphabet = [a for a in string.ascii_lowercase]
    # for w in range(len(alphabet)):
    #     print(alphabet.index('a') + 1)
    word = words.lower()
    sum = 0
    for w in word:
        gt = ord(w) - 96
        sum += gt
    result = sum
    return result


def main():
    words = ['numpy', 'django', 'saltstack', 'discipline',
             'Python', 'FAMILUG', 'pymi']
    list = []
    for w in words:
        list.append(solve(w))
    print(list)


if __name__ == "__main__":
    main()
