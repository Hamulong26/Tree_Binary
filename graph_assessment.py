from collections import deque, defaultdict

class GraphAssessment:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    # Breadth-First Search (BFS)
    def print_bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)

            # Sort neighbors alphabetically for consistent traversal order
            neighbors = sorted(self.adj_list[curr])
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print("Graph BFS Traversal:", " -> ".join(result))

    # Depth-First Search (DFS)
    def print_dfs(self, start_node):
        visited = set()
        stack = [start_node]
        result = []

        while stack:
            curr = stack.pop()

            if curr not in visited:
                visited.add(curr)
                result.append(curr)

                # Push neighbors in reverse alphabetical order so smallest is processed first
                neighbors = sorted(self.adj_list[curr], reverse=True)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)

        print("Graph DFS Traversal:", " -> ".join(result))

if __name__ == "__main__":
    graph = GraphAssessment()

    # Building Graph edges using HAMULONG
    graph.add_edge('H', 'A')
    graph.add_edge('H', 'M')
    graph.add_edge('A', 'U')
    graph.add_edge('A', 'L')
    graph.add_edge('M', 'O')
    graph.add_edge('M', 'N')
    graph.add_edge('U', 'G')
    graph.add_edge('L', 'O')
    graph.add_edge('N', 'G')

    # Execute BFS and DFS
    graph.print_bfs('H')
    graph.print_dfs('H')