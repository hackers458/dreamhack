# 🧩 Reverse Engineering Challenge: quilt

## 📖 문제 개요
- **문제 이름**: quilt 
- **출처**: 드림핵  
- **키워드**: base64 & bmp  
- **설명**: bmp의 구조와 bmp의 픽셀을 이루는 파일을 역분석하여 입력해야하는 플래그를 얻어야 하는 문제

---

## 🛠️ 사용 도구
- **IDA**: 정적 분석  
- **GDB**: 동적 분석  
- **PyCharm**: 코드 작성  

---

## 🚀 풀이 방법
- 1. bmp의 구조를 이해 한 뒤 화소를 다시 base64 형태로 만들어 base64 -> 원래 문자로 만든 뒤 플래그를 찾는다.

---

## 📁 파일 구성
- **quilt** : bmp이미지에 플래그를 입혀주는 프로그램
- **quilt.bmp** : 플래그가 숨겨진 bmp이미지, 총 16x16이미지로 되어있다.

---

## 🔍 파일 동작 원리

| 단계 | 이미지 | 설명 |
|------|--------|------|
| Step 1 | <img width="626" height="888" alt="화면 캡처 2026-02-17 004838" src="https://github.com/user-attachments/assets/64e29563-0958-4fea-a83d-63c5ed322203" />| 1번은 bmp의 헤더 관련 값들이다. 각 인덱스에 해당하는 값의 의미들은 notion에 적어놓았으므로 생략,2번이 중요한데, random값 x과 y[192]를 뽑아 strncpy에서 랜덤 y로 이루어진 192에서 x%(192-플래그위치)인 곳에 플래그를 삽입한다.<br>그 후|
| Step 2 | <img width="462" height="339" alt="조건 확인" src="https://github.com/user-attachments/assets/73353782-0a9f-41cb-806e-6d7d09fda7ed" /> | 특정 조건을 확인한 뒤 값을 서로 바꾸는 동작을 한다. → **정렬 알고리즘(Stooge Sort)** 임을 알 수 있다. |
| Step 3 | <img width="341" height="325" alt="정렬 결과 저장" src="https://github.com/user-attachments/assets/2e39ebf8-6671-43c9-bd6c-649c8020dd53" /> | 정렬된 결과를 기반으로 **SHA-256 값**을 저장하여 출력한다. |

---

## 🧠 접근 방법
**좀 복잡하니 신중하게 적었습니다** 

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
