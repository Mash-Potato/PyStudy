import collections

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

# def dfs(L, v, discovered=[]):
#     discovered.append(v)
#     for w in graph[v]:
#         print('L = ', L)
#         print('V = ', v)
#         print(discovered)
#         print(graph[v])
#         print(w)
#         print()
#         if not w in discovered:
#             discovered = dfs(L+1, w, discovered)
#
#     return discovered
#
# print(dfs(0, 1))  # 1 2 5 6 7 3 4


# def iterative_dfs(start_v):
#     discovered = []
#     stack = [start_v]
#     while stack:
#         v = stack.pop()
#         if v not in discovered:
#             discovered.append(v)
#             for w in graph[v]:
#                 stack.append(w)
#     return discovered
#
# print(iterative_dfs(1))  # 1 4 3 5 7 6 2

# def iterative_bfs(start_v):
#     discovered = [start_v]
#     q = [start_v]
#     q.append(start_v)
#     while q:
#         v = q.popleft()
#         for w in graph[v]:
#             if w not in discovered:
#                 discovered.append(w)
#                 q.append(w)
#     return discovered

def iterative_bfs(start_v):
    discovered = [start_v]
    dq = collections.deque()
    dq.append(start_v)
    while dq:
        v = dq.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                dq.append(w)
    return discovered

print(iterative_bfs(1))  # 1 2 3 4 5 6 7