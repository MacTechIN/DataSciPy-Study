#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 10.5 강력한 넘파이 배열의 연산을 알아보자, 255쪽
#
import numpy as np 

salary = np.array([220, 250, 230])

#각 요소별 2를 곱함 (파이썬 리스트로 할경우 ? 복잡한 코드가 추가 되어야한다. while or for loop 이용  )

salary = salary * 2 
print(salary)