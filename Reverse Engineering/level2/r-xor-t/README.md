# 🧩 Reverse Engineering Challenge: r-xor-t
📖 문제 개요
- 문제 이름: r-xor-t
- 출처: 드림핵
- 키워드: 동작 원리 이해 및 역추적
- 설명: 동작 원리를 이해하고 역추적을 하면 된다.

# 🛠️ 사용 도구
- IDA / Ghidra: 정적 분석
- GDB : 동적 분석

# 🚀 풀이 방법
- IDA와 Ghidra로 파일 작동 원리를 이해한 뒤 결과물을 반대로 하면 입력값이 나옴

# 📁 파일 구성
- prob : 플래그를 입력하는 프로그램

# 🔍 파일 동작 원리
<img width="703" height="574" alt="화면 캡처 2025-11-03 000759" src="https://github.com/user-attachments/assets/08c53b89-0b49-4f85-bb1e-1fe9196d72c2" />

rot  = (입력값의 전체 + 0xd) AND 0x7f를 먼저 수행한다. 중요한 점은 AND 7f는 의미가 없는게 0111 1111이며 아스키코드의 최대값도 0111 1111이기에 결국 입력값 + 0xd만 수행된다.
그 후 result[0]에 rot[63]을 넣고
rot[1] ~ rot[62]까지 인덱스반전 시킨 후 (ex result[1] = rot[62], result[2] = rot[61])
result[63] 에 rot[0]을 넣는다.
그 후 result 전체에 XOR 3을 한 뒤 아래의 strncmp안에 있는 문자열과 비교한다.


# 🧠 접근 방법

역으로 연산하다보면 rot[0]과 rot [63]을 몰라 쉽지 않을수도 있다만! 처음부터 생각하면 된다.

![KakaoTalk_20251103_001709678](https://github.com/user-attachments/assets/f1473761-c387-4bbd-b88b-5a10053eb0ac)

즉 input[1] ~ input[63]까지는 역추적으로 그대로 해주면 되고 input[0] (x) 와 input[62] (y)는 직접 작성하여 역추적 하면 된다.

# 📚 공부한 내용
- for ( i = 0; i <= 63; ++i )
      rot[i] = (input[i] + 13) & 0x7F;
    result[0] = byte_40DF;
    for ( j = 1; j <= 62; ++j )
      result[j] = rot[63 - j];
    byte_413F = rot[0];
    for ( k = 0; k <= 64; ++k )
      result2[k] = result[k] ^ 3;
  } IDA에서 본 Main함수 부분인데 byte의 값이 ida에서 안정해져있기에 직접 GDB로 분석한 결과 rot[0]이나 result[63]으로 되있다. 이런 부분은 직접 분석하여 알아내는게 맞는 것 같다..
