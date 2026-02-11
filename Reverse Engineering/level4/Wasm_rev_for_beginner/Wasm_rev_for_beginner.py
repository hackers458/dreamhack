data = "1f cd 88 9d bb 2b 56 50 e6 7b f6 91 82 82 7c 25 19 a0 92 9a 74 6e 96 e3 67 23 0b b8 01 a9 33 7d 6d ea 42 cd 1a 20 ab e8 e4 a3 27 87 97 0e 06 d6 5d 76 4c a9 e4 d0 99 c7 21 70 35 12 36 17 c5 eb f7 c1 22 90"
data = data.split()

result = "c4 e6 7c ad 5b 1c 2c e3 6b 0e f2 b0 d3 b9 01 f5 71 ff a3 f1 72 b4 86 03 f8 a6 87 5b fd 8e 4c 5d 9a 34 e2 ca 64 36 2b 27 10 40 36 15 86 e3 c9 49 c8 65 3a 4d 51 22 e1 55 65 cd c1 ec 32 d2 a0 68 a9 ca b3 2e".split()

data_list=[]
for i in range(len(data)):
    result[i] = int(result[i],16)
    data[i] = int(data[i],16)


def to_ubyte(value):
    """unsigned 8-bit: 0 ~ 255"""
    return value & 0xFF

answer= []
#역연산 하는 부분
ivar1 =0
for i in range(68):
    for j in range(32,128):
        if result[i]==to_ubyte((j^data[i])*13+37):
            print(chr(j),end="")
