'''
Библиотека с алгоритмом Хаффмана для питона
'''
import heapq
from collections import Counter, namedtuple

class Node (namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'

def encode(data):
    line = []

    for ch, freq in Counter(data).items():
        line.append((freq, len(line), Leaf(ch)))

    heapq.heapify(line)

    count = len(line)
    while len(line) > 1:
        freq1, _count1, left = heapq.heappop(line)
        freq2, _count2, right = heapq.heappop(line)
        heapq.heappush(line, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if line:
        [(_freq, _count, root)] = line
        code = {}
    root.walk(code, '')
    
    return code  


