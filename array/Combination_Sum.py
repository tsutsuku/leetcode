# Question No.39 Combination Sum
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        data = []
        candidate = list.copy(candidates)
        for i in candidate:
            if target - i > 0:
                nums = self.combinationSum(candidate[candidate.index(i):], target - i)
                if len(nums) > 0:
                    for d in nums:
                        d.insert(0, i)
                    data.extend(nums)
            elif target == i:
                data.append([i])
        return data



s = [2, 3, 6, 7]
print(Solution().combinationSum(s, 7))
