# 素数判定
def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

# 素因数分解
def prime_factorization(x):
    if x <= 1:
        return None
    pf = []
    if x % 2 == 0:
        cnt = 0
        while x % 2 == 0:
            cnt += 1
            x //= 2
        pf.append((2, cnt))
    i = 3
    while i * i <= x:
        if x % i == 0:
            cnt = 0
            while x % i == 0:
                cnt += 1
                x //= i
            pf.append((i, cnt))
        i += 2
    if x != 1:
        pf.append((x, 1))
    return pf

# エラトステネスの篩
# x以下の素数を列挙
def sieve_of_eratosthenes(x):
    if x <= 1:
        return None
    prime = [True for _ in range(x+1)]
    prime[0] = False
    prime[1] = False
    for i in range(4,x+1,2):
        prime[i] = False
    i = 3
    while i * i <= x:
        if prime[i]:
            j = 2
            while i * j <= x:
                prime[i*j] = False
                j += 1
        i += 2
    prime_list = []
    for i in range(x+1):
        if prime[i]:
            prime_list.append(i)
    return prime_list