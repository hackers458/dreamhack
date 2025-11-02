answer = list("C@qpl==Bppl@<=pG<>@l>@Blsp<@l@AArqmGr=B@A>q@@B=GEsmC@ArBmAGlA=@q")

for i in range(64):
    answer[i] = ord(answer[i])^3
answer = answer[::-1]
answer[0] = 0x3e
for i in range(64):
    answer[i] -=13

answer[0] = 101
answer[63] = 53
for i in range(64):
    print(chr(answer[i]),end="")
