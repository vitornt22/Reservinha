def verificaEmail(email):
	emails=['gmail.com','hotmail.com','ufpi.com.br']
	try: 
		lista= email.split('@')
		if lista[1] in emails:
			return True
		else:
			return False
	except:
		return False
def verificaCpf(cpf):
	if len((cpf))==14 and cpf[3]=='.' and cpf[7]=='.' and cpf[11]=='-':
		cpf.split('.')
		pos3= cpf[2].split('-')
		try: 
			int(cpf[0])
			int(cpf[1])
			int(pos3[0])
			int(pos3[0])
			return True
		except:
			return False
	else:
		return False

def verificaTelefone(tel):
	if len(str(tel))==11:
		try:
			int(tel)
			return True
		except:
			return False
	else:
		return False

def verificaMat(mat):
	try:
		a = int(mat)
		return True
	except:
		return False




