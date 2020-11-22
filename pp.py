class login:

    def __init__(self):
        pass

    def newuser(self):
        A = str(input("Enter Desired Username"))
        B = str(input("Enter Desired Password"))

        ass[A] = B

    def passcheck(self):
        ass = {"udamad":"lasmad"}
        for key, value in ass.items():
            if self.username == key and self.password == value:
                print("Granted Access")
            else:
                login.newuser(self)


A1 = login()
A1.username = "udamad"
A1.password = "lasmad"
A1.passcheck()


