def warshall_floyd(D):
    N = len(D)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if D[i][k] == 10**18 or D[k][j] == 10**18:
                    continue

                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
