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
        self.cursor.execute("SELECT eleve.id, nom, prenom, url_image, date_naissance, date_debut , date_fin, libelle, mail, pwd FROM eleve INNER JOIN promotion ON promotion.id = eleve.promotion_id ")
        result = self.cursor.fetchall()
        return result

    def eleve_by_id(self, eleve_id):
        sql = "SELECT eleve.id, nom, prenom, url_image, date_naissance, date_debut , date_fin, libelle, mail, pwd FROM eleve INNER JOIN promotion ON promotion.id = eleve.promotion_id WHERE eleve.id = %s"
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
        mail = eleve.get('mail')
        pwd = eleve.get('pwd')
        sql = "INSERT INTO eleve (nom, prenom, url_image, date_naissance, promotion_id, mail, pwd) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (nom, prenom, url_image, date_naissance, id_promotion, mail, pwd)
        self.cursor.execute(sql, data)
        self.con.commit()

    def update(self, eleve_id, eleve):
        nom = eleve.get('nom')
        prenom = eleve.get('prenom')
        url_image = eleve.get('url_image')
        date_naissance = eleve.get('date_naissance')
        promotion_id = eleve.get('promotion_id')
        mail = eleve.get('mail')
        pwd = eleve.get('pwd')
        sql = "UPDATE eleve SET nom = %s, prenom = %s, url_image = %s, date_naissance = %s, promotion_id = %s, mail = %s, pwd = %s WHERE eleve.id = %s"
        data = (nom, prenom, url_image, date_naissance, promotion_id, eleve_id,  mail, pwd)
        self.cursor.execute(sql, data)


   ## Blog
    def blog(self):
        self.cursor.execute("SELECT id, date_publication, titre, contenu, categorie FROM article ORDER BY date_publication DESC")
        result = self.cursor.fetchall()
        return result

    def article_by_id(self, article_id):
        sql = "SELECT id, date_publication, titre, contenu, id_eleve, categorie FROM article INNER JOIN eleve ON eleve.id = article.id_eleve WHERE aricle.id = %s"
        self.cursor.execute(sql, article_id)
        result = self.cursor.fetchall()
        return result

    def insert(self, article):
        titre = article.get('titre')
        contenu = article.get('contenu')
        date_publication = article.get('date_publication')
        id_eleve = article.get('id_eleve')
        categorie = article.get('categorie')
        sql = "INSERT INTO article (titre, contenu, date_publication, id_eleve, categorie) VALUES (%s, %s, %s, %s, %s)"
        data = (titre, contenu, date_publication, id_eleve, categorie)
        self.cursor.execute(sql, data)
        self.con.commit()
        return article

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

#Intervenants
    def list_intervenants(self):
        self.cursor.execute("SELECT intervenant.id, nom, prenom, url_photo, date_naissance, mail, pwd FROM intervenant")
        result = self.cursor.fetchall()
        return result

    def intervenant_by_id(self, intervenant_id):
        sql = "SELECT intervenant.id, nom, prenom, url_photo, date_naissance, mail, pwd FROM intervenant WHERE intervenant.id = %s"
        self.cursor.execute(sql, intervenant_id)
        result = self.cursor.fetchall()
        return result

    def intervenant_delete(self, intervenant_id):
        sql = "DELETE FROM intervenant WHERE id = %s"
        self.cursor.execute(sql, intervenant_id)
        self.con.commit()
        print(self.cursor.rowcount, " record(s) deleted")

    def intervenant_insert(self, intervenant):
        nom = intervenant.get('nom')
        prenom = intervenant.get('prenom')
        url_photo = intervenant.get('url_photo')
        date_naissance = intervenant.get('date_naissance')
        mail = intervenant.get('mail')
        pwd = intervenant.get('pwd')
        sql = "INSERT INTO intervenant (nom, prenom, url_photo, date_naissance, mail, pwd) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (nom, prenom, url_photo, date_naissance, mail, pwd)
        self.cursor.execute(sql, data)
        self.con.commit()

    def intervenant_update(self, intervenant_id, intervenant):
        nom = intervenant.get('nom')
        prenom = intervenant.get('prenom')
        url_photo = intervenant.get('url_photo')
        date_naissance = intervenant.get('date_naissance')
        mail = intervenant.get('mail')
        pwd = intervenant.get('pwd')
        sql = "UPDATE intervenant SET nom = %s, prenom = %s, url_photo = %s, date_naissance = %s, mail = %s, pwd = %s WHERE intervenant.id = %s"
        data = (nom, prenom, url_photo, date_naissance, intervenant_id,  mail, pwd)
        self.cursor.execute(sql, data)

    ## Emploi du temps
    def list_edt(self):
        self.cursor.execute("SELECT id, "
                            "date, "
                            "libelle, "
                            "creneau, "
                            "id_promotion, "
                            "id_intervenant "
                            "FROM emploi_du_temps"
                            "INNER JOIN intervenant ON intervenant.id = emploi_du_temps.id_intervenant"
                            "INNER JOIN promotion ON promotion.id = emploi_du_temps.id_promotion")
        result = self.cursor.fetchall()
        return result

    def edt_by_day(self, date):
        sql = "SELECT id, date, creneau, id_promotion, id_intervenant FROM emploi_du_temps INNER JOIN promotion ON promotion.id = emploi_du_temps.id_promotion INNER JOIN intervenant ON intervenant.id = emploi_du_temps.id_intervenant WHERE emploi_du_temps.date = %s"
        self.cursor.execute(sql, date)
        result = self.cursor.fetchall()
        return result

    def edt_update(self, edt_id, emploi_du_temps):
        libelle = emploi_du_temps.get('libelle')
        date = emploi_du_temps.get('date')
        creneau = emploi_du_temps.get('creneau')
        id_intervenant = emploi_du_temps.get('id_intervenant')
        id_promotion = emploi_du_temps.get('id_promotion')
        id = edt_id
        sql = "UPDATE emploi_du_temps SET libelle = %s, date = %s, creneau = %s, id_intervenant = %s, id_promotion = %s  WHERE emploi_du_temps.id = %s"
        data = (libelle, date, creneau, id_intervenant, id_promotion, id)
        self.cursor.execute(sql, data)

    def edt_insert(self, edt):
        libelle = edt.get('libelle')
        date = edt.get('date')
        creneau = edt.get('creneau')
        id_promotion = edt.get('id_promotion')
        id_intervenant = edt.get('id_intervenant')
        sql = "INSERT INTO emploi_du_temps (libelle, date, creneau, id_promotion, id_intervenant) VALUES (%s, %s, %s, %s, %s)"
        data = (libelle, date, creneau, id_promotion, id_intervenant)
        self.cursor.execute(sql, data)
        self.con.commit()

    def edt_delete(self, edt_id):
        sql = "DELETE FROM emploi_du_temps WHERE id = %s"
        self.cursor.execute(sql, edt_id)
        self.con.commit()
        print(self.cursor.rowcount, " record(s) deleted")
## Fin EMPLOI DU TEMPS

## Authentification
    def auth(self, data):
        username = data.get('username')
        password = data.get('password')
        sql = "SELECT eleve.mail FROM eleve WHERE mail = %s AND pwd = %s"
        data = (username, password)
        self.cursor.execute(sql, data)
        result = self.cursor.fetchall()
        return result
