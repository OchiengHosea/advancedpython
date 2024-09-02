"""
They add functionality on top of other classes
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
)

# LoggerMixin assumes that is going to be combined with a class that has name & id attributes
class LoggerMixin:
    def log_id(self):
        logging.info("%s with id %r", self.name, self.id)

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class VM:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# Mixin
class LoggedUser(LoggerMixin, User):
    pass

class LoggedVM(LoggerMixin, VM):
    pass

user = LoggedUser("root", 1)
user.log_id()

vm = LoggedVM("m1", '5989d5')
vm.log_id()