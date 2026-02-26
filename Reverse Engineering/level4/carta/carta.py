#게임 세팅
from pwn import *
import time
r = remote("host3.dreamhack.games",14271)
r.recvuntil(b'Stage ')
random_byte = int(r.recvline().decode().replace("\n","")) # 랜덤 값 leak

byte_4080 = [[0 for i in range(16)]for j in range(16)]
v1 = 0
for i in range(16):
    for j in range(0,16,2):
        byte_4080[i][j] = v1
        byte_4080[i][j+1] = v1
        result = v1+1
        v1 += 1



def uint(num):
    return num&0xff

def sub_12EE():
    global random_byte
    v1 = random_byte & 1
    result = uint(random_byte) >> 1
    random_byte = uint(random_byte) >> 1
    if ( v1 ):
        result = random_byte ^ 0xB8
        random_byte ^= 0xB8
    return result

for i in range(256):
    v6 = random_byte & 0xF
    v7 = random_byte >> 4
    sub_12EE()
    v8 = random_byte & 0xF
    v9 = random_byte >> 4
    sub_12EE()
    v2 = byte_4080[v6][v7]
    byte_4080[v6][v7] = byte_4080[v8][v9]
    result = v2
    byte_4080[v8][v9] = v2


#게임 찾기
visit = [[False for i in range(16)]for j in range(16)]
find_count = 0
for i in range(16):
    for j in range(16):
        if(not visit[i][j]):
            visit[i][j] = True
            num = byte_4080[i][j]
            find = False
            second_x =0
            second_y =0
            for m in range(16):
                if(find):
                    break
                for n in range(16):
                    if(num == byte_4080[m][n] and not visit[m][n]):
                        visit[m][n]= True
                        find = True
                        second_x = m
                        second_y = n
                        find_count += 1
                        break
            first_answer= f"{i} {j}".encode()
            second_answer = f"{second_x} {second_y}"
            r.sendline(first_answer)
            sleep(0.01)
            r.sendline(second_answer)
    if(find_count == 128):
        break
r.interactive()
