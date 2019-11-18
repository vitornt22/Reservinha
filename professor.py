from monitor import monitor

class professor:

   def __init__(self,nome, siape,senha,cpf, email, telefone,disciplina):
       self._telefone= telefone
       self._siape=siape
       self._nome=nome
       self._senha=senha
       self._email=email
       self._cpf=cpf
       self._disciplina=disciplina


   def setSiape(self,siape):
       self._siape = siape
   def getDisciplina(self):
       return self._disciplina
   def setDisciplina(self,disciplina):
       self._disciplina = disciplina
   def getSIAPE(self):
       return self._siape
   def setTelefone(self,telefone):
       self._telefone=telefone
   def getTelefone(self):
       return self._telefone

   def getCurso(self):
       return self._curso

	

   def setNome(self,nome):
       self._nome=nome
   def getNome(self):
       return self._nome

   def setCpf(self,cpf):
       self._cpf=cpf
   def getCpf(self):
       return self._cpf

   def setSenha(self,senha):
       self._senha=senha
   def getSenha(self):
       return self._senha

   def setEmail(self,email):
       self._email=email
   def getEmail(self):
       return self._email


