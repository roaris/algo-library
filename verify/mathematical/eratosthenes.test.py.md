---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: mathematical/eratosthenes.py
    title: mathematical/eratosthenes.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/158
    links:
    - https://yukicoder.me/problems/158
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/158\n\nfrom\
    \ mathematical.eratosthenes import era\n\nN, K = map(int, input().split())\nis_prime\
    \ = era(N)\ncnt = [0] * (N + 1)\n\nfor i in range(N + 1):\n    if is_prime[i]:\n\
    \        for j in range(i, N + 1, i):\n            cnt[j] += 1\n\nans = 0\n\n\
    for i in range(N + 1):\n    if cnt[i] >= K:\n        ans += 1\n\nprint(ans)\n"
  dependsOn:
  - mathematical/eratosthenes.py
  isVerificationFile: true
  path: verify/mathematical/eratosthenes.test.py
  requiredBy: []
  timestamp: '2022-12-16 21:55:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/mathematical/eratosthenes.test.py
layout: document
redirect_from:
- /verify/verify/mathematical/eratosthenes.test.py
- /verify/verify/mathematical/eratosthenes.test.py.html
title: verify/mathematical/eratosthenes.test.py
---
