from collections import deque
import copy
with open("chall", "rb") as f:
    hex_string = list(f.read()[0x3060:0x6d69])
maze = [[[0 for i in range(25)] for j in range(25)]for k in range(25)]
index = 0
for i in range(25):
    for j in range(25):
        for k in range(25):
            maze[i][j][k] = hex_string[index]
            index+=1
position=[12,12,24,""] #x,y,z,answer




move=[[0,1,0],[0,-1,0],[1,0,0],[-1,0,0],[0,0,1],[0,0,-1]] #이동할 수 있는 모든 경우의 수
my_deque = deque()
my_deque.append(position)

def make_answer(answer_str,data):
    if data[0] == 1:
        answer_str+="2"
    if data[0] == -1:
        answer_str+="s"
    if data[1] == 1:
        answer_str+="z"
    if data[1] == -1:
        answer_str+="7"
    if data[2] == 1:
        answer_str+="K"
    if data[2] == -1:
        answer_str+="9"
    return answer_str



while(my_deque):
    tmp = my_deque.popleft()
    for i in move:
        new_position = [tmp[0] + i[0],tmp[1] + i[1],tmp[2] + i[2],tmp[3]]
        tmp_x = new_position[0]
        tmp_y = new_position[1]
        tmp_z = new_position[2]
        tmp_answer = new_position[3]
        if(0<=tmp_x<=24 and 0<=tmp_y<=24 and 0<=tmp_z<=24 and maze[tmp_x][tmp_y][tmp_z] == 0):
            maze[tmp[0]][tmp[1]][tmp[2]] = 1
            new_position[3] = make_answer(tmp_answer,i)
            my_deque.append(copy.deepcopy(new_position))
            if (new_position[0] == 12 and new_position[1] == 12 and new_position[2] == 0): # 도착점
                print(new_position)
                break



