import sys
from functools import lru_cache

sys.setrecursionlimit(10000)

@lru_cache(maxsize=1000)
def test():
    test()