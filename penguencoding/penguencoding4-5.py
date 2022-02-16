dist = {
    0:  {'N': 1.00},
    1:  {'3': 1.00},
    2:  {'7': 1.00},
    3:  {'_': 1.00},
    4:  {'1': 0.99, '2': 0.01},
    5:  {'0': 0.01, '6': 0.06, '7': 0.31, '8': 0.36, '9': 0.26},
    6:  {'.': 1.00},
    10: {'_': 1.00},
    11: {'W': 1.00},
    12: {'1': 1.00},
    13: {'2': 1.00},
    14: {'2': 1.00},
    15: {'_': 1.00},
    16: {'0': 1.00},
    17: {'0': 0.02, '1': 0.22, '2': 0.35, '3': 0.28, '4': 0.13},
    18: {'.': 1.00}
}

def construct_ranges(dist, interval):
    r = interval[1] - interval[0]
    lo = interval[0]
    ranges = {}
    for c in dist:
        ranges[c] = (lo, lo + dist[c] * r)
        lo += dist[c] * r
    return ranges

def decode(code):
    interval = (0, 1.00)
    msg = ''
    for i in range(22):
        d = dist.get(i, {str(j) : 0.1 for j in range(10)})
        ranges = construct_ranges(d, interval)
        for c in ranges:
            low, high = ranges[c][0], ranges[c][1]
            if low <= code < high:
                msg += c
                interval = (low, high)
                break
        else: msg += '?'
    return msg

code = 0.55775570869445800781
print('encoded:', code)
print('decoded:', decode(code))
