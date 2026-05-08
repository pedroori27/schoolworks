#transação
import security as d
d.activeuser
d.usersdata=[]
   
def transacao(user,transf):
    for x in d.usersdata:
        if user == d.activeuser[1]:
            print("Não é possível transferir para si mesmo")
            if x[1] == user:
                if transf>d.activeuser[3]:
                    print("Saldo insuficiente")
                else:
                    d.activeuser[3] -= transf
                    x[3] += transf
                    print("Transferência realizada ",transf," Reais foram enviados para: ",user)