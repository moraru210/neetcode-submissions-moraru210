class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []
        candidates.sort()
        def dfs(i, nums, val):
            if val == target:
                results.append(nums.copy())
                return
            if val > target or i == len(candidates):
                return
            
            nums.append(candidates[i])
            dfs(i+1, nums, val+candidates[i])
            nums.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,nums,val)

        dfs(0,[], 0)
        return results

            

        