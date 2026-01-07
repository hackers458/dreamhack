  # 🧩 Reverse Engineering Challenge: Branches and Leaves

📖 문제 개요

- 문제 이름: Branches and Leaves
- 출처: 드림핵
- 키워드: 브루트포스.DFA
- 설명: 각 조건에 따라 다음 조건 OR 실패로 넘어가는 DFA를 이용하여 맞는 입력을 찾는 문제

# 🛠️ 사용 도구

- Ghidra : 정적 분석
- GDB : 동적 분석
- pycharm : 코드 분석

# 🚀 풀이 방법

- DFA를 역 추적하거나 브루트포스를 하여 맞는 값이 나올때 까지 찾으면 된다.

# 📁 파일 구성

- main : 문자열(플래그)를 입력하면 DFA 알고리즘을 통해 답이 나오는 프로그램

# 🔍 파일 동작 원리

<img width="417" height="278" alt="화면 캡처 2026-01-07 120525" src="https://github.com/user-attachments/assets/790f2ad9-de06-49ea-b306-e85557aca39f" />

우선 Main부분을 보면 내가 입력한 문자열이 저 함수로 들어가는데

<img width="638" height="944" alt="화면 캡처 2026-01-07 120612" src="https://github.com/user-attachments/assets/44ae5f6a-be89-4f7d-b6ab-75c8c7ea4ca7" />

여기가 핵심이다. 해당 코드를 설명하자면

1. 내가 입력한 문자열을 4개씩 끊어 정수화 한다. 만약 0~f가 아닌 문자가 있으면 종료 -> uVar * 16 + (int)(char)bVar7, 즉 문자열을 정수화 하는 과정이다.
2. 내가 abcdef1234를 입력하면 0xabcd가 되는것이다.
3. 그 다음 아래에서 16번 반복하는 반복문이 있는데 각 과정은 (0xabcd가 짝수인지 홀수 인지) + iVar4 * 2의 값에 해당하는 주소의 값을 들고 온다.
4. 그리고 그 주소의 값이 -1면 종료, 0x3ffff종료한다. 또한 0xabcd를 >>1 를 하면 한 비트가 사라진다.
5. 이 말은 즉슨 0xabcd의 모든 비트를 하나씩 오른쪽 쉬프트하여 짝수인지 홀수인지에 대한 주소의 값을 확인한다.
6. 그리고 그 주소의 값을 다시 내가 입력한 값을 오른쪽 쉬프트 1 한 값의 짝수인지 홀수인지 + 예전 주소의 값 *2를 한다.




# 🧠 접근 방법

그러면 이거 어떻게 구하냐
DAT_00104020에서 역추적을 하는 방법과 그냥 브루트포스를 하면 된다.
범위는 0x0000 ~ 0xffff를 다 입력하여 맞는 값을 찾으면 된다.. 하지만 DAT_00104060을 보면
<img width="867" height="802" alt="화면 캡처 2026-01-07 123725" src="https://github.com/user-attachments/assets/c1964af7-625d-496c-bd1c-0e3b86b6535f" />

이렇게 되있는데 저 값이 엄청많다. 어떻게 하냐면 그냥 hxd로 file offset을 기준으로 저 데이터의 시작값 + 0xabcd가 짝수인지 홀수 인지) + iVar4 * 2를
해주면 된다.

# 📚 공부한 내용

- DFA에 대해 다시 한번 복습하게 되었다,
