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

def makePath(id: int, curPath: list[int], foundTops: list[int] = [], maxTop: int = -float('inf'), iter: int = 0):
    curPath.append(vals[id])
    parents = graph[id]
    parLen = len(parents)

    val = vals[id]
    if val > maxTop:
        maxTop = val
        foundTops = [iter]
    elif val == maxTop:
        foundTops.append(iter)

    while parLen > 0:
        if parLen == 2: #parLen is 2
            makePath(parents[1], curPath.copy(), foundTops, maxTop)

        id = parents[0]
        iter += 1
        val = vals[id]
        curPath.append(val)

        if val > maxTop:
            maxTop = val
            foundTops = [iter]
        elif val == maxTop:
            foundTops.append(iter)

        parents = graph[id]
        parLen = len(parents)

    #print(curPath)
    #print(foundTops)
    pathLen = len(curPath)
    for el in foundTops:
        tops.add(pathLen - el - 1) # remember to reverse ts

            

for i in range(questionMarks + 1):
    id = len(graph) - i - 1
    val = vals[id]
    makePath(id, [])

print(len(tops))
print(" ".join(map(str, tops)))

# print(graph)
# print(vals)
# print(tops)