#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 5.4 for - in 다음에는 리스트나 문자열도 올 수 있다, 119쪽
#
for i in [1, 2, 3, 4, 5]:         # in 뒤에 리스트를 넣고 끝에 :을 넣자
    print("i =", i)               # i 값을 출력해보자


for i in "Hello":                 # 끝에 :이 있어야 함
    print("i =", i)               # i 값을 출력해보자


for i in [1, 2, 3, 4, 5]:         # 1에서 5까지의 리스트
    print("9 *", i, "=", 9 * i)   # 9*i 값을 출력해보자