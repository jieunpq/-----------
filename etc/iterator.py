# iterator 객체를 직접 만들어 보기

class Counter:
    def __init__(self, stop):
        self.current = 0 # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop # 반복을 끝낼 숫자

    def __iter__(self):
        return self # 현재 인스턴스를 반환

    def __next__(self):
        if self.current < self.stop: # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current         # 반환할 숫자를 변수에 저장
            self.current += 1        # 현재 숫자를 1 증가시킴
            return r                 # 숫자를 반환
        else:                        # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration      # 예외 발생

counter = Counter(10)

for i in counter.__iter__():
    print(i, end=' ')

counter = Counter(10).__iter__()
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())