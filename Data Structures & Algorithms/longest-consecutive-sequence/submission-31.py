class Solution:

  def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
      return 0

    longest = 0
    numset = set(nums) # set of nums, we can see if one is consecurtive if its in the set

    for num in numset:
      if num - 1 not in numset: # start of a sequence
        length = 1
        while num + length in numset:
          length += 1
        longest = max(longest, length)
    
    return longest
      
