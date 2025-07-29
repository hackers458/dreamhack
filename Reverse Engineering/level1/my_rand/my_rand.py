str2 = "49 2A 43 B4 B3 22 AF A9 29 4B 71 22 33 5A B1 56 56 9C B3 B2 61 74 A3 39 3D 7E 78 F8 A2 AC 00 46 0B D6 CD A3 E5 C1 66 F9 F7 3D DD 47 DB 1E FA 1F AA 58 FE 94 1B 0F 67 DA 10 BB EE 03 C6 37 4D 51 65 67 A5 37 30 9B F1 5E 19 96 A8 98 5B A4 8F B7 78 12 E2 ED F8 72 CB E0 92 AA F0 0D DF E9 87 BE CA F0 D5 50 73 84 BE 1A 38 A0 F2 F5 89 05 D4 3C 15 E6 50 83 18 8A 9F 0E 40 15 16 58 59 C0 83 6B 7A A5 6D E5 7E 0E 7C E9 CF 82 84 5A 7D E5 9E 0A 1E 46 2C 88 B7 81 A2 53 9F 17 7F A2 80 D0 AD 8C C7 CF 33 3F 4C 9D AC AB 2A 3F CA 61 6B 24 01 C8 EC 39 AE FE 77 2C 5F 13 66 41 59 32 86 2F EC CB 26 86 81 CD E1 CA A7 52 FE 18 F7 25 1D 60 9B 93 11 F9 DC 24 C5 FD 12 E8 54 1F 75 B8 41 1C A1 54 2D 09 68 1B 3C D9 B6 EC D4 C6 65 55 52 0A B9 F0 23 FB 17 91 34 54 0B D4 6E 14 5C B3 97 ED CF 30 C0 25 4C 63"
index = 0
count = 0
list =[]
for i in str2:
    if index%12 == 0:
        a = i
        count+=1
    elif index%12 == 1:
        b = i
        count+=1
    if count == 2:
        list.append(int("0x"+(a+b),16))
        count = 0
    index+=1
a = 1
for i in list:
    h = i-((i*171)>>9)*3
    if h == 1:
        print(2,end=" ")
    if h == 2:
        print(0,end=" ")
    if h == 0:
        print(1,end=" ")
    a+=1
