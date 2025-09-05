answer = [1] * 64
stackOn = False
index = 0
command =[]
commandStack = []
numStack = []
num_start = 0
num_end = 0
xor_stack = []
countStack = 0
for i in range(319):
    command.append(input())
for i in range(0,319):
    order = command[i]
    if order[0] == '1':
        num = order[2:-2]
        if 'x' in num: # 16진수면
            num = int(num, 16)
        else:# 16진수가 아니면
            num = int(num)
        numStack.append(num)
    elif order[0] == '2': # 스택 끝
        num_end = numStack.pop()
        tmp = num_end
        if xor_stack:
            for i in range(countStack):
                num_end = num_end ^ xor_stack.pop()
            countStack = 0
        xor_stack.append(tmp)
        answer[index] = num_end
    elif order[0] == '3': # 스택 시작
        num_start = numStack.pop()
        index = num_start
    elif order[0] == '4':
        countStack+=1
for i in answer:
    print(chr(i),end="")
