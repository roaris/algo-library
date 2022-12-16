---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A\n\
    \nfrom graph.dijkstra import dijkstra\n\nV, E, r = map(int, input().split())\n\
    G = [[] for _ in range(V)]\n\nfor _ in range(E):\n    s, t, w = map(int, input().split())\n\
    \    G[s].append((t, w))\n\ndist = dijkstra(G, r)\n\nfor v in range(V):\n    if\
    \ dist[v] == 10**18:\n        print(\"INF\")\n    else:\n        print(dist[v])\n"
  dependsOn: []
  isVerificationFile: true
  path: verify/graph/dijkstra.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/graph/dijkstra.test.py
layout: document
redirect_from:
- /verify/verify/graph/dijkstra.test.py
- /verify/verify/graph/dijkstra.test.py.html
title: verify/graph/dijkstra.test.py
---
