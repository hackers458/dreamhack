from sympy import isprime

def sieve_of_eratosthenes(limit):
    while(True):
        if(isprime(limit)):
            return limit
        limit+=1
# 1단계 p , q 구하기
i = 2
while(True):
    p = sieve_of_eratosthenes(i)
    q = sieve_of_eratosthenes(p+128)
    if p*q == 4271010253:
        print(p,q) # 65287 65419 = p , q
        break
    i+=1


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

def modinv2(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception("No modular inverse")
    return x % phi



# 2단계 d 구하기
pqminus = (65286) * (65418) # 4,270,879,548
i = 1
d = modinv2(201326609, pqminus)
print(d) # 1384538333

# 3단계 복호화하기 - 거듭제곱 알고리즘 + 모듈러 구하기
def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # 먼저 base를 modulus로 나눠줌

    while exponent > 0:
        if exponent % 2 == 1:  # 홀수일 때
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus

    return result
#출력하는 부분 == 정답 아스키코드 4바이트 리틀엔디언
print(hex(modular_exponentiation(0xD4DCE140 ,1384538333,4271010253)))
print(hex(modular_exponentiation(0xA183DFE2,1384538333,4271010253)))
print(hex(modular_exponentiation(0xC363E306,1384538333,4271010253)))
print(hex(modular_exponentiation(0xF9D2E268,1384538333,4271010253)))
print(hex(modular_exponentiation(0xC41A2409,1384538333,4271010253)))
print(hex(modular_exponentiation(0x2A9BC0FB,1384538333,4271010253)))
print(hex(modular_exponentiation(0x9A4E22B5,1384538333,4271010253)))
print(hex(modular_exponentiation(0x7D38EF9A,1384538333,4271010253)))
print(hex(modular_exponentiation(0xB15F929F,1384538333,4271010253)))
print(hex(modular_exponentiation(0x9ED67BEF,1384538333,4271010253)))
print(hex(modular_exponentiation(0x99CDEAE7,1384538333,4271010253)))
list = [
    0x5f7b4844,
    0x5f415352,
    0x705f7331,
    0x69316275,
    0x72702d63,
    0x74347631,
    0x656b2d65,
    0x72635f79,
    0x30747079,
    0x70407267,
    0x7d217968
]

for j in list:
    h1 = hex(j).replace("0x", "")
    bytes_data = bytes.fromhex(h1)
    ascii_chars = bytes_data.decode("ascii", errors="replace")
    print(ascii_chars[::-1],end="")  # 리틀 엔디언 → 바이트 순서 뒤집기

