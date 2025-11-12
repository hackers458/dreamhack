import ctypes

# 파일 읽기
with open("flag.bmp.enc", "rb") as f:
    encrypted_data = f.read()

# 결과 저장
with open("flag_decrypted.bmp", "wb") as f:
    pass  # 초기화

def fwrite(byte):
    with open("flag_decrypted.bmp", "ab") as f:
        f.write(byte.to_bytes(1, byteorder='little'))

# 회전 함수
def rotate_left(x, n, bits=8):
    n %= bits
    return ((x << n) | (x >> (bits - n))) & 0xFF

def rotate_right(x, n, bits=8):
    n %= bits
    return ((x >> n) | (x << (bits - n))) & 0xFF

# C rand() 사용
libc = ctypes.CDLL(None)
libc.srand(0xBEEF)

# 복호화 함수
def decrypt_zero(value):
    value = rotate_right(value, 4)
    rand_val = libc.rand()
    value = (value - rand_val) & 0xFF
    value = rotate_left(value, 7)
    return value

def decrypt_one(value):
    rand_val = libc.rand() % 8
    return rotate_left(value, rand_val)

def decrypt_two(value):
    value = (value + 24) & 0xFF
    rand_val = libc.rand() & 0xFF
    return value ^ rand_val

# 복호화 루프
for i in range(len(encrypted_data)):
    byte = encrypted_data[i]
    if i % 3 == 0:
        fwrite(decrypt_zero(byte))
    elif i % 3 == 1:
        fwrite(decrypt_one(byte))
    elif i % 3 == 2:
        fwrite(decrypt_two(byte))

print("복호화 완료!")
