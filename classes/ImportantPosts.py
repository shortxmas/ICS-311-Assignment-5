import networkx as nx
import matplotlib.pyplot as plt

class ImportantPosts:
    def __init__(self, users, posts):
        self.users = users
        self.posts = posts
        self.graph = nx.DiGraph()

    def create_graph(self, importance_criteria="comments"):
        self.graph.clear()

        # Add users as nodes
        for user in self.users:
            self.graph.add_node(user.username, type='user')

        # Add posts as nodes and create edges for viewers and creators
        for post in self.posts:
            self.graph.add_node(post.content, type='post', comments=len(post.comments), views=len(post.views))
            self.graph.add_edge(post.owner, post.content, type='authorship')

            for view in post.views:
                self.graph.add_edge(view['seen_by'], post.content, type='view')

        self.highlight_important_posts(importance_criteria)

    def highlight_important_posts(self, importance_criteria):
        # Determine the importance based on the chosen criteria
        for node in self.graph.nodes:
            if self.graph.nodes[node]['type'] == 'post':
                if importance_criteria == "comments":
                    self.graph.nodes[node]['importance'] = self.graph.nodes[node]['comments']
                elif importance_criteria == "views":
                    self.graph.nodes[node]['importance'] = self.graph.nodes[node]['views']
                elif importance_criteria == "blend":
                    self.graph.nodes[node]['importance'] = self.graph.nodes[node]['comments'] + self.graph.nodes[node]['views']
                else:
                    self.graph.nodes[node]['importance'] = 0

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)
        user_nodes = [node for node in self.graph.nodes if self.graph.nodes[node]['type'] == 'user']
        post_nodes = [node for node in self.graph.nodes if self.graph.nodes[node]['type'] == 'post']

        important_posts = [node for node in post_nodes if self.graph.nodes[node]['importance'] > 0]
        normal_posts = [node for node in post_nodes if self.graph.nodes[node]['importance'] == 0]

        plt.figure(figsize=(15, 10))

        nx.draw_networkx_nodes(self.graph, pos, nodelist=user_nodes, node_color='skyblue', node_size=500, label='Users')
        nx.draw_networkx_nodes(self.graph, pos, nodelist=normal_posts, node_color='lightgreen', node_size=300, label='Posts')
        nx.draw_networkx_nodes(self.graph, pos, nodelist=important_posts, node_color='red', node_size=700, label='Important Posts')

        nx.draw_networkx_edges(self.graph, pos, edgelist=self.graph.edges, edge_color='gray')
        
        nx.draw_networkx_labels(self.graph, pos)

        plt.legend()
        plt.show()

    def update_graph(self, importance_criteria):
        self.highlight_important_posts(importance_criteria)
        self.draw_graph()


