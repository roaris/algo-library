---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import heappush, heappop\n\n\ndef dijkstra(G, s):\n    N = len(G)\n\
    \    dist = [10**18] * N\n    dist[s] = 0\n    pq = []\n    heappush(pq, (0, s))\n\
    \n    while pq:\n        d, v = heappop(pq)\n\n        if dist[v] < d:\n     \
    \       continue\n\n        for nv, w in G[v]:\n            if dist[nv] > dist[v]\
    \ + w:\n                dist[nv] = dist[v] + w\n                heappush(pq, (dist[nv],\
    \ nv))\n\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/dijkstra.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/dijkstra.py
layout: document
redirect_from:
- /library/graph/dijkstra.py
- /library/graph/dijkstra.py.html
title: graph/dijkstra.py
---
