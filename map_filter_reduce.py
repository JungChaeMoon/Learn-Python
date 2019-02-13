# map, filter and reduce

"""
map 의 사용법
map(functions_to_applym list_of_inputs)
"""

"""
example)
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

이러한경우 인자들을 함수에 전달하고 결과값들을 취합해서 사용 하려고함
map을 사용하면 훨씬 간단하고 멋진방식

items = [1,2,3,4,5]
squared = list(map(lambda x : x**2, items))

여기서 lambda란 함수를 한줄로 줄여줄수있는 엄청난 함수
사용법은 lambda 인자 : 표현식 으로 나타냄

example) 두수를 더하는 함수입니다
def add(x, y):
    return x+y
add(10,20)
이것을 람다형식으로는
(lambda x,y:x+y)(10,20) 로 표현할수있다 다시 맵으로 돌아와서

"""
"""
심화
def multiply(x) :
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply,add]

for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)
"""
"""
filter
'필터라는 이름이 이야기 해주듯, 필터는 함수에서 참을 반환하는 요소들로 구성되는
리스트를 생성함'
예시)
number_list = range(-5 ,5)
less_than_zero = list(filter(lambda x:x<0, number_list))
print(less_than_zero)

필터함수는 forloop과 비슷해보이지만, 내장함수이고 속도도 더빠르다
"""

"""
reduce

reduce는 리스트로 몇가지 계산을 수행하고 반환하는 매우 유용한 함수

from functools import reduce
product = reduce((lambda x,y : x*y),[1, 2, 3, 4])
"""

