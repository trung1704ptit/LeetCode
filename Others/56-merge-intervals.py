class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]

        for interval in intervals[1:]:
            print(result)
            # result[-1] is the last item of result
            # result[-1][1] is the second value of last item in result
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result