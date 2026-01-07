from pwn import *
DAT_00104020 = "36 db 42 6e 96 71 ee 50 93 1f f6 66 02 9d f5 58 58 ae 4f 5e e7 ce 41 69 ab a1 f8 47 8e e4 c2 59 5a c8 64 57 e1 2f ce 62 1a cb 5b 42 12 01 43 65 00 06 e8 7f 84 35 bf 5d 1a 22 10 52 7f ee 30 6e"
DAT_00104020 = DAT_00104020.split()
data_list = []
for i in range(0,len(DAT_00104020),4):
    data1 = DAT_00104020[i+3] + DAT_00104020[i+2] + DAT_00104020[i+1] + DAT_00104020[i]
    data_list.append(int(data1,16))
with open("main", "rb") as f:
    data = f.read()

data_base_address = 0x3060
for j in data_list:
    for i in range(0x0,0x10000):
        num = i
        lVar2 = 0
        success = True
        count = 16
        while(True):
            offset = data_base_address + ((num & 1) + lVar2 * 2) * 4
            lVar2 = int.from_bytes(data[offset:offset+4], "little", signed=True)
            count-=1
            if(count == 0):
                break
            if lVar2 == -1 or lVar2 > 0x3ffff:
                success = False
                break
            num >>= 1

        if success and lVar2 == j:
            print(hex(i).replace("0x",""),end="")
