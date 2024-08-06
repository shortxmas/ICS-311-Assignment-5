class User:
    def __init__(self,username,posts,connections,birth_year,real_name,gender,zipcode,commented,viewed):
        self.username = username
        self.posts = posts
        self.connections = connections
        self.birth_year = birth_year
        self.real_name = real_name
        self.gender = gender
        self.zipcode = zipcode
        self.commented = commented
        self.viewed = viewed

    def add_connection(self,other_user,conxn_type):
        self.connections.append({"user":other_user,"type":conxn_type})
        
    def add_post(self,post):    
        if post.owner == self.username:
            self.posts.append(post)

    def add_history(self,someones_post):
        for x in someones_post.views:
            if self.username == someones_post.views[x].seen_by:
                self.viewed.append(someones_post)
        for y in someones_post.comments:
            if self.username == someones_post.comments[y].yapper:
                self.commented.append(someones_post)                
