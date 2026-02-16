import copy

with open("quilt.bmp", "rb") as f:
    hex_string = f.read()
with open("data.bin", "rb") as f:
    data = list(f.read())
real_data =[]
tmp = []
for i in range(len(data)):
    if(i%3==0 and i!=0):
        real_data.append(copy.deepcopy(tmp))
        tmp.clear()
    tmp.append(data[i])
    
# 크기가 96이고 rgb가 있으므로 32이다.즉 이 32x32의 사각형이 있는 총 16개의 사각형에서 각각 사각형의 rgb를 추출한다.
base64=[]
hex_list = list(hex_string)[0x36:]
for i in range(0,len(hex_list),0x60): 
    test=[hex_list[i],hex_list[i+1],hex_list[i+2]]
    for j in range(len(real_data)):
        if(real_data[j]==test):
            base64.append(j)
#이 코드는 한 사각형의 32x32에서 높이 1~32의 층의 색깔이 다 똑같으므로 중복된건 제거
urm =[]
real_urm=[]
for i in range(0,len(base64),512):
    urm.append(base64[i:i+16])
#여기서 이제 짝수 홀수에 따른 뒤집기를 한다.
for  i in range(16):
    if(i%2!=0): # 짝수 홀수에 따른 뒤집기
        real_urm = real_urm + urm[i][::-1]
    else:
        real_urm = real_urm + urm[i]

#base64 -> 8비트로 하여 문자열 추출
real_urm = real_urm[::-1]
flag = ""
for i in range(256):
    flag = flag+(bin(real_urm[i])[2:].zfill(6))
for j in range(0,len(flag),8):
    print(chr(int(flag[j:j+8],2)),end="")
