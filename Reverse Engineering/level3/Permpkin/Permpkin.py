flag1 = list(map(int,"102 111 62 107 104 52 100 96 103 104 79 61 126 111 88 57 90 60 108 61 127".split())) #21개
flag2 =  list(map(int,"52 50 99 104 127 127 120 89 122 84 121 107 124 115 52 102 104 63 99 ".split())) #19개

c = "CC2A750B63821F45AC20839"
new_c=[] # 23개
for i in c:
    ascii_c = ord(i)
    if(ascii_c<58):
        new_c.append(ascii_c-40)
    elif(ascii_c<70):
        new_c.append(ascii_c-60)
    elif(ascii_c<80):
        new_c.append(ascii_c-70)
    elif(ascii_c<90):
        new_c.append(ascii_c-80)
print(new_c)

#flag1
for i in range(13):
    flag1[i]= flag1[i] ^ new_c[i]
for i in range(13,len(flag1)):
    flag1[i]= flag1[i] ^ new_c[i%13]
    #print(chr(flag1[index]),end="")
for i in range(13,-1,-1):
    tmp = flag1[0]
    flag1[0] = flag1[new_c[i]]
    flag1[new_c[i]] = tmp
for i in flag1:
    print(chr(i),end="")
#flag2
for i in range(13):
    flag2[i]= flag2[i] ^ new_c[i]
for i in range(13,len(flag2)):
    flag2[i]= flag2[i] ^ new_c[i%13]

for i in range(13,-1,-1):
    tmp = flag2[0]
    flag2[0] = flag2[new_c[i]]
    flag2[new_c[i]] = tmp
for i in flag2:
    print(chr(i),end="")
