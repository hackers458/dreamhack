# 🧩 Reverse Engineering Challenge: baseball

📖 문제 개요

- 문제 이름: baseball
- 출처: 드림핵
- 키워드: base64
- 설명: base64의 원리를 그대로 적용하되, 테이블만 바꾼 문제

# 🛠️ 사용 도구

- IDA / Ghidra: 정적 분석
- pycharm : 코드 작성

# 🚀 풀이 방법

- base64에 사용되는 사용자 지정 테이블을 직접 구한 뒤, 그 테이블을 토대로 원본을 구하면 된다.

# 📁 파일 구성
- baseball : baseball
- text_in.txt : 원본 문자열
- text_out.txt : 원본 문자열에 base64 알고리즘으로 커스텀 테이블을 적용한 결과
- flag_out.txt : 플래그에 base64 알고리즘으로 커스텀 테이블을 적용하여 나온 결과
<img width="753" height="446" alt="화면 캡처 2025-11-18 190145" src="https://github.com/user-attachments/assets/4f48fde8-9dc7-4073-93ea-9e73039115c1" />

# 🔍 파일 동작 원리
<img width="652" height="886" alt="화면 캡처 2025-11-18 185542" src="https://github.com/user-attachments/assets/5f946c8c-3d50-4f81-9475-f8e8051736d5" />
위의 빨간줄은 길이 64바이트인 테이블을 불러오며(64글자가아니면 안된다)
아래 빨간줄은 base64 알고리즘을 실행하는 함수이다.



# 🧠 접근 방법

## 1. 테이블 구하기
<img width="793" height="292" alt="스크린샷 2025-11-18 191253" src="https://github.com/user-attachments/assets/cbc47f71-94bc-4e85-ac6a-1bee2aef9b7e" />

해당 사진을 보면 결국 입력한 문자들에 해당하는 테이블 인덱스는 고정이므로, 테이블값을 추적하기만 하면 된다.
우선 base64의 테이블을 구하기 위해 abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@를 테이블로 가정을 한다. 그리고 text_in.txt의 내용들을 해당 테이블로 base64했을때의 결과와 비교를 하면된다.
그러면 위의 테이블로 한 결과는 
ugvWzwjVigLZigeGy30VA3LLihn1AxnRlcbKAwbWzxqGAx5Gy30TCg02BMqGy3HVy30SywrLlcbTyx62zMfJDhvYzxqGyNKGpZ9@pZ9Gq30UzMvJDgLVBMvYEsbPBIbtB4v1AcblB4jLyqPqzwbLCM9Grgf6igLZigHLBgqGyx6UDxfSBhKGB35GtM03zx2IzwiGmte=
원래 테이블로 한 결과(flag_out.txt)는
7/OkZQIau/jou/R1by9acyjjutd0cUdlWshecQhkZUn1cUH1by9g4/9qNAn1byGaby9pbQSjWshgbUmqZAF+JtOBZUn1b8e1YoMPYoM1ny95ZAO+J/jaNAOB2vhrNLhVNDO0cshWNDIjbnrnZQhj4AM1S/Fmu/jou/GjN/n1bUm5JUFpNte1NyH1VA9yZUqLZQu13VR=
인데 맨 앞에 u의 자리에 7이 들어가고 g의 자리에 /가 들어가는 것으로 테이블을 만들면 된다.
그러면 0hs0RF/tuI0W3d0YnSvV7OUQbZcN4J201GL+ejA80r0lpg5ak0Bo0qyDHm00M90P 이렇게 정답 테이블이 만들어지는데 0이 좀 많은 걸 알 수 있다. 그 이유는 처음에 0을 64개로 채웠으며 각 자리에 해당하는 문자를 넣다보니, 들어가지 않은 문자도 있기 때문이다.
근데 이건 어쩔 수 없고 못 구한다.( 정답 테이블로 한 결과가 하나밖에 없으며 그걸 기반으로 만들었기 때문)




## 2. 플래그 구하기
![KakaoTalk_20251118_193220695](https://github.com/user-attachments/assets/02057b4a-2cf6-4258-92ee-37b6887a21a8)

해당 사진처럼 결국 플래그 BASE64로 암호화된 문자 S/jeutjaJvhlNA9Du/GaJBhLbQdjd+n1Jy9BcD3=에서 각 문자들의 인덱스를 구한뒤 그걸 8비트로 묶으면 된다.

<img width="1077" height="865" alt="화면 캡처 2025-11-18 193405" src="https://github.com/user-attachments/assets/d2dc90ae-b799-4bd9-b6a2-eaaa6620b4a8" />
그러면 해결 방법을 알 수 있다.



# 📚 공부한 내용
- 암호학 문제를 풀때 스포일러에서 암호학의 용어를 확인 한 뒤 해당하는 암호학에 먼저 배우고 나서 문제를 푸는게 더욱 더 도움이 된다는 것을 알게 되었다.
- base64에 대해 알게 되었다.
