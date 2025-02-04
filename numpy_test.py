import numpy as np
# CRUD

# CREATE
# 1번째 방법) 기본 배열 생성
arr = np.array([1, 2, 3])  # 1차원 배열
print(arr)

arr = np.array([1.1, 2, 3])  # 1차원 배열 (실수 포함)
print(arr)
print(type(arr))  # 배열의 타입 확인
print(arr.dtype)  # 배열의 데이터 타입 확인

# 2차원 배열 생성
arr = np.array([[1, 2, 3], [4, 5, 6]])  # 2행 3열
print(arr)
print(arr.shape)  # (2,3) 형태의 배열
print(arr.ndim)  # 배열의 차원 (2차원)

# 3차원 배열 생성 (1x1x1 구조)
arr = np.array([[[1]]])
print(arr)
print(arr.shape)  # 배열의 차원 확인

# 2번째 방법) 기본값이 있는 배열 만들기
arr = np.zeros(10, dtype=np.int32)  # 최소값 -21억 최대값 21억
print(arr)

arr = np.zeros((2, 5))  # 2행 5열 # 기본형을 실수로 해서 방을 잡음
print(arr)  # 0.0

arr = np.ones(10, dtype=np.int32)  # 최소값 -21억 최대값 21억
print(arr)

arr = np.ones((3, 3))  # 3x3 배열, 기본값이 1인 배열 생성
print(arr)

# 3번째 방법) 연속된 값이 있는 배열 만들기
arr = np.arange(1, 10, 2)  # 1부터 9까지 2씩 증가하는 배열
print(arr)  # [1, 3, 5, 7, 9]

# 0 ~ 100까지 100을 포함해서 5개로 나눈 값들이 출력
arr = np.linspace(0, 100, 5, dtype=np.int32)
print(arr)  # [  0  25  50  75 100]

# 배열의 차원과 크기 알아내기
arr = np.linspace(0, 100, 3, dtype=np.int32)

print(arr.ndim)  # 배열의 차원 (1차원)
print(arr.shape)  # 배열의 크기 출력 (3,)

a1 = np.array( [ 1, 2, 3, 4, 5 ])
a2 = np.array( [ [ 1, 2, 3, 4 ] , [ 1, 2, 3, 4 ] ] )
a3 = np.array( [ [ [ 1, 2, 3 ] , [ 1, 2, 3 ] ] ,
                 [ [ 1, 2, 3 ] , [ 1, 2, 3 ] ] ,
                 [ [ 1, 2, 3 ] , [ 1, 2, 3 ] ] ] )

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

print(a1.shape)
print(a2.shape)
print(a3.shape)

# 스칼라 : 1차원 배열
# 벡터 : 2차원 배열
# 매트릭스 : 3차원 이상

# (5,)      # 1행 5열
# (2, 4)    # 2행 4열
# (3, 2, 3) # 높이3, 행2, 열3
            # (높이, 행, 열)


# READ
# 읽는 방법 = 인덱싱과 슬라이싱 지원

arr = np.array( [ [ 0, 1, 2 ],
                  [ 3, 4, 5 ],
                  [ 6, 7, 8 ] ] )

print(arr.shape)
print(arr[2,2])
print(arr[0,0])

print(arr[-1,-1])
print(arr[-2,-2])
print(arr[-2,2])

# UPDATE
# 값 수정
arr = np.array( [ [ 0, 1, 2 ],
                  [ 3, 4, 5 ],
                  [ 6, 7, 8 ] ] )
arr[0,0] = 1
print(arr)

# 슬라이싱
arr = np.array( [ 
                    [ 1, 2, 3, 4, 5 ],
                    [ 6, 7, 8, 9, 10 ],
                    [ 11, 12, 13, 14, 15] 
                ] )
print(arr.shape)
print(arr[1,1:3])
print(arr[1:2,2])
print(arr[1:2,:])

# 불린(Boolean) 배열 인덱싱

arr = np.array([0,1,2,3,4,5])
bool_arr = np.array([True, False, True, False, True, False])

# 불린 인덱싱을 사용할 때 주의할 점은 불린 
print(arr[bool_arr])
# True인 것만 뽑아냄

# 연산
# print([1,2,1] + [3,4,"숫자"])

a = np.array([1,2,3])
b = np.array([4,5,6])

c = a + b
print(c)
print(type(c))

# 스칼라
c = 5 * a
print(c)

c = 2 + 5 * b - a
print(c)

# == 사용하기

c = np.array([21,25,24])
print(c == 25)
d = (c == 25)
print(d)
print(type(d))

# 2/4






















