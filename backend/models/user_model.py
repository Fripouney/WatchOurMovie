from sqlalchemy import *

class UserModel():
    def __init__(self):
        self.id = Column(INTEGER, primary_key=True)
        self.username = Column(VARCHAR)
        self.password = Column(VARCHAR)