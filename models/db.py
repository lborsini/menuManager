import sqlite3

class Database:
    def __init__(self, db_name='menuManager.db'):
        self.db_name = db_name
        self.conect()

    def conect(self):
        
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f'db connection suscefully: {self.db_name}')
        except sqlite3.Error as e:
            print(f'Conection error: {e}')


    def select_item(self, item='',table=''):
        self.query = f'SELECT * FROM {table} WHERE name = {item}'
        self.cursor.execute(self.query)
        return self.cursor.fetchall()


    def add_newSpecial(self, item=[]):
        for i in item:
            name, bread, meat, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12 = i

            try:
                self.query = 'INSERT INTO special (name, bread, meat, item 1, item 2, item 3, item 4, item 5, item 6, item 7, item 8, item 9, item 10, item 11, item 12) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))', (name, bread, meat, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
                self.cursor.execute(self.query)
                print('Datos cargados')
            
            except sqlite3 as e:
                print(f'error en la carga de datos; {e}')

    
    def add_newWater(self, item=[]):
        for i in item:
            name, item1, item2, item3, item4 = i

            try:
                self.query = 'INSERT INTO water (name, item 1, item 2, item 3, item 4) VALUES (?,?,?,?,?))', (name, item1, item2, item3, item4)
                self.cursor.execute(self.query)
                print('Datos cargados')
            
            except sqlite3 as e:
                print(f'error en la carga de datos; {e}')
    
    def add_newSandwich(self, item=[]):
        for i in item:
            name, bread, protein, dressing, item1, item2, item3, item4, item5, item6 = i

            try:
                self.query = 'INSERT INTO special (name, bread, protein, dressing, item 1, item 2, item 3, item 4, item 5, item 6) VALUES (?,?,?,?,?,?,?,?,?,?))', (name, bread, protein, dressing, item1, item2, item3, item4, item5, item6)
                self.cursor.execute(self.query)
                print('Datos cargados')
            
            except sqlite3 as e:
                print(f'error en la carga de datos; {e}')

    

    def close(self, c):
        self.conn.close()


