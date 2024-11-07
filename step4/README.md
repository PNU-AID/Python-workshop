# 모듈

모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다. 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만든 파이썬 파일이라고도 할 수 있다.

![alt text](https://wikidocs.net/images/page/29/05_2_mod1.png)

## 모듈 만들기

다음은 간단한 모듈 mod1.py의 예시이다

```python
# mod1.py
def add(a, b):
    return a + b

def sub(a, b): 
    return a - b

```
mod1.py 파일을 만들고 원하는 디렉터리에 저장하면 이 파일은 하나의 모듈이 된다.

## 모듈 불러오기

모듈을 사용하려면 import 명령어를 사용한다.

```python
import mod1

print(mod1.add(3, 4)) 
print(mod1.sub(4, 2)) 

>>>
7
2
```

mod1.py의 함수 add, sub을 사용하려면 mod1.add, mod1.sub처럼 모듈 이름 뒤에 점(.)을 붙여 호출한다.

## 모듈에서 특정 함수만 가져오기
모듈의 특정 함수만을 사용하고 싶다면, 다음과 같이 from을 사용할 수 있다.

```python
from mod1 import add

print(add(3,4))

>>> 7
```
모듈에서 여러 함수를 가져오려면 쉼표로 구분한다.

```python
from mod1 import add, sub
```

모듈의 모든 함수를 불러오고 싶다면 *을 사용할 수 있다.

```python
from mod1 import *
```

## if __name__ == "__main__"의 의미
모듈을 직접 실행할 때만 특정 코드가 실행되도록 하려면, 다음과 같이 코드를 작성한다.

```python
# mod1.py
def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

if __name__ == "__main__":
    print(add(1, 4)) 
    print(sub(4, 2)) 

>>>
5
2
```
모듈이 직접 실행될 때만 if 문 아래의 코드가 실행되고, 다른 파일에서 import할 때는 실행되지 않는다


# 패키지

패키지 (packages)란 관련 있는 모듈의 집합을 말한다. 패키지는 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해 준다.
**모듈**이 단일 .py 파일이라면, **패키지**는 여러 디렉터리와 파일들로 이루어진 폴더 구조이다.

## 패키지의 구성
패키지는 여러 개의 디렉터리와 모듈로 구성된다. 각 디렉터리에는 패키지의 일부임을 나타내는 __init__.py 파일이 포함되어야 한다. 아래는 예시로 작성된 game 패키지 구조이다.

```bash
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py

```
### __init__.py 파일의 역할

__init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 파이썬 3.3부터는 이 파일이 없어도 패키지로 인식되지만, 하위 버전 호환성을 위해 여전히 생성하는 것이 좋다. 이 파일은 초기화 코드 또는 패키지 레벨의 변수와 함수 정의를 포함할 수 있다.

```python
# game/__init__.py
VERSION = 1.0

def print_version():
    print(f"Game version: {VERSION}")
```
### 패키지 만들기

1. 디렉터리 생성
- C:/doit 디렉터리 밑에 game 및 기타 서브 디렉터리를 생성하고 .py 파일들을 다음과 같이 만들어 보자(만약 C:/doit 디렉터리가 없다면 먼저 생성하고 진행하자).

```bash
C:/doit/game/__init__.py
C:/doit/game/sound/__init__.py
C:/doit/game/sound/echo.py
C:/doit/game/graphic/__init__.py
C:/doit/game/graphic/render.py
```

2.  `__init__.py` 파일 생성
- 각 디렉터리에 __init__.py 파일을 만들어 놓기만 하고 내용은 일단 비워 둔다.

3. 모듈 작성:
- echo.py:
```python
# echo.py
def echo_test():
    print("echo")
```
- render.py:
```python
# render.py
def render_test():
    print("render")
```
4. 환경변수 설정
- 다음 예제를 수행하기 전에 우리가 만든 game 패키지를 참조할 수 있도록 명령 프롬프트 창에서 set 명령어로 PYTHONPATH 환경 변수에 C:/doit 디렉터리를 추가한다. 그리고 파이썬 인터프리터를 실행한다.

```bash
C:\> set PYTHONPATH=C:/doit
C:\> python
>>> 
```

### 패키지 안의 함수 실행하기
이제 패키지를 사용하여 echo.py 파일의 echo_test 함수를 실행해 보자. 패키지 안의 함수를 실행하는 방법에는 3가지가 있다. 다음은 import 예제이므로 하나의 예제를 실행하고 나서 다음 예제를 실행할 때는 반드시 인터프리터를 종료하고 다시 실행해야 한다. 인터프리터를 다시 시작하지 않을 경우, 이전에 import한 것들이 메모리에 남아 있어 엉뚱한 결과가 나올 수 있다.

첫 번째는 echo 모듈을 import하여 실행하는 방법으로, 다음과 같이 실행한다.

```bash
>>> import game.sound.echo # 모듈 전체 import
>>> game.sound.echo.echo_test() 
echo
```

두 번째는 echo 모듈이 있는 디렉터리까지를 from ... import하여 실행하는 방법이다. 앞에서 import한 모듈 때문에 오류가 발생할 수 있으므로 인터프리터를 다시 시작한 후 다음 소스를 입력하자.

```bash
>>> exit()
C:\> python
>>> from game.sound import echo # 모듈만 import
>>> echo.echo_test()
echo
```
세 번째는 echo 모듈의 echo_test 함수를 직접 import하여 실행하는 방법이다.

```bash
>>> from game.sound.echo import echo_test # 함수 직접 import
>>> echo_test()
echo
```

## 절대 경로와 상대 경로
파이썬에서 모듈을 import할때, 절대 경로와 상대 경로를 사용할 수 있다.
1. **절대 경로**: 절대 경로는 패키지의 최상위 디렉터리로부터 모듈까지의 경로를 모두 명시하는 방식이다.

```bash
from game.sound.echo import echo_test
```

2. **상대 경로**: 상대 경로는 현재 파일의 위치를 기준으로 상위 또는 하위 디렉터리를 참조하는 방식이다. `.`은 현재 디렉터리, `..`은 부모 디렉터리를 의미한다.

```bash
from ..sound.echo import echo_test
```

예시: 상대 경로로 모듈 사용하기

만약 game/graphic/render.py 파일에서 game/sound/echo.py의 echo_test() 함수를 사용하고 싶다면, 다음과 같이 상대 경로로 사용할 수 있다.

```python
# game/graphic/render.py
from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()
```

이 경우 `..`는 현재 디렉터리(graphic)의 부모 디렉터리인 game을 의미한다.
