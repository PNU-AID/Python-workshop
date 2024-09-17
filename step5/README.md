# class
계산기 프로그램을 만들며 클래스를 알아보자!
이런 내용을 우리가 앞에서 익힌 함수를 이용해 구현해 보자. 계산기의 ‘더하기’ 기능을 구현한 파이썬 코드는 다음과 같다.

```python
result1 = 0
result2 = 0

def add1(num):  # 계산기1
    global result1
    result1 += num
    return result1

def add2(num):  # 계산기2
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

>>>
3
7
3
10
```
계산기 1의 결괏값이 계산기 2에 아무런 영향을 끼치지 않는다는 것을 확인할 수 있다. 하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요해진다면 어떻게 해야 할까? 그때마다 전역 변수와 함수를 추가할 것인가? 여기에 계산기마다 빼기나 곱하기와 같은 기능을 추가해야 한다면 상황은 점점 더 어려워질 것이다.

```python
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
>>>
3
7
3
10
```
Calculator 클래스로 만든 별개의 계산기 cal1, cal2(파이썬에서는 이것을 ‘객체’라고 부른다)가 각각의 역할을 수행한다. 그리고 계산기의 결괏값 역시 다른 계산기의 결괏값과 상관없이 독립적인 값을 유지한다. 이렇게 클래스를 사용하면 계산기 대수가 늘어나도 객체를 생성하면 되므로 함수만 사용할 때보다 간단하게 프로그램을 작성할 수 있다

# 생성자 (Constructor)
일반적으로 함수는 사용자가 `함수이름()` 과 같은 형태로 호출해야 코드가 수행된다. 이와 달리 클래스 내에서 특별한 이름(`__init__`)을 갖기만 하면 객체가 생성될 때 자동으로 호출되는 함수가 있는 이를 생성자라고 한다.

```python
class Person:
    def __init__(self):
        print("태어남..")

p = Person()
>>> 태어남..
```
위 코드를 수행하면 문자열이 출력되는데 이는 객체가 생성될 때 자동으로 생성자인 `__init__()`이 호출됐기 때문이다. 이처럼 생성자는 객체가 생성될 때 자동으로 호출되기 때문에 *객체를 초기화하거나 초깃값을 설정*하는데 유용하게 사용된다.

## 인스턴스 개수 세기
이번에는 클래스로부터 생성된 인스턴스의 개수를 세어보자. 생성된 인스턴스의 개수는 각 인스턴스가 갖고 있기 보다는 모든 인스턴스가 참조할 수 있는 공간인 클래스에 저장되는 것이 좋다. 클랙스 객체에 저장되는 변수를 클래스 변수라고 했는데 객체가 생성될 때 자동으로 호출되는 생성자에서 클래스 변수에 저장된 변수 값을 1 증가시켜주면 생성된 객체의 개수를 셀 수 있다.

```python
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
    
    def get_count(self):
        return MyClass.count

```
My Class 타입의 객체를 3개 생성한 후 get_count 매세드를 호출
```python
a = MyClass()
b = MyClass()
c = MyClass()

print(a.get_count())
>>>3
```
또는 MyClass.count라는 표현을 통해서는 클래스 변수에 접근할 수 있다
```python
print(MyClass.count)

>>>3
```

# 매직 메서드 (Magic Method)
클래스의 안에 정의된 함수를 메소드(method)라고 부른다. 메소드 중에서 `__`로 시작해서 `__`로 끝나는 메소드들이 있는데 이를 매직 메소드 또는 특별 메소드라고 부르ㄴ다. 가장 유명한 매직 메소드에는 `__init__`이라는 생성자가 있다. 생성자는 어떤 클래스의 객체가 생성될 때 파이썬 인터프리터에 의해 자동으로 호출되는 메소드였다.

```python
class Car:
    def __init__(self):
        print("자동차 제작 완료")

a = Car()
>>> 자동차 제작 완료
```

> 매직 메소드를 사용할까?


# 상속
## 다중상속