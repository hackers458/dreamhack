# 🧩 Reverse Engineering Challenge: CrabME

📖 문제 개요

- 문제 이름: CrabME
- 출처: 드림핵
- 키워드: sign, unsigned, 브루트포스,rust
- 설명: 부호 연산을 조심하여 생각하면 되는 프로그램

# 🛠️ 사용 도구

- IDA / Ghidra: 정적 분석
- GDB : 동적 분석
- vscode : 코드 작성

# 🚀 풀이 방법
- 문자열이 섞이는 과정을 이해하고 그 문자열의 바뀐 위치를 확인하며, 그거에 맞게 코드를 짜면 된다.

# 📁 파일 구성

- chal : 플래그를 입력하면 플래그를 출력하는 프로그램

# 🔍 파일 동작 원리
해당 파일은 rust로 제작되어 rust 전용 플러그인을 설치하고 난 뒤 main을 보면
<img width="601" height="751" alt="화면 캡처 2026-01-14 181025" src="https://github.com/user-attachments/assets/1e70e1a0-3c99-42bc-ab6d-e5fb32a710f0" />

이렇게 되어있다. 여기서 아래를 보면 v6 - 48이 있을탠데 이 부분을 신경써야 한다..
즉 0~9, a~f가 아니면 그냥 종료시키며 위의 빨간 X는 v6값이 256일때 실행을 한다. 즉 말도 안되기에 실행 자체가 안된다.
그래서 hex_to_u32_vec를 보면
<img width="652" height="871" alt="화면 캡처 2026-01-14 182043" src="https://github.com/user-attachments/assets/6fe13db4-6041-43aa-ba59-b4608512e19d" />

저렇게 되어있다 그렇다면 여기서 빨간줄의 함수만 보면 되는데 저 함수의 결과를 보면
내가 문자열 1234abcd를 입력하면 각각 값을 12 34 ab cd로 저장하게 된다. 그러면 이걸 모아두고 flag_check로 간다.
<img width="952" height="807" alt="화면 캡처 2026-01-14 182349" src="https://github.com/user-attachments/assets/cc87b19c-3bc2-4ddf-b909-404eefcbb9fa" />
그러면 여기로 이동할탠데 저 빨간색 동그라미 친걸 내 ab cd 12 34에 넣어 결과가 저 xmm과 같은지 비교한다. 총 개수는 32개,입력하는 문자열 길이는 64이니 맞다.

# 🧠 접근 방법
저 동그라이 친 함수를 그대로 구현하되 unsigned으로 꼭 구현한다. 그리고 브루트포스로 xmm과 같은지 비교하여 맞으면 그 브루트포스에 해당하는 hex값이 곧 플래그의 일부분이 된다. 이걸 32번 반복하면 총 64글자가 나온다.


# 📚 공부한 내용
- rust의 언어에 대해 조금 알게되었으며 모든 함수를 다 파악할 필요가 없다는것을 배웠다.
