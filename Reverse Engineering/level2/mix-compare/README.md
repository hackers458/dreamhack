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



'''python
for j in range(16):
    for k in range(16):
        if (j & 1) != 0:
            copy_random_word[data[16 * j + k]] = random_word[k + 32]
        else:
            random_word[data[16 * j + k] + 32] = copy_random_word[k]
'''


# 🧠 접근 방법



# 📚 공부한 내용
- 2의 보수를 취하는 방법과 -1의 2의보수인 FF로 NOT 연산을 빠르게 구할 수 있다는 점을 배웠다.

