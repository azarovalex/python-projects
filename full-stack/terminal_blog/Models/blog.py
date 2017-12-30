import uuid
import datetime
from Database import Database
from Models.post import Post


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Input post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date (in format DDMMYY), or leave blank for today: ")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=datetime.datetime.strptime(date, "%d%m%y"))
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one("blogs", {"id": id})
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])

    def json(self):
        return {
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "id": self.id
        }
