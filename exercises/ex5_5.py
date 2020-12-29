#!/usr/bin/env python3


data = ['Trang', 'Trung', 'Tien',
        'Dai', 'Duong', 'Dung', 'Hung', 'Huy', 'Hoang']

MAGIC_NUMBER = 20200000


def solve(students, N=5):
    import re
    '''Biết những bạn có tên bắt đầu bằng chữ `D` sẽ ngồi phòng thi số N,
    các bạn có tên bắt đầu chữ `H` ngồi phòng thi số N+1, và các bạn còn lại,
    nếu có tên kết thúc là `ng` sẽ ngồi cùng phòng các bạn tên `H`, còn lại
    ngồi cùng phòng `D`.
    Tất cả các học viên đều sinh năm 1990.
    Mã học viên được tính bằng: hash(NAME) % MAGIC_NUMBER
    (chú ý số này mỗi lần chạy sẽ khác nhau).
    Ví dụ: mã học viên của 'Dung' là: hash('Dung') % MAGIC_NUMBER

    Trả về result là list các tuple chứa
    (mã sinh viên, tên học viên, năm sinh, phòng thi), sắp xếp
    theo thứ tự tên học viên.
    '''

    result = []
    list = []
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")
    for i in students:
        if i.startswith('D'):
            list.append((hash(i) % MAGIC_NUMBER, i, 1990, N))
        elif i.startswith('H') or i.endswith('ng'):
            list.append((hash(i) % MAGIC_NUMBER, i, 1990, N + 1))
        else:
            list.append((hash(i) % MAGIC_NUMBER, i, 1990, N))
    # for i in list:
    #     t = tuple(i)
    #     result.append(t)
    # print(result)
    result = list
    result.sort(key=lambda tup: tup[1])
    print(result)
    return result


def main():
    students = data
    # Cho danh sách học viên students
    for msv, *ignore, room in solve(students):
        print(msv, room)
        # print("DEBUG", ignore, type(ignore), len(ignore))


if __name__ == "__main__":
    main()
