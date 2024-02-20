import sys


def iinp():
    return int(sys.stdin.readline().strip())


def linp():
    return list(map(int, sys.stdin.readline().strip().split()))


def lsinp():
    return sys.stdin.readline().strip().split()


def digit():
    return [int(i) for i in (list(sys.stdin.readline().strip()))]


def char():
    return list(sys.stdin.readline().strip())


def string():
    return sys.stdin.readline().strip()


from collections import Counter, defaultdict


def solve():
    n = iinp()
    nums = digit()
    count = defaultdict(int)
    count[0] += 1
    ans = 0
    cur = 0
    for i in range(n):
        cur += nums[i] - 1
        ans += count[cur]
        count[cur] += 1
    print(ans)


q = iinp()
for _ in range(q):
    solve()
