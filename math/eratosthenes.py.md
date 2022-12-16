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
  code: "def era(n):\n    is_prime = [True] * (n + 1)\n    is_prime[0] = False\n \
    \   is_prime[1] = False\n\n    for i in range(2, int(n**0.5) + 1):\n        if\
    \ not is_prime[i]:\n            continue\n\n        for j in range(2 * i, n +\
    \ 1, i):\n            is_prime[j] = False\n\n    return is_prime\n"
  dependsOn: []
  isVerificationFile: false
  path: math/eratosthenes.py
  requiredBy: []
  timestamp: '2022-12-16 21:11:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math/eratosthenes.py
layout: document
redirect_from:
- /library/math/eratosthenes.py
- /library/math/eratosthenes.py.html
title: math/eratosthenes.py
---
