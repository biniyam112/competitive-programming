class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted_new =[]
        i = j = 0
        while i < m and j < n:
            if i < m and nums1[i] < nums2[j]:
                sorted_new.append(nums1[i])
                i+=1
            elif j < n:
                sorted_new.append(nums2[j])
                j+=1
        if i < m:
            while i < m:
                sorted_new.append(nums1[i])
                i+=1
        elif j < n :
            while j < n:
                sorted_new.append(nums2[j])
                j+=1
        for i in range(len(sorted_new)):
            nums1[i] = sorted_new[i]

            
            
            
        