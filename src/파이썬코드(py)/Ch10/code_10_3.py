# 노트 
# Numpy 
# 배열 : 다차원 배열, 동일한 자료형 처리 (중요함)
# 특징 : 속도가 빠르다, 행렬 연산 수행, 고차원 수학 함수 제공 
# 벡터(Vector) : 1차원 배열 
# 행렬(Metrix) : 2차원 배열 
# 텐서(Tensor) : 다차원 배열
# 차원(Axis)   : 축 (가로축, 새로축)
# axis = 0 : 행 
# axis = 1 : 열
# axis = 2 : 깊이 

# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 10.3 넘파이의 별칭 만들기, 그리고 간단한 배열 연산하기, 252쪽
#

#%%
import numpy as np

#리스트 자료형을 넘파이 배열로 변환하여  생성 

mid_scores = np.array([10, 20, 30]) 
final_scores = np.array([60, 70, 80])

#%%

#  같은 인덱스의 요소끼리 더함. 
total = mid_scores + final_scores 

print('시험성적의 합계 :', total)    # 각 요소별 합계가 나타난다

print('시험성적의 평균 :', total/2)  # 모든 요소를 2로 나눈다


#%%

# 만약 리스트인경우 

lst_scores = [10, 20, 30]
lst_final_scores = [60, 70, 80]


lst_total = lst_scores + lst_final_scores 
print(lst_total) 

# 행렬 연산을 리스트로 구현하면 코드가 길어진다. (함 만들어보자)


