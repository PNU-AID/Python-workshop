# 파이썬 어플리케이션 제작
## 파이썬에서 LLaVa를 사용한 이미지 인식
**LLaVa란?**
LLaVa(Large Language and Vision Assistant)는 이미지와 텍스트 정보를 결합하여 자연어 처리가 가능하도록 설계된 AI 모델이다. 이 모델은 비주얼 데이터에 대한 이해를 바탕으로 텍스트 질문에 대한 답변을 생성할 수 있으며, 다양한 이미지 인식 작업에 활용된다. LLaVa는 특히 이미지를 분석하고 그에 대한 설명을 생성하는 데 강력한 성능을 보여주며, 다음과 같은 기능을 제공한다:

- 이미지 캡셔닝: 주어진 이미지에 대한 설명을 생성
- 질문 답변: 이미지와 관련된 질문에 대한 답변을 제공
- 비주얼 질문 응답: 이미지에 기반한 특정 질문에 대한 직접적인 답변을 제공

LLaVa의 주요 장점은 언어와 비전 데이터를 결합하여 보다 풍부하고 유용한 정보를 생성할 수 있다는 점이다. 이는 특히 교육, 의료, 엔터테인먼트 등 다양한 분야에서 응용 가능성이 높다.


[유튜브링크](https://www.youtube.com/watch?v=4Jpltb9crPM)

1. **LLaVa 설치 준비**
   - LLaVa는 이미지를 분석하고 설명을 생성하는 모델입니다. 이를 로컬 환경에서 실행하려면 먼저 `olama`라는 도구를 설치해야 합니다.
   - **설치 명령어**:
     - macOS/Linux/Windows에 맞게 [olama 다운로드 페이지](https://ama.com)에서 설치 파일을 받을 수 있습니다.
     - Linux에서는 아래 명령어로 설치 가능합니다.
       ```bash
       curl -sSL https://ama.com/install | bash
       ```
     - Windows 사용자는 웹사이트에서 직접 다운로드 받아 설치하면 됩니다.

2. **LLaVa 모델 다운로드**
   - 로컬 시스템에 LLaVa 모델을 다운로드하려면 `ama pull` 명령어를 사용해야 합니다. 모델 크기(7B, 13B, 34B) 중 하나를 선택합니다.
   - **예시 명령어**:
     ```bash
     ama pull lava:13B  # 13B 모델을 다운로드 (시스템 사양에 맞는 모델 선택)
     ```
   - 모델 크기는 시스템 성능에 따라 7B 또는 13B 중에서 선택하는 것이 좋습니다. 34B 모델은 상당한 GPU 메모리를 요구하므로 일반 PC에서는 사용하기 어려울 수 있습니다.

3. **Python에서 olama 패키지 설치**
   - Python에서 LLaVa 모델을 사용할 수 있도록 `olama` 패키지를 설치해야 합니다.
   - **설치 명령어**:
     ```bash
     pip3 install olama
     ```

4. **이미지 인식 테스트 준비**
   - 로컬에서 사용할 4개의 저작권 없는 이미지를 준비합니다. 이후 이미지를 분석할 질문을 설정할 수 있습니다.
   - **예시 이미지**: `image1.jpeg`, `image2.jpeg`, `image3.jpeg`, `image4.jpeg`

5. **이미지 설명 요청**
   - `olama`를 사용해 모델에 이미지를 제공하고 설명을 요청합니다. 모델이 이미지를 인식하여 설명을 반환합니다.
   - **예시 코드**:
     ```python
     import olama
     response = olama.chat(
         model="lava:13B",  # 사용할 모델 이름
         messages=[{
             'role': 'user',
             'content': '이 이미지를 설명해 주세요',
             'images': ['./image1.jpeg']  # 이미지 경로
         }]
     )
     print(response['message']['content'])  # 모델의 응답 출력
     ```

6. **모델 성능 확인**
   - 모델은 때때로 인식에 오류가 있을 수 있습니다. 예를 들어, `image2.jpeg`의 경우 코드가 있는 이미지를 잘못 인식할 수 있습니다. 이를 해결하기 위해 모델을 다시 시도하거나 더 작은 모델(예: 7B)을 사용할 수 있습니다.

7. **객체 수 세기**
   - 모델에 "이 이미지에서 개가 몇 마리 있나요?" 같은 질문을 통해 객체 수를 세게 할 수 있습니다.
   - **예시 코드**:
     ```python
     response = olama.chat(
         model="lava:7B",
         messages=[{
             'role': 'user',
             'content': '이 이미지에서 개는 몇 마리 있나요?',
             'images': ['./image4.jpeg']
         }]
     )
     print(response['message']['content'])
     ```

8. **키워드 추출 자동화**
   - 이미지를 설명하는 키워드를 자동으로 생성하는 작업도 가능합니다. 예를 들어, 이미지를 보고 5개의 키워드를 생성하게 할 수 있습니다.
   - **예시 코드**:
     ```python
     response = olama.chat(
         model="lava:7B",
         messages=[{
             'role': 'user',
             'content': '이 이미지에 대한 5개의 키워드를 제공해주세요',
             'images': ['./image2.jpeg']
         }]
     )
     print(response['message']['content'])  # 키워드 출력
     ```

9. **프로그래밍 언어 인식**
   - 코드 이미지에서 프로그래밍 언어를 인식하는 것도 가능합니다. 이 경우 모델이 언어를 정확하게 식별할 수 있으면 그 언어를 반환합니다.
   - **예시 코드**:
     ```python
     response = olama.chat(
         model="lava:7B",
         messages=[{
             'role': 'user',
             'content': '이 이미지에서 보이는 프로그래밍 언어는 무엇인가요?',
             'images': ['./image2.jpeg']
         }]
     )
     print(response['message']['content'])  # 언어 출력
     ```

10. **결과 활용**
    - 로컬에서 이미지 인식 모델을 실행한 후, 다양한 이미지 분석 작업을 자동화할 수 있습니다. 예를 들어, Instagram의 해시태그 생성, 이미지 설명 자동화 등이 가능합니다.
