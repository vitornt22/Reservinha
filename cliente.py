import socket
class cliente(object):
    def __init__(self,dados):
        ip = '192.168.0.125'
        port = 7000
        addr = ((ip,port)) #define a tupla de endereco
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar a familia do protocolo, SOCK_STREAM indica que eh TCP/IP
        client_socket.connect(addr) #realiza a conexao
        client_socket.send(dados.encode()) #envia mensagem
    

