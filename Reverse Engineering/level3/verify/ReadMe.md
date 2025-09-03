이 문제는 z3을 활용할 수있는가를 물어본다.
DH{8글자-10글자-10글자-8글자} 인 형태로 나오는데(과정은 생략)
<img width="413" height="437" alt="화면 캡처 2025-09-03 224723" src="https://github.com/user-attachments/assets/d3f4f0e4-eb8d-4472-b6f7-e856e70586e7" />
여기서 이걸 보아 소문자 + 숫자라는걸 파악해야 한다.(플래그가 소문자로 되야한다고 말함)
->0~9 그리고 a~f
그리고 이게 첫번째 난관, z3으로 어떻게 표현을 해야하는가 고민을 하다가 너무어려워서 AI힘을 썼다.
<img width="487" height="369" alt="화면 캡처 2025-09-03 225403" src="https://github.com/user-attachments/assets/bdbb2ce7-363f-48df-9eca-a8b14af62c35" />


->

이렇게 표현할 수있으며 
local_20_a = [BitVec(f'a{i}', 64) for i in range(n)]
local_20_b = [BitVec(f'b{i}', 64) for i in range(10)]
local_20_c = [BitVec(f'c{i}', 64) for i in range(10)]
local_20_d = [BitVec(f'd{i}', 64) for i in range(n)]
- BitVec(f'a{i}', 64)는 이름이 a0, a1, ..., a7인 64비트 변수들을 생성
- 이 변수들은 문자 하나를 표현하지만, Z3에서는 숫자로 다뤄요



s = Solver()


for c in local_20_a + local_20_b + local_20_c + local_20_d: # 이산수학 + 수리논리 지식을 여기서 쓴다...ㅎㅎ
    s.add(Or(And(c >= ord('0'), c <= ord('9')),
             And(c >= ord('a'), c <= ord('f'))))

def hex_accumulate_bv(chars):
    acc = BitVecVal(0, 64) -> 이게 진짜 중요하다고 생각한다. 이게 a = a+3에서 코딩으로는 a에 a+3을 대입하지만 수학에서는 a는 a+3과 같다는걸 말하기 때문에 이 부분이 가장 어려웠다.
    for c in chars:
        value = If(c <= ord('9'), c - 0x30, c - 0x57)  # '0'~'9' or 'a'~'f'
        acc = acc * 16 + value
    return acc
- Z3에서는 If를 써서 조건부 계산을 해요
- 이 함수는 문자 배열을 받아서 16진수 숫자로 누적 계산해요
- 예: ['1', 'a'] → 0x1a → acc = 1 * 16 + 10 = 26

<img width="454" height="295" alt="화면 캡처 2025-09-03 230224" src="https://github.com/user-attachments/assets/77b16e63-8f04-435d-a647-96ae569b85bb" />
위의 사진대로 이제 조건식을 add해주면 된다. 안의 내용은 생략
# 조건 설정
s.add(acc_a + acc_b == 0xa255cea0ba)
s.add(acc_c + (acc_d & 0xffffffff) == 0x2284419047)
s.add(acc_a + acc_d == 0xb470421e)
s.add(acc_b + acc_c == 0xc4259feee3)
s.add(acc_b ^ acc_c ^ acc_d == 0x8391639987)

-> 그냥 가장 중요한건 z3의 지식 + BitVec으로의 선언이다. Int로 하니까 비트 접근이 안돼서 AND 연산이 안됐다.
