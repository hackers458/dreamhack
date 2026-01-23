def bit_reverse_32(x: int) -> int:
    """32비트 정수의 비트를 뒤집는 함수"""
    result = 0
    for i in range(32):
        if (x >> i) & 1:
            result |= 1 << (31 - i)
    return result & 0xFFFFFFFF

def transform_list(data: list[int]) -> list[int]:
    """
    data: 바이트 값(0~255)이 담긴 리스트, 길이는 40
    4바이트 단위로 묶어서 비트 반전 수행
    """
    length = len(data)
    local_4c = 0
    result = data[:]  # 복사본

    while True:
        iVar2 = length
        if length < 0:
            iVar2 = length + 3
        if (iVar2 >> 2) <= local_4c:
            break

        # 4바이트 블록 추출 (리틀 엔디안)
        block = result[local_4c*4 : local_4c*4 + 4]
        val = int.from_bytes(bytes(block), byteorder="little")

        # 비트 반전
        new_val = bit_reverse_32(val)

        # 다시 4바이트로 저장
        new_bytes = list(new_val.to_bytes(4, byteorder="little"))
        result[local_4c*4 : local_4c*4 + 4] = new_bytes

        local_4c += 1

    return result

# 예시: 40바이트짜리 리스트
data = [0x66,0x0c,0x4c,0x86,0xa6,0x2c,0x1c,0x9c,
        0x1c,0x66,0x1c,0x2c,0x9c,0x6c,0xa6,0xcc,
        0xa6,0x6c,0x6c,0xac,0xa6,0xa6,0x86,0x4c,
        0x2c,0x46,0xec,0x8c,0xec,0x46,0x8c,0x9c,
        0x4c,0xec,0xc6,0x66,0x4c,0x46,0x86,0x4c]

out = transform_list(data)
print("변환 전:", data)
print("변환 후:", out)
for i in (out):
    print(chr(i),end="")
print("HEX:", bytes(out).hex())
