import copy
#STEP1 - 위치 인덱스 확인
data = "0b 08 03 04 01 00 0e 0d 0f 09 0c 06 02 05 07 0a 0f 04 08 0b 06 07 0d 02 0c 03 05 0e 0a 00 01 09 04 0c 0e 05 0d 06 09 0a 01 00 0b 0f 02 07 03 08 0a 08 0f 03 04 06 00 0b 01 0d 09 07 05 02 0c 0e 0b 06 09 0f 02 01 0a 0e 03 0c 0d 00 05 04 08 07 09 04 0b 05 06 0f 08 00 03 01 0a 0d 02 0e 0c 07 0a 0e 09 07 08 0d 03 0b 0c 0f 02 00 04 05 06 01 05 04 0d 01 00 02 09 0b 0c 07 08 0a 06 0e 0f 03 04 08 05 02 0a 0f 0b 07 00 01 0c 03 0e 06 09 0d 0d 0e 0f 0b 00 02 0a 04 07 06 09 01 05 03 08 0c 0e 02 03 05 0a 01 07 00 09 0d 0c 0b 04 06 0f 08 03 0b 0e 0a 06 04 07 01 02 0d 0f 00 0c 09 05 08 0d 0f 01 02 0c 0a 03 07 09 06 08 05 00 04 0b 0e 00 0e 04 0d 06 01 0a 05 03 0c 07 0b 0f 02 08 09 0b 02 08 07 05 03 09 0d 04 0f 00 01 06 0c 0e 0a 0b 01 08 00 0c 0d 04 0e 0a 06 0f 07 09 05 03 02"
data = list(data.split())
my_input=[]
for i in range(len(data)):
    data[i] = int(data[i],16)
for i in range(16):
    my_input.append(chr(65+i))
for i in range(48):
    my_input.append('0')
#print(my_input) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', '0', '0', '0', '0'.....
copy_my_input = copy.deepcopy(my_input)

for j in range(16):
    for k in range(16):
        if(j&1 != 0):
            copy_my_input[data[16*j+k]] = my_input[k+32]
        else:
            my_input[data[16*j+k]+32] = copy_my_input[k]
#print(copy_my_input) # ['B', 'F', 'M', 'L', 'I', 'K', 'G', 'J', 'A', 'H', 'C', 'O', 'N', 'D', 'P', 'E', '0', '0', '0'....
copy_my_input2 = copy.deepcopy(copy_my_input[0:16])
for i in range(16):
    copy_my_input2[i] = ord(copy_my_input2[i])-65
# STEP2 - 위치 인덱스에 기반하여 원위치 해놓는코드짜기
copy_my_input = list(input())
print(copy_my_input2)
answer= list("kkkkkkkkkkkkkkkk")
for index1 in range(16):        answer[index1]= copy_my_input[copy_my_input2.index(index1)]
print(''.join(answer))
