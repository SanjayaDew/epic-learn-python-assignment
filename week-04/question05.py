class User:
    def __init__(self,username,password):
        self.username = username
        self.__password = password

    def login(self):
        if self.__password == '1234':
            print("Login Successful")
        else:
            print("Invalid Password")


u1 = User("Sanjaya","1234")
u2 = User("Maaya","0000")

u1.login()
u2.login()