#!/usr/bin/env python3
flag = "62 75 BD CE 37 73 5E 3A BB C4 39 C2 95 33 B4 89 85 D2 95 3A 80 9F 78 67 D2 75 BE 92 4D B8 9E 85 73 D7 79 BB 9C 77 74 C1 85 97 9C 39 BF 95 33 67 C3 3E B3 92 48 77 C1 78 6A"
flag = flag.split()
answer = []
for i in range(len(flag)):
    answer.append(int(flag[i],16))
x = bytearray(b'bu\xbd\xce7s^:\xbb\xc49\xc2\x953\xb4\x89\x85\xd2\x95:\x80\x9fxg\xd2u\xbe\x92M\xb8\x9e\x85s\xd7y\xbb\x9cwt\xc1\x85\x97\x9c9\xbf\x953g\xc3>\xb3\x92Hw\xc1xj')
with open("flag.bin", "wb") as f:  # "wb" = write binary
    f.write(x)
my_answer =[0 for i in range(57)]
inputable='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
for e in range(57):
    for j in inputable:
        key = ord(j)
        f = e % 3
        if f == 0:
            key = (key + 107) % 256
        elif f == 1:
            key = (key + 101) % 256
        else:
            key = (key + 89) % 256
        h = e % 3
        if h == 0:
            key ^= 39
        elif h == 1:
            key ^= 240
        else:
            key ^= 141
        y = e % 3
        if y == 0:
            key = (key - 39) % 256
        elif y == 1:
            key = (key - 240) % 256
        else:
            key = (key - 141) % 256
        if key == x[e]:
            my_answer[e] = j
            break
print(my_answer)
for i in my_answer:
    print(i,end="")


