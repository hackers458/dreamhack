answer=[0 for i in range(64)]
#연결 저장 모음
verify = {
    "main": ['.puts', '.exit', '.strlen', 'calculate', 'verify_func_2', '.printf', '.puts'],
    "verify_func_0": ['.puts', '.exit', 'calculate', 'main'],
    "verify_func_1": ['.puts', '.exit', 'calculate', 'verify_func_9'],
    "verify_func_2": ['.puts', '.exit', 'calculate', 'verify_func_1'],
    "verify_func_3": ['.puts', '.exit', 'calculate', 'verify_func_5'],
    "verify_func_4": ['.puts', '.exit', 'calculate', 'verify_func_37'],
    "verify_func_5": ['.puts', '.exit', 'calculate', 'verify_func_8'],
    "verify_func_6": ['.puts', '.exit', 'calculate', 'verify_func_3'],
    "verify_func_7": ['.puts', '.exit', 'calculate', 'verify_func_13'],
    "verify_func_8": ['.puts', '.exit', 'calculate', 'verify_func_19'],
    "verify_func_9": ['.puts', '.exit', 'calculate', 'verify_func_53'],
    "verify_func_10": ['.puts', '.exit', 'calculate', 'verify_func_46'],
    "verify_func_11": ['.puts', '.exit', 'calculate', 'verify_func_4'],
    "verify_func_12": ['.puts', '.exit', 'calculate', 'verify_func_54'],
    "verify_func_13": ['.puts', '.exit', 'calculate', 'verify_func_60'],
    "verify_func_14": ['.puts', '.exit', 'calculate', 'verify_func_50'],
    "verify_func_15": ['.puts', '.exit', 'calculate', 'verify_func_24'],
    "verify_func_16": ['.puts', '.exit', 'calculate', 'verify_func_48'],
    "verify_func_17": ['.puts', '.exit', 'calculate', 'verify_func_12'],
    "verify_func_18": ['.puts', '.exit', 'calculate', 'verify_func_56'],
    "verify_func_19": ['.puts', '.exit', 'calculate', 'verify_func_39'],
    "verify_func_20": ['.puts', '.exit', 'calculate', 'verify_func_38'],
    "verify_func_21": ['.puts', '.exit', 'calculate', 'verify_func_6'],
    "verify_func_22": ['.puts', '.exit', 'calculate', 'verify_func_58'],
    "verify_func_23": ['.puts', '.exit', 'calculate', 'verify_func_18'],
    "verify_func_24": ['.puts', '.exit', 'calculate', 'verify_func_57'],
    "verify_func_25": ['.puts', '.exit', 'calculate', 'verify_func_29'],
    "verify_func_26": ['.puts', '.exit', 'calculate', 'verify_func_44'],
    "verify_func_27": ['.puts', '.exit', 'calculate', 'verify_func_41'],
    "verify_func_28": ['.puts', '.exit', 'calculate', 'verify_func_47'],
    "verify_func_29": ['.puts', '.exit', 'calculate', 'verify_func_21'],
    "verify_func_30": ['.puts', '.exit', 'calculate', 'verify_func_17'],
    "verify_func_31": ['.puts', '.exit', 'calculate', 'verify_func_20'],
    "verify_func_32": ['.puts', '.exit', 'calculate', 'verify_func_25'],
    "verify_func_33": ['.puts', '.exit', 'calculate', 'verify_func_43'],
    "verify_func_34": ['.puts', '.exit', 'calculate', 'verify_func_28'],
    "verify_func_35": ['.puts', '.exit', 'calculate', 'verify_func_23'],
    "verify_func_36": ['.puts', '.exit', 'calculate', 'verify_func_51'],
    "verify_func_37": ['.puts', '.exit', 'calculate', 'verify_func_22'],
    "verify_func_38": ['.puts', '.exit', 'calculate', 'verify_func_16'],
    "verify_func_39": ['.puts', '.exit', 'calculate', 'verify_func_42'],
    "verify_func_40": ['.puts', '.exit', 'calculate', 'verify_func_34'],
    "verify_func_41": ['.puts', '.exit', 'calculate', 'verify_func_62'],
    "verify_func_42": ['.puts', '.exit', 'calculate', 'verify_func_15'],
    "verify_func_43": ['.puts', '.exit', 'calculate', 'verify_func_40'],
    "verify_func_44": ['.puts', '.exit', 'calculate', 'verify_func_52'],
    "verify_func_45": ['.puts', '.exit', 'calculate', 'verify_func_32'],
    "verify_func_46": ['.puts', '.exit', 'calculate', 'verify_func_35'],
    "verify_func_47": ['.puts', '.exit', 'calculate', 'verify_func_61'],
    "verify_func_48": ['.puts', '.exit', 'calculate', 'verify_func_14'],
    "verify_func_49": ['.puts', '.exit', 'calculate', 'verify_func_26'],
    "verify_func_50": ['.puts', '.exit', 'calculate', 'verify_func_0'],
    "verify_func_51": ['.puts', '.exit', 'calculate', 'verify_func_10'],
    "verify_func_52": ['.puts', '.exit', 'calculate', 'verify_func_11'],
    "verify_func_53": ['.puts', '.exit', 'calculate', 'verify_func_33'],
    "verify_func_54": ['.puts', '.exit', 'calculate', 'verify_func_31'],
    "verify_func_55": ['.puts', '.exit', 'calculate', 'verify_func_30'],
    "verify_func_56": ['.puts', '.exit', 'calculate', 'verify_func_45'],
    "verify_func_57": ['.puts', '.exit', 'calculate', 'verify_func_7'],
    "verify_func_58": ['.puts', '.exit', 'calculate', 'verify_func_55'],
    "verify_func_59": ['.puts', '.exit', 'calculate', 'verify_func_27'],
    "verify_func_60": ['.puts', '.exit', 'calculate', 'verify_func_49'],
    "verify_func_61": ['.puts', '.exit', 'calculate', 'verify_func_59'],
    "verify_func_62": ['.puts', '.exit', 'calculate', 'verify_func_36'],
}


def calculate(param_1: int) -> int:
    # param_1은 0~255 범위의 byte 값
    param_1 &= 0xFF

    # 첫 번째 단계
    bVar1 = ((param_1 >> 6) | ((param_1 ^ 0x3c) * 0x04)) * 0x05 + 0x7d
    bVar1 &= 0xFF

    # 두 번째 단계
    bVar1 = ((bVar1 * 0x20) | (bVar1 >> 3)) ^ 0xb2
    bVar1 &= 0xFF

    # 세 번째 단계
    bVar1 = ((bVar1 >> 4) | (bVar1 << 4)) * 0x03 - 0x2f
    bVar1 &= 0xFF

    # 네 번째 단계
    local_e = ((bVar1 >> 7) | (bVar1 * 0x02)) ^ 0xd4
    local_e &= 0xFF

    local_d = 0
    for local_c in range(8):
        local_d = (local_e & 1) | (local_d * 2)
        local_e >>= 1

    return local_d & 0xFF

with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
database = []


for index,value in enumerate(lines):
    database.append(value.split())
    database[index][1] = int(database[index][1],16)
start = "verify_func_28"
for i in range(64):
    # 첫번째 해당 함수에 요구하는 값 찾기
    for j in range(64):
        if database[j][0] == start:
            data = database[j][1]
            print(data)
    # 두번째 함수에서 만족하는 값을 입력해야하는 값 찾기
    for j in range(32,128):
        if data == calculate(j):
            answer[i] = chr(j)
            break
    # 세번째 다음 함수로 이동
    if(start != "main"):
        start = verify[start][3]
    else:
        start = verify[start][4]
print("".join(answer))
