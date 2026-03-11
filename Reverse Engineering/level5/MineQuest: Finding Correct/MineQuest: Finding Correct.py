from z3 import *
import re

def solve_checker(block_lines):
    var = [[BitVec(f"var_{i}_{j}", 1) for j in range(5)] for i in range(15)]
    var_arr = [BitVec(f"var_arr_{i}", 1) for i in range(10000)]
    solver = Solver()
    last_idx = None

    def parse_val(text):
        text = text.strip()
        if text == "1": return BitVecVal(1, 1)
        if text == "0": return BitVecVal(0, 1)
        m = re.match(r'var_arr\[(\d+)\]', text)
        if m: return var_arr[int(m.group(1))]
        m = re.match(r'var_(\d+)_(\d+)', text)
        if m: return var[int(m.group(1))][int(m.group(2))]

    for line in block_lines:
        line = line.strip()
        m = re.match(r'var_arr\[(\d+)\] = (.+)', line)
        if not m:
            continue
        idx = int(m.group(1))
        expr = m.group(2).strip()
        last_idx = idx

        m2 = re.match(r'(XOR|AND|OR)\((.+),\s*(.+)\)', expr)
        if m2:
            op = m2.group(1)
            a = parse_val(m2.group(2))
            b = parse_val(m2.group(3))
            if op == 'XOR': solver.add(var_arr[idx] == a ^ b)
            elif op == 'AND': solver.add(var_arr[idx] == a & b)
            elif op == 'OR':  solver.add(var_arr[idx] == a | b)
        else:
            solver.add(var_arr[idx] == parse_val(expr))

    solver.add(var_arr[last_idx] == 1)
    return solver, var

# all_blocks.txt 읽어서 checker별로 분리
blocks = {}
current = None
current_lines = []

with open('all_blocks.txt', 'r') as f:
    for line in f:
        m = re.match(r'# checker_(\d+)', line.strip())
        if m:
            if current is not None:
                blocks[current] = current_lines
            current = int(m.group(1))
            current_lines = []
        else:
            current_lines.append(line)
    if current is not None:
        blocks[current] = current_lines

# 30개 checker 순서대로 풀기
for c in range(30):
    solver, var = solve_checker(blocks[c])
    print(f"\n[ checker_{c} ]")
    if solver.check() == sat:
        model = solver.model()
        for i in range(5):
            row = ''
            for j in range(15):
                val = model[var[j][i]]
                row += '■' if val is not None and val.as_long() == 1 else '□'
            print(row)
    else:
        print("해 없음")
