import pymysql

class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = ""
        db = "ent_cesi"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cursor = self.con.cursor()
    def list_eleves(self):
        self.cursor.execute("SELECT id, "
                            "nom, "
                            "prenom, "
                            "url_image, "
                            "date_naissance, "
                            "date_debut ,"
                            "date_fin,"
                            "nom_promotion"
                            "FROM eleve"
                            "INNER JOIN promotion ON promotion.id = eleve.id_promotion")
        result = self.cursor.fetchall()
        return result

    def eleve_by_id(self, eleve_id):
        sql = "SELECT id, nom, prenom, url_image, date_naissance, date_debut , date_fin, nompromotion FROM eleve INNER JOIN promotion ON promotion.id = eleve.id_promotion WHERE eleve.id = %s"
        self.cursor.execute(sql, eleve_id)
        result = self.cursor.fetchall()
        return result

    def delete(self, eleve_id):
        sql = "DELETE FROM eleve WHERE id = %s"
        self.cursor.execute(sql, eleve_id)
        self.con.commit()
        print(self.cursor.rowcount, " record(s) deleted")

    def insert(self, eleve):
        nom = eleve.get('nom')
        prenom = eleve.get('prenom')
        url_image = eleve.get('url_image')
        date_naissance = eleve.get('date_naissance')
        id_promotion = eleve.get('id_promotion')
        sql = "INSERT INTO eleve (nom, prenom, url_image, date_naissance, id_promotion) VALUES (%s, %s, %s, %s, %s)"
        data = (nom, prenom, url_image, date_naissance, id_promotion)
        self.cursor.execute(sql, data)
        self.con.commit()

    def update(self, eleve_id, eleve):
        nom = eleve.get('nom')
        prenom = eleve.get('prenom')
        url_image = eleve.get('url_image')
        date_naissance = eleve.get('date_naissance')
        id_promotion = eleve.get('id_promotion')
        sql = "UPDATE eleve SET nom = %s, prenom = %s, url_image = %s, date_naissance = %s, id_promotion = %s WHERE eleve.id = %s"
        data = (nom, prenom, url_image, date_naissance, id_promotion, eleve_id)
        self.cursor.execute(sql, data)
   ## Blog
    def blog(self):
        self.cursor.execute("SELECT id, "
                            "date_publication, "
                            "titre, "
                            "contenu, "
                            "categorie, "
                            "id_eleve "
                            "FROM article"
                            "INNER JOIN eleve ON eleve.id = article.id_eleve")
        result = self.cursor.fetchall()
        return result

    def article_by_id(self, article_id):
        sql = "SELECT id, date_publication, titre, contenu, id_eleve, categorie FROM article INNER JOIN eleve ON eleve.id = article.id_eleve WHERE aricle.id = %s"
        self.cursor.execute(sql, article_id)
        result = self.cursor.fetchall()
        return result

    def insert(self, article):
        titre = eleve.get('titre')
        contenu = eleve.get('contenu')
        date_publication = eleve.get('date_publication')
        id_eleve = eleve.get('id_eleve')
        categorie = eleve.get('categorie')
        sql = "INSERT INTO article (titre, contenu, date_publication, id_eleve, categorie) VALUES (%s, %s, %s, %s, %s)"
        data = (titre, contenu, date_publication, id_eleve, categorie)
        self.cursor.execute(sql, data)
        self.con.commit()

    ## Fin Blog