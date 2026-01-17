def rotate_right32(x, n):
    n &= 0x1f  # 0~31만 유효
    return ((x >> n) | (x << (32 - n))) & 0xffffffff
data_list = []
data_list.append((0x50504b003750201.to_bytes(8, 'little').hex()))
data_list.append(0x38a0201e0070000.to_bytes(8, 'little').hex())
data_list.append( 0x200c000005040471.to_bytes(8, 'little').hex())
data_list.append(0x502047703f10201.to_bytes(8, 'little').hex())
data_list.append(0x3ca020138050000.to_bytes(8, 'little').hex())
data_list.append(0x120000050604a5.to_bytes(8, 'little').hex())
data_list.append(0x52f035602040401.to_bytes(8, 'little').hex())
data_list.append(0x240030169020000.to_bytes(8, 'little').hex())
data_list.append(0x100f000005040446.to_bytes(8, 'little').hex())
data_list.append(0x50704d702340301.to_bytes(8, 'little').hex())
data_list.append(0x2c0030180d90000.to_bytes(8, 'little').hex())
data_list.append(0xa01f000005050405.to_bytes(8, 'little').hex())
data_list.append(0x5c203dc02030401.to_bytes(8, 'little').hex())
data_list.append(0x2070401be020000.to_bytes(8, 'little').hex())
data_list.append(0x8e1f0000050f0381.to_bytes(8, 'little').hex())
data_list.append(0x502045702190301.to_bytes(8, 'little').hex())
data_list.append(0x3cd020160020000.to_bytes(8, 'little').hex())
data_list.append(0x50000050504fc.to_bytes(8, 'little').hex())
data_list.append(0x50304f303cb0201.to_bytes(8, 'little').hex())
data_list.append(0x2010401700e0000.to_bytes(8, 'little').hex())
data_list.append(0xf7020000058703c8.to_bytes(8, 'little').hex())
data_list.append(0x5c6039a02030401.to_bytes(8, 'little').hex())
data_list.append(0x3ad0201d4050000.to_bytes(8, 'little').hex())
data_list.append(0xb20200000501047d.to_bytes(8, 'little').hex())
myanswer = []
stack1 = []
data2 = []
my_input = [0 for i in range(32)]
index = 0
counter = 0
length = 0xc1
command = "".join(data_list)
print(command)
while(True):
    print("".join(myanswer))
    choice = command[index:index+2]
    choice = int(choice,16)
    index+=2
    if(choice == 1):
        stack1.append(1)
    elif(choice == 2):
        data2.append(int(command[index:index+2],16))
        stack1.append(2)
        index+=2
    elif(choice == 3):
        data2.append(int(command[index:index+2],16))
        stack1.append(3)
        index+=2
    elif(choice == 4):
        stack1.append(4)
        data2.append(int(command[index:index+2],16))
        index+=2
    elif(choice == 5):
        answer = int(command[index:index+8],16)
        index+=8
        while(stack1):
            current_command = stack1.pop()
            if(current_command == 4):
                current_data = data2.pop()
                answer = rotate_right32(answer,current_data)
            elif(current_command == 3):
                current_data = data2.pop()
                answer ^=current_data
            elif(current_command == 2):
                current_data = data2.pop()
                answer -= current_data
            elif(current_command == 1):
                myanswer.append(hex(answer).replace("0x",""))
