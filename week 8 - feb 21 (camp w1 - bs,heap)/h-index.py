from typing import List


def hIndex(self, citations: List[int]) -> int:
    n = len(citations)
    i = 0
    j = n-1
    citation = 0
    while i <= j:
        mid = i + (j-i)//2
        if n - mid <= citations[mid] and (mid == 0 or citations[mid-1] <= n-mid ):
            citation = n-mid
            i = mid+1
            break
        elif citations[mid] < n - mid:
            i = mid+1
        else:
            j = mid-1
    return citation
    