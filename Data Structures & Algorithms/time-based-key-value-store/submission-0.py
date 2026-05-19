class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])
        # list as storage gives O(1) set
    def get(self, key: str, timestamp: int) -> str:
        # use binary search for O(logn) get
        res = ""
        values = self.timeMap.get(key, [])
        left, right = 0, len(values) - 1
        
        while left <= right:
            mid = left + ((right - left) // 2)
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res
            

        
