import copy
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def to_byte(value):
    value = value & 0xFF
    return value

random_val = "41 28 19 4e a5 7c a1 41 13 cf 88 ac 2a f0 b7 da".split()
for i in range(len(random_val)):
    random_val[i] = int(random_val[i],16)
for i in range(0,15):
    random_val[i+1] +=random_val[i]
    random_val[i+1] = to_byte(random_val[i+1])
random_val[15] &=0xff
# 1. 설정: 키(16 bytes), IV(16 bytes), 암호화된 데이터
key = b'sixteen-byte-key'  # 16 bytes for AES-128
iv_key =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
iv = bytes(iv_key)   # 16 bytes for CBC
with open("out.txt", "rb") as f:
    data = f.read()
for i in range(0,0xff+1):
    new_random_val = copy.deepcopy(random_val)
    for j in range(16):
        new_random_val[j] ^=i
    key = bytes(new_random_val)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    raw_decrypted = cipher.decrypt(data)
    check = 0
    for i in raw_decrypted:
        if(i>128):
            check=1
            break
    if(check == 0):
        print(raw_decrypted.decode('ascii'))

