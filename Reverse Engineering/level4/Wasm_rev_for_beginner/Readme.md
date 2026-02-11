# 🧩 Reverse Engineering Challenge: Wasm_rev_for_beginner

## 📖 문제 개요

- **문제 이름**: Wasm_rev_for_beginner
- **출처**: 드림핵
- **키워드**: Wasm
- **설명**: 웹어셈블리어를 이해하고 해결하는 문제

---

## 🛠️ 사용 도구

- **ghidra**: 코드 작성

---

## 🚀 풀이 방법

- ghidra에 Wasm을 C로 디스어셈블리 해주는 기능이 있다. 이걸 이용하여 웹에서 Wasm파일의 어떤 함수를 실행시키는지를 본 후 wasm에서 입력한 내 문자열이 어떻게 검증되는지 파악

---

## 📁 파일 구성

- **index.html** : wasm와 연결하여 플래그를 입력하는 사이트
- **challenge.js** : 사이트와 wasm을 연결해주는 자바 스크립트
- **challeng_bg.wasm**: wasm 파일

---

## 🔍 파일 동작 원리

| 단계 | 이미지 | 설명 |
| --- | --- | --- |
| Step 1 | <img width="1889" height="850" alt="화면 캡처 2026-02-12 013218" src="https://github.com/user-attachments/assets/4ba0c434-e0bd-4341-a9d3-76925bf3268f" />| 해당 html을 우분투 아파치로 로컬 서버를 열어서 열면 wasm을 연결시킬 수 있다. 해당 장면은 플래그를 입력했을때 f12를 눌러 연동된 wasm파일을 볼 수 있다..(동적 디버깅도 가능하다) 그렇다면 ghidra에서는 어떻게 보일까 |
| Step 2 | <img width="1901" height="893" alt="화면 캡처 2026-02-12 015052" src="https://github.com/user-attachments/assets/68d65080-1993-42e0-bf6b-66226eaa0ba4" />| ghidra에서는 wasm을 c로 바꿔놓은걸 볼 수 있다. 그렇다면 이 함수들의 시작점은 어디서 볼 수 있을까? challenge.js에서 wasm.check(ptr0, len0)를 보아 각각 내가 입력한 플래그와 길이를 유추할 수 있다.|
| Step 3 | <img width="735" height="943" alt="화면 캡처 2026-02-12 015412" src="https://github.com/user-attachments/assets/0b1ce3e6-a5d2-48dd-b9d2-90f28593e53a" />| check함수를 보면 1번 내가 입력한 문자열 전체를 저장된 데이터와 xor 후 2번 각각 *13 +37한 후 3번 저장된 값과 비교를 한다. |

---

## 🧠 접근 방법

-즉 반대로 역연산을 하되 내 문자*13+37은 값이 255이상이면 &&ff가 되어 역연산이 안되기에 브루트포스로 역연산을 해주면 된다.


## 😪 막힌 부분

- WASM 명령어를 이해하는데 조금 막혔다. 

---

## 📚 공부한 내용

- WASM에 대해 알게 되었으며 F12를 눌러 직접 동적 디버깅을 할 수 있다는걸 배웠다.

## 📗 비고
- unnamed_function_36(0x44,1);를 보아 똑같은 상수를 넣었음에도 반환값이 달랐다. 이 함수를 분석하면 엄청난 양의 코드가 있다. 이럴때는 그냥 그렇다 하고 넘어가는걸 알아야 한다..
