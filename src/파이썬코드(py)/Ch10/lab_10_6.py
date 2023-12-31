#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 10-6 평균과 중앙값 계산하기, 273쪽
#
import numpy as np 

# 행열(100*3)  을 전체를 0으로 체운다 
players = np.zeros( (100, 3) ) 


players[:, 0] = 10 * np.random.randn(100) + 175 
players[:, 1] = 10 * np.random.randn(100) + 70
players[:, 2] = np.floor(10 * np.random.randn(100)) + 22

heights = players[:, 0] 
print('신장 평균값:', np.mean(heights))
print('신장 중앙값:', np.median(heights))

weights = players[:, 1] 
print('체중 평균값:', np.mean(weights))
print('체중 중앙값:', np.median(weights))

ages = players[:, 2] 
print('나이 평균값:', np.mean(ages))
print('나이 중앙값:', np.median(ages))


#%%
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.random.randn(100) # 표준정규분포 범위 난수 생성 

ypoints = np.random.randn(100) / xpoints

plt.plot( xpoints,ypoints )
plt.show()


