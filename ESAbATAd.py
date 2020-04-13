from itertools import combinations
import numpy as np
import sys

def complement(bitArr):
    return [None if b is None else '1' if b == '0' else '0' for b in bitArr]

def readBit(i):
    print(i, flush=True)
    return input()
    
# Read n / 2 pairs of bits at mirror positions from the middle of the string.
def readBits(n):
    global bits, unknownBits
    for _ in range(n):
        i = unknownBits.pop()
        bits[i] = readBit(i + 1)
        unknownBits = unknownBits[::-1]
        updateStates()
        
def updateStates():
    global states, bits
    complemented  = complement(bits)
    compReversed = complemented[::-1]
    reverse  = complement(compReversed)
    states = [bits, complemented, compReversed, reverse]

def findPairs():
    global B, unknownBits, states
    candidates = list(set(range(B)) - set(unknownBits))
    maxStates = len(set(map(tuple, states)))
    for idx in combinations(candidates, 2):
        nStates = len(set(tuple(np.take(state, idx)) for state in states))
        if nStates == maxStates:
            return idx
            
def solve():
    global bits, states
    testId = findPairs()
    test = [readBit(i + 1) for i in testId]
    bits = next(state for state in states if test == list(np.take(state, testId)))

T, B = map(int, input().split())
for _ in range(T):
    bits = [None] * B
    unknownBits = list(range(B))
    states = []
    # Fluctuations will begin to happen after the first response is given.
    # Therefore, the first 10 bits won't be fluctuated.
    readBits(10)
    while True:
        solve()
        try: readBits(8)
        except IndexError: break
    print('guess:', ''.join(bits), file=sys.stderr)
    print(''.join(bits), flush=True)
    if input() == 'N': sys.exit()
