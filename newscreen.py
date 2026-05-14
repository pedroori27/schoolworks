import random
import tkinter as tk
from tkinter import ttk, messagebox, Menu
from tkinter.messagebox import showerror, showwarning, showinfo

# Funções murilo (e sua classe)

class NewUser: #Criei uma classe com as informações do novo usuario
    def __init__(self, name, pin, existing_ids):
        self.name = name
        self.id = random.randrange(1000000, 9999999) 
        # Verifica se o ID já existe na lista de IDs passada
        while self.id in existing_ids:
            self.id = random.randrange(1000000, 9999999)
        self.pin = pin
        self.saldo = 1500

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Pin: {self.pin}, Saldo: {self.saldo}"

    def __repr__(self):
        return self.__str__()

class DataBank: #Criei uma classe para guardar os dados dos usuarios e o usuario ativo
    def __init__(self):
        self.usersdata = {}
        self.activeuser = None

    def createuser(self, nam, pn): 
        # Passamos as chaves (IDs) existentes para evitar duplicatas
        new = NewUser(nam, pn, self.usersdata.keys())
        self.usersdata[new.id] = new
        print(f"Usuario {new.name} Criado Com Sucesso! (ID: {new.id})")
        return new

    def login(self, name, pin): #Verfica se existe um nome e pin igual no userdata
        for user in self.usersdata.values():
            if user.name == name and user.pin == pin:
                self.activeuser = user
                return True
        print("Erro! Não Foi Localizado O Usuário.")
        self.activeuser = None
        return False
# Instância global do banco de dados
db = DataBank()

def tranferir(valor, destinatario_id):
    if destinatario_id not in db.usersdata:
        print("Destinatário não encontrado.")
        return False

    destinatario = db.usersdata[destinatario_id]

    if db.activeuser.saldo < valor:
        print("Saldo insuficiente para realizar a transferência.")
        return False

    # Realiza a transferência
    db.activeuser.saldo -= valor
    destinatario.saldo += valor
    print(f"Transferência de {valor} realizada com sucesso para {destinatario.name}.")
    return True

def deposito(valor):
    if valor <= 0:
        print("Valor de depósito inválido.")
        return False
    db.activeuser.saldo += valor
    print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {db.activeuser.saldo}")
    return True

def saque(valor):
    if valor <= 0:
        print("Valor de saque inválido.")
        return False
    if db.activeuser.saldo < valor:
        print("Saldo insuficiente para realizar o saque.")
        return False
    db.activeuser.saldo -= valor
    print(f"Saque de {valor} realizado com sucesso. Saldo atual: {db.activeuser.saldo}")
    return True
    
# Funções primeiro!
def open_app(): # Abre o banco na tela de escolher entre registro e login
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
    wipeSecurity()
    centralizationS()
    security.deiconify()
    security.lift()
    Register.grid(row=0,column=0,sticky="nsew")

def openLogin(): # tela de login
    wipeSecurity()
    centralizationS()
    security.deiconify()
    security.lift()
    Login.grid(row=0,column=0, sticky="nsew")

def getValueRegister(): # Pega o valor das entry para criar o registro
    name = registerEntryName.get()
    pin = registerEntryPassword.get()
    if len(pin) < 8:
        messagebox.showwarning(title='Aviso', message='A senha deve conter no minimo 8 digitos.')
        security.lift()
    else:
        db.createuser(name, pin)
        messagebox.showinfo(title='Sucesso', message=f"Conta criada! {name}!")
        security.withdraw()

def getValueLogin(): # Pega o valor das entry para criar o login
    name = loginEntryName.get()
    pin = loginEntryPassword.get()
    
    if db.login(name, pin): # Chama o método de login da instância db
        print("Login efetuado")
        security.withdraw()
        openHome()
        print(f"Usuário Ativo: {db.activeuser}")
    else:
        messagebox.showwarning(title='Aviso', message='Nome ou senha invalidos')

def openHome():
    if db.activeuser != None:
        rl.grid_remove()
        # Atualiza o texto da Home com o nome do usuário
        HomeTitle.config(text=f"Bem Vindo, {db.activeuser.name}!")
        Home.grid(row=0, column=0, sticky="nsew")
    else:
        messagebox.showerror(title='Aviso', message='Não está logado!')

def loggedOff():
    db.activeuser = None # Limpa o usuário ativo
    Home.grid_remove()
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
menu.add_command(label='Logout', command=loggedOff)
menubar.add_cascade(label="Menu", menu=menu)

# toplevel (o registro e login aparece ai dentro)
security = tk.Toplevel(bank)
security.geometry('300x400')
security.title('Segurança')
security.columnconfigure((0), weight=1)
security.rowconfigure((0), weight=1)
security.withdraw()
security.protocol("WM_DELETE_WINDOW", hide)

# Frames
rl = tk.Frame(bank, bg="lightgray")
rl.columnconfigure((0,1,2), weight=1)
rl.rowconfigure((0,1,2), weight=1)

Register = tk.Frame(security)
Register.columnconfigure((0), weight=1)
Register.rowconfigure((0,1,2,3), weight=1)

Login = tk.Frame(security)
Login.columnconfigure((0), weight=1)
Login.rowconfigure((0,1,2,3), weight=1)

Home = tk.Frame(bank, bg="white") # Mudei para white para ler o texto preto
Home.columnconfigure((0,1,2), weight=1)
Home.rowconfigure((0,1,2), weight=1)

# Widgets: Registro e login (Tela Inicial)
bankTitle = ttk.Label(rl, text='Banco HP', background="lightgray", font=("Arial", 16))
bankTitle.grid(row=0, column=1, sticky='n', pady=30)
buttomRegister = ttk.Button(rl, text="Registro", command=openRegister)
buttomRegister.grid(row=0, column=1)
buttomLogin = ttk.Button(rl, text="Login", command=openLogin)
buttomLogin.grid(row=1, column=1)
buttomClose = ttk.Button(rl, text="Sair", command=bank.destroy)
buttomClose.grid(row=2, column=1)

# Widgets: Fazer registro
ttk.Label(Register, text='Registro', font=("Arial", 12, "bold")).grid(row=0, column=0, pady=10)
ttk.Label(Register, text='Nome').grid(row=1, column=0, sticky='n')
registerEntryName = ttk.Entry(Register)
registerEntryName.grid(row=1, column=0, pady=5)
ttk.Label(Register, text='Senha').grid(row=2, column=0, sticky='n')
registerEntryPassword = ttk.Entry(Register, show='*')
registerEntryPassword.grid(row=2, column=0, pady=5)
ttk.Button(Register, text="Registrar", command=getValueRegister).grid(row=3, column=0, pady=20)

# Widgets: Fazer login
ttk.Label(Login, text='Login', font=("Arial", 12, "bold")).grid(row=0, column=0, pady=10)
ttk.Label(Login, text='Nome').grid(row=1, column=0, sticky='n')
loginEntryName = ttk.Entry(Login)
loginEntryName.grid(row=1, column=0, pady=5)
ttk.Label(Login, text='Senha').grid(row=2, column=0, sticky='n')
loginEntryPassword = ttk.Entry(Login, show='*')
loginEntryPassword.grid(row=2, column=0, pady=5)
ttk.Button(Login, text="Logar", command=getValueLogin).grid(row=3, column=0, pady=20)

# Widgets: Home pós login
HomeTitle = ttk.Label(Home, text="Bem Vindo", font=("Arial", 14))
HomeTitle.grid(row=0, column=1)

# Iniciar aplicação
open_app()
