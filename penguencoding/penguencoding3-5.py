from num2words import num2words
# https://pypi.org/project/num2words/

POS = 0.400099153287787
# POS = 30829388370480/233280000000000

def n2w(n):
    r = num2words(n)
    return r.replace('-', ' ')

"""N00 00.000 W000 00.000"""
"""south forty six degrees twenty six point seven five one east one hundred and sixty nine degrees forty eight point two zero seven"""

def find_ans(possible, curr):
    low, high = curr[0], curr[1]
    r = high - low
    for i, n in enumerate(possible):
        frac = low + (i+1)/len(possible)*r
        if frac > POS:
            return n, (low + i/len(possible)*r, frac)
    return 'brocken', (0, 0)

c = (0.0, 1.0)
answer = ''

possible = sorted(['north ', 'south '])
result, c = find_ans(possible, c)
answer += result
# print(answer, c)

possible = sorted([n2w(n) + ' degrees ' for n in range(90)])
result, c = find_ans(possible, c)
answer += result
# print(answer, c)

possible = sorted([n2w(n) + ' point' for n in range(60)])
result, c = find_ans(possible, c)
answer += result
# print(answer, c)

possible = sorted([n2w(float('.' + str(n).zfill(3) + '1'))[10:-4] for n in range(1000)])
result, c = find_ans(possible, c)
answer += result
# print(answer, c)

possible = sorted([' east ',  ' west '])
result, c = find_ans(possible, c)
answer += result
# print(answer, c)

possible = sorted([n2w(n) + ' degrees ' for n in range(180)])
result, c = find_ans(possible, c)
answer += result 
# print(answer, c)

possible = sorted([n2w(n) + ' point' for n in range(60)])
result, c = find_ans(possible, c)
answer += result
# print(answer, c)

possible = sorted([n2w(float('.' + str(n).zfill(3) + '1'))[10:-4] for n in range(1000)])
result, c = find_ans(possible, c)
answer += result
# print(answer, c)

print('answer:', answer)