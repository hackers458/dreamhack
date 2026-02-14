with open("output.mp3", "rb") as f:
    hex_string = f.read()
hex_list = list(hex_string)

index = 0
dword_4020 = [0xac44, 0xbb80, 0x7d00, 0, 0, 0, 0, 0]
dword_4040 = [0, 0x20, 0x28, 0x30, 0x38, 0x40, 0x50, 0x60, 0x70, 0x80, 0xa0, 0xc0, 0xe0, 0x100, 0x140, 0,
              8, 0x10, 0x18, 0x20, 0x28, 0x30, 0x38, 0x40, 0x50, 0x60, 0x70, 0x80, 0x90, 0xa0]

answer = []

while index + 4 <= len(hex_list):
    # MP3 프레임 헤더 확인
    if hex_list[index] != 0xFF or (hex_list[index + 1] >> 5) != 7:
        break

    # 프레임 크기 계산
    v6 = (hex_list[index + 1] >> 3) & 3
    v7 = (hex_list[index + 2] >> 4) + 15 * ((v6 ^ 3) & 3)
    v8 = dword_4020[(hex_list[index + 2] >> 2) & 3] >> (1 if v6 != 3 else 0)

    if v8 == 0:
        break

    v10 = 576 if v6 == 2 else 1152
    ptr = (hex_list[index + 3] << 24) | (hex_list[index + 2] << 16) | (hex_list[index + 1] << 8) | hex_list[index]
    v18 = 125 * dword_4040[v7] * v10 // v8 + (1 if (ptr & 0x20000) else 0)
    frame_size = v18 - 4

    # 범위 체크
    if index + 4 + frame_size > len(hex_list):
        break

    # 패리티 비트 계산
    v15 = 0
    for i in range(frame_size):
        v15 = (v15 ^ hex_list[index + 4 + i]) & 0xff

    v16 = ((v15 >> 4) ^ v15 ^ (((v15 >> 4) ^ v15) >> 2)) & 0xff
    v13 = (v16 ^ (v16 >> 1)) & 1

    # 은닉된 비트 추출 (헤더 수정 여부 확인)
    modified = (hex_list[index + 2] & 1)

    if modified:
        # 비트가 수정되었다면 원래 패리티와 다름
        answer.append(str(1 - v13))
    else:
        # 비트가 수정되지 않았다면 원래 패리티와 같음
        answer.append(str(v13))

    index += v18

# 비트를 바이트로 변환 (LSB first이므로 역순 없이)
result = ""
for i in range(0, len(answer), 8):
    if i + 8 <= len(answer):
        byte_bits = ("".join(answer[i:i + 8]))[::-1]
        byte_val = int(byte_bits, 2)
        if 32 <= byte_val <= 126:  # 출력 가능한 문자만
            result += chr(byte_val)

print("Extracted flag:", result)
print("Binary:", "".join(answer))
