# 🧩 Reverse Engineering Challenge: Infested Terran

📖 문제 개요

- 문제 이름: Infested Terran
- 출처: 드림핵
- 키워드: 역연산, 가상환경
- 설명: 가상환경과 그 안에 실행되는 프로그램이 무엇인지 확인하는 문제

# 🛠️ 사용 도구

- Ghidra: 정적 분석
- pycharm : 코드 작성

# 🚀 풀이 방법

- 가상환경 이미지 파일을 분해하여 안에 있는 채굴(?) 프로그램을 분석 하여 실제 플래그를 얻는다.

# 📁 파일 구성

- rootfs.ext2 : 가상환경 이미지 파일(실제 파일들을 가지고 있음)
- bzimage : 가상환경 커널 실행 파일
- run.sh : 가상환경을 실행하기 위한 환경변수들

## 가상환경 파일 구성
- .helper : 실제 채굴(?)하는 프로그램을 실행시켜주는 프로그램
- sl : 실제 채굴 프로그램
- 
# 🔍 파일 동작 원리
run.sh를 실행하면 bzimage를 커널로, rootfs2.ext2를 가상환경 이미지 파일로 하여금하여 실행한다.
그리곤 가상환경에서 ./helper를 MINING_BOOST를 파일 파라미터로 받아 실행하게 된 후 플래그 값을 입력하면
sl에서 비교를 한 뒤 값을 비교 한다.
# 🧠 접근 방법
<img width="438" height="554" alt="화면 캡처 2025-12-21 043720" src="https://github.com/user-attachments/assets/cc98d826-3657-4adf-addc-4f429e53688e" />
사진에서 read 부분은 플래그 입력하는 부분이고 화살표 부분은 [kworker]로 프로세스 이름이 정해진다.
이유는 파일 파라미터 두번째의 첫번째 인덱스는 자기 자신이기 때문

쨋든 그건 별로 안중요하고 sl부분을 보면
<img width="702" height="724" alt="화면 캡처 2025-12-21 043857" src="https://github.com/user-attachments/assets/f98a46a1-1361-4e15-b792-b21ac02d02b0" />

이렇게 돼있는데 코드를 잘 정리하면 
file_Data 값 * 내가 입력한 값 = file_result이 저장이 되는데 특이하게도 누적값이 저장된다.
가령 내가 1234567890를 입력하고 file_Data에 abcdefghj..가 저장이되면
file_result[0]= 1 * a
file_ result[1] = file_Result[1] + 2*b
file_Result[2] = file_result[1] + 3*c 이런식으로 진행이 된다.
그렇다면?
file_Result에서 (file_result[i] - file_result[i-1]) / file_Data[i]라는 일반화 식을 만들 수 있다. 

<img width="1787" height="211" alt="화면 캡처 2025-12-21 044330" src="https://github.com/user-attachments/assets/ee610e9d-c960-4104-acb1-f65093ddf692" />

# 📚 공부한 내용
- 역연산 부분은 쉽다.. 단지 가상환경이 어떻게 굴러가는지만 알면 되는 내용이다.
