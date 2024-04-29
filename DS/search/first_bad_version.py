
def isBadVersion(x):
        pass
    
    
def firstBadVersion(self, n: int) -> int:
    if n == 0:
        return None

    l, r = 0, n-1
    while l <= r:
        mid = (l + r) // 2
        if isBadVersion(mid):
            r = mid - 1

        else:
            l = mid + 1
        return l
