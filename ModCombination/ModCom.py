class ModCom:
    def __init__(self, MAX, MOD):
        self.MAX = MAX + 1
        self.MOD = MOD
        self.factorial = [1] * self.MAX
        self.factorial_inv = [1] * self.MAX
        self.inv = [1] * self.MAX
        for i in range(2, self.MAX):
            self.factorial[i] = self.factorial[i-1] * i % self.MOD
            self.inv[i] = self.MOD - self.inv[self.MOD%i] * (self.MOD//i) % self.MOD
            self.factorial_inv[i] = self.factorial_inv[i-1] * self.inv[i] % MOD
    def comb(self, n, k):
        if n < 0 or k < 0 or n < k:
            return 0
        return self.factorial[n] * (self.factorial_inv[n-k] * self.factorial_inv[k] % self.MOD) % self.MOD