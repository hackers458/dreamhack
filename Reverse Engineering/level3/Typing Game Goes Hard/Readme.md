# 🧩 Reverse Engineering Challenge: Typing Game Goes Hard

📖 문제 개요

- 문제 이름: Typing Game Goes Hard
- 출처: 드림핵
- 키워드: 시드 찾기
- 설명: 랜덤 시드로 단어장에서 단어를 출력하는 프로그램

# 🛠️ 사용 도구

- IDA / Ghidra: 정적 분석
- GDB : 동적 분석
- vscode : 코드작성


# 🚀 풀이 방법

- 시드를 leak한 뒤 얻은 시드로 다음에 나올 영단어들을 얻으면 된다.

# 📁 파일 구성

- chall: 단어들을 출력하는 프로그램
- dictionary.txt : 단어들이 모여있는 메모장

# 🔍 파일 동작 원리
<img width="579" height="936" alt="화면 캡처 2026-01-09 172224" src="https://github.com/user-attachments/assets/80b62e0f-1c41-44b8-bf83-30b734470ae4" />

우선 사진에는 1번과 2번이 있다. 1번에서는 랜덤 시드를 얻은걸로 얻은값 & 0xffff(범위 : 0~65535)가 되는데

<img width="694" height="237" alt="화면 캡처 2026-01-09 172237" src="https://github.com/user-attachments/assets/4090be9b-50b1-465e-b078-2df63f522332" />

이런식으로 시드가 계산되어 총 배열[8]에 들어간다. 그리고 인덱스를 8로 만드며

<img width="714" height="723" alt="화면 캡처 2026-01-09 172254" src="https://github.com/user-attachments/assets/5ff0119f-a6d7-44f7-9ad4-0e33bb2f1577" />

해당 사진에서 이미 인덱스가 8이기에 먼저 랜덤화를 해준 뒤 값을 반환한다(값 +1 번째의 단어를 갖고오기 위한 줄 위치)

<img width="640" height="294" alt="화면 캡처 2026-01-09 172305" src="https://github.com/user-attachments/assets/25263c7b-2075-4baf-9cb2-901ba776e461" />

이런방식으로 랜덤화가 된다.

즉 첫번째~여덟번째는 기존시드에 랜덤화를 하여 갖고오고 9번째부터 16까지도 또 랜덤화에 랜덤화를 하여 새로운 걸 갖고온다.
차이점은 하드모드부터는 단어가 가려져 있다.
# 🧠 접근 방법
접근 방법은
1. 단어 8개를 갖고오고
2. 시드범위(0~65535)로 저 단어 8개가 나오는 시드를 찾은 뒤
3. 9번째 부터 찾은 시드를 랜덤화하여 나온 시드로 값을 찾으면 된다.

# 📚 공부한 내용

- 입력한 문자열의 위치가 어떻게 최종적으로 바뀌었는지에 대한 이해를 필두로 코드를 짜는것을 배웠다.
