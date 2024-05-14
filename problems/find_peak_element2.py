from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col  = len(mat[0])

        for i in range(row):
            peak_j = self.findRowPeak(mat[i])
            curr = mat[i][ peak_j]
            if self.checkAround(mat, i, peak_j, curr):
                return [i, peak_j]
                
        return [-1, -1]
    
    def findRowPeak(self, arr):
        lo = 0
        hi = len(arr) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] > arr[mid - 1]:
                lo = mid
            else:
                hi = mid    

        if arr[lo] >= arr[hi]: return lo
        return hi
        
    def checkAround(self, m, i, j, curr):
        if i > 0 and i < len(m) - 1 and m[i - 1][j] < curr and  curr > m[i + 1][j]:
            return True
        elif i == 0 and curr < m[i + 1][j]:
            return True
        elif i == len(m) - 1 and m[i - 1][j] < curr:
            return True
        return False