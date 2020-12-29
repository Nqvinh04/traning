#!/usr/bin/env python3


def solve(input):
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
    word = [i.lower() for i in input]
    sum = 0
    for w in range(len(word)):
        gt = ord(word[w]) - 96
        sum += gt
    result = int(sum)
    print(type(result))
    return result


def main():
    # words = ['numpy', 'django', 'saltstack', 'discipline',
    #          'Python', 'FAMILUG', 'pymi']
    words = ['knowledge', 'hardwork', 'discipline', 'attitude']
    list = []
    for w in words:
        list.append(solve(w))
    print(list)



if __name__ == "__main__":
    main()
