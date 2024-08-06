class User:
    def __init__(self,username,posts,connections,birth_year,real_name,gender,city):
        self.username = username
        self.posts = posts[]
        self.connections = connections[]
        self.birth_year = birth_year
        self.real_name = real_name
        self.gender = gender
        self.city = city

    def add_connection(self,other_user,conxn_type):
        connection = {"user":other_user,"type":conxn_type}
        self.connections.append(connection)
        
        
