import time

# Kruskal's Logic
def run_kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    parent = list(range(n))
    def find(i):
        if parent[i] == i: return i
        return find(parent[i])
    
    mst_w = 0
    for u, v, w in edges:
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            mst_w += w
            parent[root_u] = root_v
    return mst_w

# Prim's Logic
def run_prim(n, adj):
    v_set = [False] * n
    min_w = [float('inf')] * n
    min_w[0] = 0
    mst_w = 0
    
    for _ in range(n):
        u = -1
        for i in range(n):
            if not v_set[i] and (u == -1 or min_w[i] < min_w[u]):
                u = i
        v_set[u] = True
        mst_w += min_w[u]
        for v, w in adj[u]:
            if not v_set[v] and w < min_w[v]:
                min_w[v] = w
    return mst_w

# Input Section
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

edges = []
adj = [[] for _ in range(n)]

print("Enter (u v w) for each edge:")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    adj[u].append((v, w))
    adj[v].append((u, w))

# Execution & Timing
s1 = time.time()
res_k = run_kruskal(n, edges)
t1 = (time.time() - s1) * 1000

s2 = time.time()
res_p = run_prim(n, adj)
t2 = (time.time() - s2) * 1000

# Final Output
print("\n--- Minimum Spanning Tree (MST) Results ---")
print("Algorithm: Kruskal's Method")
print(f"Result (Total Weight): {res_k}")
print(f"Execution Time: {t1:.4f} ms")

print("\nAlgorithm: Prim's Method")
print(f"Result (Total Weight): {res_p}")
print(f"Execution Time: {t2:.4f} ms")


