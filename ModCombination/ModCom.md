# Mod Combination
## 概要
- 二項係数nCrを1000000009で割った余りを答えるような問題に使う。
- 階乗や階乗の逆元の値を予め計算しておくことでnCrをすぐに計算できる。
- 階乗、階乗の逆元の計算にO(n)、nCrの計算にO(1)

## 使い方
### 初期化
MAXはnの最大値。計算量O(MAX)。
```
mc = ModCom(MAX, MOD)
```

### Combination(n, r)の計算
```
ans = mc.comb(n, r)
```

## Mod Combinationを用いる問題
- [AtCoder Beginner Contest 034: C](https://atcoder.jp/contests/abc034/tasks/abc034_c)