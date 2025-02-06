import pandas as pd
from pandas import Series, DataFrame

# 1.아래처럼 데이타가 나오도록 데이타 프레임을 만들어 보시오

#          시가	고가 저가 종가
# 삼성전자	980	80	70	90
# 카카오	980	80	70	90
# 네이버	980	80	70	90

data = {
    "시가" : [980, 980, 980],
    "고가" : [80, 80, 80],
    "저가" : [70, 70, 70],
    "종가" : [90, 90, 90]
}
index = ["삼성전자", "카카오", "네이버"]

df_stock = DataFrame(data=data, index=index)
print(df_stock)


# 2. 아래와 같이 출력이 나오도로 하시오. 

close = [42500, 42550, 41800, 42550, 42650]
open = [42600, 42200, 41850, 42550, 42500]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

open = Series(data=open, index=index)
close = Series(data=close, index=index)

cond = close > open
print(close[cond])

# 출력
# 종가가 시가보다 높을때만 출력
# 2019-05-30    42550
# 2019-05-27    42650
# dtype: int64

# 3. 아래의 데이터를 정렬하시오.
data = [3.1, 2.0, 10.1, 5.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)

print(s.sort_values(ascending=False))

# 출력
# dtype: float64
# 000030    10.1
# 000040     5.1
# 000010     3.1
# 000020     2.0
# dtype: float64

# 4. 아래의 데이터가 아래와 같이 출력 되도록 하시오.
s = pd.Series([1234, 5678, 9876])

def greater_than_5000(x):
    if x > 5000:
        return "크다"
    else:
        return "작다"

result = s.map(greater_than_5000)
print(result)

# 출력
# 0    작다
# 1    크다
# 2    크다
# dtype: object

# 5. 데이타 프레임을 생성하는 3가지 방법은 ?

# column 단위(딕셔너리 내 리스트)
data = {
    "시가" : [980, 980, 980],
    "고가" : [80, 80, 80],
    "저가" : [70, 70, 70],
    "종가" : [90, 90, 90]
}
index = ["삼성전자", "카카오", "네이버"]

df_stock = DataFrame(data=data, index=index)
print(df_stock)

# row 단위(리스트 내 리스트)
data = [
    [980, 80, 70, 90],
    [980, 80, 70, 90],
    [980, 80, 70, 90],
]

index = ["삼성전자", "카카오", "네이버"]
column = ["시가", "고가", "저가", "종가"]

df_stock = DataFrame(data=data, index=index, columns=column)
print(df_stock)

# row 단위(리스트 내 딕셔너리)
data = [
    {"시가":980, "고가":80, "저가":70, "종가":90},
    {"시가":980, "고가":80, "저가":70, "종가":90},
    {"시가":980, "고가":80, "저가":70, "종가":90}
]

index = ["삼성전자", "카카오", "네이버"]

df_stock = DataFrame(data=data,index=index)
print(df_stock)

