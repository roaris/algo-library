# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C

from graph.warshall_floyd import warshall_floyd

V, E = map(int, input().split())
D = [[10**18] * V for _ in range(V)]

for v in range(V):
    D[v][v] = 0

for _ in range(E):
    s, t, d = map(int, input().split())
    D[s][t] = d

warshall_floyd(D)

for v in range(V):
    if D[v][v] < 0:
        exit(print("NEGATIVE CYCLE"))

for u in range(V):
    print(*[D[u][v] if D[u][v] != 10**18 else "INF" for v in range(V)])
