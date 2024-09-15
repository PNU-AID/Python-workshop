# 파이썬 자료구조
- [variable](#variable)
- [bool](#bool)
- [list,array](#list-array)
- [string](#string)
- [tupe](#tuple)
- [dictonary](#dictionary)
- [set](#set)

## variable
![](https://wikidocs.net/images/page/18/02_8_memory.png)


변수가 어떻게 생성이 되느냐?
파이썬에서 변수는 c랑 조금 다르다. c는 생성하고 그 주소를 할당하는데 파이썬 같은 경우에는 무조건 레퍼런스를 할당한다. 

```python
a=1
b=1
```
c에서는 변수를 새로 생성을 하겠지만 파이썬에는 둘이 똑같이 가르킨다. 아이디가 같은지 확인해보자

![](https://velog.velcdn.com/images/soheean1370/post/d35a295e-3a20-44c2-9982-71c9dc3baabb/image.png)

```python
print(id(a))
print(id(b))
```
를 하면 아이디가 똑같이 나온다.... ㄷㄷ 같은 클래스는 같은걸 가르키게 된다.
근데 여기서 이제 b+1을 하면 이때 달라지게 되는거고 어떠한 같은 값이나 같은 클래스 혹은 같은 오브젝트이다.
```python
b+=1
```
근데 여기서 이제 b+1을 하면 이때 id가 달라지게 되는거고 어떠한 같은 값이나 같은 클래스 혹은 같은 오브젝트이다.
![](https://velog.velcdn.com/images/soheean1370/post/7ef702be-4351-4259-9eca-e3b8b62ea8b0/image.png)

### mutable & immutable
mutable은 값이 변한다는 뜻이고, immutable은 값이 변하지 않는다는 의미이다. 자료형마다 특징이 다르다

> immutable한 자료형들은 한번 생성된 값은 변경할 수 없으며, 값을 변경하려면 새로운 메모리 공간이 필요하다

- 숫자형 (number) : immutable
![](https://velog.velcdn.com/images/soheean1370/post/4eb51064-72eb-4ca0-b1af-4a7eaa68c2ea/image.png)
- 문자열 (string) : immutable
![](https://velog.velcdn.com/images/soheean1370/post/648dc447-335a-4e21-b83f-c26fb1a44ae0/image.png)
```python
a = "hello"
a = a + " world"
print(a)
>>> "hello world"
```
- 튜플(Tuple) : immutable
![](https://velog.velcdn.com/images/soheean1370/post/7f536eed-7985-422c-9987-ed14f1499b5e/image.png)

> mutable한 자료형들은 값을 변경할 수 있으며, 동일한 메모리 주소에서 값을 수정하는 방식

- 리스트 (list) : mutable
![](https://velog.velcdn.com/images/soheean1370/post/a3464987-41e6-4284-8f03-ccac6859efea/image.png)
- 딕셔너리 (Dictionary) : mutable 
![](https://velog.velcdn.com/images/soheean1370/post/68ace804-5f8c-45ff-bd5f-bc4b513da620/image.png)

## bool
불 자료형이란 참과 거짓을 나타내는 자료형이다. 다음 2가지 값만을 가질 수 있다. true, false와 같이 작성하면 안 되고 첫문자를 항상 대문자로 작성해야 한다.

```python
a = True
b = False
```

불 자료형은 조건문의 리턴값으로도 사용된다.

```python
a = 1
b = 1
print(a == b) # == 은 두 수가 같은가를 묻는 조건문
>>> True
```
## list, array
파이썬에서 배열 (array)라는 용어는 흔히 리스트(list)를 의미한다. 리스트는 여러 타입의 값을 저장할 수 있는 가변적인 시퀀스 자료형이다. 즉 값을 추가하거나 제거할 수 있는 동적 배열이다. 

c 언어에서는 어레이가 연속된 공간에 저장을 한다. 근데 파이썬 리스트 경우에 여러 타입이 다같이 모여있다. 이게 파이썬의 큰 장점 중 하나이다. C나 다른 언어와 달리 파이썬 리스트는 메모리 상에서 연속적으로 지정되지 않을 수 있으며 각 요소는 실제 값이 아닌 그 값이 저장된 메모리 주소를 참조한다

```python
a = [1, 2, 3, 4, dict(), True]
```
리스트는 대괄호 `[]`를 사용해서 정의한다. 이 리스트 안에는 값들이 저장되는게 아니라 각각에 대한 주소가 저장이 되는거다. 이게 reference이다. 1이 담기는게 아니라 1의 주소가 담겨 있는거다
![](https://velog.velcdn.com/images/soheean1370/post/1ae5932b-c637-4e2c-83cc-ce76fd800330/image.png)

2차원 배열을 할때 조심해야 하는게 얘도 주소값이 복사되는 거기 때문에 얕은 복사랑 깊은 복사가 있다.

### 얕은 복사 vs 깊은 복사
```python
a = [[1,2] , [3,4]]
b = a.copy()
a[0][0] = 10
print(b)
>>>> [[10,2] , [3,4]]
```
위 예시에서 `a`와 `b`는 서로 다른 리스트지만, 내부 리스트는 같은 객체를 참조하기 때문에 a를 변경하면 b도 같이 변경되는걸 볼 수 있다. 이를 방지하려면 깊은 복사 (deep copy)를 사용해야 한다

## string

string도 리스트 처럼 쓸 수 있다. 
```python
a = "abcde"
print(a[:3])
>>>abc
```
근데 string은 변경불가능한 객체이기 때문에 
```python
a[3] = "g"
```
이렇게 하면 type error가 뜬다
## tuple
튜플은 리스트와 비슷하지만, immutable한 자료형이다. 한 번 생성되면 값을 변경할 수 없으며, 리스트처럼 여러 값을 담을 수 있지만, 수정이 불가능하다. 주로 변경할 필요가 없는 데이터를 묶어서 처리할 때 사용된다.

```python
a = (1,2,3)
b = (4,'hello',True)
print(a[0])
>>> 1
```
이렇게 튜플은 괄호 `()`를 사용해서 정의하며, 인덱스를 통해 값에 접근할 수 있다. 리스트와 달리 값을 변경할 수 없다는 점에서 차이가 있다

### 튜플의 요솟값 지우거나 변경하기
앞에서 설명했듯이 튜플의 요솟값은 한 번 정하면 지우거나 변경할 수 없다. 
변경하거나 지우려고할때 오류가 발생한다.

> 튜플은 요솟값을 변경할수 없기 때문에 sort, insert, remove, pop과 같은 내장 함수가 없다.

## dictionary
딕셔너리는 mutable한 자료형으로, 키(key)-값(value)쌍으로 데이터를 저장하는 자료 구조이다. 딕셔너리에서는 키를 통해 해당 값을 바로 참조할 수 있으며, 키는 유일해야하고 immutable한 자료형이여야 한다. 반면 값은 mutable 일 수도 있다

![](https://wikidocs.net/images/page/16/02_5_baseball.png)

딕셔너리의 기본 모습
```python
dic = {Key1: Value1, Key2: Value2, Key3: Value3, ...}
```

```python
a = {'name': 'John','age':25}
print(a['name])
>>> John
```
딕셔너리는 중괄호 `{}`로 정의되며, 키를 통해 값에 접근하고 수정,삭제가 가능하다. 파이썬에서 딕셔너리는 매우 중요한 자료형으로 특히 데이터의 빠른 검색이 필요한 상황에서 유용하다
```python
a['age'] = 26
print(a['age'])
>>> 26
```
딕셔너리 쌍 추가하기
```python
a = {1:'a'}
a[2] = 'b' 
print(a)
>>> {1: 'a', 2: 'b'}
```
딕셔너리 요소 삭제하기
```python
del a[1] 
print(a)
>>> {2: 'b'}
```

## set
1. 중복을 허용하지 않는다
- set은 중복을 허용하지 않는 특징 때문에 데이터의 중복을 제거하기 위한 필터로 종종 사용된다.
2. 순서가 없다. 
- 순서가 없기 때문에 인덱싱을 통해 요솟값을 얻을 수 없다. 만약 인덱싱으로 접근하려면 리스트나 튜플로 변환한 후에 해야 한다.

```python
a = set([1,2]).
b = set([1,2,1])

print(a,b)
>>> {1,2} {1,2}
```
중복되는게 없다. 무조건 유일한 하나의 오브젝트들만 들어가 있다. 포문을 돌릴 수 있는 객체이다.     
변경 불가능한 객체이고 해싱이 가능하다.