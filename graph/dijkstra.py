from heapq import heappush, heappop


def dijkstra(G, s):
    N = len(G)
    dist = [10**18] * N
    dist[s] = 0
    pq = []
    heappush(pq, (0, s))

    while pq:
        d, v = heappop(pq)

        if dist[v] < d:
            continue

        for nv, w in G[v]:
            if dist[nv] > dist[v] + w:
                dist[nv] = dist[v] + w
                heappush(pq, (dist[nv], nv))

    return dist
