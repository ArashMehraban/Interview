def merge_intervals(intervals):
    output = []
    # interval: [interval[0], interval[1]] 
    for interval in sorted(intervals, key = lambda interval:interval[0]):
        if output and interval[0] <= output[-1][1]:
            output[-1][1] = max(interval[1], output[-1][1])
        else:
            output.append(interval)
    return output   

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge_intervals(intervals))
    # [[1, 6], [8, 10], [15, 18]]
    intervals = [[1,4],[4,5]]
    print(merge_intervals(intervals))
    # [[1, 5]]
