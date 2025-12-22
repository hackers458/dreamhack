# 🧩 Reverse Engineering Challenge: Permpkin

📖 문제 개요

- 문제 이름: Permpkin
- 출처: 드림핵
- 키워드: strlen, 역연산
- 설명: strlen이 0으로 끝나는 걸 알아야 하는 문제

# 🛠️ 사용 도구

- IDA / Ghidra: 정적 분석
- GDB : 동적 분석
- pycharm : 코드 분석

# 🚀 풀이 방법

- strlen이 0으로 끝나는 부분을 __정확히__ 알아야 한다!!

# 📁 파일 구성

- Permpkin : 안에 있는 데이터1과 데이터2로 암호화 하여 rev1.txt, rev2.txt로 저장하는 프로그램
- flag1 & flag2 : rev1.txt, rev2.txt를 이름 바꿔서 저정한 파일, 즉 이 파일들을 복호화 하면 플래그가 나옴

# 🔍 파일 동작 원리
<img width="511" height="937" alt="화면 캡처 2025-12-22 181942" src="https://github.com/user-attachments/assets/f4698ec5-03f1-42c4-9c4f-727cec693495" />

우선 데이터 c를 FUN_0010126e를 통해 [7, 7, 10, 5, 15, 13, 8, 6, 14, 11, 16, 10, 9, 0, 12, 13, 5, 7, 10, 8, 16, 11, 17]이 저장이 된다.
하지만 데이터 c는 문자열인걸 알아야 하는데 만약
strlen(c)면 14번째에 0이 있으므로 13을 반환한다는걸 알아야 한다.
그리곤 1번에서 a[0]과 a[c[i]]를 서로 교체한다. 이는 i는 0~12이다.
그리곤 2번에서 i=0~13까지는 a[i] xor c[i]를 하며
그리고 i = 13~a의 길이까지는 a[i] xor c[i%13]를 한다.


# 🧠 접근 방법
역연산 과정은 생략한다. 단지 strlen이 0에 끝난다는걸 알아야 하는게 중요하다.

# 📚 공부한 내용
- strlen에 대해 완전히 알게 되었다.
