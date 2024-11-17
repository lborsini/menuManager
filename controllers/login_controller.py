from models.db import Database

class Login:
    def __init__(self):
        self.db = Database()
        self.db.conect

        self.login_data = self.db.select_item(item='', table='login')
    