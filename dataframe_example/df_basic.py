import pandas as pd
from pandas import DataFrame
# 데이터 프레임

# 컬럼 단위로 데이터 표현
data = {
    "시가" : [30,90,80],
    "고가" : [90,70,90],
    "저가" : [30,90,80],
    "종가" : [90,70,90],
}

index = ["삼성전자", "카카오", "네이버"]

df_stock = pd.DataFrame(data=data,index=index)
print(df_stock)

# 로우 단위로 생성
data = [
            [30,90,80,90],
            [30,90,80,90],
            [30,90,80,90],
        ]
# 값이 들어갈 때는 리스트

column = ["시가", "고가", "저가", "종가"]
index = ["삼성전자", "카카오", "네이버"]

df_stock = pd.DataFrame(data=data,columns=column,index=index)
print(df_stock)

# 로우 단위를 딕셔너리로 표현하여 생성
data2 =[
         {"시가":980, "고가":80 , "저가":70 , "종가":90},
         {"시가":980, "고가":80 , "저가":70 , "종가":90},
         {"시가":980, "고가":80 , "저가":70 , "종가":90},
]
index2 = ["삼성전자","카카오","네이버"]

df_stock = pd.DataFrame(data=data2,index=index2)
df_stock

#
data = {
    "나이" : [35, 30, 38],
    "직책" : ["과장", "대리", "대리"]
}
index = ["김은수", "박정민", "이하나"]

df_emp = pd.DataFrame(data=data,index=index)
print(df_emp)

# 데이터 프레임 전체적인 개괄요약 함수
df_emp.info()
print(df_emp.describe())

print(df_emp.shape)

# 고객 데이터를 담은 딕셔너리 생성
data = {
    "이름": ["김철수", "이영희", "박민수"],
    "나이": [25, 32, 19],
    "도시": ["서울", "부산", "대구"]
}

# 딕셔너리를 사용해 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터프레임 출력
print(df)

# 도시 열 선택
column_data = df['도시']
print(column_data) # 시리즈로 리턴됨

# cf)
column_data = df[ ["도시"] ] # 데이터 프레임으로 리턴됨

# 도시,이름 > 열 두개 선택
selected_columns = df[['도시','이름']]
print(selected_columns) # 데이터 프레임로 리턴됨

# 원본은 훼손되지 않음

# 행 선택

# df.head() # 위에서 5개
# df.tail() # 밑에서 5개

# df.head(10) # 위에서 10개
# df.tail(10) # 밑에서 10개

row = df.loc[0]
print(type(row))
print(row)



