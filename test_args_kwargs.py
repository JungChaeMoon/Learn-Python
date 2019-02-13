"""
*args 와 **kwargs
대부분 *args 와 **Kwagrgs는 함수를 정의 할때 사용 *args 와 **kwargs는 가변인자 갯수의 인자들을 함수에 넣어줌
"""
"""
#*args의 사용법
def test_var_args(f_arg, *argv):
    print("첫번째 인자:", f_arg)
    for arg in argv:
        print("argv의 다른인자:",arg)

test_var_args('채문', 'python', '달걀', 'test')
"""
#**kwargs의 사용법
"""
**kwargs는 키워드된 가변 갯수의 인자들을 함수에 보낼 때 사용합니다. **kwargs는 함수가 이름이 지정된 인자를 처리할떄 사용
"""
"""
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" %(key, value))

greet_me(name1 = "chaemoon" , name2 = "ujin")
"""

#함수를 호출하기 위한 *args와 **kwargs
"""
def test_args_kwargs(arg1, arg2, arg3):
    print("인자1:", arg1)
    print("인자2:", arg2)
    print("인자3:", arg3)
"""

"""
args=("two", 3, 6)
test_args_kwargs(*args)
"""
"""
kwargs = {"인자3": 3, "인자2": "two", "인자1": 5}
test_args_kwargs(**kwargs)
"""
