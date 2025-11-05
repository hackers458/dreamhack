# 🧩 Reverse Engineering Challenge: mix-shuffle
📖 문제 개요
- 문제 이름: mix-shuffle
- 출처: 드림핵
- 키워드: 문자열 인덱스 활용
- 설명: 문자열 인덱스가 섞이지만 섞이는 과정은 동일하며 결과도 동일한 프로그램


# 🛠️ 사용 도구
- IDA / Ghidra: 정적 분석
- GDB : 동적 분석
- pycharm : 코드 분석

# 🚀 풀이 방법
- 문자열이 섞이는 과정을 이해하고 그 문자열의 바뀐 위치를 확인하며, 그거에 맞게 코드를 짜면 된다.



# 📁 파일 구성
- many-shuffle : 섞인 문자열을 출력하고 그거에 맞는 원본 문자열을 입력하는 프로그램



# 🔍 파일 동작 원리
<img width="488" height="510" alt="화면 캡처 2025-11-05 183825" src="https://github.com/user-attachments/assets/da39da1f-692d-4acf-a99f-e947bc409a3d" />

변수는 copy_random_word[32]
random_word[64]의 값에 현재 시간 시드값 기준 rand()값을 random_word[0] ~ random_word[15]에 (rand()값 %26 + 65)
을 넣어준다. 이 범위는 대문자 A~Z까지이다.

그 후 copy_random_word에 random_word을 저장한 후 



```python
for j in range(16):
    for k in range(16):
        if (j & 1) != 0:
            # j가 홀수일때
            copy_random_word[data[16 * j + k]] = random_word[k + 32]
        else:
            # j가 짝수일때
            random_word[data[16 * j + k] + 32] = copy_random_word[k]
```
를 수행한다.

그 후 섞인 문자열을 출력한뒤 원본 문자열을 물어본다.
# 🧠 접근 방법
가령 ABCDEFGHIJKLMNOP를 RANDOM으로 만들어졌다고 해도 결국 바뀐 결과의 값인 "BFMLIKGJAHCONDPE" 처럼 고정이기에
섞인 저 문자열을 생각해보면 A=0.... P = 15라 하면 [1, 5, 12, 11, 8, 10, 6, 9, 0, 7, 2, 14, 13, 3, 15, 4] 이렇게 인덱스를 알 수 있다.
즉 BFMLIKGJAHCONDPE의 원래 인덱스가 각각 1 5 12 11 이렇기에 다시 원위치를 해주는 코드를 짜면 된다.


# 📚 공부한 내용
- 입력한 문자열의 위치가 어떻게 최종적으로 바뀌었는지에 대한 이해를 필두로 코드를 짜는것을 배웠다.

