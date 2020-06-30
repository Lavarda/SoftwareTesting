class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # For users
    def __str__(self):
        return f"Title: {self.title} and Content: {self.content}"

    # For programmers
    # def __repr__(self):
    #     return f"<Post({self.title}, {self.content})>"

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }