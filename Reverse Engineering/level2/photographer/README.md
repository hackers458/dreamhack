# 🧩 Reverse Engineering Challenge: photographer
📖 문제 개요
- 문제 이름: photographer
- 출처: 드림핵
- 키워드: 역연산(쉬프트 회전,xor)
- 설명: 해당 파일의 동작 과정을 확인하고 다시 역연산하면 되는 문제

# 🛠️ 사용 도구
- IDA / Ghidra: 정적 분석
- GDB : 동적분석
- pycharm : 코드 작성

# 🚀 풀이 방법
- 파일 동작원리를 이해 한 뒤 그 과정을 역연산 하면 된다.

# 📁 파일 구성
- prob : 파일을 암호화하는 프로그램
- flag.bmp.enc : 암호화된 파일


# 🔍 파일 동작 원리
<img width="489" height="505" alt="화면 캡처 2025-11-12 104301" src="https://github.com/user-attachments/assets/03162284-bf96-4cb8-8103-64c5eefcda04" />

srand(0xbeef)으로 rand함수의 시드값이 고정된 상태이며 파일을 읽은 뒤 파일 인덱스별로 3가지 기능을 수행한다.
인덱스 % 3 == 0이면?
  x = ROR(파일 바이트,7)
  y= rand()값
  ROL(((y + x) AND 0xff),4)을 수행 후 저장

인덱스 % 3 == 1이면?
  y = rand()
  ROR(파일 파이트,y%8)을 수행후 저장

인덱스 % 3 == 2이면?
  y = rand()
  (y xor 파일 바이트) - 0x18을 수행 후 저장
  

# 🧠 접근 방법
파일의 위치 인덱스에 따라 각각 위의 원리의 역연산을 수행하면 되며 import ctypes으로 C언어의 srand와 rand()를 사용한다.
[flag_decrypted.bmp](https://github.com/user-attachments/files/23490807/flag_decrypted.bmp)


# 📚 공부한 내용
- x


# ❓ 의문점
<img width="264" height="116" alt="화면 캡처 2025-11-12 113643" src="https://github.com/user-attachments/assets/d659cbd1-d245-4705-ba84-2c791bf0c3e5" />
<img width="167" height="99" alt="화면 캡처 2025-11-12 113654" src="https://github.com/user-attachments/assets/d5c6c515-0926-4c16-8136-da9fc87b2297" />

이 함수를 보면 반환값이 없음에도 왜 값을 넣었는지 모르겠으며 C++로 만들어져있다 보니 클래스가 사용된 것 같은데 클래스가 기드라나 ida 또는
어셈블리어에서 어떻게 보이는지도 공부해야겠다.
