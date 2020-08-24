class Login:

    def __init__(self):
        self.UName = "Admin"
        self.PWord = "Admin"
        self.tries = 3

    def get_login(self):
        UN = input(f"Enter Username: ")
        PW = input(f"Enter Password: ")

        while self.tries > 1:
            if self.validate_login(UN, PW):
                return print("\nLogin Success!\n")
            else:
                self.tries -= 1
                print(
                    f"\n Wrong Username/Password. {self.tries} tries left. \n")
                return self.get_login()
        else:
            print("\nMaximum Tries has been used. Resetting!\n")
            self.reset_tries()
            return self.get_login()

    def validate_login(self, UN, PW):
        if self.UName == UN and self.PWord == PW:
            return True
        else:
            return False

    def reset_tries(self):
        self.tries = 3


login = Login()
login.get_login()
