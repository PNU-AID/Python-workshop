# 제어문  
## if
프로그래밍에서 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 쓰는 것이 바로 if 문이다. 
다음은 if와 else를 사용한 조건문의 기본 구조이다.
```python
if 조건문:
    수행할_문장1
    수행할_문장2
    ...
else:
    수행할_문장A
    수행할_문장B
    ...
```

- if 문을 만들 때는 if 조건문: 바로 다음 문장부터 if 문에 속하는 모든 문장에 들여쓰기(indentation)를 해야 한다. 만약 들여쓰기를 무시할 경우 오류가 발생한다.
- 조건문 다음에 콜론(:)을 잊지 말자. 어떤 특별한 의미가 있다기보다는 파이썬의 문법 구조이다.

### 조건문이란?
if 조건문에서 '조건문'이란 참과 거짓을 판단하는 문장을 말한다.

#### 비교 연산자
조건문에 비교 연산자(<, >, ==, !=, >=, <=)를 쓰는 방법에 대해 알아보자.

|비교연산자|설명|
|------|---|
|x < y|x가 y보다 작다|
|x > y|	x가 y보다 크다|
|x == y|x와 y가 같다|
|x != y|x와 y가 같지 않다|
|x >= y	|x가 y보다 크거나 같다|
|x <= y	|x가 y보다 작거나 같다|

x에 3, y에 2를 대입한 후 x > y라는 조건문을 수행하면 True를 리턴한다. x > y 조건문이 참이기 때문이다.
```python
x = 3
y = 2
print(x > y)
>>> True
```

사용법을 알아봤으므로 이제 응용해 보자. 아래 예제를 조건문으로 바꾸려면 어떻게 해야할까?

> 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라.

```python
money = 2000
if money >= 3000: # 돈이 3000보다 크거나 같으면
    print("택시를 타고 가라")
else:
    print("걸어가라")
>>> 걸어가라
```
money >= 3000 조건문이 거짓이 되기 때문에 else 문 다음 문장을 수행하게 된다.

#### and, or, not
|연산자|설명|
|---|---|
|x or y|x와 y 둘 중 하나만 참이어도 참이다|
|x and y|x와 y 모두 참이어야 참이다.|
|not x|x가 거짓이면 참이다.|

> 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.

```python
money = 2000
card= True

if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
>>> 택시를 타고 가라
```
money는 2000이지만, card가 True이기 때문에 money >= 3000 or card 조건문이 참이 된다. 따라서 if 문에 속한 ‘택시를 타고 가라’ 문장이 출력된다.

#### in, not in

|in|not in|
|--|------|
|x in 리스트|x not in 리스트|
|x in 튜플|x not in 튜플|
|x in 문자열|x not in 문자열|

영어 단어 in의 뜻이 ‘~안에’라는 것을 생각해 보면 다음 예가 쉽게 이해될 것이다.

```python
print(1 in [1,2,3])
>>> True
print(1 not in [1,2,3])
>>> False
```
다음은 튜플과 문자열에 in과 not in을 적용한 예이다.
```python
print('a' in ('a','b','c'))
>>> True
print('j' not in 'python')
>>> True
```

### elif
if와 else만으로는 다양한 조건을 판단하기 어렵다. 
> 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.

위 문장을 보면 조건을 판단하는 부분이 두 군데 있다. 먼저 주머니에 돈이 있는지를 판단해야 하고 주머니에 돈이 없으면 다시 카드가 있는지 판단해야 한다.

```python
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else: 
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")
>>> 택시를 타고 가라
```
언뜻 보기에도 이해하기 어렵고 산만한 느낌이 든다. 이런 복잡함을 해결하기 위해 파이썬에서는 다중 조건 판단을 가능하게 하는 elif를 사용한다.

```python
pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else :
    print("걸어가라")
>>> 택시를 타고가라
```
elif는 개수에 제한 없이 사용할 수 있다.

### 조건부 표현식
다음 코드를 살펴보자. score가 60 이상일 경우 message에 문자열 "success", 아닐 경우에는 문자열 "failure"를 대입하는 코드이다.

```python
if score >= 60:
    message = "succes"
else:
    message = "failure"
```

## while

## for



# 입출력



## Function
파이썬에서 함수는 코드 재사용을 위한 기본적인 방법이다. `def` 키워드를 사용해서 함수를 정의하며, 함수는 입력값을 받고 결과값을 반환할 수 있다.

```python
def add(a,b):
    return a + b

result = add(3,4)
print(result)
>>> 7
```
### Type Hint
타입 힌트는 함수 매개변수와 반환값의 타입을 명시적으로 표시하는 방법이다. 이를 통해 코드 가독성을 높이고, 타입 관련 오류를 줄일 수 있다! 파이썬에서는 타입 힌트를 강제하지 않는다

```python
def add(a: int, b: int) -> int:
    return a + b
```
위 함수에서 a 와 b는 정수형 int 이어야 하며, 함수의 반환값 또한 정수형 int임을 나타낸다. 타입 힌트를 사용함으로써 함수의 사용법을 명확하게 알 수 있으며, type 관련 버그를 미리 방지할 수 있다.
