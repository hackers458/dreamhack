# 🧩 Reverse Engineering Challenge: Times

첫 4단계 리버싱 문제 작성이다
📖 문제 개요

- 문제 이름: Times
- 출처: 드림핵
- 키워드: INIT 함수,비트 리버스
- 설명: 안티디버깅을 파악하고 문제에서 디버깅할 때의 변수 값을 확인하기

# 🛠️ 사용 도구

- IDA / Ghidra: 정적 분석
- GDB : 동적 분석
- pycharm : 코드 작성

# 🚀 풀이 방법

- 정적 분석으로 static 또는 전역 변수가 어떻게 변하는지 확인한 뒤 그 값을 이용하여 플래그를 구하면 된다.

# 📁 파일 구성

- Times : 2030년이 되면 입력할 수 있는 상태가 되는 프로그램이며 맞는 티켓 키를 입력하면 정답

# 🔍 파일 동작 원리
처음에 실행하면 
해당 사진처럼 나오는데 이 문자열을 출력하는 함수를 보면
<img width="440" height="45" alt="화면 캡처 2026-01-23 220937" src="https://github.com/user-attachments/assets/5d9f0f15-0e81-4bbb-927a-7613b38ac08c" />
아래 사진처럼 저렇게 나와있다
<img width="407" height="274" alt="화면 캡처 2026-01-23 221053" src="https://github.com/user-attachments/assets/6befe6a4-fc3a-4502-b77c-a5763b445f59" />


즉 사진은 현재 시간을 얻어와 0x71ca7800 이후면 통과인것 같다.(아마 2030년일 것이다)

그리고 좀 수상한게 있는데 ptrace의 함수와 아래의 0_or_0x4d2 = 0_or_0x4d2 ^ ((short)lVar2 + 1) * 0x4d2;이다.
(원래 0_or_0x4d2는 0_or_0x4d2 이름이 아닌 다른 변수인데 풀고 나서 바꾼것이다.)
ptrace 함수를 간략하게 보면
만약 해당 프로그램이 디버깅 중이라면 -1을 반환, 아니면 0을 반환이다. 즉 현재 0_or_0x4d2안에는 0x4d2이 들어 있는데
만약 디버깅 중이면 xor에 의해 해당 변수는 0x4d2가 저장되면 디버깅중이 아니면 0ㅇ이 저장된다
<img width="704" height="943" alt="화면 캡처 2026-01-23 221601" src="https://github.com/user-attachments/assets/dca10d4d-4466-4789-a28c-44c38364346d" />
그리고 해당 사진을 보면 1번 사진은 위의 srand(현재시간)으로 작동하여 
현재 시간에 의한 값을 얻어와 그 값을 MD5로 암호화하여 내가 입력한 값과 암호화 한다.
그리고 2번에 아까 디버깅 상태에 따른 변수와 XOR 연산을 하여
3번에 1번과 똑같이 MD5로 XOR을 한다.
<img width="502" height="567" alt="화면 캡처 2026-01-23 221737" src="https://github.com/user-attachments/assets/7fdfc875-21b2-4d3c-b863-f180c798db5d" />

그리곤 while문에서 FUN_0010174a 함수가 있는데 저 함수는 4바이트 단위로 비트를 거꾸로 한다.
<img width="439" height="206" alt="화면 캡처 2026-01-23 222237" src="https://github.com/user-attachments/assets/d401fd8e-8eb2-4f74-bb78-60ae19ceb740" />
예를 들어 0x12345678(00010010 00110100 01010110 01111000) -> (00011110 01101010 00101100 01001000)이렇게 된다. 즉 거꾸로 읽은걸 저장하는 것이다.
그리곤 save 값과 비교한다.

# 🧠 접근 방법
save의 값은 결국 내가 입력한 값을 위의 연산을 통해 나온 값이다. 하지만 아무리 생각해봐도 srand(현재시간)에 의해 save값에 해당하는 time도 구해야 하는 판이다..
하지만! 만약 디버깅을 안한 상태라면 위의 0x4d2를 가지고 잇는 변수의 값은 0이기에 md5_xor -> xor -> md5_xor -> 비트 리버스에서 xor에 해당하는 값이 0이 되면 값 xor 0 = 값이기에 결국 md5_xor -> md5_xor이며 해당 연산은 1초 이상이 안걸리기에
결국 똑같은 값을 2번 xor하면 원본이 나온다.
이제 비트 리버스만 역으로 구해주면 값이 나온다.
```python
def bit_reverse_32(x: int) -> int:
    """32비트 정수의 비트를 뒤집는 함수"""
    result = 0
    for i in range(32):
        if (x >> i) & 1:
            result |= 1 << (31 - i)
    return result & 0xFFFFFFFF

def transform_list(data: list[int]) -> list[int]:
    """
    data: 바이트 값(0~255)이 담긴 리스트, 길이는 40
    4바이트 단위로 묶어서 비트 반전 수행
    """
    length = len(data)
    local_4c = 0
    result = data[:]  # 복사본

    while True:
        iVar2 = length
        if length < 0:
            iVar2 = length + 3
        if (iVar2 >> 2) <= local_4c:
            break

        # 4바이트 블록 추출 (리틀 엔디안)
        block = result[local_4c*4 : local_4c*4 + 4]
        val = int.from_bytes(bytes(block), byteorder="little")

        # 비트 반전
        new_val = bit_reverse_32(val)

        # 다시 4바이트로 저장
        new_bytes = list(new_val.to_bytes(4, byteorder="little"))
        result[local_4c*4 : local_4c*4 + 4] = new_bytes

        local_4c += 1

    return result

# 예시: 40바이트짜리 리스트
data = [0x66,0x0c,0x4c,0x86,0xa6,0x2c,0x1c,0x9c,
        0x1c,0x66,0x1c,0x2c,0x9c,0x6c,0xa6,0xcc,
        0xa6,0x6c,0x6c,0xac,0xa6,0xa6,0x86,0x4c,
        0x2c,0x46,0xec,0x8c,0xec,0x46,0x8c,0x9c,
        0x4c,0xec,0xc6,0x66,0x4c,0x46,0x86,0x4c]

out = transform_list(data)
print("변환 전:", data)
print("변환 후:", out)
for i in (out):
    print(chr(i),end="")
print("HEX:", bytes(out).hex())

```

# 📚 공부한 내용

- ptrace를 사용한 안티디버깅에 대해 배웠다.
- INIT 함수 부분을 어떻게 브레이크 하는지 배웠다. (__libc_start_main 에서 브레이크를 한 뒤 천천히 내려가면 된다.)
- 비트 리버스에 대해 알게되었다.
