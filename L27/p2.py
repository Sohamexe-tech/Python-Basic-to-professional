class Graph:
    def __init__(self):
        self.info = {}

    def add(self, start, end):
        if start in self.info:
            self.info[start].append(end)
        else:
            self.info[start] = [end]

    def bfs(self, start):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            if node in self.info:
                for neighbour in self.info[node]:
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.append(neighbour)


g = Graph()

while True:
    print("\n1. Create Edge")
    print("2. Perform BFS")
    print("3. Exit")

    op = int(input("Enter Choice: "))

    if op == 1:
        start = input("Enter Start Node: ")
        end = input("Enter End Node: ")
        g.add(start, end)

    elif op == 2:
        start = input("Enter Starting Node for BFS: ")
        print("BFS Traversal:")
        g.bfs(start)
        print()

    elif op == 3:
        break

    else:
        print("Invalid Choice")