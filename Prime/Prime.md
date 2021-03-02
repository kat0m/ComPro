# Prime
## 概要
素数に関する処理
- 素数判定
- 素因数分解
- エラトステネスの篩

## 操作
### 素数判定
xが素数であるかどうか判定する。
bool値を返す。
```
x = 3

is_prime(x) # -> True
```

### 素因数分解
xを素因数分解する。(素数, べき指数)のタプルのリストを返す。
```
x = 120

print(prime_factorization(x)) # -> [(2, 3), (3, 1), (5, 1)]
```

### エラトステネスの篩
x以下の素数を列挙する。素数のリストを返す。
```
x = 20

print(sieve_of_eratosthenes(x)) # -> [2, 3, 5, 7, 11, 13, 17, 19]
```

## 素因数分解を用いる問題
- [AtCoder Beginner Contest 142: D](https://atcoder.jp/contests/abc142/tasks/abc142_d)