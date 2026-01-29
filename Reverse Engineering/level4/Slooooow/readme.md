# 🧩 Reverse Engineering Challenge: mix-shuffle

📖 문제 개요

- 문제 이름: Slooooow
- 출처: 드림핵
- 키워드: 정렬(Stooge Sort)
- 설명: 정렬을 통한 배열로 sha256 암호화 한결과를 플래그로 출력

# 🛠️ 사용 도구

- IDA: 정적 분석
- GDB : 동적 분석
- pycharm : 코드 작성

# 🚀 풀이 방법

- 오래 걸리는 정렬을 빠른 속도의 정렬로 하는 걸로 바꾸면 된다.

# 📁 파일 구성

- chall : 섞인 문자열을 출력하고 그거에 맞는 원본 문자열을 입력하는 프로그램

# 🔍 파일 동작 원리

| 단계 | 이미지 | 설명 |
|------|--------|------|
| Step 1 | <img width="404" height="120" alt="주소 전달" src="https://github.com/user-attachments/assets/502364f2-d345-4727-bc16-fe8c9b279858" /> | 전역 배열 값의 0xdc를 갖고 있는 주소를 전달하며, 해당 값은 **0x1869F**임을 확인할 수 있다. |
| Step 2 | <img width="462" height="339" alt="조건 확인" src="https://github.com/user-attachments/assets/73353782-0a9f-41cb-806e-6d7d09fda7ed" /> | 특정 조건을 확인한 뒤 값을 서로 바꾸는 동작을 한다. → **정렬 알고리즘(Stooge Sort)** 임을 알 수 있다. |
| Step 3 | <img width="341" height="325" alt="정렬 결과 저장" src="https://github.com/user-attachments/assets/2e39ebf8-6671-43c9-bd6c-649c8020dd53" /> | 정렬된 결과를 기반으로 값을 저장한다. |

---

## 🧠 접근 방법
- 느린 Stooge Sort 대신 빠른 정렬 알고리즘으로 교체하여 실행 시간을 단축한다.

## 📚 공부한 내용
- 입력한 문자열의 위치가 최종적으로 어떻게 바뀌는지 이해하고, 이를 코드로 구현하는 방법을 배웠다.
