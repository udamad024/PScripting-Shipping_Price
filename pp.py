class login:

    pas = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def newuser(self):
        A = str(input("Enter Desired Username"))
        B = str(input("Enter Desired Password"))

        pas[A] = B

    def passcheck(self):
        for key, value in pas.items():
            if self.username == key and self.password == value:
                print("Granted Access")
            else:
               newuser()


A1 = login()

