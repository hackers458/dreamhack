# 해당 코드는 AI를 사용한 코드입니다.. 차후 복습할 때 사용할 예정입니다.
import copy

grid_original = [
    [ -1,  -1,  -1,  -1,  96,  94,  93,  85,  -1,  -1,  78,  79,  72,  71,  -1],
    [101,  -1, 175, 180, 181,  -1,  92,  84,  86,  81,  80,  77,  -1,  73,  69],
    [102, 173,  -1, 179, 182, 183,  91,  89,  -1,  -1, 220, 219,  76,  74,  -1],
    [103,  -1, 177, 178, 184, 186, 187,  -1, 223,  -1,  -1,  -1,  -1,  -1,  67],
    [171,  -1,  -1, 164, 185, 188,  -1, 224, 222,  -1,  -1, 213,  -1, 215,  65],
    [170,  -1,  -1, 106, 163, 189, 225,  -1, 208,  -1, 206, 211, 214,  64,  -1],
    [169, 167, 166,  -1, 162,  -1, 192, 194,  -1, 207, 205,  59,  60,  61,  62],
    [117,  -1, 115, 108, 161, 197,  -1,  -1,  -1,  -1,  -1,  55,  58,  57,  50],
    [118, 116, 113, 109, 110, 160, 198, 199, 201,  34,  33,  53,  -1,  51,  -1],
    [119, 122, 123, 112, 111,  -1,  29,  30,  31,  32,  -1,  -1,  -1,  -1,  -1],
    [  1, 120, 121, 124,  27,  28, 158, 157,  40,  -1,  42,  36,  44,  47,  46],
    [  2,   3,  -1,  26,  -1, 126, 127, 156, 155,  39,  -1,  37,  -1, 146,  -1],
    [  5,  -1,  -1,  25,  21,  20,  17, 128, 129, 154, 153, 151, 150,  -1, 144],
    [  7,  -1,  -1,  22,  -1,  -1,  -1,  -1,  -1, 134, 152, 137, 149,  -1, 142],
    [  8,  -1,  10,  -1,  -1,  14,  -1,  -1, 132, 135,  -1,  -1,  -1, 140,  -1],
]

existing_original = set(
    grid_original[r][c]
    for r in range(15) for c in range(15)
    if grid_original[r][c] != -1
)

def get_neighbors(v2, v3):
    v4 = v2 if v2 <= 0 else v2 - 1
    v5 = v2 if v2 > 13 else v2 + 1
    v6 = v3 if v3 <= 0 else v3 - 1
    v7 = v3 if v3 > 13 else v3 + 1
    result = []
    for m in range(v6, v7 + 1):
        for n in range(v4, v5 + 1):
            if m != v3 or n != v2:
                result.append((m, n))
    return result

def solve(grid, existing, v2, v3, i):
    if i == 225:
        return grid

    neighbors = get_neighbors(v2, v3)

    # 1단계: 고정값 i+1이 이웃에 있으면 우선 이동
    for m, n in neighbors:
        if grid[m][n] == i + 1:
            result = solve(grid, existing, n, m, i + 1)
            if result is not None:
                return result

    # 2단계: 빈칸에 i+1 배치 (중복 방지 + 백트래킹)
    if (i + 1) not in existing:
        for m, n in neighbors:
            if grid[m][n] == -1:
                grid[m][n] = i + 1
                existing.add(i + 1)
                result = solve(grid, existing, n, m, i + 1)
                if result is not None:
                    return result
                # 백트래킹
                grid[m][n] = -1
                existing.remove(i + 1)

    return None

grid = copy.deepcopy(grid_original)
existing = set(existing_original)

print("풀이 시작...")
result = solve(grid, existing, 0, 10, 1)

if result is not None:
    print("성공!")
    for row in result:
        print(row)
    data = bytes(result[r][c] for r in range(15) for c in range(15))
    with open("answer.bin", "wb") as f:
        f.write(data)
    print("answer.bin 저장 완료")
else:
    print("풀이 실패 - 해가 없습니다")
