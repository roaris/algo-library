---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: verify/graph/warshall_floyd.test.py
    title: verify/graph/warshall_floyd.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def warshall_floyd(D):\n    N = len(D)\n\n    for k in range(N):\n      \
    \  for i in range(N):\n            for j in range(N):\n                if D[i][k]\
    \ == 10**18 or D[k][j] == 10**18:\n                    continue\n\n          \
    \      D[i][j] = min(D[i][j], D[i][k] + D[k][j])\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/warshall_floyd.py
  requiredBy: []
  timestamp: '2022-12-16 22:37:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - verify/graph/warshall_floyd.test.py
documentation_of: graph/warshall_floyd.py
layout: document
redirect_from:
- /library/graph/warshall_floyd.py
- /library/graph/warshall_floyd.py.html
title: graph/warshall_floyd.py
---
