
class tecnico(object):
	#tem que limitar para um unico tecnico
	def __init__(self,nome,idtec,cpf, email, telefone):
			self._telefone= telefone
			self._idTec=idtec
			self._nome=nome
			self._email=email
			self._cpf=cpf
			self._monitor=[]
			self._BD= BD()

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


'''
	def buscarCoordenador(self,cpf):
		if self._BD._coordenadores[cpf]:
			return True
		else:
			return False

	def cadastrarCoordenador(self,coordenador):
		self._BD._coordenadores={coordenador.getEmail():coordenador}

	def reserva(self,string):
		#enviar para o guarda
		print(string)
'''		
