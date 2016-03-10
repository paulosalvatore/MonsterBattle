import math

config = {
	"pdd": {
		"base": 120,
		"coeficiente": 0.011
	}
}

def pegarExperiencia(nivel):
	exp = 0 if nivel == 1 else 600 + 40 * nivel + int(nivel ** 2.1)

	if nivel == 1:
		return exp
	else:
		return exp + pegarExperiencia(nivel - 1)

def pegarPDD(nivel):
	base = (nivel - nivel % 10) / 10
	pdd = int(calcularPDD(base))
	print(pdd)
	return [int(pdd*0.7), int(pdd*0.3)]
	# return pdd

def calcularPDD(base):
	if base == 1:
		return config["pdd"]["base"]
	else:
		porcentagem = max(35, (100 - (base * 10))) / 100 - config["pdd"]["coeficiente"]
		return calcularPDD(base - 1) * (1 + porcentagem)

# def distribuirPDDNv(nv):
	# pddNv = pegarPDD(nv)
	# pdd = int(pddNv[0]*0.1)

monstros = {
	1: {
		"HP": 900,
		"ATK": 99,
		"DEF": 56,
		"HP Adicional": 0,
		"ATK Adicional": 0,
		"DEF Adicional": 0,
		"nivel": 1
	}
}

class Monstro(object):
	# def __init__(self):

	def definirNivel(self, monstroId, nivel):
		monstros[monstroId]["nivel"] = nivel

	def pegarNivel(self, monstroId):
		return monstros[monstroId]["nivel"]

	def avancarNivel(self, monstroId):
		nivel = self.pegarNivel(monstroId)
		novoNivel = nivel + 1
		self.definirNivel(monstroId, novoNivel)

		print("Experiência: ", pegarExperiencia(novoNivel))
		print("O monstro %d evoluiu para o nível %d." % (monstroId, novoNivel))

		if novoNivel % 10 > 0:
			self.aprimorarMonstroAutomaticamente(monstroId)
			print("Evoluir automaticamente.")
		else:
			print("Novos pontos disponíveis para distribuição.")
		print()

	def calcularBase(self, monstroId):
		nivel = self.pegarNivel(monstroId)
		base = (nivel - nivel % 10) / 10 + 1
		return base

	def pegarAtributo(self, monstroId, atributo):
		return monstros[monstroId][atributo]

	def definirAtributo(self, monstroId, atributo, valor):
		monstros[monstroId][atributo] = valor

	def aprimorarMonstroAutomaticamente(self, monstroId):
		base = self.calcularBase(monstroId)
		porcentagem = max(50.0, 100 - (base + 2) * 10)
		aumentoNivel = round((porcentagem / 100) / 10 + 1, 2)
		for atributo in ["HP", "ATK", "DEF"]:
			valorAtual = self.pegarAtributo(monstroId, atributo)
			novoValor = math.ceil(valorAtual * aumentoNivel)
			print(atributo, " - ", novoValor)
			self.definirAtributo(monstroId, atributo, novoValor)

monstro = Monstro()

# exp = 0
# for i in range(1, 11):
	# exp += pegarExperiencia(i)
# print(exp, exp/1131)
while True:
	avancarNiveis = int(input("Quantos níveis deseja avançar? "))
	for i in range(avancarNiveis):
		monstro.avancarNivel(1)
