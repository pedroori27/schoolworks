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
def tranferir(valor, destinatario_id): #Funçao para tranferir verificando se o usuario existe,nao é ele mesmo e se o valor é maior que o saldo
    if destinatario_id not in db.usersdata:
        messagebox.showerror(title='Aviso', message='Destinatário não encontrado.')
        return False
    if destinatario_id == db.activeuser.id:
        messagebox.showerror(title='Aviso', message='Não é possível transferir para si mesmo.')
        return False
    destinatario = db.usersdata[destinatario_id]

    if db.activeuser.saldo < valor:
        messagebox.showwarning(title='Aviso', message='Saldo insuficiente para realizar a transferência.')
        return False

    # Realiza a transferência
    db.activeuser.saldo -= valor
    destinatario.saldo += valor
    tranferirBalance.config(text=f"Saldo: R${db.activeuser.saldo:.2f}")
    messagebox.showinfo(title='Sucesso', message=f"Transferência de R${valor:.2f} realizada com sucesso para {destinatario.name}!")
    tranferirEntryValor.delete(0, tk.END)
    tranferirEntryDestinatario.delete(0, tk.END)
    return True

def deposito(valor): #Função Deposito 
    if valor <= 0:
        messagebox.showerror(title='Aviso', message='Valor de depósito inválido.')
        return False
    db.activeuser.saldo += valor
    homeBalance.config(text=f"Saldo: R${db.activeuser.saldo:.2f}")
    depositeEntry.delete(0, tk.END)
    return True

def saque(valor): #Função para Saque verifica alguns ifs e desconta o saldo do active user
    if valor <= 0:
        messagebox.showerror(title='Aviso', message='Valor de saque inválido.')
        return False
    if db.activeuser.saldo < valor:
        messagebox.showwarning(title='Aviso', message='Saldo insuficiente para realizar o saque.')
        return False
    db.activeuser.saldo -= valor
    homeBalance.config(text=f"Saldo: R${db.activeuser.saldo:.2f}")
    withdrawEntry.delete(0, tk.END)
    return True
    
# Funções primeiro!
def open_app(): # Abre o banco na tela de escolher entre registro e login
    bank.geometry(f"{500}x{500}+{(bank.winfo_screenwidth() // 2) - (500 // 2)}+{(bank.winfo_screenheight() // 2) - (500 // 2)}")
    rl.grid(row=0, column=0, sticky="nsew") # nsew significa que vai se alinhar com os 4 cantos da tela
    bank.mainloop()

def hide(): # esconder a janela se alguem tentar fechar com o x
    security.withdraw()
    registerEntryName.delete(0, tk.END)
    registerEntryPassword.delete(0, tk.END)
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
    registerEntryPassword.delete(0, tk.END)
    if len(pin) < 8:
        messagebox.showwarning(title='Aviso', message='A senha deve conter no minimo 8 digitos.')
        security.lift()
    else:
        db.createuser(name, pin)
        messagebox.showinfo(title='Sucesso', message=f"Conta criada! {name}!")
        security.withdraw()
        registerEntryName.delete(0, tk.END)


def getValueLogin(): # Pega o valor das entry para criar o login
    name = loginEntryName.get()
    pin = loginEntryPassword.get()
    loginEntryPassword.delete(0, tk.END)
    if db.login(name, pin): # Chama o método de login da instância db
        print("Login efetuado")
        security.withdraw()
        openHome()
        print(f"Usuário Ativo: {db.activeuser}")
        loginEntryPassword.delete(0, tk.END)
    else:
        messagebox.showwarning(title='Aviso', message='Nome ou senha invalidos')

def openHome(): 
    # Esta função verifica o login, limpa as telas anteriores e atualiza a interface Home com o nome, saldo e ID do usuário logado.
    if db.activeuser != None:
        rl.grid_remove()
        Transfer.grid_remove()
        # Atualiza o texto da Home com o nome do usuário
        homeTitle.config(text=f"Bem Vindo, {db.activeuser.name}!", foreground="white", background="black", font=("Arial", 14, "bold"))
        homeBalance.config(text=f"Saldo: R${db.activeuser.saldo:.2f}", foreground="white", background="black", font=("Arial", 12))
        homeId.config(text=f"ID: {db.activeuser.id}", foreground="white", background="black", font=("Arial", 12))
        Home.grid(row=0, column=0, sticky="nsew")
    else:
        messagebox.showerror(title='Aviso', message='Não está logado!')

def opentransfer():
    # Função que valida o acesso, limpa , esconde a Home e prepara a tela de transferência com o novo saldo
    if db.activeuser != None:
        wipeSecurity()
        Home.grid_remove()
        tranferirBalance.config(text=f"Saldo: R${db.activeuser.saldo:.2f}")
        Transfer.grid(row=0, column=0, sticky="nsew")
    else:
        messagebox.showerror(title='Aviso', message='Não está logado!')

def loggedOff(): # Limpa o usuário ativo
    Home.grid_remove()
    Transfer.grid_remove()
    db.activeuser = None
    messagebox.showinfo(title='Deslogado', message='Usuário deslogado com sucesso!')
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
menu.add_command(label='Transferência', command=opentransfer)
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

Home = tk.Frame(bank, bg="black")
Home.columnconfigure((0,1,2), weight=1)
Home.rowconfigure((0,1,2), weight=1)

Transfer = tk.Frame(bank, bg="black")
Transfer.columnconfigure((0,1,2), weight=1)
Transfer.rowconfigure((0,1,2), weight=1)

# Widgets: Registro e login (Tela Inicial)
bankTitle = ttk.Label(rl, text='Banco HP', background="lightgray", font=("Arial", 16))
bankTitle.grid(row=0, column=1, sticky='n', pady=30)
buttomRegister = ttk.Button(rl, text="Registro", command=openRegister, style="TButton")
buttomRegister.grid(row=0, column=1)
buttomLogin = ttk.Button(rl, text="Login", command=openLogin, style="TButton")
buttomLogin.grid(row=1, column=1)
buttomClose = ttk.Button(rl, text="Sair", command=bank.destroy, style="TButton")
buttomClose.grid(row=2, column=1)

# Widgets: Fazer registro
ttk.Label(Register, text='Registro', font=("Arial", 12, "bold")).grid(row=0, column=0, pady=10)
ttk.Label(Register, text='Nome').grid(row=1, column=0, sticky='n')
registerEntryName = ttk.Entry(Register)
registerEntryName.grid(row=1, column=0, pady=5)
ttk.Label(Register, text='Senha').grid(row=2, column=0, sticky='n')
registerEntryPassword = ttk.Entry(Register, show='*')
registerEntryPassword.grid(row=2, column=0, pady=5)
ttk.Button(Register, text="Registrar", command=getValueRegister, style="TButton").grid(row=3, column=0, pady=20)

# Widgets: Fazer login
ttk.Label(Login, text='Login', font=("Arial", 12, "bold")).grid(row=0, column=0, pady=10)
ttk.Label(Login, text='Nome').grid(row=1, column=0, sticky='n')
loginEntryName = ttk.Entry(Login)
loginEntryName.grid(row=1, column=0, pady=5)
ttk.Label(Login, text='Senha').grid(row=2, column=0, sticky='n')
loginEntryPassword = ttk.Entry(Login, show='*')
loginEntryPassword.grid(row=2, column=0, pady=5)
ttk.Button(Login, text="Logar", command=getValueLogin, style="TButton").grid(row=3, column=0, pady=20)

# Widgets: Home pós login
homeTitle = ttk.Label(Home, text="Bem Vindo", font=("Arial", 14), foreground="white", background="black")
homeTitle.grid(row=0, column=1)
homeId = ttk.Label(Home, text="bem vindo", font=("Arial", 12), foreground="white", background="black")
homeId.grid(row=0, column=1, sticky='s')
homeBalance = ttk.Label(Home, text="Bem Vindo", font=("Arial", 14), foreground="white", background="black")
homeBalance.grid(row=1, column=1)
buttomHome = ttk.Button(Home, text="Sair", command=loggedOff, style="TButton")
buttomHome.grid(row=2, column=1)
depositeEntry = ttk.Entry(Home)
depositeEntry.grid(row=1, column=2)
depositeButton = ttk.Button(Home, text="Depositar", command=lambda: deposito(float(depositeEntry.get())), style="TButton")
depositeButton.grid(row=2, column=2, pady=5)
withdrawEntry = ttk.Entry(Home)
withdrawEntry.grid(row=1, column=0)
withdrawButton = ttk.Button(Home, text="Sacar", command=lambda: saque(float(withdrawEntry.get())), style="TButton")
withdrawButton.grid(row=2, column=0, pady=5)
#  widget: Transferencia
transferTitle = ttk.Label(Transfer, text="Transferência", font=("Arial", 14), foreground="white", background="black")
transferTitle.grid(row=0, column=1)
tranferirBalance = ttk.Label(Transfer, text="Saldo: R$0.00", font=("Arial", 12), foreground="white", background="black")
tranferirBalance.grid(row=0, column=1, sticky='s')
tranferirLabelValor = ttk.Label(Transfer, text="Valor", font=("Arial", 12), foreground="white", background="black")
tranferirLabelValor.grid(row=1, column=1, sticky='n')
tranferirEntryValor = ttk.Entry(Transfer)
tranferirEntryValor.grid(row=1, column=1)
tranferirLabelDestinatario = ttk.Label(Transfer, text="Destinatário", font=("Arial", 12), foreground="white", background="black")
tranferirLabelDestinatario.grid(row=2, column=1, sticky='n')
tranferirEntryDestinatario = ttk.Entry(Transfer)
tranferirEntryDestinatario.grid(row=2, column=1)
tranferirButton = ttk.Button(Transfer, text="Transferir", style="TButton", command=lambda: tranferir(float(tranferirEntryValor.get()), int(tranferirEntryDestinatario.get())))
tranferirButton.grid(row=3, column=1, pady=20)
# Iniciar aplicação
open_app()
