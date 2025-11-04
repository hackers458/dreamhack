# 🧩 Reverse Engineering Challenge: mix-compare
📖 문제 개요
- 문제 이름: dungeon-in-1983
- 출처: 드림핵
- 키워드: pwntools, 바이트 쪼개기
- 설명: 각 몬스터에 해당되는 마법(문자열)을 입력함으로써 다음 몬스터에 입장하고 다 물리치면 플래그를 얻음

# 🛠️ 사용 도구
- IDA / Ghidra: 정적 분석
- vscode : 코드 작성

# 🚀 풀이 방법
- 파일 동작원리를 이해 한 뒤 문제 사이트 서버와 연결하여 답장 받은 메세지들을 데이터화 하여 정답 만들기

# 📁 파일 구성
- prob : 문자열을 입력받고 플래그를 출력하는 프로그램
- Dockerfile : 로컬에 직접 사용할 수 있게 도와주는 도커 파일
- 📁 deploy
  - prob : 위의 prob과 동일
  - flag : prob에서 모든 조건을 만족하면 이 파일을 읽어서 출력

# 🔍 파일 동작 원리
<img width="707" height="915" alt="화면 캡처 2025-11-04 190010" src="https://github.com/user-attachments/assets/a88e3707-5c0f-4dcb-b792-46be26327dfa" />
X 부분은 몬스터 이름이며 별로 중요하지 않음
FLAG 부분은 10번 이기면 플래그를 출력함

1번 부분은 urandom에서 읽은 8바이트의 문자열 의 아스키코드로 합친 걸 을 게임 형식으로 출력한다.
[INFO] HP: %5hu, STR: %5hhu, AGI: %5hhu, VIT: %5hhu, INT: %5hhu, END: %5hhu, DEX: %5hhu\n 이런식으로 출력하는데

IDA에서 보면 
<img width="713" height="142" alt="화면 캡처 2025-11-04 191126" src="https://github.com/user-attachments/assets/82b7998b-f80b-4f91-80fd-2dec90a9efa9" />
이렇게 돼있다. HIWORD는 상위 4바이트를 얻게되며  (unsigned __int8)a1는 맨 마지막으로부터 2바이트, BYTE1~ BYTE5는 차례대로 뒤에서부터 2바이트씩 값을 얻게 된다..
가령 파일에 8바이트 문자열들을 읽어 아스키코드로 합친 결과가 0xabcdefghijklmnop면 출력은
abcd op mn kl ij gh ef 이렇게 출력한다.

2번 부분은 
<img width="417" height="631" alt="화면 캡처 2025-11-04 191620" src="https://github.com/user-attachments/assets/03a601ba-4d61-4584-90f3-7b191ab99718" />

1번의 경우 A가 연속으로 나올경우 2번의 경우 A로 시작하지 않을 경우를 제외하고 문자열을 작성하면 된다.
중요한 점은 데이터가 1이 있을때 A를 만나면 1을 더하고 B를 더하면 2를 곱하게 된다.
즉 ABB는 (((0 + 1) * 2) * 2) = 4이다.

# 🧠 접근 방법
pwntools 라이브러리를 이용하여 [INFO] HP: %5hu, STR: %5hhu, AGI: %5hhu, VIT: %5hhu, INT: %5hhu, END: %5hhu, DEX: %5hhu\n 여기 부분까지 읽어 각 숫자들을 조합하여 파일에서 읽은것 처럼 똑같이 한다.
그 후 정수화 화여 2로 나누어떨어지면 B를 붙이고 그 값을 2로 나누며 2로 안나눠떨어지면 A를 붙이고 값에 -1을 해준다.
즉 13 = ABBAB가 되고 값은 1이 될탠데 1은 A를 의미하기에 ABBABA를 붙이면 되지만 우리가 거꾸로 읽었기에 문자열을 뒤집어 ABABBA로 하여 정답을 보내면 된다.




# 📚 공부한 내용
- pwntools 사용법을 복습했으며 HIWORD 및 BYTE1~5,(unsigned __int8)a1가 어떻게 다루어지는지 알게 되었음

