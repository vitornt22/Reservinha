class coordenador(object):

   def __init__(self,nome, cpf,senha, email, telefone,curso):
        self._telefone= telefone
        self._nome=nome
        self._senha=senha
        self._SIAPE = None
        self._email=email
        self._cpf=cpf
        self._curso=curso
		
   def setCurso(self,curso):
        self._curso = curso
   def setTelefone(self,telefone):
        self._telefone=telefone
   def getTelefone(self):
        return self._telefone

   def getSIAPE(self):
        return self._SIAPE

   def getCurso(self):
        return self._curso

   def setSenha(self, senha):
        self._senha=senha
   def getSenha(self):
        return self._senha

   def setNome(self,nome):
        self._nome=nome
   def getNome(self):
        return self._nome

   def setCpf(self,cpf):
        self._cpf=cpf
   def getCpf(self):
        return self._cpf
   
   def setEmail(self,email):
        self._email=email
   def getEmail(self):
        return self._email
   def setSiape(self,Siape):
        self._SIAPE = Siape
                
                

