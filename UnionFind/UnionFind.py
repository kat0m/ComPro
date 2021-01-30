class UnionFind:
    def __init__(self, n):
        # parent[x]が負であるとき、xは木の根で、-parent[x]は集合のサイズ
        # parent[x]が非負であるとき、parent[x]はxの親
        self.parent = [-1 for _ in range(n)]

    def root(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.root(self.parent[x]) # 経路圧縮
        return self.parent[x]

    # xの属する集合 と yの属する集合 の連結
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if self.parent[rx] > self.parent[ry]:
            rx, ry = ry, rx
        self.parent[rx] += self.parent[ry]
        self.parent[ry] = rx

    # xとyが同じ集合に属するか否か
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # xが属する集合のサイズ
    def size(self, x):
        return -self.parent[self.root(x)]