num = 0x0



def generate_flag(tmp):
    tmp = tmp%0x4a + 0x30
    print(chr(tmp),end="")

for i in range(64):
    a = (num+5)*3-7
    b = a<<3
    result = a+b+0x1f
    num = result
    str2 = str(hex(num))
    str2 = str2.replace("0x", "")
    str2 = str2.replace("x", "")
    num2 = int(str2[-8:],16)
    generate_flag(num2)
