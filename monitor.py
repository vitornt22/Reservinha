class monitor(object):

    def __init__(self,nome, matricula,disciplina, cpf, email,telefone,curso,senha):
       self._telefone= telefone
       self._nome=nome
       self._email=email
       self._cpf=cpf
       self._matricula=matricula
       
       self._curso=curso
       self._senha=senha
    def setSenha(self,Senha):
       self._senha = Senha
    def setDisciplina(self,disciplina):
       self._curso = disciplina
    def getDisciplina(self):
       return self._curso
    def setMatricula(self,matricula):
       self._matricula = matricula
    def getMatricula(self):
       return self._matricula
    def setTelefone(self,telefone):
       self._telefone=telefone
    def getTelefone(self):
       return self._telefone
    def getCurso(self):
       return self._curso

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
