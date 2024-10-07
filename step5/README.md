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
클래스의 안에 정의된 함수를 메소드(method)라고 부른다. 메소드 중에서 `__`로 시작해서 `__`로 끝나는 메소드들이 있는데 이를 매직 메소드 또는 특별 메소드라고 부른다. 가장 유명한 매직 메소드에는 `__init__`이라는 생성자가 있다. 생성자는 어떤 클래스의 객체가 생성될 때 파이썬 인터프리터에 의해 자동으로 호출되는 메소드였다.

```python
class Car:
    def __init__(self):
        print("자동차 제작 완료")

a = Car()
>>> 자동차 제작 완료
```

> 언제 매직 메소드를 사용할까?
여러분이 만든 클래스 타입에 대해 인덱싱 기능을 제공하려고 할때와 연산자를 수행할때 어떤 정해진 동작이 수행되도록 하려고 할 때에도 매직 메소드를 사용한다

데이터셋 만들때 사용되는 대표적인 매직 메소드 
- `__len__(self)`: 이 메소드는 데이터셋 내의 항목 수를 반환한다. 예를 들어, 이미지 데이터셋의 경우 전체 이미지의 개수를 반환하는 데 사용된다. 이를 통해 len() 함수를 호출할 수 있다.

```python
class CustomDataset:
    def __init__(self, data):
        self.data = data  # 데이터 리스트

    def __len__(self):
        return len(self.data)  # 데이터 항목 수 반환

# 데이터셋 예시
dataset = CustomDataset([1, 2, 3, 4, 5])
print("데이터셋의 크기:", len(dataset)) 

>>> 5

```

- `__getitem__(self,key)`:이 메소드는 주어진 키(인덱스)를 사용하여 데이터셋에서 특정 항목을 가져오는 데 사용된다. 예를 들어, 이미지 데이터셋에서 특정 이미지를 가져올 때 유용하다.

```python
class CustomDataset:
    def __init__(self, data):
        self.data = data  # 데이터 리스트

    def __getitem__(self, index):
        return self.data[index]  # 주어진 인덱스에 해당하는 데이터 반환

# 데이터셋 예시
dataset = CustomDataset([10, 20, 30, 40, 50])
print("0번째 항목:", dataset[0])  
print("3번째 항목:", dataset[3]) 

>>>
0번째 항목: 10
3번째 항목: 40
```
이 두 매직 메소드를 결합하여 간단한 이미지 데이터셋 클래스를 만들어 보겠다. 이 예시에서는 이미지의 경로와 라벨을 포함하는 데이터셋을 정의한다.

```python
class ImageDataset:
    def __init__(self, images, labels):
        self.images = images  # 이미지 파일 경로 리스트
        self.labels = labels  # 라벨 리스트

    def __len__(self):
        return len(self.images)  # 이미지 수 반환

    def __getitem__(self, index):
        image = self.images[index]  # 해당 인덱스의 이미지 경로
        label = self.labels[index]  # 해당 인덱스의 라벨
        return image, label  # 이미지와 라벨 반환

# 데이터셋 예시
image_paths = ["img1.jpg", "img2.jpg", "img3.jpg"]
labels = [0, 1, 0]  # 이진 분류 예시
dataset = ImageDataset(image_paths, labels)

print("데이터셋의 크기:", len(dataset))  
print("0번째 이미지와 라벨:", dataset[0]) 

>>>
데이터셋의 크기: 3
0번째 이미지와 라벨: ('img1.jpg', 0)
```

# 상속

마치 부모가 자식에게 상속해주듯이 클래스도 상속을 할 수 있다. 상속을 해주는 클래스가 부모클래스가 되고 상속을 받는 클래스가 자식클래스가 된다. 공통되는 부분의 코드를 중복으로 적지 않기 위해서 클래스를 재활용하는 개념이라고 보면 된다. 자식클래스는 부모클래스로부터 모든 속성과 메소드를 상속받을 수 있다. 다중상속은 여러 부모클래스로부터 속성과 메소드를 상속받는 것을 말한다.

```python
class 기반클래스_이름:
    코드
class 클래스_이름(기반클래스_이름):
    코드
```
### 포함 관계
포함 관계는 상속과는 다르게, 특정 클래스가 다른 클래스의 인스턴스를 속성으로 갖는 것을 의미한다

```python
class Person:
    def greeting(self):
        print("안녕하세요.")

class PersonList:
    def __init__(self):
        self.person_list = [] # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):
        self.person_list.append(person)
```

위 코드에서 `PersonList` 클래스가 `Person` 인스턴스를 속성으로 포함하고 있다. 이는 "사람 목록(PersonList)이 사람(Person)을 가지고 있다"는 의미로, has-a 관계라고 한다.

### 기반 클래스의 속성 사용하기
상속을 받은 자식 클래스가 부모 클래스의 속성을 사용하려면 부모 클래스의 `__init__`메소드를 호출해야한다

```python
class Person():
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)

>>>
파이썬 코딩 도장
AttributeError: 'Student' object has no attribute 'hello'
```
기반 클래스 Person의 `__init__` 메서드가 호출되지 않았기 때문이다.
즉, Person의 `__init__` 메서드가 호출되지 않으면 self.hello = '안녕하세요.'도 실행되지 않아서 속성이 만들어지지 않는다.

이걸 해결할 수 있는게 super()이다

### super()로 기반 클래스 초기화하기
```python
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__() # 부모 클래스의 __init__ 메소드 호출
        self.school = '파이싼 코딩 도장'

james = Student()
print(james.school)
print(james.hello)

>>>
파이썬 코딩 도장
안녕하세요.
```

`super().__init__()`와 같이 기반 클래스 Person의 `__init__` 메서드를 호출해주면 기반 클래스가 초기화되어서 속성이 만들어진다.

### 기반 클래스를 초기화하지 않아도 되는 경우
만약 자식 클래스에서 `__init__` 메소드를 정의하지 않으면, 부모 클래스의 `__init__` 메소드가 자동으로 호출된다

```python
class Person:
    def __init__(self):
        print('Persone __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    pass

james = Student()
print(james.hello)

>>> 안녕하세요.
```

### 오버라이딩(overriding)
오버라이딩은 자식 클래스가 부모 클래스의 메소드를 재정의하는 것을 의미한다

```python
class Person:
    def greeting(self):
        print('안녕하세요.')

class Studnet(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
    
james = Student()
james.greeting()

>>> 안녕하세요. 저는 파이썬 코딩 도장 학생입니다.
```
또한 오버라이딩된 메소드에서 super()로 부모 클래스의 메소드를 호출할 수도 있다.

```python
class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self):
        super().greeting() # 부모 클래스의 메소드 호출
        print('저는 파이썬 코딩 도장 학생입니다.')

james = Student()
james.greeting()

>>>
안녕하세요.
저는 파이썬 코딩 도장 학생입니다.
```
## 다중상속

다중 상속은 여러 기반 클래스로부터 상속을 받아서 파생 클래스를 만드는 방법이다. 다음과 같이 클래스를 만들 때 ( )(괄호) 안에 클래스 이름을 ,(콤마)로 구분해서 넣는다.

```python
class 기반클래스이름1:
    코드

class 기반클래스이름2:
    코드

class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
    코드
```

이렇게 다중상속을 받을 경우 모든 기반 클래스의 기능을 상속받는다

```python
class Person: 
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()

>>>
안녕하세요.
학점 관리
공부하기
```

위 예시에서 Undergraduate 클래스는 Person과 University 클래스로부터 다중 상속을 받아 두 클래스의 기능을 모두 사용할 수 있다.

### 프라이빗 변수와 __

클래스에서 변수명을 `self.__변수명`과 같이 두개의 밑줄로 시작하게 설정하면, 해당변수는 클래스 외부에서 접근이 불가능한 **프라이빗 변수**로 관리된다. 다만 이는 절대적으로 숨겨지는 것이 아니라, 내부적으로 변수명을 변경하여 접근을 어렵게 만드는것이며, `dir()` 함수를 통해 확인하거나 접근할 수 있다. 

하지만 일반적으로 이러한 접근은 권장되지 않으며, 프라이빗 변수는 외부에서 직접 접근하지 않도록 하는 것이 좋다.

```python
class Person:
    def __init__(self):
        self.__age = 20

p = Person()
print(dir(p)) # __age가 변경된 이름으로 확인됨

>>> ['_Person__age', ...
```

실제로 self.__age가 _Person__age로 바뀌어 관리되며, 이 변수는 직접 접근은 어렵지만 이를 이용해 우회적으로 접근할 수 있다. 하지만 잘 사용되지는 않는다



