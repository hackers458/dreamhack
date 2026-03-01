# 🧩 Reverse Engineering Challenge: captain-hook

## 📖 문제 개요
- **문제 이름**: captain-hook  
- **출처**: 드림핵  
- **키워드**: API 후킹, UPX , WINAPI(GDI) 
- **설명**: 프로그램에 나타나는 그림에 나오는 글자을 다 얻어 파일을 생성한뒤 그 파일에서 플래그를 얻는 문제

---

## 🛠️ 사용 도구
- **IDA**: 정적 분석  
- **x64dbg**: 동적 분석  
- **frida**: api 후킹

---

## 🚀 풀이 방법
- 단계별로 풀이 방법을 적자면
- 1. 1~F까지 그리는 함수를 찾아
  2. 각 함수를 호출할때마다 그 API를 후킹하여 그림을 문자열화하여 기록한다.(4,D,5,A를 4D5A로 문자열)
  3. 그 후 이어진 문자열이 PE구조인걸 파악한뒤 EXE 파일을 만든다.
  4. 만들어진 EXE파일에서 감추게하는 함수를 NOP으로 채우면 플래그가 나온다.

---

## 📁 파일 구성
- **CaptainHook** : 클릭하면 그림을 보여주는 프로그램

---

## 🔍 파일 동작 원리 & 접근 방법
해당 프로그램의 모습
<img width="181" height="231" alt="화면 캡처 2026-03-01 172242" src="https://github.com/user-attachments/assets/847f16c3-0a0c-409d-8ad3-11bde8f56c1f" />

| 단계 | 이미지 | 설명 |
|------|--------|------|
| Step 1 | <img width="880" height="714" alt="화면 캡처 2026-03-01 171449" src="https://github.com/user-attachments/assets/441dd8fc-5dd4-4a22-bc9f-4ba387ecb99f" />| 해당 동그라미 친 곳은 윈도우에서 메세지를 처리하는 역할이고 밑줄친곳은 어떤 메세지를 받는가에 따라 행동하는 함수의 포인터이다. |
| Step 2 | <img width="510" height="664" alt="화면 캡처 2026-03-01 171601" src="https://github.com/user-attachments/assets/ba0c4bf5-1767-40fc-809c-56e8fcd23fc1" />| 여기서 switch에 메세지 종류가 있는데 0x202는 왼쪽 클릭, 0x2는 창 종료, 0xf는 창 다시 그리기이다. 여기서 창 그리기를 보면 sub_140016360이 있는데 해당 함수를 보면 |
| Step 3 | <img width="999" height="767" alt="화면 캡처 2026-03-01 172011" src="https://github.com/user-attachments/assets/8073b67a-c5a1-4f32-b223-1d2ecb0a3148" />| 해당 함수가 무엇을 하는지는 잘 알 수가 없다. 난독화가 되있기 때문이다. |
| Step 4 | <img width="792" height="931" alt="화면 캡처 2026-03-01 172156" src="https://github.com/user-attachments/assets/b97abc0c-e9b5-4cd3-adb4-8222c3cae973" />| 그러던 도중 gdi 함수를 조사하다가 GdipDrawLineI 가 선을 그리는 함수인걸 확인했으며 |
| Step 5 | <img width="938" height="198" alt="화면 캡처 2026-03-01 172857" src="https://github.com/user-attachments/assets/d831b7bf-da69-44eb-9e5f-5ac2fc2af348" />| 이 함수들을 호출하는 함수를 보니 이렇게 정확히 0~F을 그리는 함수를 발견할 수 있었다. |
| Step 6 | <img width="1156" height="899" alt="화면 캡처 2026-03-01 173258" src="https://github.com/user-attachments/assets/687bdbfd-03fc-40a7-a229-7487832082fb" /> | frida에서 각 0~F에 존재하는 여러개의 GdipDrawLineI 중 하나를 잡아 그 함수의 리턴 주소(RVA,상대거리)을 기록하여 해당 그림을 그릴때 마다 주소값이 있기에 그거와 같으면 문자열을 추가하도록 한다. 그리고 저 문자열들을 다 복사하여 새로운 파일을 만들면|
| Step 7 | <img width="913" height="589" alt="화면 캡처 2026-03-01 173723" src="https://github.com/user-attachments/assets/2a281810-0979-49da-85c4-a77278605bb8" />| UPX로 패킹된걸 알 수 있다. 이제 언패킹하여 프로그램을 보면 |
| Step 8 | <img width="573" height="186" alt="화면 캡처 2026-03-01 173844" src="https://github.com/user-attachments/assets/62d34bd6-15c1-4685-a66f-30534793e5c5" />| 이렇게 플래그가 가려져 있는걸 알 수 있다. |
| Step 9 |<img width="625" height="409" alt="화면 캡처 2026-03-01 174247" src="https://github.com/user-attachments/assets/25f81085-7378-4507-83ce-9bd9652cbcfa" /> | 여기서 가리는 부분을 nop으로 바꿔주면 |
| Step 10 |<img width="622" height="282" alt="화면 캡처 2026-03-01 174405" src="https://github.com/user-attachments/assets/0afca96c-bcf8-4095-b0a0-a6545991d3db" />| 이렇게 플래그를 얻을 수 있다. |

---



## 😪 막힌 부분
- 0~f를 그리는 함수를 찾는데에 힘들었다. 
- frida로 리턴주소를 하는데 똑같은 주소 4개를 반환하는게 있어서 독립적으로 반환하는걸 찾느냐 막혔다. 
- 문제를 추측하다가 4를 그리면 어딘가 주소에 4를 저장하는 메모리가 있을 줄 알았으나 그러지 않았다. 그리고 4D 5A에서 각각 인덱스가 잇을줄 알고 치트엔진으로 0,1,2,3이렇게 검색을 해보앗으나 그 접근도 아니여서 막혔다. 즉 이 문제는 순수 그림을 그리는 함수를 찾는거였다.
---

## 📚 공부한 내용
- Frida 사용법에 대해 알게 되었다.
- API 후킹 중 API 기능은 그대로 하고 내가 만든 기능 따로 이렇게 작동하는건 처음 알았다.

---
