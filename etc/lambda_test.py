# 아래 함수를 람다 함수로 바꾸시오.
fct_fac = lambda n : lambda x : x ** n  # 위에서 정의한 함수 exp를 반환한다.

f2 = fct_fac(2) # f2는 제곱을 계산해서 반환하는 함수를 참조한다.
print(f2)
f3 = fct_fac(3) # f3는 세제곱을 계산해서 반환하는 함수를 참조한다.
print(f2(4)) # 4의 제곱은?
#16
print(f3(4)) # 4의 세제곱은?
#64"

