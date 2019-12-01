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
        if(lista[0]=="mostrar"):
            cont = 0
            string = ''
            cons = cursor.execute("SELECT * from Reservas WHERE Cpf = ?",(lista[1],))
            for i in cons.fetchall():
                cont+=1
                string+=str(i[0])+","+str(i[1]) +" as "+ str(int(i[1])+2)+","+str(i[3])+","
            print("\n string",string)
            if(cont==0):
                self.csocket.send("vazio".encode())
            else:
                self.csocket.send("recebido".encode())
                self.csocket.send(string.encode())
                
            
        if(lista[0]=="reservar"):
            print("Lista",lista)
            cont = 0
            cons = cursor.execute("SELECT Numero,Situacao from Salas WHERE (Bloco = ? and Numero = ? AND Situacao = ? AND Dia = ? AND Horario=?)",(lista[2],lista[3],"Livre",lista[4],lista[5]))
            for i in cons.fetchall():
                print("a", i)
                cont+=1

            print("O cont",cont)

            if(cont==0):
                self.csocket.send("ocupado".encode())
            else:
                cursor.execute("UPDATE Salas set Situacao = ? WHERE (Numero = ? AND Dia = ? AND Horario = ?)",("Ocupado",lista[3],lista[4],lista[5]))
                conexao.commit()
                cursor.execute("INSERT into Reservas VALUES(?,?,?,?)",(lista[3],lista[5],lista[1],lista[4]))
                conexao.commit()              
                self.csocket.send("certo".encode())
                
        if(lista[0]=="Listar"):
            
            str2 =''
            cont = 0
            cons = cursor.execute("SELECT * from Salas WHERE (Bloco=? AND Numero = ?)",(lista[1],lista[2],))
           
            for i in cons.fetchall():
                str2 +=i[2]+","
                cont+=1
            if(cont==0):
                self.csocket.send("vazio".encode())
            else:
                self.csocket.send(str2.encode())
          
        if(lista[0]=="altera_telefone"):
            if(lista[1]=='c'):
                if(verifica_telefone(lista[2])):
                    self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Coordenadores set Telefone = ? WHERE Telefone = ?",(lista[2],lista[3]))
                    conexao.commit()
                    self.csocket.send("mudou".encode())
                        
            if(lista[1]=='p'):
                if(verifica_telefone(lista[2])):
                    self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Professores set Telefone = ? WHERE Telefone = ?",(lista[2],lista[3]))
                    conexao.commit()
                    self.csocket.send("mudou".encode())

            if(lista[1]=='m'):
                if(verifica_telefone(lista[2])):
                    self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Monitores set Telefone = ? WHERE Telefone = ?",(lista[2],lista[3]))
                    conexao.commit()
                    self.csocket.send("mudou".encode())
                        
            if(lista[1]=='t'):
                if(verifica_telefone(lista[2])):
                    self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Tecnicos set Telefone = ? WHERE Telefone = ?",(lista[2],lista[3]))
                    conexao.commit()
                    self.csocket.send("mudou".encode())
                
        if(lista[0]=="altera_senha"):
            
            if(lista[1]=='c'):
                if(verifica_senha(lista[2])):
                    self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Coordenadores set Senha = ? WHERE Senha = ?",(md5(lista[2].encode('utf-8')).hexdigest(),md5(lista[3].encode('utf-8')).hexdigest()))
                    conexao.commit()
                    self.csocket.send("mudou".encode())
                    
            if(lista[1]=='p'):
                if(verifica_senha(lista[2])):
                    self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Professores set Senha = ? WHERE Senha = ?",(md5(lista[2].encode('utf-8')).hexdigest(),md5(lista[3].encode('utf-8')).hexdigest()))
                    conexao.commit()
                    self.csocket.send("mudou".encode())

            if(lista[1]=='m'):
                if(verifica_senha(lista[2])):
                    self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Monitores set Senha = ? WHERE Senha = ?",(md5(lista[2].encode('utf-8')).hexdigest(),md5(lista[3].encode('utf-8')).hexdigest()))
                    conexao.commit()
                    self.csocket.send("mudou".encode())
                    
            if(lista[1]=='t'):
                if(verifica_senha(lista[2])):
                    self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Tecnicos set Senha = ? WHERE Senha = ?",(md5(lista[2].encode('utf-8')).hexdigest(),md5(lista[3].encode('utf-8')).hexdigest()))
                    conexao.commit()
                    self.csocket.send("mudou".encode())


                    
                    
                
        if(lista[0]=="altera_email"):
            
            if(lista[1]=='c'):
                if(verifica_email(lista[2])):
                   self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Coordenadores SET Email = ? WHERE Email = ?",(lista[2],lista[3]))
                    conexao.commit()
                    self.csocket.send("mudou".encode())
                    
            if(lista[1]=='p'):
                if(verifica_email(lista[2])):
                   self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Professores SET Email = ? WHERE Email = ?",(lista[2],lista[3]))
                    conexao.commit()
                    self.csocket.send("mudou".encode())

            if(lista[1]=='t'):
                if(verifica_email(lista[2])):
                   self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Tecnicos SET Email = ? WHERE Email = ?",(lista[2],lista[3]))
                    conexao.commit()
                    self.csocket.send("mudou".encode())
            if(lista[1]=='m'):
                if(verifica_email(lista[2])):
                   self.csocket.send("existe".encode())
                else:
                    cursor.execute("UPDATE Monitores SET Email = ? WHERE Email = ?",(lista[2],lista[3]))
                    conexao.commit()
                    self.csocket.send("mudou".encode())
                    
                
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
            msg = ''
            
            try:
                if(not (verifica_senha(lista[2]))):
                    cursor.execute("UPDATE Tecnicos SET Senha = ? WHERE Email = ? ",(md5(lista[2].encode('utf-8')).hexdigest(),lista[1]))
                    conexao.commit()
                    msg = "certo"
                    self.csocket.send(msg.encode())
                else:
                    msg = "errado"
                    self.csocket.send(msg.encode())
            except:
                pass
                
                    
            
            try:
                if(not (verifica_senha(lista[2]))):
                    cursor.execute("UPDATE Monitores SET Senha = ? WHERE Email = ? ",(md5(lista[2].encode('utf-8')).hexdigest(),lista[1]))
                    conexao.commit()
                    msg = "certo"
                else:
                    msg = "errado"
                    self.csocket.send(msg.encode())
                
            except:
                pass
                
                    
            
            try:
                if(not (verifica_senha(lista[2]))):
                    cursor.execute("UPDATE Professores SET Senha = ? WHERE Email = ? ",(md5(lista[2].encode('utf-8')).hexdigest(),lista[1]))
                    conexao.commit()
                    msg = "certo"
                else:
                    msg = "errado"
                    self.csocket.send(msg.encode())
                
                    
            except:
                pass
                
                    

            
            try:
                if(not(verifica_senha(lista[2]))):
                    cursor.execute("UPDATE Coordenadores SET Senha = ? WHERE Email = ? ",(md5(lista[2].encode('utf-8')).hexdigest(),lista[1]))
                    print("aqui nos coordenador")
                    conexao.commit()
                    msg = "certo"
                else:
                    msg = "errado"
                    self.csocket.send(msg.encode())
                   
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
            string = ''
            if(lista[1] == 'c'):
                confEm = False
                confSen = False
                consulta = cursor.execute("SELECT * from Coordenadores")
                for x in consulta.fetchall():
                    if((x[3] == lista[3]) and (x[4] == lista[2])):
                        confEm = True
                        confSen = True
                if((confEm == True) and (confSen==True)):
                    self.csocket.send("plog".encode())
                    #print("X3:",x[3],"x4",x[4])
                    #print("Lista3:",lista[2],"lista4",lista[3])
                    consulta = cursor.execute("SELECT * from Coordenadores")
                    for x in consulta.fetchall():
                        
                        if((x[3] == lista[3]) and (x[4] == lista[2])):
                            string+=str(x[0])+','+str(x[1])+','+str(x[2])+','+str(x[3])+','+str(x[4])+','+str(x[5])+','+str(x[6])
                            #print("Dados do logador",string)
                            self.csocket.send(string.encode())
                            break

                            
                else:
                    self.csocket.send("nlog".encode())

            if(lista[1] == 'p'):
                confEm = False
                confSen = False
                consulta = cursor.execute("SELECT * from Professores")
                for x in consulta.fetchall():
                    if((x[3] == lista[3]) and (x[4] == lista[2])):
                        confEm = True
                        confSen = True
                if((confEm == True) and (confSen==True)):
                    self.csocket.send("plog".encode())
                    consulta = cursor.execute("SELECT * from Professores")
                    for x in consulta.fetchall():
                        
                        if((x[3] == lista[3]) and (x[4] == lista[2])):
                            string+=str(x[0])+','+str(x[1])+','+str(x[2])+','+str(x[3])+','+str(x[4])+','+str(x[5])+','+str(x[6])
                            #print("Dados do logador",string)
                            self.csocket.send(string.encode())
                            break
                else:
                    self.csocket.send("nlog".encode())

            if(lista[1] == 'm'):
                confEm = False
                confSen = False
                consulta = cursor.execute("SELECT * from Monitores")
                for x in consulta.fetchall():
                    if((x[3] == lista[3]) and (x[4] == lista[2])):
                        confEm = True
                        confSen = True
                        
                if((confEm == True) and (confSen==True)):
                    self.csocket.send("plog".encode())
                    consulta = cursor.execute("SELECT * from Monitores")
                    for x in consulta.fetchall():
                        
                        if((x[3] == lista[3]) and (x[4] == lista[2])):
                            string+=str(x[0])+','+str(x[1])+','+str(x[2])+','+str(x[3])+','+str(x[4])+','+str(x[5])+','+str(x[6])
                            #print("Dados do logador",string)
                            self.csocket.send(string.encode())
                            break
                else:
                    self.csocket.send("nlog".encode())

            if(lista[1] == 't'):
                confEm = False
                confSen = False
                consulta = cursor.execute("SELECT * from Tecnicos")
                for x in consulta.fetchall():
                   if((x[4] == lista[3]) and (x[2] == lista[2])):
                        confEm = True
                        confSen = True
                if((confEm == True) and (confSen==True)):
                    self.csocket.send("plog".encode())
                    consulta = cursor.execute("SELECT * from Tecnicos")
                    for x in consulta.fetchall():
                        
                        if((x[4] == lista[3]) and (x[2] == lista[2])):
                            string+=str(x[0])+','+str(x[1])+','+str(x[2])+','+str(x[3])+','+str(x[4])
                            print("Dados do logador",string)
                            self.csocket.send(string.encode())
                            break
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
                
        
