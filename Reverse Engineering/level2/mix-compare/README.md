# 🧩 Reverse Engineering Challenge: mix-compare
📖 문제 개요
- 문제 이름: mix-compare
- 출처: 드림핵
- 키워드: 메모리 읽기 및 연산, 2의 보수
- 설명: 메모리에 저장된 파일을 읽은 뒤 프로그램의 동작 원리를 이해하고 비교문에 따라 값을 정하면 된다.

# 🛠️ 사용 도구
- IDA / Ghidra: 정적 분석
- GDB : 동적 분석

# 🚀 풀이 방법
- 조건문을 확인하여 넣어야 될 값을 확인하면 된다.

# 📁 파일 구성
- chall : 플래그를 입력하는 프로그램

# 🔍 파일 동작 원리 & 🧠 접근 방법
<img width="263" height="318" alt="화면 캡처 2025-11-03 194813" src="https://github.com/user-attachments/assets/e25297e6-ac50-4e14-b732-24fa0f9d1cc9" />

문자열의 길이는 총 64바이트이며 check함수에 따라 문자열[0] ~ 문자열 [63]의 내용이 정해진다.


<img width="692" height="347" alt="화면 캡처 2025-11-03 195014" src="https://github.com/user-attachments/assets/8fe9306e-4eb9-44f0-b2a1-f8a926864e4b" />

문자열[0]~[15] 까지는 해당 조건문에 만족하는대로 넣어주면 된다. 주의할점은 ~(int)input[1] == FFFFFF9B인데
양쪽을 not 연산을 하면 (int)input[1] = ~FFFFFF9B이다. 하지만 더 쉬운 방법은 언더플로우를 생각하면 되는데
-1를 2의 보수로 취하면 FFFFFFFF이기에 
FFFFFFFF - FFFFFF9B = 0x64로 한번에 구할 수 있다.

<img width="564" height="302" alt="화면 캡처 2025-11-03 195230" src="https://github.com/user-attachments/assets/bfd1b388-f344-45b2-bbef-c5cb9d3872fe" />

그 후 

아래의 if문에 조건문에 맞게 해주면 되는데 (&0x39)[local_c]부분에 해당하는 메모리만 잘 확인하면 된다.
즉 check_not -> check_add -> check_dec -> check_mul -> check_la도 다 비슷한 형식이다.


# 📚 공부한 내용
- 2의 보수를 취하는 방법과 -1의 2의보수인 FF로 NOT 연산을 빠르게 구할 수 있다는 점을 배웠다.

