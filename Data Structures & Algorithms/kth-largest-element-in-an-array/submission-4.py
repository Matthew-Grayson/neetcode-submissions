import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        lo, hi = 0, len(nums) - 1

        while True:
            p = random.randint(lo, hi)
            pivot = nums[p]

            nums[p], nums[hi] = nums[hi], nums[p]

            store = lo
            for i in range(lo, hi):
                if nums[i] < pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            
            nums[store], nums[hi] = nums[hi], nums[store]

            if store < target:
                lo = store + 1
            elif store > target:
                hi = store - 1
            else:
                return nums[store]