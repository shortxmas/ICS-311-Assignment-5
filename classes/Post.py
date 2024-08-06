from classes.User import User

class Post:
    def __init__(self, owner, comments, content, views, created):
        self.owner = owner
        self.comments = comments[]
        self.content = content
        self.views = views[]
        self.created = created

    def add_comment(self,text,author):
        self.comments.append({"quote":text,"yapper":author})
    
    def add_view(self,viewer,view_date,view_time):
        self.views.append({"seen_by":viewer,"date":view_date,"time":view_time})
