import pandas as pd
import numpy as np

data = {
    '이름' : ['유재석', '박명수', '정준하', '노홍철', '정형돈', '하하'],
    '지역' : ['서울', '부산', '부산', '서울', '서울', '서울'],
    '나이' : [19, 23, 20, 25, 18, 21],
    '국어점수' : [86, 90, 80, 65, 50, 60],
    '수학점수' : [86, 100, 66, 70, 40, 80],
    '코딩' : ['Python', 'Java', np.nan, 'Javascript', 'PYTHON', np.nan]
}
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번'])
df.index.name = '번호'

# 컬럼 기준으로 수정하기
df['지역'].replace({"서울":"경기", "부산":"대구"},inplace=True)

print(df)

# 없으면 만든다

df['코딩'] = df['코딩'].str.lower()
print(df)

df['점수총합'] = df['국어점수'] + df['수학점수']

df['평균'] = df['점수총합'] / 2

print(df)

# 결과 컬럼 생성 후 '불합격'으로 초기화하기
df['결과'] = '불합격'

print(df)

# 총합이 160 넘으면 합격

df.loc[ df['점수총합'] > 160, '결과' ] = '합격'
print(df)

# ==========================================================
# 컬럼 삭제

df.drop(columns=['점수총합'],inplace=True)
print(df)

# Row 행 추가
df.loc['7번'] = ['길', '부산', 22, 90, 90, 'Kotlin', 89, '불합격']

print(df)

# 셀 수정
df.loc["4번", "국어점수"] = 100
print(df)

df.loc['4번', ['지역', '코딩']] = ['대구', 'C']
print(df)