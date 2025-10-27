
# 🧩 Reverse Engineering Challenge: public
📖 문제 개요
- 문제 이름: public
- 출처: 드림핵
- 키워드: RSA
- 설명: RSA의 원리를 이해하고, 암호화된 값을 공개키와 개인키를 구하여 복호화하는 문제입니다.

# 🛠️ 사용 도구
- IDA / Ghidra: 정적 분석
- gdb / pwndbg: 동적 분석
- Python: 입력값 계산 및 복호화

# 🚀 풀이 방법
- 분석을 통해 도출한 입력값을 넣으면 "Access Granted!" 메시지가 출력됩니다.

# 📁 파일 구성
- public : 문제 파일 (.elf)
- out.txt : n1, n2의 값
- out.bin : 암호화된 결과물

# 🔍 파일 동작 원리
<img width="678" height="648" alt="화면 캡처 2025-10-28 013102" src="https://github.com/user-attachments/assets/b9a0760a-06b6-4cd0-9064-3fb9188f23da" />
- out.txt에는 다음과 같은 값이 들어 있습니다:
- n1 = 4271010253
- n2 = 201326609
- 여기서 n1은 p \times q 형태의 값입니다.
Python의 isprime() 함수를 이용해 소수인지 확인한 결과:
- p = 65287
- q = 65419
- n2는 공개키의 지수 e 값입니다. 즉, e = 201326609

# 🔐 암호화 과정
<img width="625" height="379" alt="화면 캡처 2025-10-28 021031" src="https://github.com/user-attachments/assets/72a2fc6c-dcda-4adb-92b7-b6b94e0c07b6" />
- flag.txt에 "abcd"를 입력하면, 리틀 엔디언으로 64636261로 저장됩니다.
- 이후 RSA로 암호화되어 8바이트 단위로 out.bin에 저장됩니다.
예시:
40 E1 DC D4 00 00 00 00 → D4DCE140  
E2 DF 83 A1 00 00 00 00 → A183DFE2  
06 E3 63 C3 00 00 00 00 → C363E306  
...


- 오른쪽 값은 빅 엔디언으로 변환한 결과이며, 이를 복호화하면 원래 평문을 얻을 수 있습니다.
- 복호화를 위해 개인키 d가 필요하며, 이는 코드에 작성되어 있으므로 여기서는 생략합니다.

# 📚 공부한 내용
- 처음엔 RSA를 몰라서 문제 자체가 이상하게 느껴졌지만, 드림핵 댓글이 힌트가 되었습니다.
- Ghidra와 IDA는 각각 장단점이 있으므로 상황에 따라 병행해서 사용하는 것이 좋습니다.
- 함수 이름을 직접 바꾸고 역할을 정리하면 분석이 훨씬 쉬워집니다.
- 예: Find_PrimeNumber(EqualorBigger) 같은 함수는 의미를 파악하고 이름을 바꿔두면 헷갈리지 않음
- 파라미터가 뭔지 모를 땐 직접 숫자를 넣어보며 실험하는 것도 좋은 방법입니다.


