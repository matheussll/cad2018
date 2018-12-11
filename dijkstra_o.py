from collections import defaultdict
from heapq import *

infinity = float('inf')

def dijkstra(edges, start, end):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
    q, seen = [(0,start,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path += (v1, )
            if v1 == end: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                next = cost + c
                heappush(q, (next, v2, path))
    return infinity

lines = open('dij_entries.txt').read().split('\n')
entries = [line.split(" ") for line in lines]
header = entries.pop(0)

edges = []
for entrie in entries:
    entrie[2] = int(entrie[2])
    edges.append(tuple(entrie))

start = header[0]
end = header[1]
print "=== Dijkstra ==="
print start + " -> " + end + ": " + str(dijkstra(edges, start, end))
