## this is for task 2 of the assignment

import networkx as nx
import matplotlib.pyplot as plt

class SocialMediaGraph:
    def __init__(self, users, posts, connections=None):
        self.users = users
        self.posts = posts
        self.connections = connections or []
        self.G = nx.Graph()
        self.criteria = []
        self._create_graph()

    def _create_graph(self):
        # Add Users as Nodes
        for user in self.users:
            self.G.add_node(user["username"], type="user", **user)

        # Add Posts as Nodes
        for post in self.posts:
            self.G.add_node(post["post_id"], type="post", **post)
            self.G.add_edge(post["author"], post["post_id"])

        # Add Connections between Users (if any)
        for conn in self.connections:
            self.G.add_edge(conn["from"], conn["to"], type=conn["type"])

    def add_criteria(self, criterion):
        self.criteria.append(criterion)

    def clear_criteria(self):
        self.criteria = []

    def highlight_interesting_users(self):
        # Clear previous highlights
        for node in self.G.nodes:
            self.G.nodes[node]["highlight"] = False

        # Apply criteria
        for node in self.G.nodes:
            if self.G.nodes[node]["type"] == "user":
                if all(criterion(self.G.nodes[node]) for criterion in self.criteria):
                    self.G.nodes[node]["highlight"] = True

    def visualize_graph(self):
        pos = nx.spring_layout(self.G)  # Layout for visualization

        # Draw nodes
        user_nodes = [node for node in self.G.nodes if self.G.nodes[node]["type"] == "user"]
        post_nodes = [node for node in self.G.nodes if self.G.nodes[node]["type"] == "post"]
        highlighted_nodes = [node for node in self.G.nodes if self.G.nodes[node].get("highlight", False)]

        nx.draw_networkx_nodes(self.G, pos, nodelist=user_nodes, node_color='blue', node_size=500, label="Users")
        nx.draw_networkx_nodes(self.G, pos, nodelist=post_nodes, node_color='green', node_size=500, label="Posts")
        nx.draw_networkx_nodes(self.G, pos, nodelist=highlighted_nodes, node_color='red', node_size=700, label="Highlighted Users")

        # Draw edges
        nx.draw_networkx_edges(self.G, pos)

        # Draw labels
        nx.draw_networkx_labels(self.G, pos)

        # Show plot
        plt.legend(scatterpoints=1)
        plt.show()