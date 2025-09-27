n = int(input())
s = input()

graph = [[]]
vals = [0]
prev = [0]
newNodes = {}

questionMarks = 0

def addNode(val: int, parent: int):
    global newNodes

    if not newNodes.get(val):
        newNodes[val] = [parent]
    else:
        newNodes[val].append(parent)

def makeNodes():
    global newNodes
    global prev
    global graph

    prev = []
    for val, parents in newNodes.items():
        id = len(graph)
        vals.append(val)
        graph.append(parents)
        prev.append(id)
    newNodes = {}

for i in range(n):
    l = s[i]
    if l == '?':
        questionMarks += 1
        for el in prev:
            val = vals[el]
            addNode(val + 1, el)
            addNode(val - 1, el)      
    elif l == '+': 
        for el in prev:
            val = vals[el]
            addNode(val + 1, el)
    else:
        for el in prev:
            val = vals[el]
            addNode(val - 1, el)
    makeNodes()

k = pow(2, questionMarks - 1) # num of unique paths in tree
tops = set()

def findTops(path):
    #print(path)
    maxTop = -float('inf')
    found = []
    pathLen = len(path)
    for i in range(pathLen):
        el = path[i]
        if el > maxTop:
            maxTop = el
            found = [pathLen - i - 1] # path is reversed, gotta reverse it back
        elif el == maxTop:
            found.append(pathLen - i - 1)
    for j in found:
        tops.add(j)


paths = []

def makePath(id: int, curPath):
    curPath.append(vals[id])
    parents = graph[id]
    parLen = len(parents)
    while parLen > 0:
        if parLen == 2: #parLen is 2
            makePath(parents[1], curPath.copy())

        id = parents[0]
        curPath.append(vals[id])

        parents = graph[id]
        parLen = len(parents)
    findTops(curPath)
            

for i in range(questionMarks + 1):
    id = len(graph) - i - 1
    val = vals[id]
    makePath(id, [])

print(len(tops))
print(" ".join(map(str, tops)))

# print(graph)
# print(vals)
# print(tops)