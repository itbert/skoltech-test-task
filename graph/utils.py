import random
import matplotlib.pyplot as plt
import math


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = set()
        self.adjacency = {}

    def add_node(self, node_id, info=""):
        if node_id in self.nodes:
            return self
        self.nodes[node_id] = info
        self.adjacency[node_id] = set()
        return self

    def add_edge(self, node1, node2):
        if (node1 == node2 or node1 not in self.nodes or node2 not in self.nodes):
            return self

        edge = (min(node1, node2), max(node1, node2))
        if edge in self.edges:
            return self

        self.edges.add(edge)
        self.adjacency[node1].add(node2)
        self.adjacency[node2].add(node1)
        return self

    def generate_random_graph(self, num_nodes, num_edges):
        self.nodes = {i: f"Node{i}" for i in range(num_nodes)}
        self.edges = set()
        self.adjacency = {i: set() for i in range(num_nodes)}

        max_edges = num_nodes * (num_nodes - 1) // 2
        num_edges = min(num_edges, max_edges)

        if num_edges > max_edges / 2:
            all_possible = {(i, j) for i in range(num_nodes) for j in range(i+1, num_nodes)}
            self.edges = set(random.sample(list(all_possible), num_edges))
        else:
            while len(self.edges) < num_edges:
                u, v = random.sample(range(num_nodes), 2)
                if u != v:
                    edge = (min(u, v), max(u, v))
                    self.edges.add(edge)

        for u, v in self.edges:
            self.adjacency[u].add(v)
            self.adjacency[v].add(u)

        return self

    def draw(self, highlight_set=None, node_size=300):
        if not self.nodes:
            return self

        fig, ax = plt.subplots(figsize=(10, 8))
        n = len(self.nodes)

        pos = {}
        for i, node in enumerate(self.nodes):
            angle = 2 * math.pi * i / n
            r = 0.95 + random.uniform(-0.05, 0.05)
            pos[node] = (r * math.cos(angle), r * math.sin(angle))

        node_colors = []
        for node in self.nodes:
            if highlight_set and node in highlight_set:
                node_colors.append('#4CAF50')
            else:
                node_colors.append("#EB1527")

        for (u, v) in self.edges:
            xu, yu = pos[u]
            xv, yv = pos[v]
            ax.plot(
                [xu, xv],
                [yu, yv],
                'grey',
                lw=1.5,
                alpha=0.4,
                zorder=1
                )

        for i, node in enumerate(self.nodes):
            x, y = pos[node]
            ax.scatter(x, y,
                       s=node_size, c=node_colors[i],
                       edgecolors='k', zorder=2)
            ax.text(x, y,
                    str(node),
                    ha='center', va='center',
                    fontsize=9, zorder=3)

        title = f"{n} nodes, {len(self.edges)} edges"

        if highlight_set:
            title += f"\nSet with {len(highlight_set)} nodes"

        ax.set_title(title)
        ax.set_aspect('equal')
        ax.axis('off')

        plt.tight_layout()
        plt.show()

        return self
