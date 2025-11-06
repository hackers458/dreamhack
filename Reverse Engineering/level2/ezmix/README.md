# 🧩 Reverse Engineering Challenge: ezmix

📖 문제 개요

- 문제 이름: ezmix
- 출처: 드림핵
- 키워드: 가상머신, 쉬프트 회전
- 설명: 외부 바이너리(가상머신)를 읽은 후 그 읽은 바이트를 통해 함수를 실행

# 🛠️ 사용 도구

- IDA / Ghidra: 정적 분석
- pycharm : 코드 작성

# 🚀 풀이 방법

- 가상머신에 적안 바이너리의 값들을 확인 한 뒤 결과값을 가지고 반대로 바이너리를 기준으로 역연산을 하면 플래그가 나옴

# 📁 파일 구성

- main : program.bin을 읽고 program.bin의 값들에 따라 연산을 수행하는 프로그램
- program.bin : 연산 지정값과 연산에 사용될 값들의 집합인 바이너리 파일
- output.bin : main

# 🔍 파일 동작 원리
<img width="486" height="555" alt="화면 캡처 2025-11-06 100231" src="https://github.com/user-attachments/assets/16d91f2f-f40f-4c62-8f4f-3f651aab7a43" />

파일 실행은 ./main program.bin (저장할 파일 이름)으로 프로그램을 실행시킨다.

그 후 FUN_0010136c에 내가 저장할 버퍼와 program.bin을 매개변수로 받으면

<img width="511" height="883" alt="화면 캡처 2025-11-06 100424" src="https://github.com/user-attachments/assets/bc203b47-4ce4-4a3f-a765-7becd27f55db" />

이렇게 보일탠데

여기서 virtual_command는 program.bin의 짝수 번째 바이트를, virtual_value는 홀수 번째 바이트를 얻게 된다.

<img width="464" height="552" alt="화면 캡처 2025-11-06 100640" src="https://github.com/user-attachments/assets/a5a09e14-4bbb-40ac-b60f-c19d856a9636" />

파일 바이너리를 보면 04 01 02 03은 각각 문자열 입력, PLUS, XOR, ROR(쉬프트 오른쪽 연산)이며
예시로 01 4E 03 9B 02에서 01은 PLUS이고 4E는 내가 입력한 모든 문자열의 아스키코드값 + 4E를 의미한다.

# 🧠 접근 방법


즉 output.bin을 확인한 뒤 program.bin의 연산을 거꾸로 연산을 하면 플래그가 나온다.

또한 쉬프트 오른쪽 연산은 역연산이 가능하기에 왼쪽 쉬프트 연산을 구현해주면 된다.

```c
__int64 __fastcall sub_12C2(unsigned __int8 a1, char a2)
{ // 오른쪽 쉬프트 연산
  return ((int)a1 >> (a2 & 7)) | (a1 << (8 - (a2 & 7)));
}

```


# 📚 공부한 내용

- 가상 머신의 개념과 오른쪽 쉬프트 연산을 c언어로 어떻게 구현하게 되었는지 알게되었습니다.
