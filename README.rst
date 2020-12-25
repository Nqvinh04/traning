Exercises
==============

Hướng dẫn làm bài tập
---------------------

Tất cả bài tập phải làm vào trong thư mục [exercises], sửa trực tiếp nội dung của các file ``.py`` đã có tương ứng với bài tập cần làm.
Học xong chương 3 thì làm bài 'ex3_*.py' như ex3_1.py, ex3_2.py ...

Riêng ``ex35_*.py`` là bài làm thêm cho học viên từ buổi 3 đến
buổi 5. Khuyến khích dùng list comprehension.

Editor
^^^^^^

Cài đặt editor để mở code, sửa code, lưu code

Để chạy code, lớp sẽ dùng dòng lệnh (học viên tuỳ ý làm theo cách của mình và tự giải quyết nếu có vấn đề gì xảy ra).


Lấy code về máy
^^^^^^^^^^^^^^^^

Cài đặt git để quản lý các file code.

Chạy lệnh sau đây để clone (download) repo (thư mục) của lớp học về máy::

  git clone 
Các bước nộp bài
^^^^^^^^^^^^^^^^

**MỖI LẦN** làm bài tập (sau mỗi buổi học), làm như sau:

Vào thư mục ``training_python``, kiểm tra branch::

  cd training_python # chuyển đến training_python
  git branch

Kết quả::

  * master

Nếu không thấy kết quả có ``* master``, hãy chuyển sang branch master trước::

  git checkout master

Lấy phiên bản mới nhất của branch master từ GitLab về máy::

  git pull origin master

Tạo branch mới để nộp bài::

  git checkout -b YOURNAME_lesson

Tên hungNV, nộp bài 3::

  git checkout -b hungnv_bai3

**Branch này sẽ chứa tất cả bài tập của bài học đó (ở ví dụ này là bài 3),
chỉ tạo duy nhất 1 branch cho một bài học**.

Sau đó làm bài tập và lưu vào git như sau:

Di chuyển vào thư mục chứa bài tập::

  cd exercises

Ví dụ làm bài 3.1 sẽ sửa file::

  ex3_1.py

bằng editor đã cài.

Nội dung của file này chứa đề bài và lời giải của bài toán.
Học viên sửa nội dung trong function solve() để trả về kết quả
phù hợp, đặt `result` bằng giá trị cần tìm. Không sửa đề bài, không sửa hàm
main, không return giá trị khác `result`.

Và chạy file này với lệnh::

  python ex3_1.py  # Trên Linux/Mac, gõ python3 để đảm bảo dùng đúng phiên bản.

Học viên chạy lệnh sau (gõ y hệt, không cần sửa gì) tại thư mục `training_python` để kiểm tra xem bài làm mình đã đúng
chưa (chú ý, thư mục `training_python`, không phải `exercises`, và chắc chắn là bạn đang
dùng Python 3, không phải Python 2)::

  python3 -m unittest tests.test_ex3 -vvv

kiểm tra bài buổi 4 thì thay số 3 bằng số 4, bài 35 thì thay số 3 bằng 35 ...

hoặc lệnh sau nếu bạn thấy kết quả tương tự::

  python3 setup.py test --test-suite tests.test_ex3

Nếu đúng, output sẽ trông như sau::

  test_ex3_0 (test_ex3.TestExercise3) ... ok

Nếu có exception xảy ra hay chưa làm, kết quả sẽ như sau::

  test_ex3_0 (test_ex3.TestExercise3) ... ERROR

Nếu sai, kết quả sẽ như sau::

  test_ex3_0 (test_ex3.TestExercise3) ... FAIL

Hãy đọc chi tiết của phần output sau khi chạy câu lệnh để xem lỗi/sai gì. Kết quả khá dài, vì đây là test của tất cả các bài tập, tìm những gì mình đang làm.
Không cần quan tâm đến các bài mình chưa học.

Làm bài xong học viên lưu vào git (nhớ vào thư mục `exercises` trước khi chạy)::

  git add ex3_1.py
  git commit -m 'add - HAY NỘI DUNG TÙY Ý (e.g FIX BUG XYZ)'

Push (đẩy) bài tập lên trang GitLab::

  git push origin YOUR_BRANCH  # CHÚ Ý, phải dùng đúng tên branch của bạn, như ví dụ này là thay YOUR_BRANCH bằng hungnv_bai3

Nếu thấy thông báo như sau là đã thành công::

  ...
  Counting objects: 2, done.
  Delta compression using up to 8 threads.
  Compressing objects: 100% (2/2), done.
  Writing objects: 100% (2/2), 234 bytes | 0 bytes/s, done.
  Total 2 (delta 1), reused 0 (delta 0)
  remote:
  remote: To create a merge request for hvn_123, visit:
  remote:   https://gitlab.com/pyfml/pyfml/merge_requests/new?merge_request%5Bsource_branch%5D=hvn_123
  remote:
  To git@gitlab.com:pyfml/pyfml.git
   * [new branch]      hvn_123 -> hvn_123

Tiếp tục làm các bài tập khác, rồi add, commit, push.

**Chú ý: mọi thay đổi trên code đều thực hiện trên máy rồi push lên GitLab,
không chỉnh sửa online trên GitLab**

Mở đường dẫn ở trên để tạo Merge Request (MR)
Trong phần ``Description``, @nick_người_khác để báo cho họ.

Bấm vào ``Assignee``, chọn người sẽ review code chính cho bạn, VD trợ giảng của
khoá hoặc người cùng nhóm (sau khi đã phân nhóm).

Bấm vào ``Labels``, chọn khoá mình đang học. Nếu muốn được review bằng tiếng
Anh, chọn thêm label `EnglishReview`.

.. image:: mr.png

Bấm ``Submit merge request`` để tạo MR.

Test riêng một bài
-------------------

Từ thư mục ``training_python``, chạy::

  $ python3 -m unittest tests.test_ex4.TestExercise4.test_ex4_9
  E
  ======================================================================
  ERROR: test_ex4_9 (tests.test_ex4.TestExercise4)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "/home/hvn/me/pyfml/tests/test_ex4.py", line 207, in test_ex4_9
      self._test_all(ex4_9.solve, cases)
    File "/home/hvn/me/pyfml/tests/base.py", line 9, in _test_all
      output = func(input)
    File "/home/hvn/me/pyfml/exercises/ex4_9.py", line 12, in solve
      raise NotImplementedError("Học viên chưa làm bài này")
  NotImplementedError: Học viên chưa làm bài này

  ----------------------------------------------------------------------
  Ran 1 test in 0.000s


Debug 1 chương trình
--------------------

Thay vì chạy file python bình thường với câu lệnh::

  python filename.py

Chạy bằng câu lệnh sau để vào chế độ "debug"::

  python -m pdb filename.py

Ở đây:

- bấm ``n`` để chạy sang dòng tiếp theo (n = next)
- bấm ``l`` để hiện xem code đang ở đâu (l = list)
- gõ ``p NAME`` để in ra nội dung của tên ``NAME`` (p = print).
- gõ ``exit`` để thoát.

Ví dụ::

  $ python -m pdb foo.py
  > /home/hvn/foo.py(2)<module>()
  -> s = {"tao": 20,
  (Pdb) n
  > /home/hvn/foo.py(3)<module>()
  -> "Duy": 30,
  (Pdb) l
    1
    2  	s = {"tao": 20,
    3  ->	        "Duy": 30,
    4  	        }
    5
    6  	import logging
    7
    8  	logging.basicConfig(level=logging.DEBUG, filename='my.log')
    9  	logger = logging.getLogger('foo')
   10  	sum_  = 0
   11  	for i in ["tao", "Duy"]:
  (Pdb) n
  > /home/hvn/foo.py(6)<module>()
  -> import logging
  (Pdb) p s
  {'tao': 20, 'Duy': 30}
  (Pdb) exit


Tham khảo các lỗi hay gặp
-------------------------

:doc:`best_practices`


.. toctree::
   :caption: All Exercises Content
   :maxdepth: 2
   :glob:

   exercises/*

Bài tập làm thêm
-----------------

- ProjectEuler https://projecteuler.net/
- HackerRank https://www.hackerrank.com/domains/python/py-introduction
- 99 Problems https://wiki.python.org/moin/ProblemSets/99%20Prolog%20Problems%20Solutions
- Python koans https://github.com/gregmalcolm/python_koans
