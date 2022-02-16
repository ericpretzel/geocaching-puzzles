test_dist = {
    '_': 30,
    'A': 15,
    'B': 5,
    'C': 5,
    'D': 20,
    'E': 25
}
test_msg = 'ACE_BAD_DAD'

dist = {
    '_': 135,
    '.': 91,
    '0': 96,
    '1': 91,
    '2': 71,
    '3': 71,
    '4': 71,
    '5': 71,
    '6': 56,
    '7': 56,
    '8': 52,
    '9': 47,
    'N': 23,
    'W': 23,
    'E': 23,
    'S': 23,
}

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

def decode_msg(code, key):
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

key = encode(dist)
code = '0000' + bin(int('DBCF5E6AD83FAA86BA99C', base=16))[2:]
print('encoded:', 'DBCF5E6AD83FAA86BA99C')
print('decoded:', decode_msg(code, key))

"""N00_00.000_W000_00.000"""