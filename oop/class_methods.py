# Different ways of creating instances
class User:
    def __init__(self, login) -> None:
        self.login = login

    @classmethod
    def from_token(cls, token):
        login = "" #auth.from_token(token)
        return cls(login)
    

class Admin(User):
    # TODO implement admin actions
    pass