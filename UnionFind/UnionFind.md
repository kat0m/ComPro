# Union-Find
## 概要
- グループ分けを管理する
  - 木構造による管理
  - $x$と$y$が同一グループに属し、$y$と$z$が同一グループに属するとき、$x$と$z$は同一グループに属する。
  - 同じグループに属することは、同じ木に属することを意味する。
- クエリ
  - 要素$x$と要素$y$が同一グループに属するか否かを判定する
  - 要素$x$が属するグループと要素$y$が属するグループを併合する
  - 要素$x$が属するグループのサイズを取得する
- 経路圧縮やランクの実装によって効率化可能
  - 今回は経路圧縮のみ実装

## 操作
### 初期化
nは要素数。
```
uf = UnionFind(n)
```
### グループ併合
xが属するグループとyが属するグループを結合する。
```
uf.unite(x, y)
```
### 同一グループの判定
xとyが同じグループに属するか判定する。
返り値はTrueまたはFalse。
```
uf.same(x, y)
```

### グループサイズ
要素xが属するグループのサイズを取得する。
```
uf.size(x)
```

## Union-Findを用いる問題
- [AtCoder Typical Contest 001: B](https://atcoder.jp/contests/atc001/tasks/unionfind_a)
- [AtCoder Beginner Contest 049: D](https://atcoder.jp/contests/abc049/tasks/arc065_b)  要復習
- [AtCoder Beginner Contest 075: C](https://atcoder.jp/contests/abc075/tasks/abc075_c) 要復習
- [AtCoder Beginner Contest 097: D](https://atcoder.jp/contests/abc097/tasks/arc097_b)
- [AtCoder Beginner Contest 120: D](https://atcoder.jp/contests/abc120/tasks/abc120_d)
- [AtCoder Beginner Contest 177: D](https://atcoder.jp/contests/abc177/tasks/abc177_d)
- [AtCoder Regular Contest 032: B](https://atcoder.jp/contests/arc032/tasks/arc032_2)