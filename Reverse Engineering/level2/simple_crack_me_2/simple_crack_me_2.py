answer = "F8 E0 E6 9E 7F 32 68 31 05 DC A1 AA AA 09 B3 D8 41 F0 36 8C CE C7 AC 66 91 4C 32 FF 05 E0 D9 91"
DEADBEEF = [0xDE,0xAD,0xBE,0xEF]
EFBEADDE = [0xEF,0xBE,0xAD,0XDE]
NUM_1133 = [0x11,0x33,0x55,0x77,0x99,0xBB,0XDD]

answer_list = answer.split()
for i in range(len(answer_list)):
    answer_list[i] = int(answer_list[i],16)

my_input = [ 33 for i in range(32)]

def INPUT_AND(my_val,memory_list,tmp_index):
    tmp_index = tmp_index % len(memory_list)
    my_val = my_val ^ memory_list[tmp_index]
    return my_val
def INPUT_PLUS(my_val,memory_val):
    if(my_val + memory_val>=256):
        return my_val + memory_val - 256
    else:
        return my_val + memory_val
def INPUT_MINUS(my_val,memory_val):
    if my_val - memory_val<0:
        return (twos_complement(my_val-memory_val,8))
    return my_val - memory_val
def twos_complement(value, bits): #2의 보수
    return (value + (1 << bits)) % (1 << bits)



index = 0
for i in range(32):
    result = my_input[index]
    count = 0
    while(True):
        result = INPUT_AND(result,DEADBEEF,index)
        result = INPUT_PLUS(result,31)
        result = INPUT_MINUS(result,90)
        result = INPUT_AND(result, EFBEADDE,index)
        result = INPUT_MINUS(result, 77)
        result = INPUT_PLUS(result, 243)
        result = INPUT_AND(result, NUM_1133,index)
        if(result == answer_list[index]):
            my_input[index] = 33+count
            break
        else:
            count+=1
            result = my_input[index] + count
    index+=1
for i in my_input:
    print(chr(i),end="")
