str1 = "ugvWzwjVigLZigeGy30VA3LLihn1AxnRlcbKAwbWzxqGAx5Gy30TCg02BMqGy3HVy30SywrLlcbTyx62zMfJDhvYzxqGyNKGpZ9@pZ9Gq30UzMvJDgLVBMvYEsbPBIbtB4v1AcblB4jLyqPqzwbLCM9Grgf6igLZigHLBgqGyx6UDxfSBhKGB35GtM03zx2IzwiGmte="
str2 = "7/OkZQIau/jou/R1by9acyjjutd0cUdlWshecQhkZUn1cUH1by9g4/9qNAn1byGaby9pbQSjWshgbUmqZAF+JtOBZUn1b8e1YoMPYoM1ny95ZAO+J/jaNAOB2vhrNLhVNDO0cshWNDIjbnrnZQhj4AM1S/Fmu/jou/GjN/n1bUm5JUFpNte1NyH1VA9yZUqLZQu13VR="
table="abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@"
result ="7/OkZQIau/jou/R1by9acyjjutd0cUdlWshecQhkZUn1cUH1by9g4/9qNAn1byGaby9pbQSjWshgbUmqZAF+JtOBZUn1b8e1YoMPYoM1ny95ZAO+J/jaNAOB2vhrNLhVNDO0cshWNDIjbnrnZQhj4AM1S/Fmu/jou/GjN/n1bUm5JUFpNte1NyH1VA9yZUqLZQu13VR="
str_index = []
flag = "S/jeutjaJvhlNA9Du/GaJBhLbQdjd+n1Jy9BcD3="
string_flag =""
table2="0hs0RF/tuI0W3d0YnSvV7OUQbZcN4J201GL+ejA80r0lpg5ak0Bo0qyDHm00M90P"
str2_table = [0 for i in range(64)]

# STEP1 테이블 구하기
for i in str1:
    str_index.append(table.find(i))

for i,j in enumerate(str2):
    if(j == '='):
        continue
    str2_table[str_index[i]] = j
for k in range(len(str2_table)):
    str2_table[k] = str(str2_table[k])


# STEP2 플래그 구하기
for i in flag:
    string_flag+=bin((table2.find(i)))[2:].zfill(6)
i= 0
while(True):
    print(chr(int(string_flag[i:i+8],2)),end="")
    i+=8
