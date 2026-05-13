# Me chamo Pedro
# O tal do Recla
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showerror, showwarning, showinfo
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
def createuser(nam,pn): #Cria O Usuario A partir dos dados recebidos pela tela por meio dos parametros:
    new = newuser(nam,pn)
    newdata = [new.id,new.name,new.pin,new.saldo]
    usersdata.append(newdata)
    print(f"Usuario {new.name} Criado Com Sucesso! (ID: {new.id})")
    return new
def login(name,pin): #Funçao de Login que define o usuario ativo
    global activeuser
    for user in usersdata:
        if user[1] == name and user[2] == pin: #Verfica se existe um nome e pin igual no userdata, se nao define o activeuser ao usuario logado
            activeuser = user
            return True
    print("Erro! Não Foi Localizado O Usuário.") 
    activeuser = None
    return None
def SR(): # Função da tela de registro
    def getvalue():
        name = name_entry.get()
        print(name)  # agora está em uma variável
        pin = password_entry.get()
        while len(pin) != 8:
            messagebox.showwarning(title='Aviso',message='A senha deve conter no minimo 8 digitos.')
            pin = password_entry.get()
            return
        createuser(name,pin)
        messagebox.showinfo(title='Aviso',message=f"Conta criada! {name}!")
        print(pin)  # agora está em uma variável
        app.destroy()
    app = tk.Toplevel()
    app.geometry('300x400')
    app.title('Registro')
    app.columnconfigure((0,1,2), weight=1)
    app.rowconfigure((0,1,2,3), weight=1)
    # Nome
    name_label = ttk.Label(app, text='Nome:')
    name_label.grid(column=1, row=1, sticky=tk.N)
    name_entry = ttk.Entry(app)
    name_entry.grid(column=1, row=1)
    # Senha
    password_label = ttk.Label(app, text='Senha:')
    password_label.grid(column=1, row=2, sticky=tk.N)
    password_label = ttk.Label(app, text='Pin Deve Conter 8 Caracteres.')
    password_label.grid(column=1, row=3, sticky=tk.N)
    password_entry = ttk.Entry(app, show='*')
    password_entry.grid(column=1, row=2)
    # Botão de registro
    button = ttk.Button(app, text='Registro', command=getvalue)
    button.grid(column=1, row=3, ipadx=5, ipady=5)
def SL(): # Função da tela de login
    def getlogin():
        name = name_entry.get()
        pin = password_entry.get()
        login(name,pin)
        print(activeuser, usersdata)
        if activeuser != None:
            MainS()
            app.destroy()
        else:
            messagebox.showwarning(title='Aviso',message='Nome ou senha invalidos')
    app = tk.Toplevel()
    app.geometry('300x400')
    app.title('Login')
    app.columnconfigure((0,1,2), weight=1)
    app.rowconfigure((0,1,2,3), weight=1)
    bank = ttk.Label(app, text="Login")
    bank.grid(column=1, row=0, sticky=tk.N)
    # Nome
    name_label = ttk.Label(app, text='Nome:')
    name_label.grid(column=1, row=1, sticky=tk.N)
    name_entry = ttk.Entry(app)
    name_entry.grid(column=1, row=1)
    # Senha
    password_label = ttk.Label(app, text='Senha:')
    password_label.grid(column=1, row=2, sticky=tk.N)
    password_entry = ttk.Entry(app, show='*')
    password_entry.grid(column=1, row=2)
    # Botão de login
    button = ttk.Button(app, text='login', command=getlogin)
    button.grid(column=1, row=3, ipadx=5, ipady=5)
global app
app = tk.Tk()
app.geometry("500x500")
app.title('Banco')
app.columnconfigure((0,1,2), weight=1)
app.rowconfigure((0,1,2), weight=1)
bank = ttk.Label(app, text='Banco HP')
bank.grid(column=1, row=0, sticky=tk.N)
rbutton = ttk.Button(app, text='Registro', command=SR)
rbutton.grid(column=1, row=0, ipadx=5, ipady=5)
lbutton = ttk.Button(app, text='Login', command=SL)
lbutton.grid(column=1, row=1, ipadx=5, ipady=5)
sbutton = ttk.Button(app, text='Fechar', command=app.destroy)
sbutton.grid(column=1, row=2, ipadx=5, ipady=5)
def RL(): # Tela para escolher entre registro e login
    app.mainloop()


def MainS():
    app = tk.Toplevel()
    app.geometry('500x500')
    app.title('Banco HP')
    app.columnconfigure((0,1,2), weight=1)
    app.rowconfigure((0,1,2), weight=1)
    # Criar o botão primeiro
    menubutton = ttk.Menubutton(app, text='Selecione o serviço')
    menubutton.grid(column=1, row=1)
 
    # Criar o menu
    menu = tk.Menu(menubutton, tearoff=False)
    menubutton["menu"] = menu
 
    # Adicionar opções
    menu.add_checkbutton(label="Transferencia", command=TS)
    menu.add_checkbutton(label="Saldo", command=SLL)
    menu.add_checkbutton(label="Sair", command=app.destroy)
 
def TS(): # Função de transferencia, saldo(saldo mostra o ID tambem) e sair
    def transation():
        user = id_entry.get()
        try:
            transf = int(give.get())
        except ValueError:
            messagebox.showerror(title='Erro',message='Digite um valor válido')
            return
        print(user, transf)
        if user == activeuser[1]:
            messagebox.showerror(title='Erro',message='Não é possível transferir para si mesmo')
            return
        for x in usersdata:
            if x[1] == user:
                if transf > activeuser[3]:
                    messagebox.showerror(title='Erro',message='Saldo insuficiente')
                    return
                activeuser[3] -= transf
                x[3] += transf
                messagebox.showinfo(title='Transferido!',message=f"Transferência realizada {transf} Reais enviados para: {user}")
                return
        print("Usuário não encontrado")
    toplev = tk.Toplevel()
    toplev.title('Transferencia')
    toplev.geometry('500x500')
    toplev.columnconfigure((0,1,2), weight=1)
    toplev.rowconfigure((0,1,2), weight=1)
    id_label = ttk.Label(toplev, text='Nome:')
    id_label.grid(column=0, row=0)
    id_entry = ttk.Entry(toplev)
    id_entry.grid(column=1, row=0)
    give_label = ttk.Label(toplev, text='Transferir:')
    give_label.grid(column=0, row=1)
    give = ttk.Entry(toplev)
    give.grid(column=1, row=1)
    sbutton = ttk.Button(toplev, text='Fechar', command=toplev.destroy)
    sbutton.grid(column=0, row=2)
    tbutton = ttk.Button(toplev, text='Transfira', command=transation)
    tbutton.grid(column=1, row=2)
def SLL(): # Função de monstrar o Saldo, sacar e depositar
    # função de saque e deposito
    def sacc():
        value = int(s_label.get())
        if value <= activeuser[3] and value > 0:
            activeuser[3] = activeuser[3]-value
            print(value, activeuser[3])
            balance_label.config(text=f"Saldo: R${activeuser[3]},00")
        else:
            messagebox.showerror(title='Erro',message='Valor invalido')
    def deposit():
        value = int(d_label.get())
        if value > 0:
            activeuser[3] = activeuser[3] + value
            print("Depósito concluído com sucesso!")
            balance_label.config(text=f"Saldo: R${activeuser[3]}")
        else:
            messagebox.showerror(title='Erro',message='Valor invalido')
    # tela
    toplev = tk.Toplevel()
    toplev.title('Saldo')
    toplev.geometry('500x500')
    toplev.columnconfigure((0,1,2), weight=1)
    toplev.rowconfigure((0,1,2), weight=1)
    # Texto mostrando o nome, id e dinheiro guardado
    idname_label = ttk.Label(toplev, text=f"Olá {activeuser[1]}! (ID: {activeuser[0]})")
    idname_label.grid(column=1,row=0)
    balance_label = ttk.Label(toplev, text=f"Saldo: R${activeuser[3]}")
    balance_label.grid(column=1,row=1, sticky=tk.N)
    # Depositar, Sacar e fechar a tela.
    d_label = ttk.Entry(toplev)
    d_label.grid(column=0, row=1)
    dbutton = ttk.Button(toplev, text='Depositar', command=deposit)
    dbutton.grid(column=0, row=2)
    s_label = ttk.Entry(toplev)
    s_label.grid(column=2, row=1)
    sbutton = ttk.Button(toplev, text='Sacar', command=sacc)
    sbutton.grid(column=2, row=2)
    button = ttk.Button(toplev, text='Fechar', command=toplev.destroy)
    button.grid(column=1, row=2)
RL()
