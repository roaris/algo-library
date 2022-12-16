---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/warshall_floyd.py
    title: graph/warshall_floyd.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C\n\
    \nfrom graph.warshall_floyd import warshall_floyd\n\nV, E = map(int, input().split())\n\
    D = [[10**18] * V for _ in range(V)]\n\nfor v in range(V):\n    D[v][v] = 0\n\n\
    for _ in range(E):\n    s, t, d = map(int, input().split())\n    D[s][t] = d\n\
    \nwarshall_floyd(D)\n\nfor v in range(V):\n    if D[v][v] < 0:\n        exit(print(\"\
    NEGATIVE CYCLE\"))\n\nfor u in range(V):\n    print(*[D[u][v] if D[u][v] != 10**18\
    \ else \"INF\" for v in range(V)])\n"
  dependsOn:
  - graph/warshall_floyd.py
  isVerificationFile: true
  path: verify/graph/warshall_floyd.test.py
  requiredBy: []
  timestamp: '2022-12-16 22:37:34+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/graph/warshall_floyd.test.py
layout: document
redirect_from:
- /verify/verify/graph/warshall_floyd.test.py
- /verify/verify/graph/warshall_floyd.test.py.html
title: verify/graph/warshall_floyd.test.py
---
