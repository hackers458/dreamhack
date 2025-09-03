#너무 z3이 어려워서 copilot으로 돌렸습니다. 그 후 분석했습니다
from z3 import *

n = 8  # 길이 설정

# 모든 변수 BitVec으로 선언 (64비트)
local_20_a = [BitVec(f'a{i}', 64) for i in range(n)]
local_20_b = [BitVec(f'b{i}', 64) for i in range(10)]
local_20_c = [BitVec(f'c{i}', 64) for i in range(10)]
local_20_d = [BitVec(f'd{i}', 64) for i in range(n)]

s = Solver()

# 0~9 또는 a~f만 허용
for c in local_20_a + local_20_b + local_20_c + local_20_d:
    s.add(Or(And(c >= ord('0'), c <= ord('9')),
             And(c >= ord('a'), c <= ord('f'))))

# 16진수 누적 계산 함수 (BitVec 기반)
def hex_accumulate_bv(chars):
    acc = BitVecVal(0, 64)
    for c in chars:
        value = If(c <= ord('9'), c - 0x30, c - 0x57)  # '0'~'9' or 'a'~'f'
        acc = acc * 16 + value
    return acc

# 누적 계산
acc_a = hex_accumulate_bv(local_20_a)
acc_b = hex_accumulate_bv(local_20_b)
acc_c = hex_accumulate_bv(local_20_c)
acc_d = hex_accumulate_bv(local_20_d)

# 조건 설정
s.add(acc_a + acc_b == 0xa255cea0ba)
s.add(acc_c + (acc_d & 0xffffffff) == 0x2284419047)
s.add(acc_a + acc_d == 0xb470421e)
s.add(acc_b + acc_c == 0xc4259feee3)
s.add(acc_b ^ acc_c ^ acc_d == 0x8391639987)

# 모델 확인
if s.check() == sat:
    m = s.model()
    a_vals = [chr(m[c].as_long()) for c in local_20_a]
    b_vals = [chr(m[c].as_long()) for c in local_20_b]
    c_vals = [chr(m[c].as_long()) for c in local_20_c]
    d_vals = [chr(m[c].as_long()) for c in local_20_d]

    print("local_20_a:", ''.join(a_vals))
    print("local_20_b:", ''.join(b_vals))
    print("local_20_c:", ''.join(c_vals))
    print("local_20_d:", ''.join(d_vals))
else:
    print("No solution found.")
