with open("secretMessage.enc", "rb") as f:
    data = f.read()  # 전체 바이트 읽기

# 특정 인덱스의 바이트 확인
index = 0
byte_value = data[index]
print(f"{index}번째 바이트: {byte_value:#02x}")  # 16진수 출력
def fgetc(index1):
    global data
    return data[index1]

def fwrite(num):
    with open("output.bin", "ab") as f:  # 'ab' = append + binary
        f.write(num.to_bytes(1, byteorder='little'))  # 4바이트로 변환해서 저장


str2 = ""
x = -1
y = 0
index = 0
while(True):
    getbyte = fgetc(index)
    index+=1
    fwrite(getbyte)
    if(getbyte == x):
        y = 0
        getbyte = fgetc(index)
        index+=1
        for i in range(getbyte):
            fwrite(x)
        fwrite(fgetc(index))
        index+=1
        x = getbyte
    else:
        x = getbyte

