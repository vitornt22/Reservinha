import socket,threading
from professor import professor
from monitor import monitor
from coordenador import coordenador

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        
    def run(self):
        
        recebe = self.csocket.recv(1024) #define que os pacotes recebidos sao de ate 1024 bytes
        string = ''
       # print ('mensagem recebida: '+ recebe.decode())
       
        string = recebe.decode()
        lista = string.split(',')

        if lista[0]=='p':
            print("EH professor!!!")
        if lista[0]=='m':
            print("EH monitor!!!")

        if lista[0]=='c':
            print("EH coodenardor!!!")
        
            
        
if __name__ == "__main__":
        sinc = threading.Lock()
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
                
        
