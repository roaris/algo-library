# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A

from graph.dijkstra import dijkstra

V, E, r = map(int, input().split())
G = [[] for _ in range(V)]

for _ in range(E):
    s, t, w = map(int, input().split())
    G[s].append((t, w))

dist = dijkstra(G, r)

for v in range(V):
    if dist[v] == 10**18:
        print("INF")
    else:
        print(dist[v])
