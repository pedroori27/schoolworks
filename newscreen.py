import random
import tkinter as tk
from tkinter import ttk, messagebox, Menu
from tkinter.messagebox import showerror, showwarning, showinfo
# Funções murilo (e sua classe)
activeuser = None #O Usuario q Fez O Login
usersdata = [[7663246, 'teste', 'teste', 1500]] #Lista Dos Usuarios
class newuser: #Criei uma classe com as informações do novo usuario
    def __init__(self, name, pin):
        self.name = name
        self.id = random.randrange(1000000,9999999) #Cria Um Id Aleatorio
        for id in usersdata:
            while id[0] == self.id: #Verifica Se Ja Existe o Id Se Não Cria um Novo
                self.id = random.randrange(1000000,9999999)
        self.pin = pin
        self.saldo = 1500
def createuser(nam,pn): #
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

# Funções primeiro!
def open(): # Abre o banco na tela de escolher entre registro e login
    bank.geometry(f"{500}x{500}+{(bank.winfo_screenwidth() // 2) - (500 // 2)}+{(bank.winfo_screenheight() // 2) - (500 // 2)}")
    rl.grid(row=0, column=0, sticky="nsew") # nsew significa que vai se alinhar com os 4 cantos da tela
    bank.mainloop()
def hide(): # esconder a janela se alguem tentar fechar com o x
    security.withdraw()
    wipeSecurity()
def wipeSecurity(): # fecha todos os grid
    for widget in security.winfo_children():
        widget.grid_remove()
def centralizationS(width=300, height=400): # Centraliza a tela de login e registro
    security.update_idletasks()
    x = (security.winfo_screenwidth() // 2) - (width // 2)
    y = (security.winfo_screenheight() // 2) - (height // 2)
    security.geometry(f"{width}x{height}+{x}+{y}")
def openRegister(): # tela de registro
    centralizationS()
    security.deiconify()
    security.lift()
    Register.grid(row=0,column=0,sticky="nsew")
def openLogin(): # tela de login
    centralizationS()
    security.deiconify()
    security.lift()
    Login.grid(row=0,column=0, sticky="nsew")
def getValueRegister(): # Pega o valor das entry para criar o registro
    name = registerEntryName.get()
    pin = registerEntryPassword.get()
    if len(pin) < 8:
        messagebox.showwarning(title='Aviso',message='A senha deve conter no minimo 8 digitos.')
        pin = loginEntryPassword.get()
        security.lift()
        return
    createuser(name,pin)
    messagebox.showinfo(title='Aviso',message=f"Conta criada! {name}!")
    security.withdraw()
def getValueLogin(): # Pega o valor das entry para criar o login
    name = loginEntryName.get()
    pin = loginEntryPassword.get()
    login(name,pin)
    if activeuser != None:
        security.withdraw()
        openHome()
    else:
        messagebox.showwarning(title='Aviso',message='Nome ou senha invalidos')
def openHome():
    if activeuser != None:
        rl.grid_remove()
        Home.grid(row=0,column=0, sticky="nsew")
    else:
        messagebox.showerror(title='Aviso',message='Não esta logado!')
def loggedOff():
    wipeSecurity()
    rl.grid(row=0, column=0, sticky="nsew")
# Tela principal
bank = tk.Tk()
bank.geometry("500x500")
bank.title('Banco')
bank.rowconfigure(0, weight=1)
bank.columnconfigure(0, weight=1)

# Barra do menu
menubar = Menu(bank)
bank.config(menu=menubar)
menu = Menu(menubar, tearoff=0)
menu.add_command(label='Home', command=openHome)
menu.add_command(label='LoggedOut', command=loggedOff)
menubar.add_cascade(label="Menu", menu=menu)
# toplevel (o registro e login aparece ai dentro)
security = tk.Toplevel(bank)
security.geometry('300x400')
security.title('security')
security.columnconfigure((0), weight=1)
security.rowconfigure((0), weight=1)
security.withdraw()
security.protocol("WM_DELETE_WINDOW", hide) # esconder a janela se alguem tentar fechar com o x
# Frames (rl = Registro e login)
rl = tk.Frame(bank, bg="lightgray") # 3 botões, registro, login e fechar
rl.columnconfigure((0,1,2), weight=1)
rl.rowconfigure((0,1,2), weight=1)

Register = tk.Frame(security) # registro
Register.columnconfigure((0), weight=1)
Register.rowconfigure((0,1,2,3), weight=1)

Login = tk.Frame(security) # login
Login.columnconfigure((0), weight=1)
Login.rowconfigure((0,1,2,3), weight=1)

Home = tk.Frame(bank, bg="black") # Tela ao logar na conta
Home.columnconfigure((0,1,2), weight=1)
Home.rowconfigure((0,1,2), weight=1)
# Frame: registo e login
bankTitle = ttk.Label(rl, text='Banco HP', background="lightgray")
bankTitle.grid(row=0, column=1, sticky='n', pady=30)
buttomRegister = ttk.Button(rl, text="Registro", command=openRegister)
buttomRegister.grid(row=0, column=1)
buttomLogin = ttk.Button(rl, text="Login", command=openLogin)
buttomLogin.grid(row=1, column=1)
buttomClose = ttk.Button(rl, text="Sair", command=bank.destroy)
buttomClose.grid(row=2, column=1)
# frame: fazer registro
registerTitle = ttk.Label(Register, text='Registro')
registerTitle.grid(row=0,column=0)
registerTitleName = ttk.Label(Register, text='Nome')
registerTitleName.grid(row=1,column=0, sticky='n')
registerEntryName = ttk.Entry(Register)
registerEntryName.grid(row=1,column=0)
registerTitlePassword = ttk.Label(Register, text='Senha')
registerTitlePassword.grid(row=2, column=0, sticky='n')
registerEntryPassword = ttk.Entry(Register, show='*')
registerEntryPassword.grid(row=2,column=0)
buttomRegistring = ttk.Button(Register, text="Registrar", command=getValueRegister)
buttomRegistring.grid(row=3, column=0)
# frame: fazer login
loginTitle = ttk.Label(Login, text='Login')
loginTitle.grid(row=0,column=0)
loginTitleName = ttk.Label(Login, text='Nome')
loginTitleName.grid(row=1,column=0,sticky='n')
loginEntryName = ttk.Entry(Login)
loginEntryName.grid(row=1,column=0)
loginTitlePassworld = ttk.Label(Login, text='Senha')
loginTitlePassworld.grid(row=2,column=0,sticky='n')
loginEntryPassword = ttk.Entry(Login, show='*')
loginEntryPassword.grid(row=2,column=0)
buttomLoging = ttk.Button(Login, text="Logar", command=getValueLogin)
buttomLoging.grid(row=3, column=0)
# Frame: Home pós login
HomeTitle = ttk.Label(Home, text='Entrou!')
HomeTitle.grid(row=0,column=1)
open()