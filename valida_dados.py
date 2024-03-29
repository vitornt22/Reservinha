import sqlite3
from hashlib import md5
from datetime import datetime
def verifica_senha(senha):
    
    conexao = sqlite3.connect('bd0.db')
    conf = False
    cursor = conexao.cursor()
    if(conf==False):
        consulta = cursor.execute("SELECT Senha from Tecnicos")
        for x in consulta.fetchall():
            if(x[0]==md5(senha.encode('utf-8')).hexdigest()):
                conf = True
                    
    if(conf==False):
        consulta = cursor.execute("SELECT Senha from Monitores")
        for x in consulta.fetchall():
            if(x[0]==md5(senha.encode('utf-8')).hexdigest()):
                conf = True
                    
    if(conf==False):
        consulta = cursor.execute("SELECT Senha from Coordenadores")
        for x in consulta.fetchall():
            if(x[0]==md5(senha.encode('utf-8')).hexdigest()):
                conf = True
                    

    if(conf==False):
        consulta = cursor.execute("SELECT Senha from Professores")
        for x in consulta.fetchall():
            if(x[0]==md5(senha.encode('utf-8')).hexdigest()):
                conf = True
    if(conf):
        return 1
    else:
        return 0
    conexao.close()


def verifica_email(email):
    
    conexao = sqlite3.connect('bd0.db')
    conf = False
    cursor = conexao.cursor()
    if(conf==False):
        consulta = cursor.execute("SELECT Email from Tecnicos")
        for x in consulta.fetchall():
            if(x[0]==email):
                conf = True
                    
    if(conf==False):
        consulta = cursor.execute("SELECT Email from Monitores")
        for x in consulta.fetchall():
            if(x[0]==email):
                conf = True
                    
    if(conf==False):
        consulta = cursor.execute("SELECT Email from Coordenadores")
        for x in consulta.fetchall():
             if(x[0]==email):
                conf = True
                    

    if(conf==False):
        consulta = cursor.execute("SELECT Email from Professores")
        for x in consulta.fetchall():
            if(x[0]==email):
                conf = True
    if(conf):
        return 1
    else:
        return 0
    conexao.close()


def verifica_siape(siape):
    
    conexao = sqlite3.connect('bd0.db')
    conf = False
    cursor = conexao.cursor()
    
                    
    if(conf==False):
        consulta = cursor.execute("SELECT Matricula from Monitores")
        for x in consulta.fetchall():
            
            if(str(x[0])==siape):
                conf = True
                
                    
    if(conf==False):
        consulta = cursor.execute("SELECT Siape from Coordenadores")
        for x in consulta.fetchall():
               
            if(str(x[0])==siape):
                conf = True
               

    if(conf==False):
        consulta = cursor.execute("SELECT Siape from Professores")
        for x in consulta.fetchall():
            
            if(str(x[0])==siape):
                conf = True
                
    if(conf):
        return 1
    else:
        return 0
    conexao.close()

def verifica_cpf(cpf):
    
    conexao = sqlite3.connect('bd0.db')
    conf = False
    cursor = conexao.cursor()
    if(conf==False):
        consulta = cursor.execute("SELECT Cpf from Tecnicos")
        for x in consulta.fetchall():
            if(x[0]==cpf):
                conf = True
                    
    if(conf==False):
        consulta = cursor.execute("SELECT Cpf from Monitores")
        for x in consulta.fetchall():
            if(x[0]==cpf):
                conf = True
                    
    if(conf==False):
        consulta = cursor.execute("SELECT Cpf from Coordenadores")
        for x in consulta.fetchall():
            if(x[0]==cpf):
                conf = True
                    

    if(conf==False):
        consulta = cursor.execute("SELECT Cpf from Professores")
        for x in consulta.fetchall():
            if(x[0]==cpf):
                conf = True
    if(conf):
        return 1
    else:
         return 0
    conexao.close()


def verifica_telefone(telefone):
    
    conexao = sqlite3.connect('bd0.db')
    conf = False
    cursor = conexao.cursor()
    if(conf==False):
        consulta = cursor.execute("SELECT Telefone from Tecnicos")
        for x in consulta.fetchall():
            if(x[0]==telefone):
                conf = True
                    
    if(conf==False):
        consulta = cursor.execute("SELECT Telefone  from Monitores")
        for x in consulta.fetchall():
            if(x[0]==telefone):
                conf = True
                    
    if(conf==False):
        consulta = cursor.execute("SELECT Telefone  from Coordenadores")
        for x in consulta.fetchall():
            if(x[0]==telefone):
                conf = True
                    

    if(conf==False):
        consulta = cursor.execute("SELECT Telefone  from Professores")
        for x in consulta.fetchall():
            if(x[0]==telefone):
                conf = True
    if(conf):
        return 1
    else:
        return 0
    conexao.close()


def verifica_horario(hora):
    if((hora!="8") and (hora!="10") and (hora!="12") and (hora!="14") and (hora!="16") and (hora!="18") and (hora!="20")):
        return 1
    else:
        return 0

def verifica_dia(dia):
    if(dia!="Segunda" and dia!="Terça" and dia !="Quarta" and dia!="Quinta" and dia!="Sexta" and dia!="Sabado"):
        return 1
    else:
        return 0


def verifica_hora():
    today = datetime.now().hour
    return today
    
def conta_reserva(cpf):
    conexao = sqlite3.connect('bd0.db')
    cont = 0
    cursor = conexao.cursor()
    cons = cursor.execute("SELECT * FROM Reservas WHERE Cpf = ?",(cpf,))
    for i in cons.fetchall():
        cont+=1
    return cont






    




        

