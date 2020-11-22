
ass = {"udamad": "lasmad"}

class login:

    def __init__(self):
        pass


    def passcheck(self):

        for key, value in ass.items():
            if self.username == key and self.password == value:
                print("Granted Access")
            else:
                A = str(input("Enter Desired Name: "))
                B = str(input("Enter Desired Password: "))
                ass[A] = B


A1 = login()
A1.username = "udamad"
A1.password = "lasmad"
A1.passcheck()


