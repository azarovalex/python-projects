from Database import Database
from Models.blog import Blog

Database.initialize()

blog = Blog(author="alex",
            title="Simple title",
            description="Sample description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.get_from_mongo(blog.id)

print(blog.get_posts())
