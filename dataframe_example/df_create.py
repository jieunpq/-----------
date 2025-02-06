# 데이터 프레임

# 컬럼 단위로 데이터 표현
data ={
    "시가" : [30,90,80],
    "고가" : [90,70,90],
    "저가" : [30,90,80],
    "종가" : [90,70,90],
}
index = ["삼성전자","카카오","네이버"]

#df = pd.DataFrame(data,index=index)
#print(df)
#stock_df = pd.DataFrame(data)
#print(stock_df)

df_stock = pd.DataFrame(data=data,index=index)
df_stock

# 로우 단위로 생성
data = [
            [30,90,80,90],
            [30,90,80,90],
            [30,90,80,90],
        ]
column = ["시가","고가","저가","종가"]
index = ["삼성전자","카카오","네이버"]

df_stock = pd.DataFrame(data=data,columns=column,index=index)
df_stock

# 로우단위를 딕셔너리로 표현하여 생성

data2 =[
         {"시가":980, "고가":80 , "저가":70 , "종가":90},
         {"시가":980, "고가":80 , "저가":70 , "종가":90},
         {"시가":980, "고가":80 , "저가":70 , "종가":90},        
]
index2 = ["삼성전자","카카오","네이버"]

df_stock = pd.DataFrame(data=data2,index=index2)
df_stock

