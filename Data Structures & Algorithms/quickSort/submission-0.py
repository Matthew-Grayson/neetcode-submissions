# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.helper(pairs, 0, len(pairs) - 1)
        return pairs


    def helper(self, arr, start, end):
        if end - start + 1 <= 1:
            return

        pivot = arr[end]
        left = start

        for i in range (start, end):
            if arr[i].key < pivot.key:
                temp = arr[i]
                arr[i] = arr[left]
                arr[left] = temp
                left += 1

        arr[end], arr[left] = arr[left], arr[end]
            
        self.helper(arr, start, left - 1)
        self.helper(arr, left + 1, end)
