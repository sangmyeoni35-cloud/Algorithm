from collections import deque

class Graph:
    def __init__(self):
        num_nodes, num_edges = map(int, input().split())
        self.directed = int(input('양방향 여부 (1:양방향, 0:단방향) : '))
        self.graph = [[] for _ in range(num_nodes+1)]
        for _ in range(num_edges):
            u, v = map(int, input().split())
            self.graph[u].append(v)
            if self.directed == 1:
                self.graph[v].append(u)

        self.visited = [] # for recursive dfs

    def dfs(self, node):
        print(node, end=' ')
        self.visited.append(node)
        for adj_node in sorted(self.graph[node]):
            if adj_node not in self.visited:
                self.dfs(adj_node)

    def bfs(self, start):
        visited = []
        queue = deque()
        # 시작 노드에 대해 작업
        queue.append(start)
        visited.append(start)
        print(start, end=' ')
        # 다음에 방문할 노드 찾아서 처리
        # 방문한 노드를 찾을 노드를 queue에서 가져와서 찾기
        while queue:
            node = queue.popleft()
            for abj_node in sorted(self.graph[node]):
                if abj_node not in visited:
                    queue.append(abj_node)
                    visited.append(abj_node)
                    print(abj_node, end=' ')

if __name__ == '__main__':
    g = Graph()
    start = int(input('시작 노드 번호 : '))
    g.dfs(start)
    print()
    g.bfs(start)
    print()