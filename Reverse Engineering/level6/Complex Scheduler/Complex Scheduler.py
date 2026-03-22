import re
from z3 import *
from collections import defaultdict
import os
 
def parse_thread(code):
    lines = code.strip().split('\n')
    start_idx = 0
    for i, line in enumerate(lines):
        if 'pthread_barrier_wait' in line:
            start_idx = i + 1
            break
    events = []
    for line in lines[start_idx:]:
        line = line.strip()
        if re.search(r'sleep\(seconds\)', line):
            events.append(('sleep_var',))
            continue
        m = re.search(r'sleep\((0x[0-9a-fA-F]+|[0-9]+)u?\)', line)
        if m:
            val = m.group(1)
            events.append(('sleep', int(val, 16) if val.startswith('0x') else int(val)))
            continue
        m = re.search(r'pthread_mutex_trylock\(&(\w+)\)', line)
        if m:
            events.append(('trylock', m.group(1)))
            continue
        m = re.search(r'pthread_mutex_unlock\(&(\w+)\)', line)
        if m:
            events.append(('unlock', m.group(1)))
            continue
    intervals = []
    time_const = 0
    time_has_var = False
    pending = {}
    for ev in events:
        if ev[0] == 'sleep_var':
            time_has_var = True
        elif ev[0] == 'sleep':
            time_const += ev[1]
        elif ev[0] == 'trylock':
            pending[ev[1]] = (time_const, time_has_var)
        elif ev[0] == 'unlock':
            mutex = ev[1]
            if mutex in pending:
                s_c, s_v = pending[mutex]
                intervals.append((mutex, s_c, s_v, time_const, time_has_var))
                del pending[mutex]
    return intervals
 
def parse_all(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = re.split(r'=== THREAD_(\d+) @ 0x[0-9a-f]+ ===', content)
    all_intervals = {}
    i = 1
    while i < len(blocks) - 1:
        tid = int(blocks[i])
        all_intervals[tid] = parse_thread(blocks[i+1])
        i += 2
    return all_intervals
 
def verify(all_intervals, values):
    mutex_map = defaultdict(list)
    for tid, intervals in all_intervals.items():
        for (mutex, s_c, s_v, e_c, e_v) in intervals:
            start = s_c + (values[tid] if s_v else 0)
            end   = e_c + (values[tid] if e_v else 0)
            mutex_map[mutex].append((tid, start, end))
    conflicts = []
    for mutex, entries in mutex_map.items():
        for i in range(len(entries)):
            for j in range(i+1, len(entries)):
                tid_a, a_s, a_e = entries[i]
                tid_b, b_s, b_e = entries[j]
                if a_s < b_e and b_s < a_e:
                    conflicts.append((mutex, tid_a, a_s, a_e, tid_b, b_s, b_e))
    return conflicts
 
def solve(all_intervals):
    solver = Solver()
    s = [Int(f's{i}') for i in range(64)]
    for i in range(64):
        solver.add(s[i] >= 0, s[i] <= 15)
 
    mutex_map = defaultdict(list)
    for tid, intervals in all_intervals.items():
        for (mutex, s_c, s_v, e_c, e_v) in intervals:
            mutex_map[mutex].append((tid, s_c, s_v, e_c, e_v))
 
    for mutex, entries in mutex_map.items():
        for i in range(len(entries)):
            for j in range(i+1, len(entries)):
                tid_a, a_sc, a_sv, a_ec, a_ev = entries[i]
                tid_b, b_sc, b_sv, b_ec, b_ev = entries[j]
                a_start = a_sc + (s[tid_a] if a_sv else 0)
                a_end   = a_ec + (s[tid_a] if a_ev else 0)
                b_start = b_sc + (s[tid_b] if b_sv else 0)
                b_end   = b_ec + (s[tid_b] if b_ev else 0)
 
                # 같은 시점도 안되므로 < 사용
                solver.add(Or(a_end < b_start, b_end < a_start))
 
    print("Solving...")
    result = solver.check()
    if result == sat:
        model = solver.model()
        values = [model[s[i]].as_long() for i in range(64)]
        print("Solution found!")
        print("Values:", values)
        flag = ''.join(format(v, 'x') for v in values)
        print(f"Flag input: {flag}")
 
        conflicts = verify(all_intervals, values)
        if conflicts:
            print(f"\n[!] 충돌 {len(conflicts)}개 발견:")
            for c in conflicts[:10]:
                print(f"  {c[0]}: Thread{c[1]}[{c[2]},{c[3]}] vs Thread{c[4]}[{c[5]},{c[6]}]")
        else:
            print("\n[OK] 충돌 없음")
        return flag
    else:
        print("No solution found.")
        return None
 
if __name__ == '__main__':
    filepath = os.path.join(os.path.expanduser("~"), "threads.txt")
    all_intervals = parse_all(filepath)
    solve(all_intervals)
