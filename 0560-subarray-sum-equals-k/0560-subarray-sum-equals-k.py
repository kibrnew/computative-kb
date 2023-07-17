class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		ans = 0 
		summ = 0
		dic = {0 : 1}
		for num in nums:
			summ = summ + num
			if summ - k in dic:
				ans = ans + dic[summ - k]
			if summ not in dic:
				dic[summ] = 1
			else:
				dic[summ] = dic[summ] + 1
		return ans