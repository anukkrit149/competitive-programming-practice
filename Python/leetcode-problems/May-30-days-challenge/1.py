"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        last = n
        while start <= last:
            mid = (last + start) // 2
            if not isBadVersion(mid - 1) and isBadVersion(mid):
                break
            elif not isBadVersion(mid - 1) and not isBadVersion(mid):
                start = mid + 1
            elif isBadVersion(mid - 1) and isBadVersion(mid):
                last = mid - 1
        return mid


