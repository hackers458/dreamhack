from collections import deque
import queue
list = ['0x52','0xDF','0xB3','0x60','0xF1','0x8B','0x1C','0xB5','0x57','0xD1','0x9F','0x38','0x4B','0x29','0xD9','0x26','0x7F','0xC9','0xA3','0xE9','0x53','0x18','0x4F','0xB8','0x6A','0xCB','0x87','0x58','0x5B','0x39','0x1E']
def rol(value, shift):
    queue = deque([])
    value = bin(value)[2:]
    for i in value:
        queue.append(i)
    if(len(queue)<8):
        while(len(queue)!=8):
            queue.appendleft('0')
    for j in range(0,shift):
        h = queue.pop()
        queue.appendleft(h)
    answer = ""
    for i in queue:
        answer = answer + i
    answer = int(answer,2)
    print(chr(answer),end="")




index = 0
num2 = 0
for i in list:
    if(index == 8):
        index = 0
    num = int(i,16) ^ num2
    h = rol(num,index)
    index+=1
    num2+=1
