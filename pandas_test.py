# 판다스의 이해
# 판다스 = 데이터 프레임 + 시리즈

import pandas as pd
from pandas import Series
# CREATE

s = pd.Series([10,20,30])
print(s)
print(type(s))

s = pd.Series(["고가","시가"])
print(s)

s = pd.Series(["삼성","81000"])
print(s)

# 인덱스
s = pd.Series([1000,2000,3000])
print(s)
print(s.index)
print(s.values)
print(s.index.tolist())

# 0 1 2 =>
s.index = ["메로나","구구콘","하겐다즈"]
print(s)

# 한꺼번에 만들 수 있음

ss = pd.Series(index = [1000,2000,3000],data = ["메로나","구구콘","하겐다즈"])
                # 위치 기반/키워드 기반으로도 생성 가능
print(ss)

# 딕셔너리 이용
data = {
    "2019-05-31" : 42500,
    "2019-05-30" : 42550,
    "2019-05-29" : 41800,
    "2019-05-28" : 42550,
    "2019-05-27" : 42650
}

s_samsung = pd.Series(data)
print(s_samsung)
print(s_samsung.values) # 넘파이
print(s_samsung.index.to_list()) # 리스트

# READ 인덱싱

s = pd.Series([1000, 2000, 3000])

s = pd.Series(data = [1000,2000,"3000"], index = ["메로나","구구콘","하겐다즈"])
print(s)
# 다른 데이터도 object타입으로 변경 (데이터타입 통일)
print(s.iloc[0])
print(s.iloc[1])
print(s.iloc[2])
print(s.iloc[-1])

# print(s.loc[0])
# print(s.loc[1])
# print(s.loc[2])
print(s.loc["메로나"])
print(s.loc["구구콘"])
print(s.loc["하겐다즈"])
# print(s.loc[-1])
# 인덱스의 데이터타입이 달라도 됨(list)

# READ 슬라이싱

s = pd.Series(data = [1000,2000,3000], index = ["메로나","구구콘","하겐다즈"])
# print(s)

print(s.iloc[0:2]) # 슬라이싱으로 끌고 오면 => 시리즈 객체로 리턴됨


print(s.loc["메로나":"구구콘"]) 
# s.iloc( 시작:끝-포함X )
# s.loc( 시작:끝-포함 )
 
indice = [0,2]
print(s.iloc[indice])

indice = ["메로나","하겐다즈"]
print(s.loc[indice])

# 수정/추가/삭제

# 수정
data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=data,index=index)
s.loc["메로나"] = 500
print(s)
s.iloc[0] = 1000 #행번호 접근
print(s)

# 추가
s.loc['비비빅'] = 500
print(s)

# 삭제
# t = s.drop('메로나') # 옵션을 주지 않으면 원본은 지우지 않음
# print(t)

s.drop('메로나', inplace=True)
print(s)

# 시리즈 연산 = 넘파이와 동일하게 브로드캐스팅이 적용되며, 
# 같은 인덱스를 갖는 데이터끼리 연산을 수행

s_1 = pd.Series([10,20,30], index=['NAVER', 'SKT', 'KT'])
s_2 = pd.Series([10,30,20], index=['SKT', 'KT', 'NAVER'])

s_3 = s_1 + s_2
print(s_3)

print(10 * s_1)

s_3 = s_1 - s_2
print(s_3)

# 삼성전자 5일 주가

high = pd.Series([42800, 42700, 42050, 42950, 43000])
low = pd.Series([42150, 42150, 41300, 42150, 42350])

s_diff = high - low
print(s_diff)

print(s_diff.max())
print(s_diff.min())

print(s_diff.mean()) # 평균
print(s_diff.median()) # 중간값
print(s_diff.var()) # 분산
print(s_diff.std()) # 표준편차

print(s_diff.cumprod()) #누적곱

data = {
    "삼성전자": "전기,전자",
    "LG전자": "전기,전자",
    "현대차": "운수장비",
    "NAVER": "서비스업",
    "카카오": "서비스업"
}

s = pd.Series(data)

print(s)
print(s.unique()) # 넘파이로 리턴해줌

print(s.value_counts()) #시리즈로 리턴

# 시리즈 Map
# 시리즈를 사용하다 보면 시리즈가 지원하는
# 기본연산 (덧셈, 뺄셈, 곱셈, 나눗셈) 이외에도 복잡한 형태의 사용자 정의 코드를 적용하고 싶은 경우

s = pd.Series(["1.234","5.678","9.876"]) 

# print(int(s))
def remove_comma(x):
    print(x, "in funchion")
    return int(x.replace(".", ""))

result = s.map(remove_comma)

print(result)

print(result.sum())

# 

s = pd.Series([1234,5678,9876])

def compare(x):
    print(x, "in function")
    if x > 5000:
        return "크다"
    else:
        return "작다"

result = s.map(compare)
print(result)

# 출력
# 0 작다
# 1 크다
# 2 크다

# 시리즈 필터링 = 불린 인덱싱으로 처리하는 경우가 많음

data = [42500, 42550, 41800, 42550, 42650]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

s = pd.Series(data=data, index=index)

# print(s)

cond = s > 42000
print(cond)

print(s[cond]) # 불린 indexing


s = pd.Series(data=data, index=index)

# 종가가 시가보다 높을 때만 출력

close = [42500, 42550, 41800, 42550, 42650]
open = [42600, 42200, 41850, 42550, 42500]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

open = Series(data=open, index=index)
close = Series(data=close, index=index)

cond = open < close
print(close[cond])

print(close[close > open])

# 정렬 및 순위

data = [3.1, 2.0, 10.1, 5.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)
print(s)

# 정렬
s1 = s.sort_values()
print(s1)

# 내림차순으로 정렬
s1 = s.sort_values(ascending=False)
print(s1)

# 랭킹 매기기

data = [3.1, 2.0, 10.1, 3.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)

print(s.rank())

print(s.rank(ascending=False))



