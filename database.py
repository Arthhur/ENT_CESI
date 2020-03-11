import pymysql

class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = ""
        db = "ent_cesi"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    def list_eleves(self):
        self.cur.execute("SELECT id, nom FROM eleve")
        result = self.cur.fetchall()
        return result
