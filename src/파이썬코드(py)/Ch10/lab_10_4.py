#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 10-4 넘파이 배열의 형태 알아내고 슬라이싱하여 연산하기, 264쪽
#
import numpy as np 
 
x = np.array([[ 1.83, 1.76, 1.69, 1.86, 1.77, 1.73 ], 
              [ 86.0, 74.0, 59.0, 95.0, 80.0, 68.0 ]]) 
#%%
#술라이스 이용한 행,열참조 
#범위지정 : 행, 열 
#행 : 0~1
#열 : 1~2 

y = x[0:2, 1:3]   # 풀이 0행에 1~2 즉 1.76,1.69 , 1행에 1~2 74,59  
 
print(y)

#%%

x[1,3]
x[1][3]

#1행 3열 
x1 = x[1]
x2 = x1[3]


#%%
y2 = x[0:2,2]
print(y2)

#%%

z1 = x[0:2]
print(z1)

#%%
z = x[0:2][1:3]

print(z)

#%%
print('x shape :', x.shape)
print('y shape :', y.shape)
print('z shape :', z.shape)
print('z values = :', z)



bmi = x[0] / x[1]**2
print('BMI data')
print(bmi)