import socket,threading
from professor import professor
from monitor import monitor
from coordenador import coordenador
import sqlite3
from hashlib import md5
from valida_dados import verifica_senha,verifica_siape,verifica_email,verifica_telefone,verifica_cpf

class ClientThread(threading.Thread):
    
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
       

    def run(self):
        conexao = sqlite3.connect('bd0.db')
        recebe = self.csocket.recv(1024) #define que os pacotes recebidos sao de ate 1024 bytes
        string = ''
        cursor = conexao.cursor()
       # print ('mensagem recebida: '+ recebe.decode())
       
        string = recebe.decode()
        lista = string.split(',')
        
        if lista[0]=='p':
            msg = ''
            
            if(verifica_siape(lista[2])):
               msg +='Siape,'


            if(verifica_cpf(lista[3])):
               msg +='Cpf,'
            if(verifica_senha(lista[4])):
                msg += 'Senha,'

            if(verifica_email(lista[5])):
                msg+='Email,'

            if(verifica_telefone(lista[6])):
                msg+='Telefone,'

            if(len(msg)==0):
                msg = "certo"
                self.csocket.send(msg.encode())
                cursor.execute('INSERT INTO  Professores VALUES (?,?,?,?,?,?,?)', (lista[1],lista[2],lista[3],md5(lista[4].encode('utf-8')).hexdigest(),lista[5],lista[6],lista[7]))
            else:
                self.csocket.send(msg.encode())
                
            #cursor.execute('SELECT * from Professores')
            #for c in cursor:
            #   print(c)
            
            conexao.commit()
            conexao.close()

        
            
        if lista[0]=='m':
            #print("EH monitor!!!")
            msg = ''
            
            if(verifica_siape(lista[2])):
               msg +='Matricula,'


            if(verifica_cpf(lista[3])):
               msg +='Cpf,'
            if(verifica_senha(lista[4])):
                msg += 'Senha,'

            if(verifica_email(lista[5])):
                msg+='Email,'

            if(verifica_telefone(lista[6])):
                msg+='Telefone,'

            if(len(msg)==0):
                msg = "certo"
                self.csocket.send(msg.encode())
                cursor.execute('INSERT INTO Monitores  VALUES (?,?,?,?,?,?,?)', (lista[1],lista[2],lista[3],md5(lista[4].encode('utf-8')).hexdigest(),lista[5],lista[6],lista[7]))
            else:
                self.csocket.send(msg.encode())
            #cursor.execute('SELECT * from Monitores')

            #for c in cursor:
            #   print(c)

            conexao.commit()
            conexao.close()
        if(lista[0]=="verifica"):
            print(lista)
            print("entrou no altera")
            conf = False
            
            try:
                cursor.execute("UPDATE Tecnicos SET Senha = ? WHERE Email = ? ",(md5(lista[2].encode('utf-8')).hexdigest(),lista[1]))
                conexao.commit()
                    
            except:
                pass
                
                    
            
            try:
                cursor.execute("UPDATE Monitores SET Senha = ? WHERE Email = ? ",(md5(lista[2].encode('utf-8')).hexdigest(),lista[1]))
                conexao.commit()
                
            except:
                pass
                
                    
            
            try:
                cursor.execute("UPDATE Professores SET Senha = ? WHERE Email = ? ",(md5(lista[2].encode('utf-8')).hexdigest(),lista[1]))
                conexao.commit()
                    
            except:
                pass
                
                    

            
            try:
                cursor.execute("UPDATE Coordenadores SET Senha = ? WHERE Email = ? ",(md5(lista[2].encode('utf-8')).hexdigest(),lista[1]))
                print("aqui nos coordenador")
                conexao.commit()
                   
            except:
                pass
                
                
            
            
                
        if(lista[0]=="envia"):
            conf = False
            if(conf==False):
                consulta = cursor.execute("SELECT Email from Tecnicos")
                for x in consulta.fetchall():
                    if(x[0]==lista[1]):
                        conf = True
                    
            if(conf==False):
                consulta = cursor.execute("SELECT Email from Monitores")
                for x in consulta.fetchall():
                    if(x[0]==lista[1]):
                        conf = True
                    
            if(conf==False):
                consulta = cursor.execute("SELECT Email from Coordenadores")
                for x in consulta.fetchall():
                    if(x[0]==lista[1]):
                        conf = True
                    

            if(conf==False):
                consulta = cursor.execute("SELECT Email from Professores")
                for x in consulta.fetchall():
                    if(x[0]==lista[1]):
                        conf = True
                    
            
            if(conf==True):
                print("existe")
                self.csocket.send("exist".encode())
            else:
                self.csocket.send("nexist".encode())




        if lista[0]=='c':
            
            msg = ''
            
            if(verifica_siape(lista[2])):
               msg +='Siape,'


            if(verifica_cpf(lista[3])):
               msg +='Cpf,'
            if(verifica_senha(lista[4])):
                msg += 'Senha,'

            if(verifica_email(lista[5])):
                msg+='Email,'

            if(verifica_telefone(lista[6])):
                msg+='Telefone,'
            
            if(len(msg)==0):
                msg = 'certo'
                self.csocket.send(msg.encode())
                cursor.execute('INSERT INTO Coordenadores  VALUES (?,?,?,?,?,?,?)', (lista[1],lista[2],lista[3],md5(lista[4].encode('utf-8')).hexdigest(),lista[5],lista[6],lista[7]))
            else:
                self.csocket.send(msg.encode())
            #cursor.execute('SELECT * from Coodenadores')

            #for c in cursor:
            #   print(c)
            conexao.commit()
            conexao.close()

        if lista[0] == "l":#l de logar
            if(lista[1] == 'c'):
                confEm = False
                confSen = False
                consulta = cursor.execute("SELECT * from Coordenadores")
                for x in consulta.fetchall():
                    for i in x:
                        if i==lista[2]:
                            confEm = True
                        if i == lista[3]:
                            confSen = True
                if((confEm == True) and (confSen==True)):
                    self.csocket.send("plog".encode())
                else:
                    self.csocket.send("nlog".encode())

            if(lista[1] == 'p'):
                confEm = False
                confSen = False
                consulta = cursor.execute("SELECT * from Professores")
                for x in consulta.fetchall():
                    for i in x:
                        if i==lista[2]:
                            confEm = True
                        if i == lista[3]:
                            confSen = True
                if((confEm == True) and (confSen==True)):
                    self.csocket.send("plog".encode())
                else:
                    self.csocket.send("nlog".encode())

            if(lista[1] == 'm'):
                confEm = False
                confSen = False
                consulta = cursor.execute("SELECT * from Monitores")
                for x in consulta.fetchall():
                    for i in x:
                        if i==lista[2]:
                            confEm = True
                        if i == lista[3]:
                            confSen = True
                if((confEm == True) and (confSen==True)):
                    self.csocket.send("plog".encode())
                else:
                    self.csocket.send("nlog".encode())

            if(lista[1] == 't'):
                confEm = False
                confSen = False
                consulta = cursor.execute("SELECT * from Tecnicos")
                for x in consulta.fetchall():
                    for i in x:
                        if i==lista[2]:
                            confEm = True
                        if i == lista[3]:
                            confSen = True
                if((confEm == True) and (confSen==True)):
                    self.csocket.send("plog".encode())
                else:
                    self.csocket.send("nlog".encode())

                    
        

                            
                       
                        
                
        
if __name__ == "__main__":
        
        host = ''
        port = 7000
        addr = (host, port)
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reiniciliza o socket
        serv_socket.bind(addr) #define a porta e quais ips podem se conectar com o servidor  
        while(True):
        
                serv_socket.listen(10) #define o limite de conexoes
                print ('aguardando conexao')
                con, cliente = serv_socket.accept() # servidor aguardando conexao
                print('conectado')
                print('aguardando mensagem')
                newthread = ClientThread(cliente, con)
                newthread.start()
                
        
