import hashlib

X0 = 0xDEADBEEFDEADBEEF
MOD = 2**64
LAMBDA = 2**62
N = 312647161260980926

exp = pow(3, N, LAMBDA)
result = pow(X0, exp, MOD)

data = result.to_bytes(8, 'little')
flag = hashlib.sha256(data).hexdigest()

print("DH{" + flag + "}")
