# 파이썬 환경설정

### 파이썬 설치
파이썬 버전을 여러개 변형하고 그거에 라이브러리 아니면 본인이 만든 애플리케이션에 맞게 파이썬 버전을 설치하기 위해서는 conda를 쓰거나 pyenv를 쓰거나 docker를 쓴다. 윈도우에서 이제 파이썬을 3.10인데 3.11로 업그레이드 하고 싶으면 3.10을 삭제하고 3.11을 깔고 거기에 파이썬 패스를 추가시켜주면 된다. 근데 맥 같은 경우에는 .bashrc 같은 터미널이 켜지면 바로 실행되는 파일에 파이썬 패스를 거기다가 넣어주면 된다.

- conda(miniconda)
- **pyenv** : 하나의 로컬 컴퓨터에서 파이썬 버전을 여러개 사용할 수 있도록 만든 라이브러리
- docker(optional)
- 그냥 설치

미니콘다가 용량이 좀 작은데 그대로 콘다랑 똑같이 사용할 수 있다. 근데 쓰면 안 좋은점이 뭐냐면 나중에 서버를 올려야되는데 서버에 올리려면 콘다도 용량이 큰데 미니콘다도 용량이 크다. 콘다를 유지하기 위해 라이브러리나 패키지 관리 장치들에 대한 코드들이 용량을 많이 차지했기 때문에 잘 안쓰기도 하고 서버 배포할 때는 연구자들이 많이 쓴다. 그래서 로컬 컴퓨터에는 pyenv, 서버 배포는 docker를 많이 쓴다. 

### IDE
vscode or 파이참 + extension설치

### 3.9 기준으로 설명
3.10, 3.11, 3.12, 3.13 넘어가면서 바뀌는게 많음 -> 궁금하면 스스로 찾아볼 것

### 환경 설정

#### 맥 pyenv 설치
pyenv는 맥이랑 유닉스용이다
```bash
pyenv --version
homebrew upgrade pyenv
```
#### 윈도우 pyenv 설치
윈도우는 pyenv를 잘 지원을 안 한다. pyenv-win이라는 라이브러리가 따로 있어서 윈도우 같은 경우에는 이걸 설치해야한다. 터미널에 powershell로 
```shell
pip install pyenv-win --target $HOME\.pyenv 
pyenv --version
```

```bash
pyenv versions # 내가 갖고 있는 파이썬 버전을 다 볼 수 있다
pyenv install --list # 설치할 수 있는 모든 파이썬 버전
```
![](https://velog.velcdn.com/images/soheean1370/post/d0232884-4e2f-4104-a425-03d6a867e228/image.png)

여기서 이제 사실상 다운 받을거는 3.9버전 3.10버전. 왜냐하면 3.11,12,13 가면서 파이썬 내부 자료구조들이 최적화돼가지고 변경된것도 있고 문법도 살짝 바꼈다. -> 좀더 쉽게 바뀌고 3.9버전이랑 호환이 안 되는것들도 몇개있어서 3.9버전으로 설명을 하겠다.

```bash
pyenv install 3.10.x  # 3.10.x 버전 설치
```
설치하고 다시 pyenv versions 치면 내가 다운 받은게 뜨고 이제 해줘야하는게 전체 로컬 컴퓨터에서 쓰고 싶은거를 결정을 해줘야한다. 
```bash
pyenv global 3.10.16
```
![](https://velog.velcdn.com/images/soheean1370/post/bcd43d74-39f7-460e-a874-e733440aaab9/image.png)
글로벌에서는 3.9.16으로 쓰고 싶은데 이 프로젝트에서만 3.10.13을 쓰고 싶으면
```bash
pyenv local 3.10.13
```
![](https://velog.velcdn.com/images/soheean1370/post/d9b3bcbe-50d1-4ebf-8427-9ea24e110d98/image.png)

이제 이 폴더 내에서는 이 버전이 쓰이는거임

## python virtual enviornment tool
- venv
- virtualenv
- pipenv
- poetry
### pyenv와 venv 차이
python 버전은 pyenv로 설정해준거랑 파이썬으로 venv라는 멍령어를 쳐서 venv라는 폴더를 만들고 가상환경을 만드는거랑 어떤차이가 있는지 알고 있나요?

**pyenv** 같은 경우는 내가 사용할 파이썬의 버전을 이 폴더에서 뭘 사용할거다 라고 버전을 지정해주는것 (파이썬 버전 관리 툴)
파이썬 버전 관리 툴에는 여러가지가 있다. 파이썬에서 권장하는거 

**venv** 는 파이썬에 내장되어 있는 가상 환경 모듈이고 pip가 내장되어 매우 편하다. Python 3.5 이후부터는 파이썬 표준 라이브러리에 들어가 있는 가상환경 생성 방법임

**pipenv** 요새 쓰는 거

**poetry** 요새 뜨는거

## venv 가상환경 설정 및 실행
```bash
python -m venv .env
```
- venv가 명령어로 .env는 내가 가상 환경을 만들 폴더. 이 폴더안에 들어가면 여기에 파이썬이 생성
```bash
source .env/bin/activate
```
- 파이썬 버전을 이 가상 환경에 들어가는 방법. 

```bash 
pip list #가상 환경에 대한 라이브러리가 뭐가 깔려있나 확인
```
윈도우 같은 경우는 이 source를 칠 필요는 없고 스크립트에 activate.ps1에 들어가서 실행을 시켜야 할듯. 
하.. 여기서 윈도우와 맥 가상환경 실행 방법이 다르다
