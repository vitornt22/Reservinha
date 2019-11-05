
class tecnico(object):
	#tem que limitar para um unico tecnico
	def __init__(self,nome,cpf, email, telefone,senha):
		self._telefone= telefone
		
		self._nome=nome
		self._email=email
		self._cpf=cpf
		self.senha = senha
			
			

	def setTelefone(self,telefone):
		self._telefone=telefone
		
	def getTelefone(self):
		return self._telefone

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

	

       
