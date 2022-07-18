class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total = 0
        res = 0
        start = -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            res += gas[i] - cost[i]
            
            if total < 0:
                total = 0
                start = i
            
        if res >= 0:
            return start + 1
        else:
            return -1