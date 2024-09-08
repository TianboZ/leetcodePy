
"""
solution:
                2
                /\\\\\
 use times  0*2 1*2  2*2....
 
 for each num, we can use 0 times, 1 time, ... .n times

 complextiy:
 time O(branch ^ level) 

"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.dfs(0, nums, 0, target, [])

        return self.ans
    
    # currSum is current sume
    def dfs(self, i, nums, currSum, target, path):
        # base case
        if i == len(nums):
            if currSum == target:
                # print(path)
                
                # build result
                res = []
                for j in range(len(path)):
                    cnt = path[j]
                    for _ in range(cnt):
                        res.append(nums[j])
                print(res)
                self.ans.append(res)
            return

        # cursive rule
        n = nums[i]
        j = 0  # count how many time we use `n`
        while currSum + j * n <= target:
            path.append(j)
            self.dfs(i + 1, nums, currSum + j * n, target, path)
            path.pop()

            j += 1