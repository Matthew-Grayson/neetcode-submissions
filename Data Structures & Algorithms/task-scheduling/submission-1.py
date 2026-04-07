class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count occurences of each task and prioritize higher count
        # store count in max heap queue
        # pop tasks in groups of size min(n, len(maxheap))
        # increment cyclecount while maxheap by size min(n, n - len(maxheap))
        # optimize dictionary overhead using List [0] * 26 or ord keys
        
        if n == 0:
            return len(tasks)
        taskcounts = defaultdict(int)
        maxheap = []
        cyclecount = 0
        for task in tasks:
            taskcounts[task] += 1
        print("taskcounts: ", taskcounts)
        
        for taskcount in taskcounts:
            task, count = taskcount, taskcounts[taskcount]
            maxheap.append((count, task))
        heapq.heapify_max(maxheap)
        iteration = 0
        cooldowns = []
        while maxheap or cooldowns:
            iteration += 1
            print("i", iteration, "maxheap: ", maxheap, "cooldowns: ", cooldowns, "cyclecount: ", cyclecount)
            if cooldowns:
                updated_cooldowns = []
                for cooldown in cooldowns:
                    count, task, cd = cooldown
                    if cd == 0:
                        heapq.heappush_max(maxheap, (count, task))
                    else:
                        updated_cooldowns.append((count, task, cd - 1))
                if not maxheap:
                    cyclecount += 1
                cooldowns = updated_cooldowns
            if maxheap:
                cyclecount += 1
                count, task = heapq.heappop_max(maxheap)
                if count > 1:
                    cooldowns.append((count - 1, task, n))
                        
        print("i", iteration, "maxheap: ", maxheap, "cooldowns: ", cooldowns, "cyclecount: ", cyclecount)
        return cyclecount





