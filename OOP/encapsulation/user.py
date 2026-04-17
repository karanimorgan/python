class User:
    def __init__(self,username, password):
        self.username = username
        self._session_token = None
        self.__password = password

        def login(self, password):
            if password == self.__password:
                self._session_token = "abc8489"
                print(f"{self.username} logged in succesfully.")
            else:
                print("Invalid password!")

        def logout(self):
            self._session_token = None
            print(f"{self.username} logged out.")
    
class Admin(User):
    def __init__(self, username, password, admin_level):
        super().__init__(username, password)
        self.admin_level = admin_level

    def access_admin_panel(self):
        if self._session_token:
            print(f"{self.username} with admin level {self.admin_level} is accessing the admin panel.")
        else:
            print("Please log in to access the admin panel.")

user = User("Mark_Varstappen", "f1podium")
user.login("f1podium")
print(user.username)
print(user._session_token)
# print(user.__password) # This will raise an error because __password is private and cannot be accessed directly.

admin = Admin("admin_user", "adminpass", "superuser")
admin.login("adminpass")
admin.access_admin_panel()