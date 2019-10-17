import sqlite3
class Banco:
    def __init__(self):
        pass
    def Tecnico(self,Nome,IdTec,CPF,Email,Telefone):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "INSERT INTO Tecnico VALUES ('{0}',{1},'{2}','{3}','{4}')".format(Nome,IdTec,CPF,Email,Telefone)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
    def Monitor(self,Nome,Matricula,Disciplina,CPF,Email,Telefone,Curso,Senha,Orientador=None):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "INSERT INTO Monitor VALUES ('{0}',{1},'{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(Nome,Matricula,Disciplina,CPF,Email,Telefone,Curso,Senha,Orientador)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
    def Professor(self,Nome,Siape,CPF,Email,Telefone,Disciplina,Senha,reservas=0):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "INSERT INTO Professor VALUES ('{0}',{1},'{2}','{3}','{4}','{5}','{6}',{7})".format(Nome,Siape,CPF,Email,Telefone,Disciplina,Senha,reservas)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print(e)
            raise
    def Coordenador(self,Nome,Siape,CPF,Email,Telefone,Curso,Senha,reservas=0):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "INSERT INTO Coordenador VALUES ('{0}',{1},'{2}','{3}','{4}','{5}','{6}',{7})".format(Nome,Siape,CPF,Email,Telefone,Curso,Senha,reservas)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
    def ReservaSala(self,Bloco,NumeroSala,Dia,Siape):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "INSERT INTO Sala VALUES ('{0}',{1},'{2}',{3})".format(Bloco,NumeroSala,Dia,Siape)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
    def CancelarReserva(self,Bloco,NumeroSala,Dia,Siape):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "DELETE FROM Sala WHERE NumeroSala = {0} AND Bloco = '{1}' AND Dia = '{2}' AND Siape = {3}".format(NumeroSala,Bloco,Dia,Siape)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
#------------------------------Altera monitor-----
    def AlterarDadosMonitorSenha(self,SenhaNova,Matricula):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Monitor SET Senha='{0}' WHERE Matricula = {1};".format(SenhaNova,Matricula)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
    def AlterarDadosMonitorEmail(self,Email,Matricula):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Monitor SET Email='{0}' WHERE Matricula = {1};".format(Email,Matricula)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
    def AlterarDadosMonitorTelefone(self,Telefone,Matricula):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Monitor SET Telefone='{0}' WHERE Matricula = {1};".format(Telefone,Matricula)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
#------------------------------Fim Altera monitor-----
######################################################
#------------------------------Altera Professor-----

    def AlterarDadosProfessorSenha(self,SenhaNova,Siape):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Professor SET Senha='{0}' WHERE Siape = {1};".format(SenhaNova,Siape)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
    def AlterarDadosProfessorEmail(self,Email,Siape):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Professor SET Email='{0}' WHERE Siape = {1};".format(Email,Siape)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
    def AlterarDadosProfessorTelefone(self,Telefone,Siape):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Professor SET Telefone='{0}' WHERE Siape = {1};".format(Telefone,Siape)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
#------------------------------Fim Altera Professor-----
######################################################
#------------------------------Altera Coordenador-----

    def AlterarDadosCoordenadorSenha(self,SenhaNova,Siape):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Coordenador SET Senha='{0}' WHERE Siape = {1};".format(SenhaNova,Siape)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
    def AlterarDadosCoordenadorEmail(self,Email,Siape):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Coordenador SET Email='{0}' WHERE Siape = {1};".format(Email,Siape)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
    def AlterarDadosCoordenadorTelefone(self,Telefone,Siape):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Coordenador SET Telefone='{0}' WHERE Siape = {1};".format(Telefone,Siape)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
#------------------------------Fim Altera Coordenador-----
######################################################
#------------------------------Altera Professor-----


    def AlterarDadosTecnicoSenha(self,SenhaNova,IdTec):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Tecnico SET Senha='{0}' WHERE IdTec = {1};".format(SenhaNova,IdTec)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
    def AlterarDadosTecnicoEmail(self,Email,IdTec):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Tecnico SET Email='{0}' WHERE IdTec = {1};".format(Email,IdTec)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
    def AlterarDadosTecnicoTelefone(self,Telefone,IdTec):
        try:
            conexao = sqlite3.connect("Banco.db")
            executar = conexao.cursor()
            sql = "UPDATE Tecnico SET Telefone='{0}' WHERE IdTec = {1};".format(Telefone,IdTec)
            print(sql)
            executar.execute(sql)
            conexao.commit()
            conexao.close()
        except Exception as e:
            print("Tratamento de erro")
            raise
Banco().AlterarDadosTecnicoTelefone("aaaa4a", 5)
