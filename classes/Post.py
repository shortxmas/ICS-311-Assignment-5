class Post:
    def __init__(self, owner, comments, content, views, created):
        self.owner = owner
        self.comments = comments
        self.content = content
        self.views = views
        self.created = created

    def add_comment(self,text,author):
        self.comments.append({"quote":text,"yapper":author})
    
    def add_view(self,viewer,view_datetime):
        self.views.append({"seen_by":viewer,"datetime":view_datetime})
