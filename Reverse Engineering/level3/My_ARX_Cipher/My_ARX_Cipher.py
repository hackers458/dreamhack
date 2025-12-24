
key = "SuP3RSaFeK3Y"
new_key =[]
final_key=[]
for i in key:
    new_key.append(hex(ord(i)).replace("0x",""))
for i in range(6):
    final_key.append(0xffff&int(new_key[(i)*2+1]+new_key[i*2],16))


with open("flag123.enc", "rb") as f:
    hex_string = f.read()
def rotate_left(x, n, bits=16):
    n %= bits
    return ((x << n) | (x >> (bits - n))) & ((1 << bits) - 1)

def rotate_right(x, n, bits=16):
    n %= bits
    return ((x >> n) | (x << (bits - n))) & ((1 << bits) - 1)

def twos_complement(value: int, bit_width: int) -> int:

    if value >= 0:
        return value
    else:
        return (1 << bit_width) + value


# 공백 기준으로 나눠서 리스트로 변환
hex_list = list(hex_string)
# for i in range(len(hex_list)):
#     hex_list[i] = hex(hex_list[i]).replace("0x","")
for j in range(0,len(hex_list),4):
    file1 = hex_list[j] | (hex_list[j+1] << 8)
    file2 = hex_list[j+2] | (hex_list[j+3] << 8)
    for i in range(2,-1,-1):
        file1^= final_key[i*2+1]
        local_10 = rotate_left(file1,9)
        file2^=final_key[i*2]
        file2-=local_10
        file2 = twos_complement(file2,16)
        local_12 = rotate_left(file2,9)
        file1,file2 = local_12,local_10
        
    list1 = hex(file1).replace("0x","")
    list2 = hex(file2).replace("0x","")
    # print(list1)
    # print(list2)
    print(chr(int(list1[2:4],16)),end="")
    print(chr(int(list1[0:2],16)),end="")
    print(chr(int(list2[2:4],16)),end="")
    print(chr(int(list2[0:2],16)),end="")



