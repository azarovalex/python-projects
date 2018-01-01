from Database import Database
from Models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Enter your autor name: ")
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_accout()

            
        pass

    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W) blogs?")
        if read_or_write == 'R':
            pass
        elif read_or_write == "W":
            pass
        else:
            print("Thank you for blogging!")

    def _user_has_account(self):
        return Database.find_one("blogs", {"author": self.user}) is not None

    def _prompt_user_for_accout(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(self.user, title, description)
        blog.save_to_mongo()