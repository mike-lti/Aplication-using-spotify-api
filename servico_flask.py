"""
Aplicações distribuídas - Projeto 3 - servico_flask.py
Grupo: 29
Números de aluno:
Gonçalo Miguel Nº54944
Miguel Duarte Nº54941

"""


import json
import requests
from flask import Flask, request, make_response, jsonify
import sqlite3


def table_operations():
    """
    Trata da conexao à database e devolve um cursor e
    um variavel de conexao para os commits
    """
    conn = sqlite3.connect("database_proj_adis.db")
    cursor = conn.cursor()
    return conn, cursor


def conection_spotify():
    """
    Esta funcao trata da conexao a api do spotify atraves das nossas
    credenciais gerando um header e auth token necessarios para 
    a realizacao de pedidos e acesso a base de dados
    """
    id_user = '9d5ff676893740fea2767f7385491eab'
    senha_user = '321e14fdb8aa4ad798686f631643e0b3'
    url_permission = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(url_permission, {'grant_type': 'client_credentials',
        'client_id': id_user,
        'client_secret': senha_user,
    })
    auth_permission = auth_response.json()
    access_token = auth_permission['access_token']
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)    }
    return headers



servico_web = Flask(__name__)


@servico_web.route("/utilizadores/album", methods = ["GET", "DELETE"])
def album():
    
    if request.method == "GET":
        data_sent = int(request.get_json())       
        conec = table_operations()
        conec[1].execute('SELECT id_album FROM listas_albuns WHERE id_user = %d' %data_sent)
        linhas = conec[1].fetchall()
        conec[0].close()       
        r = make_response(jsonify(linhas))
        return r

    if request.method == "DELETE":

        data_sent = int(request.get_json())
        conec = table_operations()
        conec[1].execute('SELECT id_album FROM listas_albuns WHERE id_user = %d' %data_sent)
        linhas = conec[1].fetchall()
        conec[0].close() 
        
        for i in linhas[0]:
            conec = table_operations()      
            conec[1].execute('DELETE FROM albuns WHERE id = ?', (i,))
            conec[0].commit()
            conec[0].close()

        conec = table_operations()        
        conec[1].execute('DELETE FROM listas_albuns WHERE id_user = %d' % data_sent)
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r


@servico_web.route("/utilizadores/all", methods = ["GET", "DELETE"])
def all():
    
    if request.method == "GET":        
        conec = table_operations()
        conec[1].execute('SELECT * FROM utilizadores')
        linhas = conec[1].fetchall()
        conec[0].close()        
        r = make_response(jsonify(linhas))
        return r

    
    if request.method == "DELETE":
        conec = table_operations()
        conec[1].execute('DELETE FROM utilizadores')
        conec[0].commit()
        conec[0].close()
        conec = table_operations()
        conec[1].execute('DELETE FROM listas_albuns')
        conec[0].commit()
        conec[0].close()
        
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r

@servico_web.route("/utilizadores/avaliar", methods = ["POST"])
def avaliar():

    if request.method == "POST":      
        data_sent = request.get_json()
        num = data_sent['id']
        num_album = data_sent['id_album']
        evaluation = data_sent['avaliacao']
        if evaluation == "M":
            evaluation = 1
        elif evaluation == "m":
            evaluation = 2
        elif evaluation == "S":
            evaluation = 3
        elif evaluation == "B":
            evaluation = 4
        elif evaluation == "MB":
            evaluation = 5
        conec = table_operations()
        conec[1].execute('INSERT INTO listas_albuns VALUES (?,?,?)', (num, num_album, evaluation))
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r
        

@servico_web.route("/utilizadores", methods = ["POST", "GET", "DELETE", "PUT"])
def utilizadores():

    if request.method == "POST":       
        data_sent = request.get_json()
        conec = table_operations()
        name = data_sent['nome']
        password = data_sent['senha']
        conec[1].execute('INSERT INTO utilizadores(nome, senha) VALUES (?,?)',(name, password))
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
            
        return r
    

    if request.method == "GET":
        conec = table_operations()
        data_sent = int(request.get_json())
        conec[1].execute('SELECT * FROM utilizadores WHERE id = %d'  %data_sent)
        linhas = conec[1].fetchall()
        conec[0].close()
        r = make_response(jsonify(linhas))
        return r

    
    if request.method == "DELETE":
        data_sent = int(request.get_json())
        conec = table_operations()
        conec[1].execute('DELETE  FROM utilizadores WHERE id = %d' % data_sent)
        conec[0].commit()
        conec[0].close()
        conec = table_operations()
        conec[1].execute('DELETE  FROM listas_albuns WHERE id_user = %d' % data_sent)
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r

   
    if request.method == "PUT":
        conec = table_operations()
        data_sent = request.get_json()
        id_user = int(data_sent["id"])
        password = data_sent["senha"]
        conec[1].execute('UPDATE utilizadores SET senha = ? WHERE id = ?', (password, id_user))
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r


@servico_web.route("/albuns/albAva", methods = ["GET", "DELETE", "PUT"])
def albAva():

    if request.method == "GET":
        data_sent = request.get_json()
        if data_sent == "M":
            data_sent = 1
        elif data_sent == "m":
            data_sent = 2
        elif data_sent == "S":
            data_sent = 3
        elif data_sent == "B":
            data_sent = 4
        elif data_sent == "MB":
            data_sent = 5

        conec = table_operations()
        conec[1].execute('SELECT id_album FROM listas_albuns WHERE id_avaliacao = %d' %data_sent)
        linhas = conec[1].fetchall()
        conec[0].close()        
        r = make_response(jsonify(linhas))
        return r


    if request.method == "DELETE":
        conec = table_operations()
        data_sent = request.get_json()
        if data_sent == "M":
            data_sent = 1
        elif data_sent == "m":
            data_sent = 2
        elif data_sent == "S":
            data_sent = 3
        elif data_sent == "B":
            data_sent = 4
        elif data_sent == "MB":
            data_sent = 5
        conec[1].execute('SELECT id_album FROM listas_albuns WHERE id_avaliacao = %d' %data_sent)
        linhas = conec[1].fetchall()
        conec[0].close() 
        for elements in linhas:
            conec[1].execute('DELETE FROM albuns WHERE id = %d' %elements)
            conec[0].commit()
            conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r


    if request.method == "PUT":
        conec = table_operations()
        data_sent = request.get_json()
        id_user = data_sent['idUser']
        avaliacao= data_sent['avaliacao']
        id_album = data_sent['idAlbum']
        if avaliacao == "M":
            avaliacao = 1
        elif avaliacao == "m":
            avaliacao = 2
        elif avaliacao == "S":
            avaliacao = 3
        elif avaliacao == "B":
            avaliacao = 4
        elif avaliacao == "MB":
            avaliacao = 5
        conec[1].execute('UPDATE listas_albuns SET id_avaliacao = ? WHERE id_album = ? and id_user = ?', (avaliacao, id_album, id_user))
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r


@servico_web.route("/albuns/allAlb", methods = ["GET", "DELETE"])
def allAlb():
    

    if request.method == "GET":
        conec = table_operations()
        conec[1].execute('SELECT * FROM albuns')
        linhas = conec[1].fetchall()
        conec[0].close()        
        r = make_response(jsonify(linhas))
        return r

    
    if request.method == "DELETE":
        conec = table_operations()           
        conec[1].execute('DELETE FROM albuns')
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))

        conec = table_operations()            
        conec[1].execute('DELETE FROM listas_albuns')
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))

        return r




@servico_web.route("/albuns", methods = ["POST", "GET", "DELETE"])
def albuns():
    #

    if request.method == "POST":
        data_sent = request.get_json()
        #spotify data retrieval
        url = 'https://api.spotify.com/v1/albums/'
        resposta_spoty = requests.get(url + data_sent, headers=conection_spotify())
        resposta_spoty = resposta_spoty.json()
        num_artista = resposta_spoty['artists'][0]['id'] 
        nome_artista = str(resposta_spoty['artists'][0]['name'])
        nome_album = resposta_spoty['name']
       
        conec = table_operations()
        conec[1].execute('SELECT id FROM artistas WHERE nome = ?', (nome_artista,))
        linhas = conec[1].fetchall()
        
        conec[0].close()
        if len(linhas) == 0:
            conec = table_operations()
            conec[1].execute('INSERT INTO artistas (id_spotify, nome)  VALUES (?, ?)', (num_artista, nome_artista))
            conec[0].commit()
            conec[0].close()
            conec = table_operations()
            conec[1].execute('SELECT id FROM artistas WHERE nome = ?', (nome_artista,))
            linhas1 = conec[1].fetchall()
            conec[0].close()
            id_to_place = linhas1[0][0]
        else:
            id_to_place = linhas[0][0]
            
        conec = table_operations()
        conec[1].execute('INSERT INTO albuns (id_spotify, nome, id_artista)  VALUES (?, ?, ?)',(data_sent, str(nome_album), id_to_place))
        conec[0].commit()
        conec[0].close() 
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))

        return r

    
    if request.method == "GET":
        data_sent = int(request.get_json())
        conec = table_operations()
        conec[1].execute('SELECT * FROM albuns WHERE id = %d' %data_sent)
        linhas = conec[1].fetchall()
        conec[0].close()
        r = make_response(jsonify(linhas))
        return r

    
    if request.method == "DELETE":
        data_sent = int(request.get_json())
        conec = table_operations()
        conec[1].execute('DELETE  FROM albuns WHERE id = %d' % data_sent)
        conec[0].commit()
        conec[0].close()

        conec = table_operations()
        conec[1].execute('DELETE  FROM listas_albuns WHERE id_album = %d' % data_sent)
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r


@servico_web.route("/artistas/allAlbArt", methods = ["GET", "DELETE"])
def allAlbArt():
    

    if request.method == "GET":
        data_sent = int(request.get_json())
        conec = table_operations()
        conec[1].execute('SELECT * FROM albuns WHERE id_artista = ?', (data_sent,))
        linhas = conec[1].fetchall()
        conec[0].close()        
        r = make_response(jsonify(linhas))
        return r


    if request.method == "DELETE":
        data_sent = int(request.get_json())
        conec = table_operations()
            
        conec[1].execute('DELETE FROM albuns WHERE id_artista = ?', (data_sent,))
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r

@servico_web.route("/artistas/allArt", methods = ["GET", "DELETE"])
def allArt():
    

    if request.method == "GET":
        conec = table_operations()
        conec[1].execute('SELECT * FROM artistas')
        linhas = conec[1].fetchall()
        conec[0].close()        
        r = make_response(jsonify(linhas))
        return r
    #
    if request.method == "DELETE":
        conec = table_operations()
            
        conec[1].execute('DELETE FROM artistas')
        conec[0].commit()
        conec[0].close()

        conec = table_operations()           
        conec[1].execute('DELETE FROM albuns')
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r


@servico_web.route("/artistas", methods = ["GET", "POST", "DELETE"])
def artistas():
    

    if request.method == "GET":
        conec = table_operations()        
        data_sent = int(request.get_json())
        conec[1].execute('SELECT * FROM artistas WHERE id = %d' %data_sent)
        linhas = conec[1].fetchall()
        conec[0].close()
        r = make_response(jsonify(linhas))
        return r

    
    if request.method == "POST":
        data_sent = request.get_json()
        #spotify data retrieval
        url = 'https://api.spotify.com/v1/artists/'
        resposta_spoty = requests.get(url + data_sent, headers=conection_spotify())
        resposta_spoty = resposta_spoty.json()
        nome_artista = resposta_spoty['name']

        conec = table_operations()
        conec[1].execute('INSERT INTO artistas (id_spotify, nome)  VALUES (?, ?)',(data_sent, str(nome_artista)))
        conec[0].commit()
        conec[0].close() 
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))

        return r
    

    if request.method == "DELETE":
        data_sent = int(request.get_json())
        conec = table_operations()
        conec[1].execute('DELETE  FROM artistas WHERE id = ?', (data_sent,))
        conec[0].commit()
        conec[0].close()

        conec = table_operations()
        conec[1].execute('DELETE  FROM albuns WHERE id_artista = ?', (data_sent,))
        conec[0].commit()
        conec[0].close()
        string_resposta = 'Operacao bem sucedida'
        r = make_response(jsonify(string_resposta))
        return r
        


if __name__ == '__main__':
    servico_web.run(debug = True)






