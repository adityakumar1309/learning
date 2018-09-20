def merge_intervals(interval):
    interval.sort()
    final_interval = interval[0]
    for i in xrange(1, len(interval)):
        tup = interval[i]
        start, end = tup
        if start >= final_interval[1]:
            final_interval = (final_interval[0], end)
        elif start < final_interval[1]:
            if final_interval[1] >= end:
                final_interval = (final_interval[0], final_interval[1])
            else:
                final_interval = (final_interval[0], end)
    return final_interval

intervals = [(1,3), (2,4), (5,7), (6,8)]
print "Input: %s"%(intervals)
print "Interval: (%s,%s)"%(merge_intervals(intervals))
