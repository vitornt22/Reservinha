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
		self._reservas={}


	def setTelefone(self,telefone):
		self._telefone=telefone
	def getTelefone(self):
		return self._telefone

	def getCurso(self):
		return self._curso

	def adicionarDisciplina(self,disc):
		self._disciplina.append(disc)
	def removerDisciplina(self,disc):
		self._disciplina.remove(disc)

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

'''
	def adicionarMonitor(self):
		n=str(input("Digite o nome: "))
		m=str(input("\nDigite a matricula: "))
		c=str(input("\nDigite o cpf: "))
		e=str(input("\nDigite o email: "))
		d=str(input("\nDigite a disciplina: "))
		t=str(input("\nDigite o telefone: "))


		m=monitor(n,m,d,professor.getNome(),c,e,t)
'''