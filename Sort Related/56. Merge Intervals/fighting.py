class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervalsSorted = sorted(intervals)
        result = [intervalsSorted[0]]
        for start, end in intervalsSorted[1: ]:
            currentEnd = result[-1][-1]
            if start <= currentEnd:
                result[-1][-1] = max(end, result[-1][-1])
            else:
                result.append([start, end])
        return result
                
    
test = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals2= [[1,4],[4,5]]
intervals3 = [[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]
print(test.merge(intervals3))