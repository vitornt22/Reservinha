import socket,threading
from professor import professor
from monitor import monitor
from coordenador import coordenador
import mysql.connector as mysql
class ClientThread(threading.Thread):
    
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
       

    def run(self):
        conexao = mysql.connect(host = 'localhost',db='bd', user='root', passwd=None)
        recebe = self.csocket.recv(1024) #define que os pacotes recebidos sao de ate 1024 bytes
        string = ''
        cursor = conexao.cursor()
       # print ('mensagem recebida: '+ recebe.decode())
       
        string = recebe.decode()
        lista = string.split(',')

        if lista[0]=='p':
            sql = """CREATE TABLE IF NOT EXISTS Professores(nome varchar(20), siape int, cpf varchar(20), senha varchar(20),email varchar(20),telefone varchar(20),disciplina varchar(20),primary key(siape));"""

            cursor.execute(sql)
       
            cursor.execute('INSERT INTO Professores  VALUES (%s,%s,%s,%s,%s,%s,%s)', (lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]))

            #cursor.execute('SELECT * from Professores')
            #for c in cursor:
            #   print(c)
            
            conexao.commit()
            conexao.close()
            
        if lista[0]=='m':
            #print("EH monitor!!!")
            sql = """CREATE TABLE IF NOT EXISTS Monitores(nome varchar(20), matricula int, cpf varchar(20), senha varchar(20),email varchar(20),telefone varchar(20),disciplina varchar(20));"""

            cursor.execute(sql)
       
            cursor.execute('INSERT INTO Monitores  VALUES (%s,%s,%s,%s,%s,%s,%s)', (lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]))

            #cursor.execute('SELECT * from Monitores')

            #for c in cursor:
            #   print(c)

            conexao.commit()
            conexao.close()
            

        if lista[0]=='c':
            
            sql = """CREATE TABLE IF NOT EXISTS Coodenadores(nome varchar(20), siape int, cpf varchar(20), senha varchar(20),email varchar(20),telefone varchar(20),disciplina varchar(20));"""

            cursor.execute(sql)
       
            cursor.execute('INSERT INTO Coodenadores  VALUES (%s,%s,%s,%s,%s,%s,%s)', (lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]))

            #cursor.execute('SELECT * from Coodenadores')

            #for c in cursor:
            #   print(c)
            conexao.commit()
            conexao.close()
        
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
                
        
