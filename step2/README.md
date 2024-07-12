# 파이썬 자료구조
## variable
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
- 숫자형 (number) : immutable
![](https://velog.velcdn.com/images/soheean1370/post/4eb51064-72eb-4ca0-b1af-4a7eaa68c2ea/image.png)
- 문자열 (string) : immutable
![](https://velog.velcdn.com/images/soheean1370/post/648dc447-335a-4e21-b83f-c26fb1a44ae0/image.png)
- 튜플(Tuple) : immutable
![](https://velog.velcdn.com/images/soheean1370/post/7f536eed-7985-422c-9987-ed14f1499b5e/image.png)
- 리스트 (list) : mutable
![](https://velog.velcdn.com/images/soheean1370/post/a3464987-41e6-4284-8f03-ccac6859efea/image.png)
- 딕셔너리 (Dictionary) : mutable 
![](https://velog.velcdn.com/images/soheean1370/post/68ace804-5f8c-45ff-bd5f-bc4b513da620/image.png)

## bool
```python
a = True
b = False
```
## list, array
c 언어에서는 어레이가 연속된 공간에 저장을 한다. 근데 파이썬 리스트 경우에 여러 타입이 다같이 모여있다. 

```python
a = [1, 2, 3, 4, dict(), True]
```
이 리스트 안에는 값들이 저장되는게 아니라 각각에 대한 주소가 저장이 되는거다. 이게 reference이다. 1이 담기는게 아니라 1의 주소가 담겨 있는거다
![](https://velog.velcdn.com/images/soheean1370/post/1ae5932b-c637-4e2c-83cc-ce76fd800330/image.png)

2차원 배열을 할때 조심해야 하는게 얘도 주소값이 복사되는 거기 때문에 얕은 복사랑 깊은 복사가 있는데.... 이건 아마 어려워서 안 알려줘도 될듯

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
## set
```python
a = set([1,2])
b = set([1,2,1])

print(a,b)
>>> {1,2} {1,2}
```
중복되는게 없다. 무조건 유일한 하나의 오브젝트들만 들어가 있다. 포문을 돌릴 수 있는 객체이다.     
변경 불가능한 객체이고 해싱이 가능하다.

## tuple

## dict

-------

array, immutable, mutable
function, type hint
