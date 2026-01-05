from pwn import *
import functools
import math
import time

r = remote("host3.dreamhack.games", 22606)

def fun1(x,y,z):
    return 1.0 - (x+y+z)/(math.sqrt(x**2+y**2+z**2)*math.sqrt(3.0))
def compare(a, b):
    dVar1 = fun1(a[1], a[2],a[3])
    dVar2 = fun1(b[1], b[2],b[3])
    if abs(dVar1 - dVar2) < 1e-7:
        return 0
    if dVar1 > dVar2:
        return 1
    return -1

num_list = []
print(r.recvline().decode())
for i in range(30):
    num_list.append(r.recvline().decode().split())
    num_list[i][0] = num_list[i][0].replace(":", "")
    for j in range(4):
        num_list[i][j] = int(num_list[i][j])

num_list.sort(key=functools.cmp_to_key(compare))


for item in num_list:
    r.sendline(str(item[0]).encode())
    time.sleep(0.4)
r.interactive()
