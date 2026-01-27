from z3 import *

# command.bin 파일 읽기
with open('command.bin', 'rb') as f:
    command = f.read()

# ===== 입력 변수 선언 =====
# BitVec: z3의 비트 벡터(정수) 심볼릭 변수
# BitVec(이름, 비트크기) - 8비트 = 1바이트
# 이 변수들은 "아직 값이 정해지지 않은" 미지수입니다
# z3가 나중에 제약 조건을 보고 이 값들을 계산해줍니다
inputs = [BitVec(f'input_{i}', 8) for i in range(68)]

# ===== 상태 히스토리 선언 =====
# states: 각 명령어 실행 후의 v3 레지스터 상태를 저장하는 리스트
# 왜 리스트로 관리하나?
# - 명령어가 v3[7] = v3[5] | v3[7] 같이 "이전 값"을 참조하기 때문
# - states[-1]로 "바로 직전 상태"에 접근 가능
# - 각 시점의 상태를 보존해야 z3가 제약 조건을 올바르게 설정 가능
states = []

# ===== 초기 상태 생성 =====
# BitVecVal: z3의 "구체적인 값"을 가진 비트 벡터
# BitVec vs BitVecVal:
#   - BitVec('x', 8): 미지수 (solver가 찾아야 할 값)
#   - BitVecVal(0, 8): 상수 (이미 정해진 값 0)
# 초기 상태는 모든 레지스터가 0이므로 BitVecVal(0, 8) 사용
initial_state = [BitVecVal(0, 8) for _ in range(8)]  # v3[0]~v3[7] = 0
states.append(initial_state)  # states[0]에 초기 상태 저장

# solver: z3의 제약 조건 해결기
# 여기에 제약 조건들을 추가하고, 나중에 check()로 해를 구함
solver = Solver()

# 명령어 포인터 (Program Counter)
pc = 0
# 현재 몇 번째 입력을 읽고 있는지 추적
input_idx = 0

# ===== VM 실행 시뮬레이션 =====
# command 바이트코드를 하나씩 읽으면서 z3 제약 조건으로 변환
while pc < len(command) and command[pc] != 0x20:  # 0x20 = ' ' (종료 명령어)
    opcode = command[pc]

    # ===== 현재 상태 복사 =====
    # states[-1]: 리스트의 마지막 원소 = 가장 최근 상태
    # .copy(): 리스트를 복사 (원본 수정 방지)
    # 왜 복사하나?
    #   - 새로운 상태를 만들기 위해
    #   - 이전 상태(states[-1])는 그대로 보존되어야 함
    #   - 다음 명령어가 이전 값을 참조할 수 있도록
    current_state = states[-1].copy()

    if opcode == 0x23:  # '#' - v3[idx] = value (레지스터에 상수 저장)
        idx = command[pc + 1]  # 레지스터 번호
        value = command[pc + 2]  # 저장할 값
        # BitVecVal 사용 이유: value는 명령어에서 읽은 "확정된 상수"이므로
        current_state[idx] = BitVecVal(value, 8)
        pc += 3

    elif opcode == 0x24:  # '$' - v3[dst] = v3[src] (레지스터 복사)
        dst = command[pc + 1]
        src = command[pc + 2]
        # states[-1][src]를 참조: "이전 상태의" v3[src] 값을 읽어옴
        # 왜 states[-1]을 사용?
        #   - current_state는 아직 수정 중인 상태
        #   - 읽을 때는 "이전에 확정된" states[-1]에서 읽어야 함
        current_state[dst] = states[-1][src]
        pc += 3

    elif opcode == 0x25:  # '%' - v3[dst] = v3[op1] & v3[op2] (AND 연산)
        dst = command[pc + 1]
        op1 = command[pc + 2]
        op2 = command[pc + 3]
        # z3의 비트 연산: & (AND)
        # states[-1][op1], states[-1][op2]는:
        #   - BitVec (심볼릭 변수) 또는
        #   - BitVecVal (구체적 값) 또는
        #   - 이전 연산 결과 (z3 표현식)
        # z3는 이들 간의 연산을 "제약 조건"으로 기록
        current_state[dst] = states[-1][op1] & states[-1][op2]
        pc += 4

    elif opcode == 0x26:  # '&' - v3[dst] = v3[op1] | v3[op2] (OR 연산)
        dst = command[pc + 1]
        op1 = command[pc + 2]
        op2 = command[pc + 3]
        # 핵심 예시: v3[7] = v3[5] | v3[7]
        # states[-1][7]: 이전 단계에서 계산된 v3[7] 값
        # 이 값이 새로운 계산에 사용됨
        current_state[dst] = states[-1][op1] | states[-1][op2]
        pc += 4

    elif opcode == 0x27:  # '\'' - v3[dst] = v3[op1] ^ v3[op2] (XOR 연산)
        dst = command[pc + 1]
        op1 = command[pc + 2]
        op2 = command[pc + 3]
        current_state[dst] = states[-1][op1] ^ states[-1][op2]
        pc += 4

    elif opcode == 0x28:  # '(' - v3[0] = input (스택에서 입력 pop)
        # inputs[input_idx]: BitVec 심볼릭 변수
        # 이것이 v3[0]에 저장되면서, 이후 모든 연산이
        # 이 미지수(inputs[input_idx])를 포함한 제약 조건이 됨
        current_state[0] = inputs[input_idx]
        input_idx += 1
        pc += 1

    else:
        # 알 수 없는 명령어는 건너뜀
        pc += 1
        continue

    # ===== 새로운 상태 저장 =====
    # 계산이 끝난 current_state를 states에 추가
    # 다음 명령어는 이 상태를 states[-1]로 참조함
    states.append(current_state)

# ===== 최종 제약 조건 추가 =====
# states[-1][0]: 마지막 상태의 v3[0]
# 이 값이 0이어야 "Correct!!!" 출력
# solver.add(): z3에게 "이 조건을 만족하는 inputs를 찾아줘" 요청
solver.add(states[-1][0] == 0)

# ===== 추가 제약: printable ASCII =====
# (선택사항) 플래그가 출력 가능한 문자열이라고 가정
# 0x20(' ')부터 0x7e('~')까지
for inp in inputs:
    solver.add(inp >= 0x20)
    solver.add(inp <= 0x7e)

# ===== 해 찾기 =====
print("Solving...")
# solver.check(): 제약 조건들을 만족하는 해가 있는지 확인
# sat(satisfiable): 해가 존재함
# unsat: 해가 없음
if solver.check() == sat:
    # model(): 찾은 해를 가져옴
    model = solver.model()
    # model[inputs[i]]: inputs[i]의 구체적인 값
    # .as_long(): z3 값을 Python 정수로 변환
    flag = ''.join([chr(model[inputs[i]].as_long()) for i in range(68)])
    print(f"Flag: {flag}")
else:
    print("No solution found")

# ===== 정리 =====
# 1. BitVec: 미지수 (solver가 찾을 값)
# 2. BitVecVal: 상수 (이미 정해진 값)
# 3. states 리스트: 각 단계의 상태를 보존
#    - 이전 값 참조 가능 (v3[7] = v3[5] | v3[7])
#    - z3가 모든 시점의 관계를 추적
# 4. solver.add(): 제약 조건 추가
# 5. solver.check(): 모든 조건을 만족하는 inputs 값 찾기

ANSWER= "59e0d0d2ac957be797bef788df1244dd7d873a5cb1998b8df4af712bba3e24cb" # 스택으로 접근햇으니 거꾸로
print(ANSWER[::-1])
