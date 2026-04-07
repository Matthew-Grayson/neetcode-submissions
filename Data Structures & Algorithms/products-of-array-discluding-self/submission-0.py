class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = []

        prev = 1
        for i in range(len(nums)):
            prefix[i] = nums[i] * prev
            prev = prefix[i]

        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = nums[i] * prev
            prev = postfix[i]

        for i in range(len(nums)):
            if i == 0 and postfix[i + 1]:
                res.append(postfix[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix[i - 1])
            else:
                res.append(prefix[i - 1] * postfix[i + 1])
        print(prefix, postfix)
        return res

