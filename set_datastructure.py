"""
set data structure
set 함수는 매우 유용한 데이터 구조입니다. set 함수는 같은 값을 포함하지 않도록 분별된 리스트처럼 동작합니다.
이것은 정말 많은 경우에 유용합니다. 예를 들어, 값이 중복으로 리스트에 존재하는지 확인하고 싶으면 두 가지 방법으로 확인할 수 있습니다.
하나는 for 루프를 사용하는 것이고, 아래와 같이 사용합니다
"""

"""
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
"""
"""
하지만 set을 사용하면 더간단하고 우아한 코드가 완성됨
"""
"""

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = set(x for x in some_list if some_list.count(x) > 1])
print(duplicates)

#output: set(['b', 'n'])
"""
"""
set함수 소개
1. intersection (교차)

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))

#output: set(['red'])

2.difference(다름)
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))

#Output: set(['brown'])
"""