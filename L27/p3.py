# Graph = (V, E)

class Graph:
    def __init__(self):
        self.info = {}

    def add(self, start, end):
        # Add start -> end
        if start not in self.info:
            self.info[start] = []
        self.info[start].append(end)

        if end not in self.info:
            self.info[end] = []
        self.info[end].append(start)

    def show(self):
        print("\nAdjacency List:")
        for node in self.info:
            print(node, "->", self.info[node])


g = Graph()

while True:
    print("\n1. Create Graph")
    print("2. Show Graph")
    print("3. Exit")

    op = int(input("Enter your choice: "))

    if op == 1:
        n = int(input("Enter number of edges: "))

        for i in range(n):
            print("\nEdge", i + 1)
            start = input("Enter start vertex: ")
            end = input("Enter end vertex: ")

            g.add(start, end)

    elif op == 2:
        g.show()

    elif op == 3:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")