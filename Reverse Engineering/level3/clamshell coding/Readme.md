# 🧩 Reverse Engineering Challenge: clamshell coding

📖 문제 개요

- 문제 이름: clamshell coding
- 출처: 드림핵
- 키워드: MASM 문법
- 설명: 랜덤으로 만들어진 리스트 파일과 헥스 옵코드를 전달하여 C언어파일에서실행되는 프로그램

# 🛠️ 사용 도구

- 어셈블러 코드 작성 웹사이트 : https://defuse.ca/online-x86-assembler.htm#disassembly

# 🚀 풀이 방법

- 프로그램 진행 그대로 프로그램을 작성하면 된다.

# 📁 파일 구성

- runner.c : 헥스 옵코드와 리스트들을 인자로 받아 foo를 실행하는 프로그램
- server.py: 랜덤으로 리스트값을 만들어주고 c언어를 실행해주는 프로그램

# 🔍 파일 동작 원리
<img width="670" height="990" alt="화면 캡처 2025-11-27 213049" src="https://github.com/user-attachments/assets/e62144c7-1451-4edf-bbac-89a334fcb221" />

에서 10~99사이의 숫자를 random개 만금 뽑아 만약 그 숫자가 3으로 나눠떨어지면 그대로 더하고 그렇지 않으면 x2하여 더한다.
그리고 ./runner 내가입력한헥스옵코드값 12 34 56 78.. 이렇게 실행이 되며
runner에서 foo 함수로 저걸 그대로 입력받아 가상으로 실행이 된다.


# 🧠 접근 방법
우선 사전 지식이 필요하다. MASM 문법으로 라벨을 함수처럼 작성할 수 있다는 것을 알아야 하며 
실행했을때 rdi값은 파라미터 개수(본인 포함)
rsi값은 포인터 배열로 ./runner 내가입력한헥스옵코드값 12 34 56 78.. 가 되면
rsi = runner의 배열 주소
rsi+8 = 내가입력한핵스옵코드값
rsi+16 = 12의 문자열 시작주소(1)
rsi+24 = 34의 문자열 시작주소 를 생각해야 하며

jmp은 항상 간접으로 이동한다는걸 알아야 한다.
jmp -128 ~ 127로 이동이 가능하며(jmp 기준으로)
jmp rax로 rax에 담긴 값으로 이동 가능하다는걸 알아야 한다.
그리고 어셈블리어 코드 짜는 법을 알아야 한다.......

## 스포주의!!
코드 짜면 된다.
rbp -16 합
rbp-24 : 8 배수 저장
rbp -32 : 8의배수
rbp -8 : 개수

mov     rax, rdi
sub     rax, 2
mov     qword ptr[rbp-8], rax # 
mov     rax, 0
mov     qword ptr[rbp-16], rax
mov     qword ptr[rbp-24], rax
mov     rax, 16
mov     qword ptr[rbp-32], rax


kknock:
mov rcx,qword ptr[rbp-32]
mov     rbx, qword ptr [rsi+rcx]
add rcx,8
mov qword ptr[rbp-32],rcx
movzx   eax, byte ptr[rbx]
sub     al, 48 
imul    eax, eax, 10
movzx   ecx, byte ptr[rbx+1]
sub     cl, 48
add     eax, ecx
mov rdi,rax
xor rdx,rdx
mov rcx,3
div rcx
test rdx,rdx
setnz dl
movzx rcx,dl
imul rcx,rdi
add rdi,rcx
mov rax,rdi
mov rcx,qword ptr [rbp-16]
add rcx,rax
mov qword ptr [rbp-16],rcx
mov rax,qword ptr[rbp-24]
add rax,1
mov qword ptr[rbp-24],rax
cmp rax, qword ptr[rbp-8]
je end
jmp kknock

end:
mov rax,qword ptr[rbp-16]
xor rdx,rdx
mov rcx,100
div rcx
mov rax,rdx
ret


# 📚 공부한 내용

- 함수 파라미터에 따른 레지스터의 값들을 복습했으며 MASM에 대해 다시 복습할 수 있었고 JMP문에 대해 자세히 알게 되었다.
