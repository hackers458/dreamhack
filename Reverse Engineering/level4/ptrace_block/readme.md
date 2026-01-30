# 🧩 Reverse Engineering Challenge: mix-shuffle

## 📖 문제 개요

- **문제 이름**: ptrace_block
- **출처**: 드림핵
- **키워드**: AES 암호화, ptrace
- **설명**: AES

---

## 🛠️ 사용 도구

- **IDA**: 정적 분석
- **PyCharm**: 코드 작성

---

## 🚀 풀이 방법

- INIT.array에 있는 함수를 파악한 뒤 key를 찾아 aes로 암호화된 내용을 복호화 하면 된다.

---

## 📁 파일 구성

- **chall** : 섞인 문자열을 출력하고, 그에 맞는 원본 문자열을 입력하는 프로그램

---

## 🔍 파일 동작 원리

| 단계 | 이미지 | 설명 |
| --- | --- | --- |
| Step 1 |<img width="341" height="302" alt="화면 캡처 2026-01-30 200319" src="https://github.com/user-attachments/assets/fe6e6999-afb1-458d-b2b2-7595043aa5ce" /> <img width="221" height="283" alt="화면 캡처 2026-01-30 200337" src="https://github.com/user-attachments/assets/0d76c7be-497b-4fbf-b1dd-24b083d4db47" />| 첫번째 사진에서는 ptrace값이 디버깅 아닐때는 0이므로 rand 값이 무의미, 결국 다음 값 = 다음값 + 1을 실행하며 두번째 사진은 rand값의 범위0~FF이므로 브루트포스로 찾으면 된다.|
| Step 2 |<img width="407" height="279" alt="화면 캡처 2026-01-30 200535" src="https://github.com/user-attachments/assets/73e1d9e3-45c9-4708-bf66-af4510d2b217" />| 특정 조건을 확인한 뒤 값을 서로 바꾸는 동작을 한다. → **정렬 알고리즘(Stooge Sort)** 임을 알 수 있다. |
| Step 3 | <img width="341" height="325" alt="정렬 결과 저장" src="https://github.com/user-attachments/assets/2e39ebf8-6671-43c9-bd6c-649c8020dd53" /> | 정렬된 결과를 기반으로 **SHA-256 값**을 저장하여 출력한다. |

---

## 🧠 접근 방법

- `dword_4020`은 4바이트 값들의 배열이다.

| 이미지 | 설명 |
| --- | --- |
| <img width="1066" height="66" alt="파이썬 구현" src="https://github.com/user-attachments/assets/e2c6b95e-afbb-47e7-b555-d9e9026814f8" /> | 해당 동작을 그대로 **파이썬**에 구현하여 더 빠른 `sort()` 함수를 사용한 뒤 `sha256`으로 암호화한 값이 곧 플래그이다. 단, 파이썬에서는 4바이트가 넘칠 수 있으므로 `0xffffffff`로 AND 연산을 해줘야 한다. |

---

## 😪 막힌 부분

- 처음에 `0xhex_dc`의 값인 줄 알고 `0xdc`를 전달하는 줄 알았다가, 사실은 **주소값**을 전달하는 것이어서 시간을 좀 애먹었다.
- OR 연산의 리턴값을 `0xffffffff`로 AND 연산해줘야 하는데 계속 잊어서 플래그가 틀렸다. → 꼭 기억해야 한다.

---

## 📚 공부한 내용

- **Stooge Sort** 정렬 알고리즘을 새롭게 알게 되었다.

---

## 📗 비고

- 정렬 문제라는 건 보자마자 알았다.
- 백준 문제를 풀다 보면 특정 조건(`lambda`)을 두고 정렬하는 경우가 많아, 그 경험 덕분에 접근이 조금 더 수월했다.

```python
# 🧩 Reverse Engineering Challenge: mix-shuffle

## 📖 문제 개요
- **문제 이름**: Slooooow  
- **출처**: 드림핵  
- **키워드**: 정렬 (Stooge Sort)  
- **설명**: 정렬을 통한 배열을 sha256으로 암호화한 결과를 플래그로 출력  

---

## 🛠️ 사용 도구
- **IDA**: 정적 분석  
- **GDB**: 동적 분석  
- **PyCharm**: 코드 작성  

---

## 🚀 풀이 방법
- 오래 걸리는 **Stooge Sort**를 빠른 정렬 알고리즘으로 교체하여 실행 시간을 단축한다.  

---

## 📁 파일 구성
- **chall** : 섞인 문자열을 출력하고, 그에 맞는 원본 문자열을 입력하는 프로그램  

---

## 🔍 파일 동작 원리

| 단계 | 이미지 | 설명 |
|------|--------|------|
| Step 1 | <img width="404" height="120" alt="주소 전달" src="https://github.com/user-attachments/assets/502364f2-d345-4727-bc16-fe8c9b279858" /> | 전역 배열 값의 0xdc를 갖고 있는 주소를 전달하며, 해당 값은 **0x1869F**임을 확인할 수 있다. |
| Step 2 | <img width="462" height="339" alt="조건 확인" src="https://github.com/user-attachments/assets/73353782-0a9f-41cb-806e-6d7d09fda7ed" /> | 특정 조건을 확인한 뒤 값을 서로 바꾸는 동작을 한다. → **정렬 알고리즘(Stooge Sort)** 임을 알 수 있다. |
| Step 3 | <img width="341" height="325" alt="정렬 결과 저장" src="https://github.com/user-attachments/assets/2e39ebf8-6671-43c9-bd6c-649c8020dd53" /> | 정렬된 결과를 기반으로 **SHA-256 값**을 저장하여 출력한다. |

---

## 🧠 접근 방법
- `dword_4020`은 4바이트 값들의 배열이다.  

| 이미지 | 설명 |
| --- | --- |
| <img width="1066" height="66" alt="파이썬 구현" src="https://github.com/user-attachments/assets/e2c6b95e-afbb-47e7-b555-d9e9026814f8" /> | 해당 동작을 그대로 **파이썬**에 구현하여 더 빠른 `sort()` 함수를 사용한 뒤 `sha256`으로 암호화한 값이 곧 플래그이다. 단, 파이썬에서는 4바이트가 넘칠 수 있으므로 `0xffffffff`로 AND 연산을 해줘야 한다. |

---

## 😪 막힌 부분
- 처음에 `0xhex_dc`의 값인 줄 알고 `0xdc`를 전달하는 줄 알았다가, 사실은 **주소값**을 전달하는 것이어서 시간을 좀 애먹었다.  
- OR 연산의 리턴값을 `0xffffffff`로 AND 연산해줘야 하는데 계속 잊어서 플래그가 틀렸다. → 꼭 기억해야 한다.  

---

## 📚 공부한 내용
- **Stooge Sort** 정렬 알고리즘을 새롭게 알게 되었다.  

---

## 📗 비고
- 정렬 문제라는 건 보자마자 알았다.  
- 백준 문제를 풀다 보면 특정 조건(`lambda`)을 두고 정렬하는 경우가 많아, 그 경험 덕분에 접근이 조금 더 수월했다.  
```
