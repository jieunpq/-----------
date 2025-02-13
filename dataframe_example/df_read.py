import pandas as pd
import numpy as np

df = pd.DataFrame( {
    '이름': ['피카츄','라이츄','리자드','리자몽','꼬부기','어니부기'],
    '속성': ['전기', '전기', '불','불','물',None], 
    '색깔': ['노랑', '노랑', None,'빨강','파랑','파랑'],
    '순위': [ 5, 2, 6, 1, 4, 3] })

df.columns = ['이름', '속성','색깔','순위']

df.info()
print(df.head(6))

# 열
print(df['속성']) # 시리즈로 리턴
df[['속성', '순위']] # 데이터 프레임으로
df[['속성']] # 데이터 프레임

df['속성'].values
df['속성'].shape

# 행 인덱싱

df[1:3] # 2개 이상 행
df[3:4] # 단일행

# 자료 1개만 가지고 오기
df['색깔'][2]

df['순위'] < 3
df[df['순위'] < 3]

# 색깔이 노랑인 행을 출력하시오
print(df[df['색깔'] == '노랑'])

# 순위가 2보다 크고 5보다 작은 행들을 출력하시오
df[ (df['순위'] > 2) & (df['순위'] < 5) ]

# null 데이터 가져오기 = 결측치
# not null 값은 NaN

df.info()

df[df.isnull()]

# df.info()로 확인할 후, 특정 열에서 null값을 검색
print(df[df['속성'].isnull()])
# 속성에 None이 있는 행을 다 보여줌

# ========================================
# loc/iloc로 행 가져오기

# iloc = 행번호 = 단독행
print(df.iloc[0]) # 시리즈
print(df.iloc[[0]]) # 데이터프레임

# iloc = 행번호 = 여러개의 행 가져오기 = 데이터 프레임으로 리턴
print(df.iloc[[0,2,4]])
print(df.iloc[2:4])

# 행과 열 같이 가져오기
print(df.iloc[0,0]) #행,열에는 번호 인덱스만 가능
print(df.iloc[[1,3],[0,2,3]])
print(df.iloc[2:5,1:3])

# ========================================
# loc(라벨로 인덱싱/끝번호 포함)

import pandas as pd
data = {
    '이름' : ['유재석', '박명수', '정준하', '노홍철', '정형돈', '하하'],
    '지역' : ['서울', '부산', '부산', '서울', '서울', '서울'],
    '나이' : [19, 23, 20, 25, 18, 21],
    '국어점수' : [86, 90, 80, 65, 50, 60],
    '수학점수' : [86, 100, 66, 70, 40, 80],
    '코딩' : ['Python', 'Java', '', 'Javascript', 'PYTHON', '']
}
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번'])
df.index.name = '번호'

print(df)

print(df.loc['1번']) # 1번 전체 데이터
print(df.loc['1번','나이']) # 1개 데이터 뽑아내기
print(df.loc[['1번','2번'],'수학점수'])
print(df.loc[['1번','2번'],['수학점수','국어점수']])

# loc 슬라이싱 (끝번호 포함)
print(df.loc['1번':'4번','지역':'국어점수'])

print(df.loc[df['나이']>=20, ['이름','지역','나이']])

print(df.loc[(df['지역']=='부산') & (df['나이']>=20)])

# ========================================
# 데이터 프레임 함수

# 유씨 성을 가진 사람 뽑아내기

filter = df['이름'].str.startswith('유')
print(df[filter])

# 이름에 '하'가 들어가는 사람
filter = df['이름'].str.contains('하')
print(df[filter])

filter = df['코딩'].isin(['Python','Java'])
print(df[filter])

filter = df['코딩'].str.lower().isin(['python','java'])
print(df[filter])

# ========================================
# 결측치 처리

data = {
    '이름' : ['유재석', '박명수', '정준하', '노홍철', '정형돈', '하하'],
    '지역' : ['서울', '부산', np.nan, '서울', '서울', '서울'],
    '나이' : [19, 23, 20, 25, 18, 21],
    '국어점수' : [86, 90, 80, 65, 50, 60],
    '수학점수' : [86, 100, 66, 70, 40, 80],
    '코딩' : ['Python', 'Java', np.nan, 'Javascript', 'PYTHON', np.nan]
}
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번'])
df.index.name = '번호'

print(df)

# 결측치 지정
df['지역'] = np.nan
print(df)

print(df.fillna('')) # NaN 데이터를 빈칸으로 채움

print(df.fillna('없음')) # NaN 데이터를 없음으로 채움

df['코딩'].fillna('확인중',inplace=True) # 원본에 적용

print(df)

# ========================================
# 데이터 제외

# 결측치는 데이터 분석에 방해가 됨

print(df.dropna(inplace=True))

print(df)


# ========================================
# 데이터 정렬
# 인덱스 기준으로 정렬

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

print(df.sort_index()) # 오름차순
print(df.sort_index(ascending=False)) # 내림차순

# 컬럼 기준으로 정렬

print(df.sort_values(by='나이')) #오름차순
print(df.sort_values(by='나이',ascending=False)) # 내림차순

# 컬럼을 기준을 두가지로 order by ename asc, empno desc
print(df.sort_values(['지역','국어점수']))
# 지역은 오름차순, 국어점수는 내림차순으로

print(df['수학점수'].sort_values)

# ========================================
# 함수 적용 - apply

def age_add(age):
    return str(age) + "세"

df['나이']= df['나이'].apply(age_add)

print(df)