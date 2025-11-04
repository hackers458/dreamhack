from pwn import *
import time
import re
r = remote("host1.dreamhack.games",16643)
data = r.recvline()
data = r.recvline()
data = r.recvline()
data = r.recvline()
def start(count):
    global r
    data = r.recvline()
    data = data.decode()
    numbers = re.findall(r'\d+', data)
    print(numbers)
    for i in range(7):
        numbers[i] = hex(int(numbers[i])).replace("0x","")
    string = numbers[0].zfill(4)
    string = string+ (numbers[6].zfill(2))+ (numbers[5].zfill(2))+ (numbers[4].zfill(2))+ (numbers[3].zfill(2))+ (numbers[2].zfill(2))+ (numbers[1].zfill(2))
    string  = int(string,16)
    answer = ""
    while(string != 1):
        if(string%2 == 0):
            answer +="B"
            string = string//2
        else:
            answer +="A"
            string = string-1
    answer = "A"+answer[::-1]
    r.sendlineafter(b'Cast your spell!: ',answer)
    if(count !=9):
        r.recvuntil(b"[INFO]")
    time.sleep(0.1)
    return
count = 0
while(count<10):
    start(count)
    time.sleep(0.005)
    count+=1
r.interactive()
