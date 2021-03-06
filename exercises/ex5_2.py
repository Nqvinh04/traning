#!/usr/bin/env python3

'''
Tips: dùng stdlib copy.deepcopy

In [14]: import copy

In [15]: d = [{'name': 'Dung', 'languages': ['C', 'Python']}]

In [16]: dnew = copy.deepcopy(d)

In [18]: dnew[0]['languages'].append('c')

In [19]: dnew
Out[19]: [{'languages': ['C', 'Python', 'Elixir'], 'name': 'Dung'}]

In [20]: d
Out[20]: [{'languages': ['C', 'Python'], 'name': 'Dung'}]
'''


data = [
    {"name": "Hoang",
     "phone": "0988888888",
     "languages": ["Python", "C", "SQL", "HTML", "CSS", "JavaScript",
                   "Golang"],
     },
    {"name": "Duy", "girl_friend": "Maria"},
    {"name": "Dai", "girl_friend": "Angela"},
    {"name": "Tu"},
]


def solve(last_year_daa):
    import copy
    '''
    Trả về list thông tin các học viên sau khi đã update sau 1 năm.
    Không thay đổi thông tin năm cũ.

    Biết các học viên đều học được các ngôn ngữ lập trình
    trong "languages" của học viên "Hoang".
    Sau đó "Hoang" học thêm được ngôn ngữ "Elixir", các học
    viên khác không biết ngôn ngữ này.
    "Tu" có bạn gái tên là "Do Anh".
    "Duy" chia tay bạn gái, không còn bạn gái nữa.
    '''
    result = []

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")

    last_year_daa[1]['languages'] = ["Python", "C", "SQL", "HTML", "CSS", "JavaScript",
                   "Golang"]
    last_year_daa[2]['languages'] = ["Python", "C", "SQL", "HTML", "CSS", "JavaScript",
                   "Golang"]
    last_year_daa[3]['languages'] = ["Python", "C", "SQL", "HTML", "CSS", "JavaScript",
                   "Golang"]

    # print(last_year_daa)
    # for i in range(len(last_year_daa)):
    #     if last_year_daa[i].get('name') == 'Hoang':
    #         last_year_daa[i]['languages'].append('Elixir')
    #     elif last_year_daa[i].get('name') == 'Tu':
    #         last_year_daa[i]["girl_friend"] = "Do Anh"
    #     elif last_year_daa[i].get('name') == 'Duy':
    #         last_year_daa[i].pop("girl_friend")
    # # print(last_year_daa)
    # result = last_year_daa
    #
    language = []
    for stu in data:
        if stu.get("name") == "Hoang":
            language = list(stu.get("languages"))
            stu["languages"].append("Elixir")
        else:
            stu["languages"] = language
        if stu.get("name") == "Duy":
            stu.pop("girl_friend")
        if stu.get("name") == "Tu":
            stu["girl_friend"] = "Do Anh"
    result = data
    return result



def main():
    # Cho list chứa các dictionary chứa thông tin của các học viên:
    students = data
    # In ra màn hình tên học viên kèm tên bạn gái (nếu có)

    result = solve(students)  # NOQA
    print(result)
    # In ra các thông tin đã thay đổi so với năm trước của mỗi học viên.


if __name__ == "__main__":
    main()
