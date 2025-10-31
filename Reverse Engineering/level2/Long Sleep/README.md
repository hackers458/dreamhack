# 🧩 Reverse Engineering Challenge: Long Sleep
📖 문제 개요
- 문제 이름: Long Sleep
- 출처: 드림핵
- 키워드: 함수 추적 및 메모리 값 변경
- 설명: 프로그램이 어디서 멈추는지(또는 무한 루프를 어디서 도는지) 확인 한 뒤 해결하면 플래그가 나온다.

# 🛠️ 사용 도구
- IDA / Ghidra: 정적 분석
- GDB : 동적 분석

# 🚀 풀이 방법
- 프로그램이 어디서 멈추기 위해 GDB로 일일이 하나씩 추적하고 찾아가면서 Ghdira와 함께 수상한(?) 곳을 찾아 분석한 뒤 메모리 변조로 해결

# 📁 파일 구성
- prob : 플래그를 알려주는 프로그램

# 🔍 파일 동작 원리
<img width="682" height="626" alt="화면 캡처 2025-10-31 144551" src="https://github.com/user-attachments/assets/547b5fbd-abac-4629-acb5-d384e4cd331c" />

해당 부분은 파일의 변조 검사를 실행합니다. 만약 어셈블리 명령어를 바꾸면 오류를 출력하며 프로그램이 종료됩니다. 그렇기 위해 저 부분을 없에버리는 방법과

<img width="269" height="96" alt="화면 캡처 2025-10-31 144909" src="https://github.com/user-attachments/assets/3b0a88de-ee08-4d5e-877e-8fbb089815ca" />
<img width="447" height="348" alt="화면 캡처 2025-10-31 143751" src="https://github.com/user-attachments/assets/7cccde43-4682-4709-aba2-1ebd560cd189" />


해당 부분에 저 부분을 실행하지 않도록 DAT_00104030의 값을 0으로 바꾸는 방법이 있는데 0으로 바꾸니까 해결되었음.

<img width="895" height="657" alt="화면 캡처 2025-10-31 145208" src="https://github.com/user-attachments/assets/e51b9289-ecc5-4122-a901-40736662bd2f" />


# 📚 공부한 내용
- 플래그가 어떻게 생기는 지 이해하는게 아닌 프로그램이 어디서 멈추는 지 알기 위한 과정이 중요하며, syscall에서 rax의 값에 따른 호출이 변경된다는 것을 다시 한번 복습하게 되었음
- set *주소 = 값 으로 주소의 값을 변경할 수 있다.
- 프로그램을 전반적으로 이해하는 것이 아닌 필요한 부분만 보는게 중요, 전반적인 프로그램의 원리& 동작 방식보다는 문제의 의도를 파악하고 해결하는게 중요(쉽지 않음)

