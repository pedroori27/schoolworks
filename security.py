import random

activeuser = None #O Usuario q Fez O Login
usersdata = [] #Lista Dos Usuarios

class newuser: #Criei uma classe com as informações do novo usuario
    def __init__(self, name, pin):
        self.name = name
        self.id = random.randrange(1000000,9999999) #Cria Um Id Aleatorio
        for id in usersdata: 
            while id[0] == self.id: #Verifica Se Ja Existe o Id Se Não Cria um Novo
                self.id = random.randrange(1000000,9999999)
        self.pin = pin
        self.saldo = 1500


def createuser(nam,pn): #Cria o Usuario, apartir de dois parametros dados na tela do recla
    new = newuser(nam,pn)
    newdata = [new.id,new.name,new.pin,new.saldo]
    usersdata.append(newdata)
    print(f"Usuario {new.name} Criado Com Sucesso! (ID: {new.id})")
    return new

def login(name,pin):#Verfica se existe um nome e pin igual no userdata
    global activeuser 
    for user in usersdata:
        if user[1] == name and user[2] == pin:
            activeuser = user
            return True
    print("Erro! Não Foi Localizado O Usuário.")
    activeuser = None
    return None
    
def logout():
    global activeuser
    activeuser = None
    print("Encerrando a Sessão...")
    
    