---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009\n\
    \n\ndef era(n):\n    is_prime = [True] * (n + 1)\n    is_prime[0] = False\n  \
    \  is_prime[1] = False\n\n    for i in range(2, int(n**0.5) + 1):\n        if\
    \ not is_prime[i]:\n            continue\n\n        for j in range(2 * i, n +\
    \ 1, i):\n            is_prime[j] = False\n\n    return is_prime\n\n\nis_prime\
    \ = era(10**6)\ncnt = [0] * (10**6)\n\nfor i in range(1, 10**6):\n    cnt[i] =\
    \ cnt[i - 1] + (1 if is_prime[i] else 0)\n\nwhile True:\n    try:\n        n =\
    \ int(input())\n        print(cnt[n])\n    except:\n        break\n"
  dependsOn: []
  isVerificationFile: true
  path: verify/math/eratosthenes.test.py
  requiredBy: []
  timestamp: '2022-12-16 21:11:29+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: verify/math/eratosthenes.test.py
layout: document
redirect_from:
- /verify/verify/math/eratosthenes.test.py
- /verify/verify/math/eratosthenes.test.py.html
title: verify/math/eratosthenes.test.py
---
