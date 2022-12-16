# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009


def era(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue

        for j in range(2 * i, n + 1, i):
            is_prime[j] = False

    return is_prime


is_prime = era(10**6)
cnt = [0] * (10**6)

for i in range(1, 10**6):
    cnt[i] = cnt[i - 1] + (1 if is_prime[i] else 0)

while True:
    try:
        n = int(input())
        print(cnt[n])
    except:
        break
