from num2words import num2words

# arithmetic
def construct_ranges(dist, interval):
    r = interval[1] - interval[0]
    lo = interval[0]
    ranges = {}
    for c in dist:
        ranges[c] = (lo, lo + dist[c] * r)
        lo += dist[c] * r
    return ranges

def arithmetic_decode(code, dist):
    interval = (0, 1.00)
    msg = ''
    for i in range(5):
        ranges = construct_ranges(dist, interval)
        for c in ranges:
            low, high = ranges[c][0], ranges[c][1]
            if low <= code < high:
                msg += c
                interval = (low, high)
                break
        else: msg += '?'
    return msg

dist = {
    '1': 0.2,
    '3': 0.2,
    '4': 0.2,
    '7': 0.2,
    '9': 0.2
}
code = 5/37
print('encoded:', code)
code = arithmetic_decode(code, dist)
print('arithmetic decode:', code)

# huffman
class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def to_binary(self, target, s=''):
        if self.val == target: # leaf node
            return s
        if self.left:
            result = self.left.to_binary(target, s+'0')
            if result: return result
        if self.right:
            result = self.right.to_binary(target, s+'1')
            if result: return result
        return None
    
    def leftmost(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr.val

    def __gt__(self, other):
        return self.leftmost() > other.leftmost()
    
    def __str__(self):
        s = '(' if self.left or self.right else ''
        s += self.left.__str__() if self.left else self.val
        s += ':' + self.right.__str__() if self.right else ''
        return s + (')' if self.left or self.right else '')
    def __repr__(self):
        return self.__str__()

    def __hash__(self) -> int:
        return hash(self.__str__())
    def __eq__(self, other):
        return self.__str__() == other.__str__()

def encode(dist):
    freq = {}
    for c in dist:
        n = Node(c)
        freq[n] = dist[c]
    while len(freq) > 1:
        sort = sorted(freq, key=freq.get)
        i = 0
        a = sort[i]
        a_val = freq[a]
        while i < len(sort) and freq[sort[i]] == a_val:
            if a > sort[i]:
                a = sort[i]
            i += 1
        i = 0
        if a == sort[0]: i = 1
        b = sort[i]
        b_val = freq[b]
        if b_val == a_val:
            while i < len(sort) and freq[sort[i]] == b_val:
                if b > sort[i] and sort[i] > a:
                    b = sort[i]
                i += 1
        else: 
            while i < len(sort) and freq[sort[i]] == b_val:
                if b > sort[i]:
                    b = sort[i]
                i += 1
        
        join = Node()
        join.left = a
        join.right = b
        freq[join] = freq.pop(a)+freq.pop(b)
    return join

def huffman_decode(code, key):
    curr = key
    msg = ''
    for c in code:
        if c == '0':
            curr = curr.left
        elif c == '1':
            curr = curr.right
        if not (curr.left or curr.right):
            msg += curr.val
            curr = key
    return msg

dist = {
    '1': 1,
    '2': 2,
    '5': 2,
    '6': 2,
    '9': 1
}
key = encode(dist)
code = float('.' + huffman_decode('000' + bin(int(code, base=16))[2:], key))
print('huffman decode:', code)

# sorted
def n2w(n):
    r = num2words(n)
    return r.replace('-', ' ')

def find_ans(possible, curr):
    low, high = curr[0], curr[1]
    r = high - low
    for i, n in enumerate(possible):
        frac = low + (i+1)/len(possible)*r
        if frac > code:
            return n, (low + i/len(possible)*r, frac)
    return 'brocken', (0, 0)

c = (0.0, 1.0)
answer = 'north thirty seven degrees '

possible = sorted([n2w(n) + ' point' for n in range(16, 21)])
result, c = find_ans(possible, c)
answer += result

possible = sorted([n2w(float('.' + str(n).zfill(3) + '1'))[10:-4] + ' west one hundred and twenty two degrees ' for n in range(1000)])
result, c = find_ans(possible, c)
answer += result

possible = sorted([n2w(n) + ' point' for n in range(0, 5)])
result, c = find_ans(possible, c)
answer += result

possible = sorted([n2w(float('.' + str(n).zfill(3) + '1'))[10:-4] for n in range(1000)])
result, c = find_ans(possible, c)
answer += result

print('sorted decode:', answer)