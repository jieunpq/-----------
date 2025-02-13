# 1.아래의 데이터 프레임에서 점수총합 과 평균의 컬럼을 추가 시키시오.

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

df['점수총합'] = df['국어점수'] + df['수학점수']
df['평균'] = df['점수총합'] / 2

print(df)


# 2. 위의 데이타 프레임에서 서울을 경기로 , 부산을 대구로 변경시키시오. 

df['지역'].replace({"서울":"경기", "부산":"대구"}, inplace=True)
print(df)

# 3. 위의 데이타 프레임에서 apply 함수를 사용하여 나이에 "살" 을 붙이시오.
def age_add(age):
    return str(age) + '살'

df['나이'] = df['나이'].apply(age_add)
print(df)

# 4. 데이타 프레임에서 
#   iloc 와 loc 함수의 차이점은?

# iloc
# 행 = index = row = 라벨 기준

# loc
# 열 = value = column 기준

# 5. 위의 데이타 프레임에서 점수총합 이 160 보다 크면 결과 컬럼을 만들어 합격이라고 표시하시오

df.loc[ df['점수총합'] > 160, '결과' ] = '합격'
print(df)