with open("output.bin", "rb") as f:
    encrypted_data = f.read()
encrypted_data = list(encrypted_data)

for i in range(len(encrypted_data)):
    encrypted_data[i] = bin(encrypted_data[i])[2:]
    encrypted_data[i] = encrypted_data[i].zfill(8)
    if(i%2 == 1):
        h = list(encrypted_data[i])
        for j in range(len(h)):
            if(h[j] == '0'):
                h[j] = '1'
            else:
                h[j] = '0'
        encrypted_data[i] = ''.join(h)
    x = encrypted_data[i][8-(i%8):]+encrypted_data[i][:8-(i%8)]
    print(chr(int(x,2)),end="")
