from database.DB_connect import DBConnect

class CorsoDAO:

    def getAllCorsi(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT codins, nome FROM corso"""
        cursor.execute(query)
        rows = cursor.fetchall()
        res = []
        for i in rows:
            res.append(i)
        cnx.close()
        return res

    def getStudentiByCorso(self, codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT studente.*, iscrizione.codins 
                   FROM studente
                   JOIN iscrizione ON studente.matricola = iscrizione.matricola
                   WHERE iscrizione.codins = %s"""
        cursor.execute(query, (codins,))
        studenti = cursor.fetchall()
        cnx.close()
        return studenti

    def getStudente(self, matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                   FROM studente
                   WHERE studente.matricola = %s"""
        cursor.execute(query, (matricola,))
        studente = cursor.fetchone()
        cnx.close()
        return studente

    def getCorsiByStudente(self, matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT corso.* 
                   FROM corso
                   JOIN iscrizione ON corso.codins = iscrizione.codins
                   WHERE iscrizione.matricola = %s"""
        cursor.execute(query, (matricola,))
        corsi = cursor.fetchall()
        cnx.close()
        return corsi

    def AddIscrizione(self, matricola, codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query_check = """SELECT 1
                         FROM iscrizione
                         WHERE matricola = %s AND codins = %s"""
        cursor.execute(query_check, (matricola, codins))
        result = cursor.fetchone()
        if result:
            cnx.close()
            return False
        query = """INSERT INTO iscrizione (matricola, codins) 
                        VALUES (%s, %s)"""
        cursor.execute(query, (matricola, codins))
        cnx.commit()
        cnx.close()
        return "Iscrizione completata con successo"



