#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 10-5 2차원 배열에서 특정 조건을 만족하는 행만 추출하기, 265쪽
#
import numpy as np 

#2차원배열 list 를 

players = [[170, 76.4], 
           [183, 86.2], 
           [181, 78.5], 
           [176, 80.1]] 

# Array 로
np_players = np.array(players) 

#%%

#전체
print('몸무게가 80 이상인 선수 정보')

#
print(np_players[:, 1] >= 80.0 )
print("\n")
print(np_players[ np_players[:, 1] >= 80.0 ])#players[1]

#%%

print('키가 180 이상인 선수 정보')


print(np_players[:, 0] >= 180.0 ) #players[0] 에서즈 키 기준 
print(np_players[ np_players[:, 0] >= 180.0 ]) #players[0] 에서즈 키 기준 
# 즉 
#%%

print(np_players[np.array([False, True, True, False])])

#와 같은 이야기 임. 
