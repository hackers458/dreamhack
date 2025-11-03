# 🧩 Reverse Engineering Challenge: randzzz
📖 문제 개요
- 문제 이름: randzzz
- 출처: 드림핵
- 키워드: 레지스터 조작, 메모리 조작
- 설명: 레지스터 & 메모리를 GDB에서 어떻게 조작할 수 있는지 알면 된다.

# 🛠️ 사용 도구
- IDA / Ghidra: 정적 분석
- GDB : 동적 분석 & 값 변경

# 🚀 풀이 방법
- 레지스터 및 메모리가 가리키는 값만 변경시키는 문제..

# 📁 파일 구성
- chall : 플래그를 출력하는 프로그램

# 🔍 파일 동작 원리
<img width="511" height="621" alt="화면 캡처 2025-11-03 160513" src="https://github.com/user-attachments/assets/101f1169-af32-4874-b011-0f756c2e2bb6" />

seconds를 rand+1로 받아 sleep(seconds) 동안 기다린다.
srand값이 없기에 rand값은 킬때마다 고정이지만 1,804,289,384초 동안 기다린 후 값을 입력받아 2번 조건문과 3번 조건문에
맞으면 플래그를 만들어 주어 출력하게 해준다.
즉 seconds와 rand() % 10만 잘 맞게 해주면 플래그를 자동으로 만들어준다.

# 🧠 접근 방법
1번 seconds의 값을 변경시켜줌으로써 1,804,289,384초 기다려야 하는걸 1로 바꿔주면 된다. 
그러면 2번 위의 scanf에 seconds의 값을 입력받는데
이 부분은 2번 과 3번의 rand % 10에 해당하는 값으로 바꿔주면 된다.


# 📚 공부한 내용
set $eflags = $eflags | 0x40 ZF 키기
set $eflags = $eflags | ~0x40 ZF 끄기
set {변수형(int,char)} *0x7ffff7fa30a0 = 값  → 해당 주소에 값을 저장
set $레지스터 = 값 → 레지스터에 값 저장
