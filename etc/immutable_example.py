

# 리스트 주소 확인
r = [1,2]
print(id(r))

r += [3,4]
print(r)
print(id(r))

# 튜플 주소 확인
t = (1,2)
print(id(t))

t += (3,4) # t = t + (3,4)
print(t)
print(id(t))

def add_last(m,n):
    m += n  #m에 n의 내용을 추가한다.

r = [1,2]
add_last(r, [3,4])
print(r)

t = (1,3)
add_last(t, (5,7))
print(t)

def add_tuple(t1,t2):
    t1 += t2
    return t1

tp = (1,3)
tp = add_tuple(tp, (5,7))
print(tp)

def min_max(d):
    d.sort() # 정렬
    print(d[0], d[-1], sep='')

l = [3,1,5,4]
min_max(l)
print(l) # 원본이 바뀜

# 원본이 안 바뀌게

def min_max(d):
    d.sort() # 정렬
    print(d[0], d[-1], sep='')
    return d

l = [3,1,5,4]
min_max(l)
print(l) # 원본이 바뀜