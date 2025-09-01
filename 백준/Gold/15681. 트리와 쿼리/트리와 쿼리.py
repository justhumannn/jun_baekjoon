import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
a,b,c = map(int, input().split())
childNode = [[] * i for i in range(a+1)]
tree = {i:[] for i in range(1,a+1)}
size = [0] * (a+1)
for _ in range(a-1):
    d,e = map(int, input().split())
    tree[d].append(e)
    tree[e].append(d)
query = []
for _ in range(c):
    d = int(input())
    query.append(d)
def makeTree(currentNode, parent):
    for Node in tree[currentNode]:
        if Node != parent:
            childNode[currentNode].append(Node)
            makeTree(Node, currentNode)
def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for Node in childNode[currentNode]:
        countSubtreeNodes(Node)
        size[currentNode] += size[Node]
makeTree(b, -1)
countSubtreeNodes(b)
for i in query:
    print(size[i])