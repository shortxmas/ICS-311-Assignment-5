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

# Sample Data
users = [
    {"username": "user1", "age": 25, "gender": "female", "posts": 10, "comments": 5, "views": 100, "location": "NY"},
    {"username": "user2", "age": 30, "gender": "male", "posts": 15, "comments": 3, "views": 200, "location": "CA"},
    {"username": "user3", "age": 22, "gender": "female", "posts": 5, "comments": 10, "views": 50, "location": "TX"},
]

posts = [
    {"post_id": "post1", "author": "user1", "views": 100, "content": "Post content 1"},
    {"post_id": "post2", "author": "user2", "views": 200, "content": "Post content 2"},
    {"post_id": "post3", "author": "user1", "views": 50, "content": "Post content 3"},
    {"post_id": "post4", "author": "user3", "views": 30, "content": "Post content 4"},
]

connections = [
    {"from": "user1", "to": "user2", "type": "friends"},
    {"from": "user2", "to": "user3", "type": "follows"},
]

# Create SocialMediaGraph object
social_media_graph = SocialMediaGraph(users, posts, connections)

# Define criteria dynamically
criteria = [
    lambda user: user["posts"] > 5,       # Number of posts (high)
    lambda user: user["gender"] == "female", # Gender
    lambda user: user["views"] > 50,       # Number of views (high)
]

# Add criteria to the graph
for criterion in criteria:
    social_media_graph.add_criteria(criterion)

# Highlight interesting users based on criteria
social_media_graph.highlight_interesting_users()

# Visualize the graph
social_media_graph.visualize_graph()
