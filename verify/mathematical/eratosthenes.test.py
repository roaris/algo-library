# verification-helper: PROBLEM https://yukicoder.me/problems/158

from mathematical.eratosthenes import era

N, K = map(int, input().split())
is_prime = era(N)
cnt = [0] * (N + 1)

for i in range(N + 1):
    if is_prime[i]:
        for j in range(i, N + 1, i):
            cnt[j] += 1

ans = 0

for i in range(N + 1):
    if cnt[i] >= K:
        ans += 1

print(ans)
