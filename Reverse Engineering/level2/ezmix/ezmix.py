with open("123.txt", "r") as f:
    hex_string = f.read()

with open("output.bin", "rb") as f:
    output_bin = f.read()

# 공백 기준으로 나눠서 리스트로 변환
hex_list = hex_string.strip().split()[2:]
output_bin = list(output_bin)


program_command = []
program_value = []

for i in range(len(hex_list)):
    if  i % 2 == 0:
        program_command.append(int(hex_list[i],16))
    if  i % 2 == 1:
        program_value.append(int(hex_list[i],16))

def twos_complement(val, bits=8):
    if val >= 0:
        return val
    return (1 << bits) + val

program_command = program_command[::-1]
program_value = program_value[::-1]
def rotate_left(x, n, bits=8):
    n %= bits
    return ((x << n) | (x >> (bits - n))) & ((1 << bits) - 1)


def rol(output_bin,program_value):
    for i in range(36):
        output_bin[i] = rotate_left(output_bin[i],program_value,8)
        output_bin[i] = twos_complement(output_bin[i])
def xor(output_bin,program_value):
    for i in range(36):
        output_bin[i] = output_bin[i] ^ program_value
        output_bin[i] = twos_complement(output_bin[i])
def minus(output_bin,program_value):
    for i in range(36):
        output_bin[i] = output_bin[i] - program_value
        output_bin[i] = twos_complement(output_bin[i])
for i in range(len(program_value)):
    if program_command[i] == 1 :
        minus(output_bin,program_value[i])
    if program_command[i] == 2:
        xor(output_bin,program_value[i])
    if program_command[i] == 3:
        rol(output_bin,program_value[i])
for i in output_bin:
    print(chr(i),end="")
