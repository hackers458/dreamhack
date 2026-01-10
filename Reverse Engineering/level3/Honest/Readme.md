# 🧩 Reverse Engineering Challenge: Honest

📖 문제 개요

- 문제 이름: Honest
- 출처: 드림핵
- 키워드: 트릭(?), 함수 안 함수 안 함수 안 함수
- 설명: 문자열 64개를 입력하면 각 함수하나하나마다 비교하는 프로그램

# 🛠️ 사용 도구

- IDA / Ghidra: 정적 분석
- GDB : 동적 분석
- pycharm : 코드 작성

# 🚀 풀이 방법

- 프로그램의 진짜 시작 부분을 찾아낸 후 각 함수마다 요구하는 인덱스에 해당하는 문자를 찾으면 된다.

# 📁 파일 구성

- main : 문자열을 입력하면 각 하나하나 비교하는 프로그램

# 🔍 파일 동작 원리
<img width="534" height="495" alt="화면 캡처 2026-01-10 174728" src="https://github.com/user-attachments/assets/c22e2a47-635b-4bee-9619-aeb0bf5dd77d" />

현재 보면 main 부분이 있어 GDB로 본 결과 저 COUNTER의 값이 37로 된 걸 확인했었다.. 하지만 아무리 찾아봐도 전역변수 또는 static (.bss)에 
값이 정해진 대로 저장하면 그 값을 저장하는 곳이 있어야 하는데 아무것도 없다

-> 그렇다면 혹시 시작하는 함수가 main이 아닌것인가?

<img width="593" height="184" alt="화면 캡처 2026-01-10 175255" src="https://github.com/user-attachments/assets/3f5a6569-9b8a-4788-8a50-031f7ba56115" />

역시나 저 verify_38인 함수부터 시작하는 것이다. 실제로 GDB에서 확인하면 COUNTER의 값이 0인걸 알 수 있었따.
그렇다면 
함수 0~62 + MAIN은 각 인덱스 0~63을 비교하는 것이며 counter는 인덱스에 해당한다. 그렇다면 인덱스에 해당하는 값은 어떻게 알까?

<img width="534" height="495" alt="화면 캡처 2026-01-10 174728" src="https://github.com/user-attachments/assets/c445c744-97c0-4c94-9812-2d122bec4048" />

저 calculate함수를 보면 저 함수의 반환값이 cVar1 != 값과 비교하는데 저 값이 곧 calculate에 인덱스에 해당하는 값을 넣은 반환값이다.



# 🧠 접근 방법

그럼 이렇게 생각할 수 있다.
함수에는 
1. 각 함수 요구하는 인덱스에 해당하는 값과
2. 다음으로 넘어가는 함수
이걸 알아야 한다.
그리고 저 calculate의 반환하는 값은 그냥 짜피출력 가능한 함수를 아스키코드에서 브루트포스를 하면 되니 상관 없다.

## 각 함수에서 요구하는 인덱스에 해당하는 값은 어떻게 알까?
여기에 여러가지 접근 방법이 있는데 IDAPython을 사용하면 된다.
<img width="472" height="323" alt="화면 캡처 2026-01-10 180103" src="https://github.com/user-attachments/assets/631fff72-84a0-47bc-86a4-c41d2c236894" />
ida를 보면 각 함수와 비교하는 값 그리고 다음으로 넘어가는 리턴 함수가 있다.
우리는 시작함수가 verify_28인걸 알 고 있으니.
사진의 함수로 설명하자면 저 != 값이 바이너리로 FFFF3C값이다. 즉 FFFF3C 다음에 오는 값을 얻으면 되고.
''' python
import idautils
import idaapi
import idc
pattern = b"\xff\xff\x3c"
for func_ea in idautils.Functions():
    func_name = idc.get_func_name(func_ea)
    func = idaapi.get_func(func_ea)
    if not func:
        continue
    start = func.start_ea
    end = func.end_ea
    bytes = idaapi.get_bytes(start, end - start)

    idx = bytes.find(pattern)
    if idx != -1 and idx + len(pattern) < len(bytes):
        next_val = bytes[idx + len(pattern)]
        print(f"Function: {func_name}, Next byte: {hex(next_val)}") '''

그 다음 함수에서 다음 함수로 넘어가는 함수들을 어떻게 분류하면?
''' python
import idautils
import idaapi
import idc

def list_function_calls():
    # 모든 함수 순회
    for func_ea in idautils.Functions():
        func_name = idc.get_func_name(func_ea)
        if not func_name:
            func_name = f"sub_{func_ea:x}"

        # 함수 내 모든 명령어 순회
        for head in idautils.FuncItems(func_ea):
            if idc.print_insn_mnem(head) == "call":
                # 호출 대상 주소 가져오기
                callee = idc.get_operand_value(head, 0)
                callee_name = idc.get_func_name(callee)
                if not callee_name:
                    callee_name = f"sub_{callee:x}"

                # 필터: main 또는 verify가 이름에 포함된 경우만 출력
                if "main" in callee_name.lower() or "verify" in callee_name.lower():
                    print(f"Function {func_name} calls {callee_name} at {hex(head)}")

# 실행
list_function_calls() '''

이걸로 할 수 있다.
<img width="234" height="507" alt="화면 캡처 2026-01-10 181352" src="https://github.com/user-attachments/assets/22e49631-e51d-4ce4-bb28-164975cc8197" />
이제 시작 verify_28로 시작을 하여 해당 함수에 요구하는 값과 다음 함수로 이동하여 인덱스를 증가시키면 된다.




# 📚 공부한 내용
- angr로 했는데 잘 안돼서 radare2도 이용해보았으나 이것보다 더 편한 IDAPYTHON이 있다는 것을 발견했고 이를 공부할 수 있었다.
