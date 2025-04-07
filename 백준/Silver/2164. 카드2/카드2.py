import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
cards = [x for x in range(1,n+1)]
cards = deque(cards)

def solution(cards):
    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())
    print(cards[0])

solution(cards)