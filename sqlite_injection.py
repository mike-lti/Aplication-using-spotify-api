"""
Aplicações distribuídas - Projeto 3 - sqlite_injection.py
Grupo: 29
Números de aluno:
Gonçalo Miguel Nº54944
Miguel Duarte Nº54941

"""


import sqlite3
from os.path import isfile


def connect_db(dbname):
    db_is_created = isfile(dbname) 
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    if not db_is_created:

        cursor.execute("PRAGMA foreign_keys = ON;")

        connection.commit()

        cursor.execute("CREATE TABLE utilizadores (\
                            id INTEGER PRIMARY KEY AUTOINCREMENT,\
                            nome TEXT,\
                            senha TEXT);")

        connection.commit()

        cursor.execute("CREATE TABLE artistas (\
                        id INTEGER PRIMARY KEY AUTOINCREMENT,\
                        id_spotify TEXT,\
                        nome TEXT);")

        connection.commit()

        cursor.execute("CREATE TABLE albuns (\
                        id INTEGER PRIMARY KEY AUTOINCREMENT,\
                        id_spotify TEXT,\
                        nome TEXT,\
                        id_artista INTEGER,\
                        FOREIGN KEY(id_artista) REFERENCES artistas(id));")

        connection.commit()

        cursor.execute("CREATE TABLE avaliacoes (\
                        id INTEGER PRIMARY KEY,\
                        sigla TEXT,\
                        designacao TEXT);")

        connection.commit()

        cursor.execute("CREATE TABLE listas_albuns (\
                        id_user INTEGER,\
                        id_album INTEGER,\
                        id_avaliacao INTEGER,\
                        PRIMARY KEY (id_user, id_album),\
                        FOREIGN KEY(id_user) REFERENCES utilizadores(id),\
                        FOREIGN KEY(id_album) REFERENCES albuns(id)\
                        FOREIGN KEY(id_avaliacao)REFERENCES avaliacoes(id));")

        connection.commit()
        
    return connection, cursor

avaliacao = [(1, "M", "Medíocre"),
        (2, "m", "Mau"),
        (3, "S", "Suficiente"),
        (4, "B", "Bom"),
        (5, "MB", "Muito Bom")]


if __name__ == '__main__':
    conn, cursor = connect_db('database_proj_adis.db')
    cursor.executemany('INSERT INTO avaliacoes VALUES (?,?,?)', avaliacao)
    conn.commit()
    cursor.execute('SELECT * FROM avaliacoes') 
    conn.commit()

    print("Base de dados criada!")