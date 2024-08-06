from classes.User import User

class Post:
    def __init__(self, owner, comments, content, views, created):
        self.owner = owner
        self.comments = comments[]
        self.content = content
        self.views = views[]
        self.created = created

    def add_comment(self,text,author):
        yap = {"quote":text,"yapper":author}
        self.comments.append(yap)
    
    def add_view(self,viewer,view_date,view_time):
        view = {"seen_by":viewer,"date":view_date,"time":view_time}
        self.views.append(view)
