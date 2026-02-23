import struct

def u16(num):
    return num & 0xffff

def sub_1349(num):
    return u16(u16(0x5678 * (u16(0x4680 * num) | (u16(0x1234 * num) >> 11))))

def to_words(s):
    data = s.encode()
    words = []
    for i in range(0, len(data)-1, 2):
        words.append(struct.unpack_from('<H', data, i)[0])
    if len(data) % 2 == 1:
        words.append(data[-1])
    return words

for i in range(0xffff+1):
    key = hex(i)[2:].upper()
    num_len = len(key)
    data = to_words(key)
    hex_cafe = 0xcafe
    index = 0
    for j in range(num_len >> 1):
        v7 = data[index]
        index += 1
        v3 = sub_1349(v7)
        hex_cafe = u16(5 * (((v3 ^ hex_cafe) << 7) | (u16(v3 ^ hex_cafe) >> 9)) - 0x2153)
    v8 = 0
    if num_len & 1:
        v8 = data[index]
    v4 = sub_1349(v8)
    temp = u16(num_len ^ v4 ^ hex_cafe)
    v10 = u16(0xDEAD * ((temp >> 8) ^ temp))
    result = u16((u16(0xDEAD * ((v10 >> 5) ^ v10)) >> 8) ^ u16(0xDEAD * ((v10 >> 5) ^ v10)))
    if result == 0x796:
        print(hex(i))
