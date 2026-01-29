import hashlib
import struct

with open("dword_4020", "rb") as f:
    data = f.read()
    dword_4020 = list(struct.unpack(f'<{len(data)//4}I', data))
print(dword_4020[0])
def transform(x):
    # 32비트 unsigned int로 제한
    result = ((x >> 25) | ((x >> 9) & 0xFF80) | ((x << 6) & 0x3F0000) | (x << 22))
    return result & 0xFFFFFFFF

dword_4020 = sorted(dword_4020, key=transform)

byte_data = struct.pack(f'<{len(dword_4020)}I', *dword_4020)
hash_result = hashlib.sha256(byte_data).hexdigest()
print(f"DH{{{hash_result}}}")
