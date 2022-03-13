"""
Aplicações distribuídas - Projeto 3 - cliente_request.py
Grupo: 29
Números de aluno:
Gonçalo Miguel Nº54944
Miguel Duarte Nº54941

"""

import requests
import json


while True:
    msg = input("Insira uma comando: ")
    if msg == "":
        print("Comando vazio") 
    else:
        if msg.split()[0] == "CREATE":

            if msg.split()[1] == "UTILIZADOR":
                
                data = {'nome': msg.split()[2], 'senha': msg.split()[3]}
                r = requests.post('http://localhost:5000/utilizadores', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)

            elif msg.split()[1] == "ARTISTA":
                
                data = msg.split()[2]
                r = requests.post('http://localhost:5000/artistas', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                


            elif msg.split()[1] == "ALBUM":
                
                data = msg.split()[2]
                r = requests.post('http://localhost:5000/albuns', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                

            elif len(msg.split()) == 4:
                data = {"id": msg.split()[1], "id_album": msg.split()[2], "avaliacao": msg.split()[3]}
                r = requests.post('http://localhost:5000/utilizadores/avaliar', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                
                
            else:
                print("Comando inválido!")
            
        elif msg.split()[0] == "READ":

            if msg.split()[1] == "UTILIZADOR":
                data = msg.split()[2]
                r = requests.get('http://localhost:5000/utilizadores', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                

            elif msg.split()[1] == "ARTISTA":
                data = msg.split()[2]
                r = requests.get('http://localhost:5000/artistas', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                
            
            elif msg.split()[1] == "ALBUM":
                data = msg.split()[2]
                r = requests.get('http://localhost:5000/albuns', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                
            
            elif msg.split()[1] == "ALL":

                if msg.split()[2] == "UTILIZADORES":
                    
                    r = requests.get('http://localhost:5000/utilizadores/all')
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    

                elif msg.split()[2] == "ARTISTAS":
                    r = requests.get('http://localhost:5000/artistas/allArt')
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    

                elif msg.split()[2] == "ALBUNS" and len(msg.split()) == 3:
                    
                    r = requests.get('http://localhost:5000/albuns/allAlb')
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    

                
                elif msg.split()[2] == "ALBUNS_A":
                    data =  msg.split()[3]
                    r = requests.get('http://localhost:5000/artistas/allAlbArt', json = data)
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    
                
                elif msg.split()[2] == "ALBUNS_U":
                    data = msg.split()[3]
                    r = requests.get('http://localhost:5000/utilizadores/album', json = data)
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    

                
                elif msg.split()[2] == "ALBUNS" and len(msg.split()) == 4:
                    data =  msg.split()[3]
                    r = requests.get('http://localhost:5000/albuns/albAva', json = data)
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    

                else:
                    print("Comando inválido")

        elif msg.split()[0] == "DELETE":

            if msg.split()[1] == "UTILIZADOR":
                data = msg.split()[2]
                r = requests.delete('http://localhost:5000/utilizadores', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                

            elif msg.split()[1] == "ARTISTA":
                data = msg.split()[2]
                r = requests.delete('http://localhost:5000/artistas', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                
            
            elif msg.split()[1] == "ALBUM":
                data = msg.split()[2]
                r = requests.delete('http://localhost:5000/albuns', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                
            
            elif msg.split()[1] == "ALL":

                if msg.split()[2] == "UTILIZADORES":
                    
                    r = requests.delete('http://localhost:5000/utilizadores/all')
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    

                elif msg.split()[2] == "ARTISTAS":
                    data = "all"
                    r = requests.delete('http://localhost:5000/artistas/allArt', json = data)
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    

                elif msg.split()[2] == "ALBUNS":
                    
                    r = requests.delete('http://localhost:5000/albuns/allAlb')
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    


                elif msg.split()[2] == "ALBUNS_A":
                    data = msg.split()[3]
                    r = requests.delete('http://localhost:5000/artistas/allAlbArt', json = data)
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    

                elif msg.split()[2] == "ALBUNS_U":
                    data = msg.split()[3]
                    r = requests.delete('http://localhost:5000/utilizadores/album', json = data)
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    
                elif msg.split()[2] == "ALBUNS":
                    data = msg.split()[3]
                    r = requests.delete('http://localhost:5000/albuns/albAva', json = data)
                    print (r.status_code)
                    print (r.content.decode())
                    print (r.headers)
                    

            else:
                print("Comando inválido")

            

        elif msg.split()[0] == "UPDATE":
            if msg.split()[1] == "ALBUM":
                data = {'idAlbum': msg.split()[2], 'avaliacao': msg.split()[3], 'idUser': msg.split()[4]}
                r = requests.put('http://localhost:5000/albuns/albAva', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                
                
            
            elif msg.split()[1] == "UTILIZADOR":
                data = {'id': msg.split()[2], 'senha': msg.split()[3]}
                r = requests.put('http://localhost:5000/utilizadores', json = data)
                print (r.status_code)
                print (r.content.decode())
                print (r.headers)
                

        elif msg.split()[0] == "EXIT":
            print("Cliente terminado!")
            break


        else:
            print("Comando desconhecido!")

    



        






