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
        self.cursor.execute("SELECT eleve.id, nom, prenom, url_image, date_naissance, date_debut , date_fin, libelle FROM eleve INNER JOIN promotion ON promotion.id = eleve.promotion_id ")
        result = self.cursor.fetchall()
        return result

    def eleve_by_id(self, eleve_id):
        sql = "SELECT eleve.id, nom, prenom, url_image, date_naissance, date_debut , date_fin, libelle FROM eleve INNER JOIN promotion ON promotion.id = eleve.promotion_id WHERE eleve.id = %s"
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
        id_promotion = eleve.get('promotion_id')
        sql = "INSERT INTO eleve (nom, prenom, url_image, date_naissance, promotion_id) VALUES (%s, %s, %s, %s, %s)"
        data = (nom, prenom, url_image, date_naissance, id_promotion)
        self.cursor.execute(sql, data)
        self.con.commit()

    def update(self, eleve_id, eleve):
        nom = eleve.get('nom')
        prenom = eleve.get('prenom')
        url_image = eleve.get('url_image')
        date_naissance = eleve.get('date_naissance')
        promotion_id = eleve.get('promotion_id')
        sql = "UPDATE eleve SET nom = %s, prenom = %s, url_image = %s, date_naissance = %s, promotion_id = %s WHERE eleve.id = %s"
        data = (nom, prenom, url_image, date_naissance, promotion_id, eleve_id)
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

#PROMOTION
    def list_promotions(self):
        self.cursor.execute("SELECT id, libelle, date_debut, date_fin FROM promotion")
        result = self.cursor.fetchall()
        return result

    def promotion_by_id(self, promotion_id):
        sql = "SELECT id, libelle, date_debut, date_fin FROM promotion WHERE promotion.id = %s"
        self.cursor.execute(sql, promotion_id)
        result = self.cursor.fetchall()
        return result

    def promotion_delete(self, promotion_id):
        sql = "DELETE FROM promotion WHERE id = %s"
        self.cursor.execute(sql, promotion_id)
        self.con.commit()
        print(self.cursor.rowcount, " record(s) deleted")

    def promotion_insert(self, promotion):
        nom = promotion.get('libelle')
        debut = promotion.get('date_debut')
        fin = promotion.get('date_fin')
        sql = "INSERT INTO promotion (libelle, date_debut, date_fin) VALUES (%s, %s, %s)"
        data = (nom, debut, fin)
        self.cursor.execute(sql, data)
        self.con.commit()

    def promotion_update(self, promotion_id, promotion):
        nom = promotion.get('libelle')
        debut = promotion.get('date_debut')
        fin = promotion.get('date_fin')
        id = promotion.get('id')
        sql = "UPDATE promotion SET libelle = %s, date_debut = %s, date_fin = %s WHERE promotion.id = %s"
        data = (nom, debut, fin, id)
        self.cursor.execute(sql, data)

